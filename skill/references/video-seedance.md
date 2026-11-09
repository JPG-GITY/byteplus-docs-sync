# Dreamina Seedance 2.0 Video Generation & VideoPilot

> **Note:** BytePlus has publicly announced that a newer **Dreamina Seedance 2.5** API is now live (promoted via `ai.byteplus.com/en/activity/seedance2-5`). At the time of this update, the linked ModelArk doc pages ([2222480](https://docs.byteplus.com/en/docs/ModelArk/2222480), [2291680](https://docs.byteplus.com/en/docs/ModelArk/2291680), [2607688](https://docs.byteplus.com/en/docs/ModelArk/2607688), [2607689](https://docs.byteplus.com/en/docs/ModelArk/2607689), [2608626](https://docs.byteplus.com/en/docs/ModelArk/2608626)) surface only this promotional banner — no model ID, parameter set, resolution/duration limits, or pricing for 2.5 were retrievable. This has since been re-confirmed against the slug-based doc URLs [seedance-2-0](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-0), [seedance-2-5](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5), [seedance-portrait-asset-guide](https://docs.byteplus.com/en/docs/ModelArk/seedance-portrait-asset-guide), and [seedance-2-5-prompt-guide](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5-prompt-guide) — all four currently render **only** the "Official Dreamina Seedance 2.5 API is now live 🚀 / Get your token package and be the pioneer / [Purchase]" banner, with no accompanying technical content. **Update:** the fifth page, [seedance-2-0-prompt-guide](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-0-prompt-guide), now renders its full technical content again (confirmed and re-captured in §8 below) — it is no longer banner-only. This does not contradict or supersede the biometric-compliance detail in §7 below (that remains sourced from the ComfyUI partner-node docs and the ModelArk Terms page cited there) — the ModelArk-hosted portrait-asset guide and the 2.5-specific pages are simply not yet retrievable as technical content, only as this marketing banner. Everything below therefore still describes **Seedance 2.0** (and 1.5 Pro where noted) and remains accurate; nothing here has been superseded by a confirmed 2.5 spec yet. <!-- TODO: verify — capture Seedance 2.5 model ID(s), resolution/duration/parameter support, and pricing once BytePlus publishes technical documentation (not just the purchase/marketing banner); also re-check seedance-portrait-asset-guide and seedance-2-5-prompt-guide once they render actual content again -->

## Contents
1. Models & specs
2. Resolution, 4K & 10-bit encoding
3. Parameter support matrix & input methods
4. Multimodal reference injection
5. Async task lifecycle
6. Frame math & video extension
7. Biometric compliance — "Trusted Outputs"
8. Video prompt engineering (the Advanced Formula)
9. Draft mode (Seedance 1.5 Pro only)
10. VideoPilot editing API
11. Pricing quick reference

---

## 1. Models & specs

Endpoint (AP Southeast only — video is **not** available in `eu-west-1`):
`POST https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks`

| Spec | Seedance 2.0 | Seedance 2.0 Fast | Seedance 2.0 Mini |
|---|---|---|---|
| Model ID | `dreamina-seedance-2-0-260128` | `dreamina-seedance-2-0-fast-260128` | `dreamina-seedance-2-0-mini-260615` |
| Resolutions | 480p, 720p, 1080p, **4k** | 480p, 720p | 480p, 720p |
| Default resolution | 720p | 720p | 720p |
| Aspect ratios | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, adaptive | same | same |
| Default ratio | adaptive | adaptive | adaptive |
| Duration | 4–15 s, or `-1` (auto) | 4–15 s, or `-1` | 4–15 s, or `-1` |
| Inference mode | online only | online only | online only |

- **Only the base `dreamina-seedance-2-0-260128` supports 1080p and 4k.** Fast and Mini top out at 720p.
- Mini reached API access on **June 22, 2026** (UTC+8); during the June 15–22 trial it was Playground-only with concurrency capped at 1.
- Note on naming: billing/pricing/resource-pack docs use the `dreamina-`-prefixed IDs above; the console and Elements/Digital-Character library URLs sometimes use the un-prefixed form `seedance-2-0-260128`. Both refer to the same model. (Seedance 1.5 Pro is `seedance-1-5-pro-251215`.)
- Prompt languages: all models support English; **Seedance 2.0 series additionally supports Japanese, Indonesian, Spanish, and Portuguese.** Recommended prompt length under ~1000 words.
- BytePlus has announced a **Dreamina Seedance 2.5** API as "now live" (see note at top of file), but no confirmed model ID or spec has been published yet — treat 2.5 as forthcoming, not yet documented. <!-- TODO: verify -->

## 2. Resolution, 4K & 10-bit encoding

Set via the **`resolution`** string. Valid values: `480p`, `720p`, `1080p` (not Fast/Mini), `4k` (base 2.0 only). Default `720p`.

**The 10-bit upgrade is implicit in `4k` — there is no separate bit-depth / HDR / pixel-format parameter.** Selecting `"resolution": "4k"` on `dreamina-seedance-2-0-260128` automatically yields:
- **10-bit encoding** (vs standard 8-bit), preserving richer color gradations and smoother tonal transitions — suitable for professional video production and HDR content.
- **H.265 (HEVC) codec.** Some players/browsers cannot play it directly — plan a decode/transcode path for previews.

4k pixel dimensions by aspect ratio (Seedance 2.0 series only):

| Aspect ratio | 4k (W×H) |
|---|---|
| 16:9 | 3840×2160 |
| 4:3 | 3326×2494 |
| 1:1 | 2880×2880 |
| 3:4 | 2494×3326 |
| 9:16 | 2160×3840 |
| 21:9 | 4398×1886 |

Video **reference inputs** also accept up to 4k (480p/720p/1080p/4k), frame rate [24, 60], each ≤200 MB, ≤3 clips totalling ≤15 s, total pixels per ref in [640×640=409600, 3326×2494=8295044]. Containers: MP4/MOV; video H.264/H.265, audio AAC/MP3.

## 3. Parameter support matrix & input methods

Two ways to pass `resolution`/`ratio`/`duration`/`frames`/`seed`/`camera_fixed`/`watermark`:
- **New (recommended)** — fields directly in the request body; **strict validation** (bad value → error). Write values in full (`"resolution": "720p"`), no abbreviations.
- **Legacy** — appended to
