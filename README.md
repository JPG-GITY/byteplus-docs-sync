# BytePlus Genius (`byteplus-docs-sync`)

**Unofficial personal project — not a BytePlus or ByteDance product, not endorsed or supported by BytePlus, no warranty.** See [Licensing & scope](#licensing--scope) before redistributing anything from this repo.

This repo contains two things:

- **The skill** — [`skill/`](skill/): a Claude/Codex Agent Skill named `byteplus-genius` ("BytePlus Genius"). `SKILL.md` + 9 reference files + `sources.json`, an index of ~18,863 BytePlus doc pages across ~93 products (~4 MB).
- **The automation** that keeps it current — a crawler over `docs.byteplus.com`, git history as the diff engine, a Claude rewrite step for the affected reference files only, and a weekly GitHub Actions run that publishes an installable zip.

Audience: BytePlus solutions engineers and their customers who want a documentation-grounded assistant for BytePlus and ModelArk.

---

## What it covers

The skill answers questions about ModelArk generative AI — Seed 2.0 LLMs and the Responses API, Seedream image generation, Seedance 2.0 video, Seed Audio 1.0 TTS and voice cloning, 3D generation, multimodal embeddings, rate limits/billing/compliance, and the Trusted Asset Library — plus the rest of the BytePlus platform (CDN, TOS object storage, RTC, VOD, media-live, VikingDB, ByteHouse, RDS, ECS, effects and ~85 more products).

Coverage comes at two depths, deliberately:

| Scope | How it's covered |
|---|---|
| **ModelArk** | **In depth.** Curated reference files kept in sync from 72 git-tracked page snapshots: `model-catalog.md`, `llm-and-responses-api.md`, `image-seedream.md`, `video-seedance.md`, `audio-generation.md`, `3d-generation.md`, `multimodal-embedding.md`, `enterprise-ops.md` — plus `trusted-asset-library.md`, which has no `routing:` rule and is maintained by hand (the automation does not refresh it). |
| **All other BytePlus products** | **Index-only.** Page titles and URLs in `sources.json` as `{product, id, title, url}`. When a detail is not in the bundled references, the skill greps the index and live-fetches the matching URL. No page bodies are bundled for these products. |

**On grounding.** Both `skill/SKILL.md` and `updater/prompts/update_reference.md` instruct the model never to invent model IDs, parameters, limits or prices, and to ground every statement in the sources. This is a prompt-level constraint, not a validated one: reference rewrites are model-generated (`claude-sonnet-5`) and auto-committed with no human review step. Treat the linked BytePlus documentation page as authoritative.

---

## Install

Agent Skills are plain filesystem folders (`SKILL.md` + `references/`), so installing means putting the folder in the right place.

> **Sanity-check any build you install.** The index is the skill's whole non-ModelArk coverage, so it is worth one command:
>
> ```bash
> unzip -p byteplus-genius.zip byteplus-genius/sources.json \
>   | python3 -c "import json,sys; print(len(json.load(sys.stdin)['entries']), 'entries')"
> ```
>
> Expect ~18,863 entries. If it prints `0`, the crawl that produced that build failed — install from a clone (below) or re-run the workflow. Guards now abort such a run instead of publishing it, but check anyway.

Release download URL:

```
https://github.com/JPG-GITY/byteplus-docs-sync/releases/download/skill-latest/byteplus-genius.zip
```

It is republished whenever a sync run produces a commit — a failed or no-change run leaves the previous asset in place, so check the release notes date and the entry count above.

### Claude Code — clone and symlink (gets the index that is on `main`)

```bash
git clone https://github.com/JPG-GITY/byteplus-docs-sync.git ~/src/byteplus-docs-sync
mkdir -p ~/.claude/skills
ln -s ~/src/byteplus-docs-sync/skill ~/.claude/skills/byteplus-genius
~/src/byteplus-docs-sync/scripts/pull.sh    # fast-forward; wire to launchd/cron for hands-off updates
```

`scripts/pull.sh` runs `git pull --ff-only` on the clone it lives in and logs to `~/Library/Logs/byteplus-docs-sync-pull.log`.

### Claude Code — from the zip

User-level (available in every project):

```bash
mkdir -p ~/.claude/skills && \
curl -fsSL https://github.com/JPG-GITY/byteplus-docs-sync/releases/download/skill-latest/byteplus-genius.zip \
  -o /tmp/byteplus-genius.zip && \
unzip -oq /tmp/byteplus-genius.zip -d ~/.claude/skills && \
rm /tmp/byteplus-genius.zip
```

Project-level instead (checked in with your repo): use `.claude/skills` as the `mkdir`/`unzip -d` target.

### Codex

Same layout, different root: `~/.agents/skills/` for a user install, `<repo>/.agents/skills/` for a project install.

```bash
mkdir -p ~/.agents/skills && \
curl -fsSL https://github.com/JPG-GITY/byteplus-docs-sync/releases/download/skill-latest/byteplus-genius.zip \
  -o /tmp/byteplus-genius.zip && \
unzip -oq /tmp/byteplus-genius.zip -d ~/.agents/skills && \
rm /tmp/byteplus-genius.zip
```

### claude.ai (web) and the Claude mobile app

Upload a zip in **Settings → Capabilities → Skills**. This is a per-user install and requires a paid plan with code execution.

To build the zip yourself from a clone (same layout the workflow produces):

```bash
cd ~/src/byteplus-docs-sync
rm -rf _pkg && mkdir -p _pkg/byteplus-genius
cp skill/SKILL.md skill/sources.json _pkg/byteplus-genius/
cp -R skill/references _pkg/byteplus-genius/references
(cd _pkg && zip -qr ../byteplus-genius.zip byteplus-genius)
```

Anthropic states that custom Skills **do not sync across surfaces**: installing on claude.ai does not install it in Claude Code, Codex, or the mobile app. Install each surface separately.

---

## Using it

- **By name:** open with `Hi BytePlus Genius` (or `Hi Model Genius`, the former name) — `SKILL.md` handles both.
- **Automatically:** just ask a BytePlus question. The skill's description triggers on BytePlus, ModelArk, Seedream, Seedance, Seed 2.0, Seed Audio/TTS, VideoPilot, CDN, object storage, RTC, VikingDB, ByteHouse, the `*.bytepluses.com` endpoints, and architecture/integration/debugging questions on the platform.

The skill reads the reference file matching your question first, then greps `sources.json` and live-fetches the exact doc page when a detail is missing. That fetch step needs the agent to be allowed to fetch URLs — in Claude Code and Codex the fetch tool must be permitted; on claude.ai it depends on the sandbox's network access. Without it, answers outside the bundled ModelArk references are limited to titles and URLs.

---

## How the sync works

```
docs.byteplus.com/en/docs
        │
        │  crawler/crawl.py  (Playwright headless Chromium)
        │  discover products → enumerate page URLs → render markdown
        ▼
   docs_cache/ ──────────── git history = the diff engine ──────────▶ changed pages
   (ModelArk/*.md = 72 deep snapshots;                                     │
    manifest.json = every enumerated page)                                 │
        │                                                                  │
        │ manifest → index                                 routing: (config.yaml)
        ▼                                                                  ▼
   skill/sources.json                                       skill/references/*.md
   (regenerated each run)                                   rewritten by Claude — ONLY the
                                                            files whose sources changed
        │
        ▼
   .github/workflows/sync.yml → auto-commit → Release `skill-latest` → byteplus-genius.zip
```

1. **`crawler/crawl.py`** — Playwright headless-Chromium crawler. Discovers products from the docs index, enumerates page URLs, renders pages to markdown. Modes: normal crawl, `--discover` (scope report only, writes nothing), and index-only vs deep per product.
2. **`updater/update_skill.py`** — asks **git** which `docs_cache/` snapshots changed, routes them to reference files via `config.yaml → routing:`, has Claude (`claude-sonnet-5`) rewrite **only the affected reference files**, and regenerates `skill/sources.json` from `docs_cache/manifest.json`. `--bootstrap` skips all model calls.
3. **`.github/workflows/sync.yml`** — weekly cron (Mondays 06:00 UTC) plus manual `workflow_dispatch`. Auto-commits, publishes the zip to the `skill-latest` Release, and optionally posts to Slack.

Two properties worth naming: **git history is the diff engine** — there is no separate change database; last week's committed snapshot is this week's baseline. And **an unchanged upstream page costs nothing** — if no source under a reference's routing rules changed, that reference is not sent to a model and not touched.

---

## Run the automation yourself

### Prerequisites

- Python 3.12
- `pip install -r requirements.txt` (`anthropic`, `httpx`, `beautifulsoup4`, `html2text`, `playwright`, `pyyaml`)
- `python -m playwright install chromium`

### Secrets (repo → Settings → Secrets and variables → Actions)

| Secret | Required? | Used for |
|---|---|---|
| `ANTHROPIC_API_KEY` | Only for the reference-rewriting step | Claude rewrites of changed reference files. `--bootstrap` and `--discover` make no model calls. |
| `SLACK_WEBHOOK_URL` | Optional | Post the changelog to Slack after a committed run. |

### Manual runs (`workflow_dispatch` inputs)

| Input | Effect |
|---|---|
| `bootstrap` | Baseline only: crawl and rebuild `sources.json`, skip all Claude rewrites. Use for a first run. |
| `discover` | Scope report only: list every discovered product slug with its page count, write nothing. |

### Local dry run

```bash
pip install -r requirements.txt
python -m playwright install chromium

# What would we crawl? No writes, no model calls.
python crawler/crawl.py --config config.yaml --discover

# Full crawl, then rebuild sources.json without spending model calls.
python crawler/crawl.py --config config.yaml
python updater/update_skill.py --config config.yaml --bootstrap
```

Single-product experiments need care. `crawl.py --product ModelArk` writes a manifest containing only that product's pages, and `--bootstrap` regenerates `sources.json` from the manifest — so it would replace the full index with a partial one. The `sources_shrink_floor_ratio` guard refuses that write; only override it if the reduction is what you want, and restore afterwards:

```bash
python crawler/crawl.py --config config.yaml --product ModelArk
ALLOW_SOURCES_SHRINK=1 python updater/update_skill.py --config config.yaml --bootstrap  # partial index!
git checkout skill/sources.json docs_cache/manifest.json                                # restore
```

Tuning lives in `config.yaml`: `crawl_all_products`, `full_snapshot_products` (which products get deep snapshots), `discover_ignore_slugs`, `min_expected_products` and `sources_shrink_floor_ratio` (the anti-wipe guards), `routing:` rules (substring or `/regex/` → reference file), `renderer` (`playwright` | `jina`), and `content_selectors` if snapshots pick up nav/footer noise.

---

## Repo layout

```
byteplus-docs-sync/
├── crawler/
│   └── crawl.py                    # Playwright crawler: discover products, enumerate URLs, render markdown
├── updater/
│   ├── update_skill.py             # git diff → routing → Claude rewrite of changed references → sources.json
│   └── prompts/
│       └── update_reference.md     # rewrite prompt; hard rule: ground everything, invent nothing
├── .github/workflows/
│   └── sync.yml                    # weekly cron + manual dispatch; commit, publish zip, notify Slack
├── config.yaml                     # products, deep-vs-index scope, routing, guards, renderer, selectors
├── docs_cache/
│   ├── ModelArk/                   # 72 git-tracked markdown snapshots — the diff engine
│   └── manifest.json               # every enumerated page; sources.json is regenerated from this
├── skill/
│   ├── SKILL.md                    # persona, routing table, live-fetch + never-invent rules
│   ├── references/                 # 9 reference files (8 routed/auto-synced + trusted-asset-library.md by hand)
│   └── sources.json                # ~18,863-page index across ~93 products, for live-fetch (~4 MB)
├── scripts/
│   └── pull.sh                     # fast-forward a local consumption clone (pair with launchd/cron)
├── SKILL_snippet.md                # paste-in block for the "resolving missing details" section
└── requirements.txt
```

---

## Coverage & limitations

- **ModelArk is deep; everything else is index-only.** The reference files and the 72 content snapshots cover ModelArk. For other products the skill has titles and URLs, not bundled text, and must fetch the page to answer in detail.
- **Why:** BytePlus docs total roughly 18.8k pages. Snapshotting every page body does not fit a GitHub Actions job (6h cap), so index-only is the deliberate trade.
- **The index is not literally every page.** `discover_ignore_slugs` excludes non-product areas (account, billing, IAM, identity, resource management, legal, support, message center, organization, plus test slugs). Enumeration also depends on a product's landing page exposing its `/docs/{slug}/{id}` navigation tree; products that don't may index as 0 pages. Run `--discover` to see per-product page counts.
- **A broken crawl has already regressed the shipped skill once.** In July 2026 a docs-site URL change collapsed discovery, and the pipeline auto-committed an empty `sources.json` over a good one and republished the release zip. `min_expected_products: 10` (fall back to the pinned product list rather than crawl nothing) and `sources_shrink_floor_ratio: 0.5` (refuse to shrink the index) now guard against a repeat. Sanity-check a build by counting entries in `sources.json` and comparing `--discover` page counts.
- **Reference content is model-written and unreviewed.** Rewrites are generated by `claude-sonnet-5` and auto-committed; the never-invent rule is prompt text, not a validation step. Verify anything load-bearing against the linked BytePlus page.
- **`trusted-asset-library.md` is not auto-synced.** It has no `routing:` rule and no row in the `SKILL.md` routing table (Trusted Outputs is routed to `references/video-seedance.md`), so it only changes when edited by hand.
- **References lag upstream by up to 7 days** (Monday 06:00 UTC cron). Trigger `workflow_dispatch` for an urgent change. `generated_at` in `sources.json` tells you when your copy's index was built — the index committed on `main` was generated 2026-07-13.
- **Live-fetch needs fetch permission** on whatever surface you run (see [Using it](#using-it)); without it, non-ModelArk answers are limited to titles and URLs.
- **Custom Skills do not sync across surfaces.** Per Anthropic, install per surface.

---

## Licensing & scope

This repo mixes original code with BytePlus-owned documentation content, so it carries **no license file at present**. Absent one, no rights are granted by default — do not assume you may reuse or redistribute any part of it.

- **Original work by the repo owner:** the Python code (`crawler/`, `updater/`), the GitHub Actions workflow, `config.yaml`, `scripts/`, and the prompt in `updater/prompts/`.
- **BytePlus documentation content:** `docs_cache/` holds verbatim rendered text of BytePlus documentation pages; `skill/references/` are editorial summaries derived from BytePlus documentation; `sources.json` contains BytePlus doc titles and URLs. This material is the property of BytePlus/ByteDance and remains subject to BytePlus's own terms. It is not relicensed here, and a blanket permissive license over the whole repo would over-claim rights the owner does not hold.

**Not an official product.** This is a personal project on a personal GitHub account. The repo owner works at BytePlus, but this is not an official BytePlus or ByteDance release, is not endorsed or supported by BytePlus, and comes with no warranty. "BytePlus", "ModelArk", "Seedream", "Seedance" and related names are used descriptively to refer to the products they identify. The BytePlus documentation at <https://docs.byteplus.com> remains the authoritative source.

This section is informational, not legal advice.