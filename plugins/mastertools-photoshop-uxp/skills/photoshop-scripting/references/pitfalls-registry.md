# Pitfalls Registry — symptom → cause → fix

Volatility: MEDIUM. Stamp 2026-07-10. Scan by symptom; each row carries versions affected and confidence. For current version numbers see `current-versions.md`.

## UXP runtime errors

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| "Event ... may modify the state of Photoshop ... only allowed from inside a modal scope" | State-changing call outside `executeAsModal` | Wrap in `await core.executeAsModal(fn, {commandName})` | apiVersion 2, PS 23+ | Verified |
| Silent no-ops; `core.mainThreadTimeOutCount` climbing | Commands issued while another modal scope holds the app, or without modal scope | Check `core.isModal`; serialize modal work; always `await` executeAsModal | UXP | Verified |
| Error naming another plugin when entering modal | Only one plugin may be modal at a time | Catch, retry/queue; inform user which plugin blocks | apiVersion 2 | Verified |
| batchPlay throws after user pressed Escape | Scope was cancelled; batchPlay refuses post-cancel | Check `executionContext.isCancelled` / `onCancel`; return promptly | apiVersion 2 | Verified |
| `document.layers` iteration is very slow | Each property access is an IPC round-trip | Single batchPlay `get` multiGet, or uxp-toolkit `UTLayer` tree parse | UXP all | Reported (bubblydoo) |
| Layer collection isn't an Array (it's a Proxy) | apiVersion 2 collections are proxies | Spread first: `[...app.activeDocument.layers]` | PS 23+ | Verified |
| `getPixels()` missing alpha on Grayscale/LAB | API bug: returns 1/3 components even with transparency (docs promise 2/4) | Select transparency channel via batchPlay, then `imaging.getSelection()`; align bounds manually | Current UXP | Verified (AdobeDocs issue #501) |
| 16-bit pixel values top out at 32768 | Photoshop's internal reduced 16-bit range | Set the full-range flag on getPixels for [0..65535] | Imaging API | Verified |
| Memory bloat after Imaging API work | ImageData held until GC | Call `.dispose()` on PhotoshopImageData promptly | Imaging API | Verified |
| Clarity/Grain/Dehaze adjustment layers invisible to scripting | New layer kinds not wired into UXP initially | Fixed in later 27.x; fall back to batchPlay by layer ID | PS 27.3 era | Verified (release notes) |
| `localStorage` undefined in a .psjs script | Scripts are throwaway contexts — no persistent storage | Write to a file via localFileSystem instead | .psjs all | Verified |
| alert/prompt/confirm missing | Moved to beta behind `enableAlerts` manifest flag (plugins only) | Add flag, or build a dialog | Recent UXP | Verified |
| "Permission denied" on fetch to localhost despite manifest entry | localhost/127.0.0.1 must be listed explicitly; known flaky | List both host forms; verify port; known bug reports exist — test on target versions | Manifest v5 | Reported |
| eval / new Function throws | Code generation blocked by default | `allowCodeGenerationFromStrings: true` (expect Marketplace scrutiny) | Manifest v5 | Verified |
| Plugin `show()` crashes after manifest v4→v5 move | Entrypoint signature changed between v4 and v5 | Update `show()` to the v5 signature | v4→v5 migration | Verified |
| Invisible/headless plugin never runs startup code from .ccx install | `entrypoints.plugin.create` fires once at install; v4 manifest or missing minVersion breaks it | Manifest v5 + correct minVersion | PS 27 era | Reported (GitHub issue #99) |

## WebView

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| postMessage between plugin and WebView silently dead | `enableMessageBridge` not set | Set `"localOnly"` or `"localAndRemote"` in the webview permission | UXP 6.4+; PS 26.6 regression | Verified/Reported |
| ArrayBuffer arrives as empty object over postMessage | Serialization bug; also very slow | Pass base64/JSON; keep payloads small | Current UXP | Reported |
| WebView won't load local HTML | Local content requires UXP 8.0+ (`plugin:` protocol); ≤7.4.3 is remote-only | Require PS 26.0+ (UXP 8) or host content remotely | UXP <8.0 | Verified |
| Gestures (pinch/swipe) don't work in Windows WebView | Adobe disabled WebView2 gestures to match WKWebView | Design without gestures | All | Verified |

## ExtendScript

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| Modern JS syntax throws immediately | Engine is ES3-era | Write ES3 or transpile; safe polyfills only (no Proxy/Symbol) | All | Verified |
| VS Code debugger won't attach / flaky | Known reliability limits of the extension | Restart host+VS Code; prefer self-contained scripts over ScriptUI-panel debugging | 2025+ | Reported |
| Cross-app call does nothing | BridgeTalk target app not running / wrong specifier | Launch target first; verify `BridgeTalk.getSpecifier` | All | Reported |

## CEP

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| Panel missing entirely in Photoshop on Apple Silicon | CEP does not run natively in PS on ARM | Run PS under Rosetta, or migrate to UXP | PS on Apple Silicon | Verified |
| Unsigned panel won't load in development | PlayerDebugMode not set | Set PlayerDebugMode=1 (per-CSXS-version plist/registry) | All CEP | Verified |
| Embedded third-party site blank | Site's CSP/frame-blocking; stricter since CEF 88 | Proxy the content or open externally | CEP 11.1+ | Verified |
| Cross-site cookies lost | SameSite=Lax default since CEF 88 | Server sets `SameSite=None; Secure` | CEP 11+ | Verified |
| jQuery/RequireJS conflicts (`module`/`exports` collisions) | Node integration injects globals | Guard/namespace; or `--mixed-context` awareness | CEP 8+ with Node | Verified |
| WebSocket connections broke moving to PS 25.12/25.13 | CEP 12 update changed behavior | Rebuild node modules against Node 17.7.1; test WS stack on CEP 12 | CEP 12 | Reported (Adobe forum) |
| Native node module fails to load | Compiled against wrong Node ABI | Rebuild against CEP's exact Node version (12.3.1 for CEP 10 / 15.9.0 CEP 11 / 17.7.1 CEP 12) | Per CEP | Verified |

## Signing / distribution

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| ZXP installs fine until one day it doesn't (cert expired) | No timestamp on signature | Always sign with `-tsa` (working TSA URL); ZXPSignCmd 4.1.3+ | All CEP | Verified |
| ZXPSignCmd segfaults / timestamp fails | Old ZXPSignCmd binary or dead TSA endpoint | Update to 4.1.3+; switch TSA | Older tools | Verified |
| Validly-signed ZXP shows blank panel after install | 2024 UPIA symlink bug | Install via host app as admin or ExManCmd; update CC Desktop | 2025-era CC | Verified (Adobe-CEP issues) |
| Hybrid plugin: "Failed to load Addon" | Debug build shipped, or unsigned/unnotarized binary | Ship release build; sign+notarize the executables (real Apple Dev cert, ≥1yr validity) | PS 24.2+ | Verified (Bolt UXP/Adobe) |
| Hybrid rejected by Marketplace | Missing an architecture | Ship all three: Mac ARM + Mac Intel + Win Intel; ≤50 MB | Hybrid | Verified |

## Color / export

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| Exported images look desaturated in browsers | Untagged wide-gamut output; browsers assume sRGB | Convert to sRGB + embed profile before export | All | Reported |
| Export As shifts colors / embeds "uRGB" / 16→8-bit ProPhoto shift | Documented Export As profile mishandling | Use Save As or Save for Web (Legacy); or explicit `convertProfile` first | PS 2022+ lineage | Reported |

## Generative

| Symptom | Cause | Fix | Versions | Confidence |
|---|---|---|---|---|
| Generative features suddenly restricted on an account | Anti-"automatic scripting" guardrails tripped | Stop scripting credit-based features; use Firefly Services for volume | All | Verified (credits FAQ) |
| Generative batchPlay descriptor broke after update | Descriptors are reverse-engineered, model churn (Firefly Image 3 removal Aug 2026) | Re-capture with Alchemist; never treat as stable API | 27.x | Verified (churn) / Uncertain (descriptors) |
