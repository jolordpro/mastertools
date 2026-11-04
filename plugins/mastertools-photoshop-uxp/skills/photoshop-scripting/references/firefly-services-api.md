# Firefly Services Photoshop API (v2)

Volatility: HIGH on dates/endpoints (cloud API — recheck at Tier A preflight). Stamp 2026-07-10. EOL dates → `current-versions.md` (v1 dies 2026 — two conflicting Adobe dates; plan to July 31, 2026).

## What it is

REST, JSON, async job model. Base host `https://photoshop-api.adobe.io`. The only sanctioned headless Photoshop and the only ToS-clean route for bulk generative work. Auth: OAuth server-to-server — client_id/secret → IMS token (`https://ims-na1.adobelogin.com/ims/token/v3`), send `Authorization: Bearer` + `x-api-key`. I/O via presigned cloud-storage URLs (S3 / Azure / Dropbox) — no local file paths. SDK: `@adobe/photoshop-apis` + `@adobe/firefly-services-common-apis` (the older adobe-photoshop-api-sdk is deprecated).

## v2 endpoint map (Verified — developer.adobe.com, 2026-07)

| Endpoint | Does |
|---|---|
| `POST /v2/edit` | Document-level adjustments (autoTone, exposure, etc.) |
| `POST /v2/create-composite` | Create/convert documents; add/edit/delete layers (pixel, adjustment, shape, text); smart objects (incl. **linked**); artboards; layer export |
| `POST /v2/execute-actions` | Run .atn actions, inline **ActionJSON**, and **server-side UXP scripting** — up to 10 mixed per request. Convenience v1 endpoints (productCrop, depthBlur, splitView, text) folded in here via published ActionJSON |
| `POST /v2/generate-manifest` | Document/layer metadata extraction; embedded smart-object extraction without opening Photoshop |
| `GET /v2/status/{jobId}` | Unified job status (replaces per-service v1 status endpoints) |
Plus the Firefly generative endpoints alongside (Generate Image, Generative Fill/Expand, Object Composite, Upscale, custom models).

**v2 net-new:** server-side UXP scripting (conditional logic, layer iteration, data-driven edits, server-side Generative Fill/Expand); linked smart objects (v1 embedded-only → file bloat, 2 GB ceiling; v2 = 5 GB + references); artboards first-class; expanded layer metadata (text settings, blend ranges); SVG workflows.
**Known v2 gaps (2026-07):** Neural Filters / Depth Blur not yet supported; `fillToCanvas` unavailable. v1 vs v2 use different JPEG encoders — expect sub-1% pixel diffs at identical quality settings.

## v1 → v2 migration diffs (Verified — Adobe migration guides)

| v1 | v2 |
|---|---|
| `inputs[]` array | single top-level `image` object (execute-actions takes one input) |
| `options.actionJSON: [...]` inline array | `options.actions[].source.content` = **stringified** JSON + `contentType:"application/json"` |
| `options.additionalImages[]`, placeholder `ACTION_JSON_OPTIONS_ADDITIONAL_IMAGES_X` | `options.additionalContents[]`, placeholder `__ADDITIONAL_CONTENTS_PATH_X__` (old accepted) |
| `options.fonts[]` | `options.fontOptions.additionalFonts[]` |
| Fonts/brushes/patterns inline | binary resources must be external URLs |
| Manifest fields: `bitDepth`, `iccProfileName`, `name`, `height`+`width`, `photoshopBuild` | `depth`, `iccProfile`, `title`, `bounds`, (removed) |
| JPEG quality numeric | **string enum** `very_poor…photoshop_max` (numeric = validation error); default `photoshop_max` |
| Single-layer export at document/canvas size | defaults `cropMode:"layer_bounds"` — set `"document_bounds"` to match v1 output |
| PSD export | single-layer only in v2 |

## Request skeleton (execute-actions with ActionJSON)

```jsonc
POST /v2/execute-actions
{
  "image": { "source": { "url": "<presigned-input>" } },
  "options": {
    "actions": [{
      "source": {
        "content": "[{\"_obj\":\"imageSize\",\"width\":{\"_unit\":\"pixelsUnit\",\"_value\":1920}}]",
        "contentType": "application/json"
      }
    }]
  },
  "outputs": [{ "destination": { "url": "<presigned-output>" }, "type": "image/jpeg", "quality": "photoshop_max" }]
}
```
Poll `/v2/status/{jobId}` until `succeeded`/`failed`. ActionJSON here is the same descriptor grammar as local batchPlay — capture with Alchemist locally, escape/stringify, ship to the cloud. This is the highest-leverage pattern: prototype on desktop, run at scale serverless.

## Cloud vs local — capability split

| | Cloud v2 | Local scripting |
|---|---|---|
| Headless / no seat / horizontal scale | ✅ | ❌ (GUI app required, always) |
| Bulk generative (ToS-clean) | ✅ | ❌ (guardrails: "automatic scripting" = misuse) |
| Every command Photoshop can do | ❌ exposed ops + ActionJSON + UXP-script subset | ✅ full DOM + batchPlay |
| Interactive UI / user-in-loop | ❌ | ✅ |
| Direct pixel buffers | ❌ | ✅ Imaging API |
| Local files without cloud round-trip | ❌ | ✅ |

## Operational notes

- Batch execution: Firefly Services offers published-workflow batch runs with per-asset results — evaluate for recurring production pipelines before hand-rolling a job loop.
- Rate limits/pricing are account-tier dependent — confirm on the account, not from memory.
- Lightroom API is being consolidated into PS API v2 (EOL July 31, 2026) — Lightroom-style ops route here too.
- Keep credentials server-side; never embed client secrets in a panel (proxy via daemon/backend).
