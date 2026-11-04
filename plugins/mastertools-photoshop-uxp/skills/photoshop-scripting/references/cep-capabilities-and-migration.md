# CEP — Capabilities & Migration

Volatility: LOW (frozen platform; watch only for removal-date news). Stamp 2026-07-10. Exact runtime versions → `current-versions.md` (CEP 12 = Chromium 99.0.4844.84 / Node 17.7.1 / NW 0.62.1 / V8 9.9.115; last major version).

## What a CEP panel actually is

An embedded Chromium (CEF3) browser process per panel, plus optional Node.js, talking to the host app through PlugPlug. Two JS worlds: the panel's V8/Chromium context, and the host's ExtendScript engine, bridged by `CSInterface.evalScript(jsxString, callback)` — async, string payloads only (JSON-serialize both directions). The `<ScriptPath>` .jsx runs in the host's main thread.

## What Chromium-in-a-panel grants (CEP 12 = Chromium 99 feature level)

- Full HTML/CSS/JS: WebGL, WebAssembly, Web Workers, canvas, iframes, `window.location`, localStorage/IndexedDB (cookies persisted per Host_Version_Extension file), embedding remote sites.
- React/Vue/Angular and any browser-compatible npm package.
- **Node integration** (off by default since CEP 6.1): manifest `<CEFCommandLine><Parameter>--enable-nodejs</Parameter></CEFCommandLine>`, optionally `--mixed-context`. Grants `fs`, `child_process` (spawn ffmpeg/ImageMagick/anything), TCP/WebSocket servers, native modules **compiled against CEP's exact Node ABI**. In separate-context mode, Node lives under the `cep_node` global inside iframes.
- Other CEF switches via manifest: `--enable-media-stream` (WebRTC), `--allow-file-access-from-files`, remote-debugging port, custom UA.
- **DevTools**: a `.debug` file at the extension root maps host apps to debug ports → attach Chrome DevTools at `localhost:<port>`. Match your Chrome/Chromium version to CEF 99 for best behavior.
- **Adobe IPC Toolkit**: cross-app messaging from a panel (e.g., a panel in one CC app commanding another).

## The real restrictions

- **Chromium 99 (March 2022) forever.** Anything the web platform shipped after — newer CSS (has(), container queries as later stabilized), newer JS intl/APIs, updated codecs, TLS behaviors — is absent. Audit against caniuse pinned to Chromium 99.
- **CSP enforcement since CEP 11.1/CEF 88**: third-party sites that send frame-blocking CSP won't embed. **SameSite=Lax** default since CEF 88 — cross-site auth cookies need `SameSite=None; Secure`.
- **Apple Silicon: no native CEP in Photoshop.** Panels appear only when PS runs under Rosetta (≈50% perf penalty). This is Adobe's own stated migration driver and differs from Illustrator/InDesign/Premiere (which got ARM CEP 11).
- **Signing**: production panels must be ZXP-signed (see distribution-and-signing.md); development bypass = PlayerDebugMode flag per CSXS version.
- Per-version quirks: panel geometry/refresh bugs; Node `module`/`exports` globals colliding with AMD loaders; CEP 12 WebSocket regressions reported on PS 25.12/25.13 (rebuild node stack against 17.7.1).
- Resource cost: each panel is its own browser process — multi-panel suites get heavy.

## Manifest skeleton (reference)

```xml
<ExtensionManifest Version="5.0" ExtensionBundleId="com.example.tool" ExtensionBundleVersion="1.0">
  <ExtensionList><Extension Id="com.example.tool.panel" Version="1.0"/></ExtensionList>
  <ExecutionEnvironment>
    <HostList><Host Name="PHXS" Version="[24.0,99.9]"/><Host Name="PHSP" Version="[24.0,99.9]"/></HostList>
    <RequiredRuntimeList><RequiredRuntime Name="CSXS" Version="12.0"/></RequiredRuntimeList>
  </ExecutionEnvironment>
  <DispatchInfoList><Extension Id="com.example.tool.panel"><DispatchInfo>
    <Resources><MainPath>./index.html</MainPath><ScriptPath>./host/main.jsx</ScriptPath>
      <CEFCommandLine><Parameter>--enable-nodejs</Parameter></CEFCommandLine></Resources>
    <UI><Type>Panel</Type><Menu>Example</Menu>
      <Geometry><Size><Height>400</Height><Width>300</Width></Size></Geometry></UI>
  </DispatchInfo></Extension></DispatchInfoList>
</ExtensionManifest>
```
`<Size>` is mandatory (enforced since CEP 9). PHXS + PHSP host codes cover both SKUs.

## Migration to UXP — the working map

| CEP piece | UXP destination |
|---|---|
| HTML/CSS UI | UXP HTML subset + Spectrum/SWC — expect layout rework (no float, no iframe; flexbox-first) |
| evalScript → .jsx logic | batchPlay + typed DOM inside executeAsModal |
| Node fs | uxp.storage.localFileSystem + permission |
| Node child_process | C++ hybrid addon, or localhost daemon, or drop the feature |
| fetch/XHR anywhere | network permission with enumerated domains |
| localStorage/IndexedDB | plugin data folder files (plugins); nothing in .psjs |
| Embedded web app | `<webview>` (UXP 8.0+ for local content; WebView2/WKWebView split) |
| ZXP + ExMan | .ccx + Marketplace/UPIA |

Truths to set expectations with (Benz/Lumenzia postmortem, Verified): it is a **rewrite**, not a port; CEP and UXP panels coexist during transition (Window > Extensions "legacy" vs Plugins menu); gate the cutover on the UXP APIs your panel actually needs existing — check the UXP changelog, not vibes.

## When keeping CEP is correct (for now)

- Users pinned to PS versions below your UXP feature floor.
- Heavy child_process/native-module workflows not yet relocated (but schedule the relocation).
- No removal date is published — recheck at every preflight; a published date flips this section to "migrate now."
