# byteplus-docs-sync

Keeps the `byteplus-models-genius` Claude skill in sync with the BytePlus
documentation, automatically and on a schedule.

## How it works

```
BytePlus docs ──crawl──▶ docs_cache/*.md ──git diff──▶ changed pages
                          (snapshot = diff engine)            │
                                                              ▼
                          skill/references/*.md ◀──Claude rewrites──┘
                          skill/sources.json    ◀──regenerated every run──
```

1. **crawler/crawl.py** — enumerates every `/en/docs/{Product}/{id}` page from each
   product's landing nav, renders each to markdown, and snapshots it into
   `docs_cache/`. Git history is the diff engine.
2. **updater/update_skill.py** — asks git which snapshots changed, routes them to
   reference files (`config.yaml → routing`), and has Claude rewrite only the
   affected references. It also regenerates `skill/sources.json`.
3. **.github/workflows/sync.yml** — runs weekly, auto-commits changes, and posts a
   Slack "aviso" with the changelog.

## One-time setup

1. Push this repo to GitHub (private).
2. Put your actual skill under `skill/` (or point `skill_dir` in `config.yaml` at it).
   Keep `sources.json` inside the skill and paste `skill/SKILL_snippet.md` into your
   `SKILL.md` — that's what stops Claude from asking you to copy-paste.
3. Repo → **Settings → Secrets and variables → Actions**:
   - `ANTHROPIC_API_KEY` (required)
   - `SLACK_WEBHOOK_URL` (optional, for the aviso)
4. **Actions → byteplus-docs-sync → Run workflow**, tick **bootstrap** the first time.
   This lands the baseline snapshot + `sources.json` without spending model calls.
5. Commit the baseline, then let the weekly cron take over. From then on each run only
   touches references whose upstream docs actually changed.

## Tuning

- **Add products**: append slugs to `products:` in `config.yaml`.
- **Routing**: edit `routing:` rules to map doc topics → reference files
  (plain substring, or `/regex/`).
- **Renderer**: `playwright` (default, self-contained) or `jina` (no browser; set
  `JINA_API_KEY` as a secret for higher limits).
- **Noisy snapshots**: if nav/footer leaks into snapshots, refine `content_selectors`.

## Local dry run

```bash
pip install -r requirements.txt
python -m playwright install chromium
python crawler/crawl.py --config config.yaml --product ModelArk
git add docs_cache && git commit -m baseline    # establish diff baseline
python updater/update_skill.py --bootstrap       # build sources.json
```
