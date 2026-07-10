#!/usr/bin/env python3
"""Turn changed doc snapshots into skill updates.

Flow:
  1. Ask git which docs_cache/*.md files changed since the last commit.
  2. Route each changed page to a reference file (config `routing`).
  3. For each affected reference file, send Claude the current file + the changed
     source pages and write back the updated file.
  4. Regenerate skill/sources.json (the live-fetch URL index) from the manifest.
  5. Print a changelog (also to $GITHUB_STEP_SUMMARY) for the commit + Slack aviso.

`--bootstrap` skips all Claude calls: it just (re)builds sources.json. Use it on
the very first run so the baseline snapshot lands without rewriting everything.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


# --------------------------------------------------------------------------- #
# git helpers                                                                  #
# --------------------------------------------------------------------------- #

def _git(*args: str) -> str:
    out = subprocess.run(["git", *args], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout


def changed_cache_files(cache_dir: str) -> dict[str, list[str]]:
    """Return {'modified': [...], 'added': [...], 'deleted': [...]} for *.md."""
    modified, deleted = [], []
    for line in _git("diff", "--name-status", "--", cache_dir).splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]
        if not path.endswith(".md"):
            continue
        if status.startswith("D"):
            deleted.append(path)
        else:
            modified.append(path)
    added = [
        p for p in _git(
            "ls-files", "--others", "--exclude-standard", "--", cache_dir
        ).splitlines()
        if p.endswith(".md")
    ]
    return {"modified": modified, "added": added, "deleted": deleted}


def cache_is_tracked(cache_dir: str) -> bool:
    return bool(_git("ls-files", "--", f"{cache_dir}/*.md").strip())


# --------------------------------------------------------------------------- #
# snapshot parsing + routing                                                   #
# --------------------------------------------------------------------------- #

_FM_RE = re.compile(r"^---\n(.*?)\n---\n\n(.*)$", re.DOTALL)


def parse_snapshot(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("'\"")
    return meta, m.group(2)


def route(url: str, title: str, rules: list[dict]) -> str | None:
    hay = f"{url}\n{title}".lower()
    for rule in rules:
        pat = rule["match"]
        if pat.startswith("/") and pat.endswith("/"):
            if re.search(pat[1:-1], hay, re.IGNORECASE):
                return rule["reference"]
        elif pat.lower() in hay:
            return rule["reference"]
    return None


# --------------------------------------------------------------------------- #
# Claude update                                                                #
# --------------------------------------------------------------------------- #

def update_reference(ref_path: Path, sources: list[tuple[str, str]], cfg: dict) -> None:
    """Rewrite one reference file from its changed source pages."""
    from anthropic import Anthropic

    template = Path(cfg["_prompt_path"]).read_text(encoding="utf-8")
    current = ref_path.read_text(encoding="utf-8") if ref_path.exists() else "(file does not exist yet — create it)"

    blocks = []
    for url, body in sources:
        blocks.append(f"<source url=\"{url}\">\n{body}\n</source>")
    sources_blob = "\n\n".join(blocks)

    user = (
        template
        .replace("{{REFERENCE_FILENAME}}", ref_path.name)
        .replace("{{CURRENT_REFERENCE}}", current)
        .replace("{{CHANGED_SOURCES}}", sources_blob)
    )

    client = Anthropic()  # reads ANTHROPIC_API_KEY
    resp = client.messages.create(
        model=cfg.get("model", "claude-sonnet-5"),
        max_tokens=int(cfg.get("max_tokens", 8000)),
        messages=[{"role": "user", "content": user}],
    )
    new_text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()
    if not new_text:
        raise RuntimeError(f"Empty model response for {ref_path.name}")

    # Strip accidental code-fence wrapping.
    new_text = re.sub(r"^```(?:markdown|md)?\n", "", new_text)
    new_text = re.sub(r"\n```$", "", new_text)

    ref_path.parent.mkdir(parents=True, exist_ok=True)
    ref_path.write_text(new_text.strip() + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# sources.json (live-fetch index used by the skill)                           #
# --------------------------------------------------------------------------- #

def rebuild_sources_index(cfg: dict) -> int:
    manifest = json.loads(Path(cfg["manifest_path"]).read_text(encoding="utf-8"))
    entries = []
    for key, page in sorted(manifest["pages"].items()):
        product, _, pid = key.partition("/")
        entries.append({
            "product": product,
            "id": pid,
            "title": page.get("title", ""),
            "url": page.get("url", ""),
        })
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "note": "Canonical BytePlus doc URLs. If a detail is missing from the "
                "reference files, fetch the matching url live before answering.",
        "entries": entries,
    }
    Path(cfg["sources_index"]).write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return len(entries)


# --------------------------------------------------------------------------- #
# changelog                                                                    #
# --------------------------------------------------------------------------- #

def emit_changelog(lines: list[str]) -> None:
    body = "\n".join(lines)
    print(body)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(body + "\n")
    # Machine-readable handoff for the workflow's Slack step.
    Path("changelog.md").write_text(body + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--bootstrap", action="store_true",
                    help="skip Claude; only (re)build sources.json")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    cfg["_prompt_path"] = str(Path(__file__).parent / "prompts" / "update_reference.md")
    cache_dir = cfg["cache_dir"]
    skill_dir = Path(cfg["skill_dir"])

    bootstrap = args.bootstrap or not cache_is_tracked(cache_dir)
    if bootstrap:
        n = rebuild_sources_index(cfg)
        emit_changelog([
            "## BytePlus docs sync — baseline",
            "",
            f"Established snapshot baseline and indexed **{n}** doc page(s) into "
            "`sources.json`. No reference files were rewritten (bootstrap run).",
        ])
        return 0

    changes = changed_cache_files(cache_dir)
    rules = cfg.get("routing", [])

    # Group changed source pages by target reference file.
    grouped: dict[str, list[tuple[str, str]]] = {}
    unrouted: list[str] = []
    for path_str in changes["modified"] + changes["added"]:
        meta, body = parse_snapshot(Path(path_str))
        url = meta.get("url", path_str)
        title = meta.get("title", "")
        ref = route(url, title, rules)
        if ref:
            grouped.setdefault(ref, []).append((url, body))
        else:
            unrouted.append(url)

    log: list[str] = ["## BytePlus docs sync", ""]
    total_changed = len(changes["modified"]) + len(changes["added"]) + len(changes["deleted"])
    if total_changed == 0:
        log.append("No documentation changes detected. ✅")
        emit_changelog(log)
        rebuild_sources_index(cfg)
        return 0

    log.append(
        f"**{len(changes['modified'])} modified · {len(changes['added'])} added · "
        f"{len(changes['deleted'])} removed** doc page(s)."
    )
    log.append("")

    for ref, sources in grouped.items():
        ref_path = skill_dir / ref
        print(f"Updating {ref} from {len(sources)} changed page(s)...")
        try:
            update_reference(ref_path, sources, cfg)
            log.append(f"### `{ref}` — updated from {len(sources)} page(s)")
            for url, _ in sources:
                log.append(f"- {url}")
            log.append("")
        except Exception as exc:  # noqa: BLE001
            log.append(f"### `{ref}` — ⚠️ update FAILED: {exc}")
            log.append("")
            print(f"ERROR updating {ref}: {exc}", file=sys.stderr)

    if unrouted:
        log.append(f"### Unrouted changes ({len(unrouted)}) — indexed, no reference rewritten")
        for url in unrouted:
            log.append(f"- {url}")
        log.append("")

    if changes["deleted"]:
        log.append("### Removed upstream (review references manually)")
        for p in changes["deleted"]:
            log.append(f"- {p}")
        log.append("")

    n = rebuild_sources_index(cfg)
    log.append(f"`sources.json` re-indexed: **{n}** page(s).")
    emit_changelog(log)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
