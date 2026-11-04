# Hybrid C++ Addons, WebView & Spectrum Web Components

Volatility: MEDIUM. Stamp 2026-07-10. Version facts → `current-versions.md`.

## C++ hybrid addons (.uxpaddon)

**What:** N-API-style native modules bundled inside a UXP plugin (Photoshop only; since PS 24.2; UDT 1.7.0+ to develop, CC Desktop 5.10+ to distribute). Manifest v5 + `enableAddon: true` + addon entry in the manifest. Concept mirrors Node.js C++ addons: JS calls in, native code runs, results marshal back over a message bridge.

**Reach:** generic native compute (pixel kernels, codecs, native libs), plus — since PS 26 — the **Photoshop C++ SDK suites** from inside the addon: expose `PSDLLMain(selector, SPBasicSuite*, PIActionDescriptor)`, acquire suites (`kPSActionDescriptorSuite`, `kPSUXPSuite`; `PIUXPSuite` gives CSDK↔UXP messaging via `SendUXPMessage`/`addSDKMessagingListener`). This is NOT a classic SDK plugin: nothing appears in Filter/File menus — choose the classic C++ SDK for menu-resident filters/formats.

**Build & ship (Verified — Adobe hybrid docs / Bolt UXP):**
- CMake + MSVC (VS2019 recommended) / Clang; rename the compiled binary to `.uxpaddon`.
- Sign + notarize **the executables only** (not the whole bundle): real Apple Developer cert (self-signed rejected; ≥1 year validity) on macOS, Authenticode on Windows.
- Marketplace constraints: **admin credentials at install**, bundle ≤ **50 MB**, and all three architectures mandatory — Mac ARM, Mac Intel, Windows Intel (no partial submissions).
- UDT hot-reload does NOT reload native binaries: unload plugin → rebuild → load.
- Debug builds fail to load in the wild ("Failed to load Addon") — ship release, signed.
- bolt-uxp ships hybrid templates plus `yarn win-sign` / `yarn mac-build` scripts and a GitHub Action.

**When:** tight pixel loops the Imaging API feeds you (JS is too slow per-pixel), linking native libraries, latency-critical compute under a modern UI. Otherwise skip the signing/tri-arch tax.

## WebView (`<webview>`)

**What:** a real browser window embedded in a UXP panel — the sanctioned escape hatch for full web rendering. Manifest v5 + `webview` permission (`domains`, `enableMessageBridge`); element attributes include `uxpAllowInspector="true"` for DevTools.

**The platform split (Verified):**
- **Windows: WebView2** (Chromium/Edge) via Adobe's shared "UXP WebView" installer (`C:\Program Files\Common Files\Adobe\...\EdgeWebView`).
- **macOS: WKWebView** (WebKit).
Feature/behavior parity is NOT guaranteed — test storage, media, and CSS on both. Adobe disabled WebView2 gestures (pinch/swipe/zoom) to match WKWebView.

**Version gates:** WebViews in dialogs since UXP 6.0; in panels since UXP 6.4; **local HTML content requires UXP 8.0+** (`plugin:` protocol from plugin/plugin-data/plugin-temp folders) — ≤7.4.3 is remote/localhost-only.

**postMessage bridge:**
- `enableMessageBridge: "localOnly"` or `"localAndRemote"` is REQUIRED or messaging is silently dead (PS 26.6 regression made this explicit).
- Envelope asymmetry: messages from the WebView arrive with `e.source` = the `HTMLWebViewElement`; from the plugin side, the page sees `e.source` = `window.uxpHost`.
- ArrayBuffer over the bridge serializes to an empty object and is slow (Reported) — send base64/JSON, keep payloads small.
- Local-content WebViews can't use `localStorage`; links don't spawn new windows.

**Cost:** each WebView is multiple OS processes — real memory and startup weight. Use only when the UXP HTML subset genuinely can't render the experience (3D/WebGL, video-heavy, OAuth flows, existing web apps).

## What UXP's own renderer lacks (why WebView exists)

UXP is V8 + Adobe's limited HTML/CSS interpreter — NOT a browser. Missing vs Chromium: `<iframe>`, `window.location` navigation, `@font-face`, `data-*` attributes, CSS float (flexbox-first), `getElementsByClassName` (use querySelectorAll), jQuery compatibility; `<ul>/<li>/<i>` render as divs; canvas is 2D-partial. Check the UXP changelog before assuming a 2021-era "unsupported" listing still holds — several gaps (2D canvas, drag-drop, Intersection/ResizeObserver) were filled later.

## Spectrum Web Components (SWC)

- Supported since **UXP 7.0**, later out of beta; enable via `enableSWCSupport: true` (implies CSSNextSupport). Consume through `swc-uxp-wrappers` (npm); React sample exists.
- Adobe: UXP-SWC support spans **~30 components**, including table, toast, card — richer than the older Spectrum UXP widgets.
- Production-readiness varies per component (tab/spacebar navigation bugs existed, since fixed) — smoke-test the specific components you ship on your minVersion. ⚠ Per-component maturity is a hands-on-verify item.
- Styling: Spectrum tokens give native Photoshop look/theming (light/dark follows host).

## Localhost daemon pattern (the other escape hatch)

When a panel needs what neither hybrid nor WebView grants (arbitrary process spawning, watching folders, system-wide access): ship a separate Node/Python daemon; the UXP panel talks to it over `fetch`/WebSocket on localhost (network permission must list localhost + 127.0.0.1 explicitly).
- **Reliability:** high once installed; you own port selection, lifecycle (launchd/Service/login item), and reconnection logic.
- **Security:** bind 127.0.0.1 only; authenticate the channel (shared token); the daemon is a real attack surface — treat like any local service.
- **Distribution cost (the catch):** the daemon cannot ship inside the .ccx — separate installer, notarization, updates, and Marketplace review questions. For internal tools this is fine; for public distribution it's the main deterrent.
- UXP plugins can be WebSocket **clients only, not servers** — the daemon always listens, the panel always dials (this asymmetry is why MCP bridges use a proxy; see psd-tooling-and-external-control.md).
