# NOTICE

**This notice is provided for information only. It is not legal advice.**

Copyright 2026 [Full legal name] (github.com/JPG-GITY)

Licensed under the Apache License, Version 2.0 — see [`LICENSE`](LICENSE).
This is the NOTICE file referred to by Apache-2.0 §4(d). A plain-text copy with
the same content is distributed as `NOTICE`; `NOTICE.md` is the rendered copy.

This repository mixes two kinds of material with two different rights layers.
Read this before reusing, redistributing, or relying on anything here.

## 1. What the Apache-2.0 grant covers

Everything in this repository is licensed under Apache-2.0 **except** the
material carved out in §2. The grant covers the repository owner's own original
work — for example `crawler/`, `updater/` (including its prompt templates),
`.github/`, `scripts/`, `config.yaml`, `requirements.txt`, `README.md`,
`SKILL_snippet.md`, and `skill/SKILL.md`.

The grant reaches only what the owner actually owns. No rights are claimed, and
none are granted, in the factual content taken from BytePlus documentation that
necessarily appears throughout these files — model IDs, endpoints, parameter and
field names, quotas and limits, prices, product names, documentation page titles
and URLs. Those facts and names belong to BytePlus / ByteDance Ltd. and its
affiliates, or to no one; the Apache-2.0 grant in `LICENSE` neither covers them
nor implies any permission from BytePlus regarding them.

## 2. BytePlus documentation content (carved out)

### 2.1 `docs_cache/` — not licensed

`docs_cache/` contains **verbatim** rendered text of BytePlus product
documentation pages (https://docs.byteplus.com), captured as markdown snapshots.

This content is the property of BytePlus / ByteDance Ltd. and its affiliates and
remains subject to BytePlus's own website and documentation terms and any
agreement between you and BytePlus. It is **not** licensed by the repository
owner: the Apache-2.0 grant does not extend to it, no rights in it are granted
here, and nothing in this repository should be read as permission from BytePlus
to copy, redistribute, or republish BytePlus documentation. Do not redistribute
these files. For any reuse beyond what BytePlus's own terms and applicable law
already allow, obtain permission from BytePlus.

### 2.2 `skill/references/` and `skill/sources.json` — two layers

These are editorial summaries written from BytePlus documentation
(`skill/references/`) and an index of BytePlus documentation page titles and URLs
(`skill/sources.json`). Two layers apply at once:

- **The owner's layer, licensed under Apache-2.0:** the selection, condensation,
  arrangement, wording, structure, and compilation of these files. This is what
  makes the skill installable and redistributable.
- **The BytePlus layer, not licensed here:** the underlying documentation
  content and factual detail described in them, and any wording reproduced from
  BytePlus documentation. That remains the property of BytePlus / ByteDance and
  subject to BytePlus's own terms, exactly as in §2.1.

**Permission to install and use the skill:** you may download, install, and
redistribute the skill folder or the release zip (`skill/SKILL.md`,
`skill/references/`, `skill/sources.json`) — including inside your own or your
employer's organization — under Apache-2.0, provided you keep `LICENSE` and this
NOTICE with it (see §6) and provided your use of the underlying BytePlus content
complies with BytePlus's own terms.

## 3. Not an official BytePlus or ByteDance product

This is a personal project on a personal GitHub account. It is **not** an
official BytePlus or ByteDance product, release, or service. It is not
maintained, reviewed, endorsed, or supported by BytePlus or ByteDance, and it
does not speak for them. The repository owner is a BytePlus employee but
publishes this in a personal capacity; all editorial choices, and any errors, are
the owner's own and not BytePlus's.

## 4. Accuracy — verify before you rely on this

The snapshots and reference files here are point-in-time, produced by an
automated crawler, and rewritten by a language model. The rewrites are
auto-committed on a schedule with no human review, and the "never invent model
IDs, parameters, limits, or prices" rule is a prompt-level instruction, not a
validated guarantee. Content can be stale, incomplete, silently degraded by
upstream site changes, or simply wrong.

**The official BytePlus documentation at https://docs.byteplus.com is the only
authoritative source.** Confirm model IDs, parameters, quotas, regions,
endpoints, limits, pricing, and compliance requirements against the official
docs — or with BytePlus directly — before relying on anything here, especially
for production, contractual, or commercial decisions. Everything here is
provided "as is", without warranties of any kind, and with no service-level or
support commitment.

## 5. Trademarks

BytePlus, ByteDance, ModelArk, Seed, Seedream, Seedance, Seed Audio, VideoPilot,
and related names, logos, and product names are trademarks or registered
trademarks of ByteDance Ltd. and/or its affiliates. The repository owner's intent
is nominative, descriptive use only — to identify the products this project
documents. No trademark license is granted by Apache-2.0 (see its §6) or by this
notice, and no affiliation, sponsorship, or endorsement is implied or claimed. If
BytePlus or ByteDance considers any use of its marks here — including the
repository name, the skill name `byteplus-genius`, or the "BytePlus Genius"
persona — inappropriate, see §7. All other trademarks belong to their respective
owners.

## 6. If you redistribute

Keep `LICENSE` and this NOTICE alongside anything you redistribute from here,
including the skill folder and the release zip. Do not redistribute
`docs_cache/` (§2.1). Do not present redistributed copies as an official
BytePlus or ByteDance product, and do not imply endorsement.

## 7. Rightsholder, trademark, and removal requests

If you represent BytePlus or ByteDance — or any other rightsholder — and want
content here changed or removed:

- **Primary (private):** email [contact email] — [Full legal name], repository
  owner. As a BytePlus employee the owner is also reachable through internal
  BytePlus channels, which is the preferred route for anything confidential.
- **Fallback:** open an issue on the repository (public — please do not put
  confidential material there).

Requests will be actioned within 5 business days of receipt, and content will be
removed on request without requiring a formal legal notice.

---

**Reminder: this notice is informational only and is not legal advice.** Have
BytePlus legal, or your own counsel, review before relying on it.

