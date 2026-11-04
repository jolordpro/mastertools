# Current Versions — THE volatile-facts file

**Stamp: 2026-07-10.** Volatility: HIGH — recheck at every Tier A preflight; treat all facts here as expired if this stamp is >30 days old. No other file in this skill may state current version facts; they must point here.

## Photoshop desktop

| Channel | Version | Confidence | Notes |
|---|---|---|---|
| Shipping (PS 2026) | v27.8 — "June 2026 release" | ⚠ Reported | Research pass dated 2026-07-10; the helpx release-notes page crawl showed mixed-era text ("current is 27.0" alongside 27.2–27.7 fixes). Verify at helpx release notes before quoting. Win 10+ / macOS 14.0+. |
| LTS (PS 2025) | v26.11.6 | ⚠ Reported | Same caveat; verify. |
| Beta | 27.8.0 20260510.m.3537 | Verified 2026-05-12 | The build carrying the "UXP backend modernization" (community.adobe.com announcement, verified verbatim 2026-07-10). Adobe: not expected to change plugin look/feel — report regressions. |

## UXP

| Fact | Value | Confidence |
|---|---|---|
| Official UXP↔PS mapping | Table ends at **UXP 8.1 → PS 26.1** (8.0→26.0, 7.4→25.5, 7.3→25.2, 7.2→25.0, 7.0→24.4, 6.0→23.3, 5.5→23.0) | Verified (AdobeDocs table, last updated 2024-11-28; confirmed not extended as of 2026-07-10) |
| UXP version in PS 27.0–27.8 / Beta | **UNKNOWN — undocumented by Adobe** | ⚠ Uncertain. Resolve at runtime: `require("uxp").versions.uxp`. PENDING: console probes. |
| V8 engine in UXP | 9.4.146.24 (last stated, UXP 6 era) | ⚠ Uncertain — may have advanced silently |
| ECMAScript / React ceiling | ES5 + most ES6; React ≤16 | Verified (Adobe docs) |

## CEP

| Fact | Value | Confidence |
|---|---|---|
| Current CEP | **12.0.0.14 — the LAST major version** (security fixes only) | Verified (Adobe announcement, re-verified 2026-07-10) |
| CEP 12 runtimes | Chromium/CEF **99.0.4844.84** (branch 4844) · Node **17.7.1** · Node-WebKit **0.62.1** · V8 **9.9.115** | Verified (announcement + CEP 12 Cookbook + Adobe blog) |
| CEP 12 shipped with | PS 25.12 / Premiere 25.0 / AE 25.0 | Verified |
| Apple Silicon | CEP is **Rosetta-only in Photoshop** (no native ARM CEP in PS, unlike AI/ID/PPro) | Verified (Adobe, Ingo Eichel) |
| Removal date | **None published** as of 2026-07-10 | Verified-absent — recheck each preflight |

## ExtendScript / Generator

- ExtendScript: frozen (ES3-era), functional in 26.x/27.x, **no published removal date** as of 2026-07-10. Debug via VS Code ExtendScript Debugger (ESTK dead since 2020). (Verified/Reported)
- Generator Node.js: 18.13.0 in PS 26.0; 22.12.0 in Beta 26.4; **PS 27.x value unknown** ⚠. Generator is legacy, being phased out. (Verified for stated builds)

## Firefly Services Photoshop API

- **v1 End of Life: 2026, with two conflicting Adobe-published dates** — overview + v2-GA pages: "end of life on **July 31, 2026**"; deprecation page: "Deprecation Notice: April 20, 2026. End of Life (EOL): **August 31, 2026**." Both live and re-verified 2026-07-10. **Plan to July 31.** (Verified conflict)
- Lightroom API also EOL **July 31, 2026**, consolidating into Photoshop API v2. (Verified 2026-07-10)
- v2 file-size ceiling: 5 GB (v1: 2 GB). (Verified)

## Generative model churn

- **Firefly Image 3: removed from PS 27.6 picker April 28, 2026; fully removed from service August 2026** across all versions/plans. Replacement: Firefly Fill & Expand model. (Verified — Adobe announcement)
- PS 27.x Generate Image partner models: Firefly Image 5, FLUX.2 Pro, Gemini ("Nano Banana"), Topaz upscale models. (Reported — release notes/CG Channel)

## Runtime probes (paste results here when run)

```
Shipping PS:  require("uxp").versions.uxp = ________   app.version = ________
Beta PS:      require("uxp").versions.uxp = ________   app.version = ________
```
