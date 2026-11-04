# Runtime Decision Matrix

Volatility: LOW-MEDIUM (the trees are stable; version facts live in `current-versions.md`). Stamp 2026-07-10.

## Capability × runtime matrix

| Capability | ExtendScript (.jsx) | CEP panel | UXP plugin | UXP script (.psjs) | External driver | Cloud (Firefly Services v2) |
|---|---|---|---|---|---|---|
| Filesystem | Full (File/Folder) | Full (Node fs) | Sandboxed: plugin / request / fullAccess | Same, no persistence between runs | Full (host OS) | Cloud storage only (presigned URLs) |
| Spawn processes | No | Yes (child_process) | Only launchProcess (open), C++ addon, or localhost daemon | Same | Yes | N/A (managed) |
| Arbitrary network | Limited (Socket) | Full | fetch/XHR/WS to declared domains only | Same | Full | REST |
| Full web rendering | No | Yes (Chromium 99) | No — limited Adobe HTML/CSS interpreter; real browser only via `<webview>` | No UI at all | No | No |
| Pixel access | DOM + Action Manager | Via evalScript to JSX | Imaging API (direct buffers) | Imaging API | Executes JSX | Via API ops |
| UI richness | ScriptUI (dated) | Full HTML/CSS | Spectrum/SWC + limited HTML | None | Host UI only | None |
| Host DOM depth | Deep (DOM+AM) | Deep (through JSX bridge) | Deep (DOM + batchPlay) | Deep | Deep (executes JSX) | Medium (exposed ops + Run Action + server-side UXP scripting) |
| Distribution burden | Loose .jsx file | ZXP + ZXPSignCmd + Marketplace | CCX / Marketplace / UPIA | Script file | Your own installer | API keys |
| Apple Silicon | Native | **Rosetta-only in PS** | Native | Native | Native | N/A |
| Future-proofness | Low (frozen) | Low (last major) | **High — Adobe's bet** | High | Medium (COM/Kevlar semi-official) | **High — Adobe's cloud bet** |

## The 7-branch tree, with rationale

1. **Headless / server / volume → Firefly Services Photoshop API v2.** There is NO supported headless desktop Photoshop — every local path requires a running GUI instance and a seat. v2 covers edits, composites, execute-actions (ATN + ActionJSON + server-side UXP scripting, up to 10 mixed per request), manifest extraction, and the generative endpoints. It is also the only ToS-sanctioned route for bulk generative work. Cost: cloud-storage round-trips; only exposed operations (no Neural Filters yet).
2. **Rich panel UI, new → UXP plugin.** CEP would mean building on a frozen Chromium 99 runtime that can't run natively in PS on Apple Silicon. UXP is where Adobe ships new API surface (Imaging, action recording, SWC, WebView).
3. **Tight-loop compute + modern UI → UXP hybrid.** JS pixel loops are slow; the C++ `.uxpaddon` (PS 24.2+) runs native code, can reach Photoshop C++ SDK suites (PS 26+), and ships inside one UXP bundle. Costs: sign+notarize executables (real Apple cert), all three architectures, ≤50 MB, admin install.
4. **Menu-resident filter/format → classic C++ SDK plugin.** Hybrid addons don't appear in Filter/File menus; the classic SDK does.
5. **Batch/logic automation, no UI → .psjs** (modern JS, async DOM, Imaging API; but no persistent storage between runs — write state to files). ExtendScript only for maintaining existing .jsx or the rare API with no UXP equivalent.
6. **Repetitive GUI sequence, zero logic → Action + Droplet.** No code to rot, no signing, survives PS updates, teachable to non-developers. Convert to code later via "Copy as JavaScript" (→ batchPlay) or Alchemist if logic emerges.
7. **Cross-app / agent / external orchestration → external driver.** Windows COM (`photoshop-python-api`), macOS AppleScript (`do javascript` bridge), Remote Connections TCP 49494 (`photoshop-connection`), or MCP bridge (see psd-tooling-and-external-control.md). All require a running GUI Photoshop. BridgeTalk works but is ExtendScript-bound legacy.

## CEP migration tree (teams holding CEP panels)

```
Does the panel use Node child_process, native node modules,
or web APIs newer than Chromium 99?
├─ NO  → Straight port: UI → UXP + Spectrum/SWC,
│         evalScript JSX logic → batchPlay/DOM.
│         Plan it as a REWRITE, not a port (Benz: "complete
│         top-to-bottom rewrite"). CEP and UXP can coexist
│         during transition (Window > Extensions vs Plugins menu).
└─ YES → Relocate the native work first:
          ├─ compute-bound → C++ hybrid .uxpaddon
          ├─ external binaries (ffmpeg etc.) / full OS access
          │    → localhost daemon (see psd-tooling file, §daemon)
          └─ full web rendering needs → <webview> (UXP 8.0+ for
               local content; WebView2/WKWebView split applies)
Keep the CEP build only for users pinned to PS versions below
your UXP feature floor. Accelerate if: Apple Silicon perf
complaints, Marketplace pressure, or Adobe publishes a removal date.
```

## Feature detection & graceful degradation

- Gate on host version via manifest `host.minVersion`; branch in code via `require("uxp").host.version` and `require("uxp").versions.uxp`.
- apiVersion: manifest v5 + `data.apiVersion: 2` (default when minVersion ≥ 23.0.0); apiVersion 1 is deprecated and slated for removal — never start new work on it.
- Manifest v4 plugins still load but cannot use v5 features (permissions, WebView, hybrid, apiVersion selection); `show()` signature differs v4↔v5.
- Feature flags to know: `enableAlerts`, `enableSWCSupport` (implies CSSNextSupport), `enableFillAsCustomAttribute`. Beta-only APIs shift — check the UXP changelog at preflight (URLs in ecosystem-watchlist.md).

## When batchPlay beats the DOM

- Bulk reads (multiGet a whole layer tree in one call vs N proxy IPC hits).
- Anything the typed DOM hasn't wrapped yet (most new features land in batchPlay first).
- Multi-step edits batched in one descriptor array = fewer redraws, one history entry when paired with suspendHistory.
The DOM wins for readability on simple, well-wrapped operations. TypeScript: `@types/photoshop` official (accuracy imperfect — Reported), community `@adobe-uxp-types/*`, and bubblydoo/uxp-toolkit's Zod-validated `batchPlayCommand` for typed descriptors.
