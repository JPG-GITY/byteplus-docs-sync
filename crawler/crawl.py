#!/usr/bin/env python3
"""Crawl BytePlus docs -> render to markdown -> snapshot into a git-tracked cache.

Enumeration relies on the fact that each product landing page
(e.g. /en/docs/ModelArk) renders the full nav tree, and every doc page has a
stable numeric-id URL of the form  /en/docs/{Product}/{digits} .

Nothing here talks to git or Anthropic; it just produces reproducible snapshots
so that `update_skill.py` can diff them.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import yaml

# --------------------------------------------------------------------------- #
# Rendering                                                                    #
# --------------------------------------------------------------------------- #


@dataclass
class RenderResult:
    html: Optional[str]   # full rendered HTML (playwright) or None (jina)
    markdown: str         # readable content as markdown
    title: str


class Renderer:
    """Base renderer interface."""

    def render(self, url: str) -> RenderResult:  # pragma: no cover - interface
        raise NotImplementedError

    def close(self) -> None:
        pass


class PlaywrightRenderer(Renderer):
    """Headless Chromium. Self-contained, no third-party services."""

    def __init__(self, cfg: dict):
        from playwright.sync_api import sync_playwright  # local import

        self._cfg = cfg
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=True)
        self._page = self._browser.new_page()
        self._timeout = int(cfg.get("timeout_seconds", 45)) * 1000

    def render(self, url: str) -> RenderResult:
        import html2text

        self._page.goto(url, wait_until="networkidle", timeout=self._timeout)
        full_html = self._page.content()
        title = (self._page.title() or "").strip()

        # Narrow to the main content region so diffs aren't polluted by nav/footer.
        content_html = full_html
        for sel in self._cfg.get("content_selectors", []):
            try:
                node = self._page.query_selector(sel)
            except Exception:
                node = None
            if node:
                content_html = node.inner_html()
                break

        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_images = True
        markdown = h.handle(content_html)
        return RenderResult(html=full_html, markdown=markdown, title=title)

    def close(self) -> None:
        try:
            self._browser.close()
            self._pw.stop()
        except Exception:
            pass


class JinaRenderer(Renderer):
    """Uses the r.jina.ai reader proxy to turn a URL into markdown."""

    def __init__(self, cfg: dict):
        import os
        import httpx

        self._timeout = int(cfg.get("timeout_seconds", 45))
        headers = {"Accept": "text/markdown"}
        token = os.environ.get("JINA_API_KEY")
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self._client = httpx.Client(headers=headers, timeout=self._timeout, follow_redirects=True)

    def render(self, url: str) -> RenderResult:
        resp = self._client.get(f"https://r.jina.ai/{url}")
        resp.raise_for_status()
        md = resp.text
        # jina prefixes "Title: ...\nURL Source: ...\nMarkdown Content:\n"
        title = ""
        m = re.search(r"^Title:\s*(.+)$", md, re.MULTILINE)
        if m:
            title = m.group(1).strip()
        return RenderResult(html=None, markdown=md, title=title)

    def close(self) -> None:
        self._client.close()


def build_renderer(cfg: dict) -> Renderer:
    kind = cfg.get("renderer", "playwright").lower()
    if kind == "playwright":
        return PlaywrightRenderer(cfg)
    if kind == "jina":
        return JinaRenderer(cfg)
    raise ValueError(f"Unknown renderer: {kind!r}")


# --------------------------------------------------------------------------- #
# Enumeration + snapshotting                                                   #
# --------------------------------------------------------------------------- #

# matches /en/docs/{Product}/{pageKey}. The pageKey is EITHER a numeric id
# (ModelArk-style, e.g. /ModelArk/1330310) OR a textual slug (most other
# products, e.g. /recommend/docs-product_overview, /bytehouse/Release-Notes).
_DOC_PATH_RE = re.compile(r"/en/docs/([A-Za-z0-9_-]+)/([A-Za-z0-9_.-]+)")


def extract_doc_links(result: RenderResult, product: str, base_url: str) -> set[str]:
    """Pull all /en/docs/{product}/{id} URLs from a rendered landing page."""
    found: set[str] = set()
    origin = f"{urlparse(base_url).scheme}://{urlparse(base_url).netloc}"

    def _consume(href: str) -> None:
        m = _DOC_PATH_RE.search(href)
        if not m:
            return
        if m.group(1).lower() != product.lower():
            return
        found.add(urljoin(origin, m.group(0)))

    if result.html:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(result.html, "html.parser")
        for a in soup.find_all("a", href=True):
            _consume(a["href"])
    else:
        # jina markdown: links look like [text](https://.../en/docs/Product/123)
        for href in re.findall(r"\]\(([^)]+)\)", result.markdown):
            _consume(href)
        for href in re.findall(r"https?://[^\s)]+", result.markdown):
            _consume(href)
    return found


# matches the product slug in /en/docs/{Product}[/...]
_PRODUCT_RE = re.compile(r"/en/docs/([A-Za-z0-9_-]+)")


def extract_product_slugs(result: RenderResult) -> set[str]:
    """Pull every distinct /en/docs/{Product} slug from a rendered index page."""
    slugs: set[str] = set()

    def _consume(href: str) -> None:
        m = _PRODUCT_RE.search(href)
        if m:
            slugs.add(m.group(1))

    if result.html:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(result.html, "html.parser")
        for a in soup.find_all("a", href=True):
            _consume(a["href"])
    else:
        for href in re.findall(r"\]\(([^)]+)\)", result.markdown):
            _consume(href)
        for href in re.findall(r"https?://[^\s)]+", result.markdown):
            _consume(href)
    return slugs


def normalize_markdown(md: str) -> str:
    md = md.replace("\r\n", "\n").replace("\r", "\n")
    md = "\n".join(line.rstrip() for line in md.split("\n"))
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def page_key(url: str) -> str:
    m = _DOC_PATH_RE.search(url)
    return f"{m.group(1)}/{m.group(2)}" if m else urlparse(url).path.strip("/")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_snapshot(cache_dir: Path, key: str, url: str, title: str, md: str) -> None:
    path = cache_dir / f"{key}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = (
        "---\n"
        f"url: {url}\n"
        f"title: {title!r}\n"
        f"key: {key}\n"
        "---\n\n"
    )
    path.write_text(frontmatter + md, encoding="utf-8")


def with_retries(fn, url: str, retries: int, delay: float):
    last = None
    for attempt in range(1, retries + 1):
        try:
            return fn(url)
        except Exception as exc:  # noqa: BLE001
            last = exc
            print(f"  ! attempt {attempt}/{retries} failed for {url}: {exc}", file=sys.stderr)
            time.sleep(delay * attempt)
    raise last  # type: ignore[misc]


def discover(cfg: dict) -> int:
    """Render the docs index, list every product slug and its page count.

    Scope report only — no snapshots written. Output also goes to
    $GITHUB_STEP_SUMMARY so it shows up in the Actions run.
    """
    base_url = cfg["base_url"].rstrip("/")
    delay = float(cfg.get("request_delay_seconds", 0.6))
    retries = int(cfg.get("max_retries", 3))
    ignore = {s.lower() for s in cfg.get("discover_ignore_slugs", [])}

    renderer = build_renderer(cfg)
    lines: list[str] = ["## BytePlus docs — discovery (scope report)", ""]
    try:
        print(f"== discovering products from {base_url}")
        home = with_retries(renderer.render, base_url, retries, delay)
        slugs = sorted(s for s in extract_product_slugs(home) if s.lower() not in ignore)
        print(f"   found {len(slugs)} product slug(s): {', '.join(slugs)}")
        lines.append(f"Found **{len(slugs)}** product slug(s).\n")
        lines.append("| Product | Pages |")
        lines.append("|---|---|")

        total = 0
        counts: list[tuple[str, int]] = []
        for slug in slugs:
            landing = f"{base_url}/{slug}"
            try:
                res = with_retries(renderer.render, landing, retries, delay)
                n = len(extract_doc_links(res, slug, base_url))
            except Exception as exc:  # noqa: BLE001
                print(f"   ! {slug}: landing failed: {exc}", file=sys.stderr)
                n = -1
            counts.append((slug, n))
            total += max(n, 0)
            print(f"   {slug}: {n} page(s)")
            time.sleep(delay)

        for slug, n in sorted(counts, key=lambda x: -x[1]):
            lines.append(f"| {slug} | {n if n >= 0 else 'landing failed'} |")
        lines.append(f"| **TOTAL** | **{total}** |")
        lines.append("")
        lines.append(
            "To crawl these, set `products:` in config.yaml to the slugs above "
            "(minus any you don't want) and run the normal sync with **bootstrap**."
        )
    finally:
        renderer.close()

    body = "\n".join(lines)
    print("\n" + body)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(body + "\n")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--product", help="crawl only this product slug")
    ap.add_argument("--discover", action="store_true",
                    help="list all product slugs + page counts; write no snapshots")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    if args.discover:
        return discover(cfg)

    base_url = cfg["base_url"].rstrip("/")
    cache_dir = Path(cfg["cache_dir"])
    delay = float(cfg.get("request_delay_seconds", 0.6))
    retries = int(cfg.get("max_retries", 3))
    products = [args.product] if args.product else cfg["products"]

    renderer = build_renderer(cfg)

    # Auto-discover every product from the docs index when requested
    # (config `crawl_all_products: true`, or products list is exactly ["*"]).
    if not args.product and (cfg.get("crawl_all_products") or products == ["*"]):
        ignore = {s.lower() for s in cfg.get("discover_ignore_slugs", [])}
        print(f"== auto-discovering all products from {base_url}")
        home = with_retries(renderer.render, base_url, retries, delay)
        products = sorted(
            s for s in extract_product_slugs(home) if s.lower() not in ignore
        )
        print(f"   crawling {len(products)} product(s): {', '.join(products)}")

    manifest: dict = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base_url,
        "pages": {},
    }

    try:
        for product in products:
            landing = f"{base_url}/{product}"
            print(f"== {product}: enumerating from {landing}")
            landing_res = with_retries(renderer.render, landing, retries, delay)
            urls = sorted(extract_doc_links(landing_res, product, base_url))
            print(f"   found {len(urls)} page(s)")

            for i, url in enumerate(urls, 1):
                time.sleep(delay)
                res = with_retries(renderer.render, url, retries, delay)
                md = normalize_markdown(res.markdown)
                key = page_key(url)
                write_snapshot(cache_dir, key, url, res.title, md)
                manifest["pages"][key] = {
                    "url": url,
                    "title": res.title,
                    "sha256": sha256(md),
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                }
                print(f"   [{i}/{len(urls)}] {key}  ({res.title[:60]})")
    finally:
        renderer.close()

    Path(cfg["manifest_path"]).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Wrote manifest with {len(manifest['pages'])} page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
