# ModelArk Trusted Asset Library (Private Virtual Portrait Library) API

The official, fully-programmatic (server-to-server) way to register characters/faces as **trusted assets** so Seedance 2.0 video generation will accept them — because under Trusted Outputs an unverified real human face is otherwise **intercepted** (blocked) at generation time.

## Contents
1. What it is & why
2. Prerequisites & authentication
3. API list
4. Async lifecycle
5. `CreateAssetGroup` — key request fields
6. `CreateAsset` — key request fields
7. Image content rules & portrait best practices
8. Using the asset in generation
9. Latency & approval
10. Rate limits
11. Constraints & Gotchas

---

## 1. What it is & why

ModelArk exposes a **Trusted Asset Library** — the console surfaces it as the **Private Virtual Portrait Library** — as a set of control-plane APIs. It is the official, fully-programmatic path to register a character or a real human face so it becomes an **approved trusted asset** that Seedance 2.0 will accept as a reference.

The reason it exists is the **Trusted Outputs** biometric policy (see `video-seedance.md` §7): Seedance 2.0 **intercepts** generation when a reference contains an unverified real human face. A real face must be turned into a **trusted asset first**, or the generation request is blocked. This API is the server-to-server equivalent of the interactive ComfyUI verified-person / liveness route documented in `video-seedance.md` §7 — same outcome (a trusted `Asset_Id`), driven entirely by API calls.

The library spans two asset kinds, each with its own sub-library:
- **Virtual Avatar** — virtual/synthetic characters.
- **Real-human Portrait** — real human faces.

## 2. Prerequisites & authentication

| Prerequisite | Detail |
|---|---|
| **Advanced Creation Rights** | Must be enabled on the account. The quota is **shared** between the **Virtual Avatar** library and the **Real-human Portrait** library — both draw from the same allowance. |
| **One-time authorization letter** | The **first** `CreateAssetGroup` call is gated by a one-time authorization letter that must be completed **in the console**. Until it is signed once, group creation fails. |
| **AK/SK (Access Key) auth** | These are **control-plane** APIs signed with **Access Key / Secret Key signature** auth. ⚠️ They do **NOT** use the generation/data-plane API key (the `Authorization: Bearer $ARK_API_KEY` used by `/contents/generations/tasks`). Signing with the wrong credential fails. |

**Region / service / version — MEASURED 2026-09-11 (live signed calls).** The library is a control-plane service consumed by Seedance (2.0 and 2.5), which is **AP-Southeast-only**, so its assets live in `ap-southeast-1`.

| Signing input | Value |
|---|---|
| Host | `ark.ap-southeast-1.byteplusapi.com`: **`byteplusapi.com`**, not the data-plane `ark.ap-southeast.bytepluses.com` |
| Request | `POST https://ark.ap-southeast-1.byteplusapi.com/?Action=<Action>&Version=2024-01-01`, JSON body, `Content-Type: application/json` |
| `Service` | `ark` |
| `Version` | `2024-01-01` |
| `Region` | `ap-southeast-1` |
| Algorithm | `HMAC-SHA256`; credential scope `<YYYYMMDD>/ap-southeast-1/ark/request`; signed headers `content-type;host;x-content-sha256;x-date` (sorted, lower-case) |

Confirmed by a successful `GetAssetQuota` whose `ResponseMetadata` returned Service `ark`, Version `2024-01-01`, Region `ap-southeast-1`.

**Temporary STS credentials (MEASURED 2026-09-11).** A temporary key (AccessKeyId starting `AKTP…`, plus SecretKey and session token) authenticated when the token was **both** sent as the `X-Security-Token` header **and** included in the signature: `x-security-token:<token>` is added to the canonical headers, where it sorts **last**, and to `SignedHeaders` (`content-type;host;x-content-sha256;x-date;x-security-token`). This matches the official `byteplussdkcore` SignerV4. An expired token fails with `ExpiredToken` / `InvalidSecretToken` ("token expired"). Permanent IAM keys (`AKLT…`) need no token. <!-- MEASURED 2026-09-11: keep unless a live test reverses it -->

## 3. API list

Ten Actions from the source, split into group-level and asset-level CRUD, plus `GetAssetQuota` (measured, last row):

| API (Action) | Kind | Purpose |
|---|---|---|
| `CreateAssetGroup` | Group · write | Create an asset group (the container / person identity). Required before any asset. The **first-ever** call triggers the one-time authorization letter (§2). |
| `CreateAsset` | Asset · write | Upload an image/character into a group. **Asynchronous** — returns immediately; processing & approval happen in the background. |
| `GetAsset` | Asset · read | Fetch one asset, including its `Status`. **Poll this** until `Status` = `Active`. |
| `GetAssetGroup` | Group · read | Fetch one asset group's details. |
| `ListAssets` | Asset · read | List assets (within a group). |
| `ListAssetGroups` | Group · read | List asset groups. |
| `UpdateAsset` | Asset · write | Update an asset's metadata. |
| `UpdateAssetGroup` | Group · write | Update a group's metadata. |
| `DeleteAsset` | Asset · write | Delete an asset. |
| `DeleteAssetGroup` | Group · write | Delete a group. |
| `GetAssetQuota` | Account · read | *(Measured 2026-09-11; not in the source's list.)* Read-only, no side effects, empty body `{}`. The response includes `aigc_writable`, `liveness_writable`, `max_assets` and `projects[]`. **The cheapest credential check**: it proves AK/SK (+ STS token), the signature and the IAM policy before any write. `aigc_writable` / `liveness_writable` show whether Advanced Creation Rights allow writes to the Virtual Avatar / Real-human libraries. |

The **per-Action documentation page URLs were not included in the source** — do not assume slugs. Find them under the ModelArk API reference on `docs.byteplus.com`.

## 4. Async lifecycle

The end-to-end flow is create-group → create-asset (async) → poll → use:

1. **`CreateAssetGroup`** → returns a group identifier (`GroupId`). (The very first call on the account requires the console authorization letter to be done, §2.)
2. **`CreateAsset`** into that group → **asynchronous**: it returns an asset identifier (`Asset_Id`) with `Status` = `Processing`. Approval/processing runs in the background.
3. **Poll `GetAsset`** until `Status` transitions out of `Processing`:

   | `Status` | Meaning |
   |---|---|
   | `Processing` | Still being processed/approved — keep polling. |
   | `Active` | Approved and usable as a trusted asset. |
   | `Failed` | Rejected (moderation/quality) — a terminal state; do not blindly retry. |

4. Once `Active`, reference the asset in Seedance 2.0 or 2.5 generation via `asset://<Asset_Id>` (§8).

*Measured 2026-09-11:* `GetAsset` returned `Id`, `Status`, `URL` (12 h signed), `GroupId` and `ProjectName`. No error/reason field was seen.

## 5. `CreateAssetGroup` — key request fields

| Field | Notes |
|---|---|
| `ProjectName` | The ModelArk **project** the group belongs to. ⚠️ It **must match** the project of the inference endpoint that will later consume the asset — see project isolation in §11. |

`CreateAssetGroup` returns the group's `GroupId`, which subsequent `CreateAsset` calls attach to. The source did **not** enumerate any additional group fields (e.g. a display name) — do not assume field names beyond the above; check the API reference.

## 6. `CreateAsset` — key request fields

| Field | Notes |
|---|---|
| `Moderation.Strategy` | `Default` (run the standard moderation pre-filter) or `Skip` (bypass it). ⚠️ To make `Skip` take effect you must **first turn off the pre-filter on the console** — setting `Skip` alone, without disabling the console pre-filter, does not work. |
| `ProjectName` | Same project the group lives in; obeys the same project-isolation rule as §5 / §11. |

`CreateAsset` is **asynchronous**: it returns an `Asset_Id` and an initial `Status` of `Processing` (§4). The source did **not** enumerate the exact field/JSON path for the uploaded image payload itself — confirm the input field in the API reference rather than assuming one.

## 7. Image content rules & portrait best practices

The uploaded image must satisfy ModelArk's **image content rules** (content-moderation / policy compliance); an image that violates them lands in `Failed`. For **real** faces, consent and likeness rights to the person are the customer's responsibility (consistent with the Trusted Outputs terms in `video-seedance.md` §7).

Best-practice **portrait shots** to maximise the odds of reaching `Active` (general photographic guidance):
- A **single**, clearly-visible subject.
- **Front-facing**, unobstructed face (no heavy occlusion, sunglasses, or extreme angles).
- **Good, even lighting**; a clean/neutral background.
- **High resolution**, no heavy filters or artefacts.

**Single-image upload limits** (Trusted Asset Library guide, character-image example):

| Constraint | Documented limit |
|---|---|
| Format | JPEG, PNG, WEBP, BMP, TIFF, GIF, HEIC/HEIF |
| Width and height | each side between **300 and 6000 px** (written as the open interval `(300, 6000)`; exactly 300 or 6000 px was not tested) |
| Aspect ratio (width / height) | between **0.4 and 2.5** (open interval `(0.4, 2.5)`) |
| File size | **< 30 MB** per image |

Check these locally before `CreateAsset`. Otherwise an out-of-range image is only discovered after upload, when processing ends in `Failed`, and `GetAsset` gives no reason field (§4). The same guide says to add only assets that inference actually needs, and to put several images of the same person into one group for consistency.

## 8. Using the asset in generation

Once an asset is `Active`, feed it into a Seedance 2.0 generation request by its handle, and reference it **positionally** in the prompt:

- **Handle in the payload:** use `asset://<Asset_Id>` inside `content[]` — image assets in `image_url.url`, audio assets in `audio_url`.
- **Reference in the PROMPT by position, not by ID:** in the prompt **text**, refer to the asset by its **ordinal position** among the content items — **"Image N" / "Video N" / "Audio N"** — and **never by the Asset ID**. Referencing the raw Asset ID in the prompt won't bind.
- **Signed URLs valid 12 h:** the `asset://` handle resolves to a **signed URL valid for 12 hours**. Consume it promptly; any exported signed URL expires after 12 h.
- **Seedance 2.5 accepts `asset://` (MEASURED 2026-09-11).** `dreamina-seedance-2-5-260628` generated from an `asset://` image as `Image 1` (prompt: "the character in Image 1"), 480p / 5 s, with identity preserved. A single request with two `asset://` images (`Image 1`, `Image 2`) plus one reference audio also generated.
- **Deleted or unknown asset → synchronous 400 (MEASURED 2026-09-11).** If an `asset://` in `content[]` was deleted or never existed, the create POST fails immediately with HTTP 400 `InvalidParameter`, message `The specified asset asset-… is not found`, and no task is created. Validate stored asset IDs (`GetAsset` / `ListAssets`) before submitting, and drop IDs that come back not found instead of retrying. <!-- MEASURED 2026-09-11 -->

## 9. Latency & approval

Stated plainly, because it drives how you must integrate:

- `CreateAsset` is **asynchronous** and **may queue** — approval is **not** instant, and the asset is **not** usable the moment `CreateAsset` returns.
- **Video assets are slower** to process than image assets.
- The **upload-time SLA is NOT guaranteed**, and **no numeric time range is published** in the source. Do **not** hard-code an expected wait or a fixed timeout tuned to a guessed duration.
- The only correct pattern is to **poll `GetAsset` until `Status` = `Active`** (with backoff), treating `Failed` as a terminal rejection.
- **One data point (MEASURED 2026-09-11):** a single Seedream-generated image, passed by a freshly-issued URL, went `CreateAsset` → `Active` in **~5 s**. This is an observation, not an SLA; keep the polling loop and don't tune a timeout to it.

## 10. Rate limits

The Asset APIs are control-plane operations and are subject to rate limiting, but the source did **not publish specific QPS/RPM figures** for them.

| Operation class | Actions | Published limit |
|---|---|---|
| Asset/group **writes** | `CreateAssetGroup`, `CreateAsset`, `UpdateAsset`, `UpdateAssetGroup`, `DeleteAsset`, `DeleteAssetGroup` | Not stated in source |
| Asset/group **reads** (incl. polling) | `GetAsset`, `GetAssetGroup`, `ListAssets`, `ListAssetGroups` | Not stated in source |

Apply the platform-wide ModelArk rule (`enterprise-ops.md` §3): any published limit is a **theoretical maximum, not a guarantee** — ramp gradually and add backoff, especially on the `GetAsset` polling loop.

**Pagination (MEASURED 2026-09-11).** `ListAssetGroups` and `ListAssets` take `PageNumber` + `PageSize` and a `Filter` object (e.g. `Filter.GroupIds`, `Filter.Name`, `Filter.Statuses`). A `PageSize` above **100** is rejected with `InvalidParameter.PageSize` (measured on `ListAssets`; assume the same cap for `ListAssetGroups`). Walk pages until one returns fewer than `PageSize` items.

## 11. Constraints & Gotchas

- ⚠️ **Wrong credential class.** These are AK/SK-signed **control-plane** APIs. The **data-plane generation API key** (`Bearer $ARK_API_KEY`) does **not** authenticate them.
- ⚠️ **Project isolation.** An asset's `ProjectName` must **match the project of the inference endpoint** that consumes it. A mismatch means the asset is effectively invisible to that endpoint's generations.
- ⚠️ **IAM policy.** Grant `ark:*Asset*` to the sub-account/role so it can create/get/list/update/delete assets and groups.
- ⚠️ **One-time authorization letter.** A purely programmatic first run fails: the **first `CreateAssetGroup`** is gated by a console authorization letter that must be completed once in the console (§2).
- ⚠️ **`Moderation.Strategy: Skip` needs console prep.** `Skip` only takes effect after you **turn off the pre-filter on the console first**; otherwise it is ignored.
- ⚠️ **Async, not synchronous.** Never treat a `CreateAsset` response as "ready" — poll `GetAsset` to `Active` before using the asset (§9).
- ⚠️ **Prompt referencing.** In the prompt text, reference assets **positionally** ("Image N / Video N / Audio N"), **never by Asset ID** (§8).
- ⚠️ **Shared quota.** Under Advanced Creation Rights, the **Virtual Avatar** and **Real-human Portrait** libraries share **one** quota allowance.
- ⚠️ **12 h signed URLs.** `asset://` resolves to a **12-hour** signed URL — don't cache/export it for longer.
- ⚠️ **Never enumerate a shared project to build a UI.** A project can hold **thousands** of asset groups: one shared project had **8,645** AIGC groups on 2026-09-11, which is 87 pages at `PageSize` 100. Listing them all for a picker takes minutes and can freeze or crash a desktop client. Store the group IDs you created, validate them with **one** `ListAssetGroups` call filtered by `Filter.GroupIds`, and find other groups by `Filter.Name` with a small page cap.
- ⚠️ **Wrong host class.** The asset APIs are signed against `ark.ap-southeast-1.byteplusapi.com` (§2), not the data-plane `ark.ap-southeast.bytepluses.com`.
- ⚠️ **STS tokens must be signed.** `X-Security-Token` goes in the headers **and** in `SignedHeaders` (§2).
- ⚠️ **Stale `asset://` → sync 400** `InvalidParameter` "The specified asset asset-… is not found" (§8). <!-- MEASURED 2026-09-11: keep unless a live test reverses it -->
- ⚠️ **Validate images before upload** against the documented limits: JPEG/PNG/WEBP/BMP/TIFF/GIF/HEIC/HEIF, each side 300–6000 px, ratio 0.4–2.5, < 30 MB (§7).
