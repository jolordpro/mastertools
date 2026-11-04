# Out-of-App PSD Tooling & External Control

Volatility: MEDIUM. Stamp 2026-07-10.

## PSD libraries — read/write without Photoshop

| Library | Lang | Read | Write | Character |
|---|---|---|---|---|
| **ag-psd** | JS/TS | Yes (common modes → RGB) | **Yes** (RGB only) | The capable writer. `useImageData:true` for raw Uint8/16/Float32 (avoids canvas alpha-premultiply corruption); 32-bit is LINEAR — gamma-correct to sRGB yourself; needs node-canvas server-side; you must supply pre-rendered bitmaps for text/vector/smart-object layers you touch |
| **@webtoon/psd** | TS | Yes (fast, zero-dep, WASM decode) | No | Parser only; `composite()` needs "Maximize Compatibility" saved into the file |
| **psd-tools** | Python | Yes | Structure-level; limited layer editing | 1.17.4 (2026-06); Pillow compositing incl. some adjustment layers; smart-object extraction with security-aware `open(external_dir=…)` |

**The universal round-trip caveat:** none of these regenerate the flattened composite after you change layer visuals — the stored composite goes stale until Photoshop re-saves (text edits via ag-psd trigger PS's "update text" warning). Deep fidelity on complex PSDs (nested smart objects, effects, adjustment stacks, 16/32-bit) is **⚠ partial and test-dependent** — run a round-trip test on a representative production template before trusting a pipeline.

**Choose libraries when:** high-volume server-side metadata/structure reads, layer extraction, fidelity-agnostic templated writes. **Choose Photoshop (or Firefly v2) when:** accurate compositing, filters, text rasterization, or smart-object rendering matter — i.e., anything broadcast-facing.

## External drivers (all require a RUNNING GUI Photoshop)

| Route | Platform | Mechanism |
|---|---|---|
| **photoshop-python-api** (loonghao) | Windows | COM (`Photoshop.Application`) wrapping the ExtendScript DOM synchronously — the workhorse for Python pipeline glue |
| **AppleScript / JXA** | macOS | Scripting dictionary + `do javascript` bridge into ExtendScript |
| **Remote Connections ("Kevlar")** | Both | Preferences → Plug-ins → Enable Remote Connections (password + restart) → TCP **49494**; encrypted messages carry ExtendScript in, results/thumbnails/events out. Python: `kyamagu/photoshop-connection` (event subscription: imageChanged, currentDocumentChanged, …). ⚠ Protocol internals are community-reverse-engineered — read the library source before building a driver |
| **Generator** | Both | `adobe-photoshop/generator-core`, Node pipeline over the same Kevlar plumbing; legacy, being phased out, Rosetta-bound on ARM like CEP |
| **CLI** | Both | ⚠ No documented switches beyond passing a file path; relative paths buggy; args don't reach scripts reliably. Do not design around the CLI |

**Headless truth:** there is no supported headless desktop Photoshop. Server-side = Firefly Services v2, full stop.

## AI-agent control (MCP) — proofs of concept, not Adobe-endorsed

- **mikechambers/adb-mcp** — MCP server → Node WebSocket **proxy** → UXP plugin. The proxy exists because UXP plugins can only be WS *clients*; something must listen.
- **alisaitteke/photoshop-mcp** — AppleScript/COM + optional UXP bridge; "recipe" tools wrap multi-step ops in one history state (a pattern worth stealing).
- **dcc-mcp/dcc-mcp-photoshop** — Rust broker + UXP WebSocket; **matrayu/adobe-mcp** — multi-app.
Pattern for an agent bridge: MCP server (or any orchestrator) ↔ localhost proxy ↔ UXP plugin dialing out; execute via batchPlay; group each tool call under one suspendHistory.

## BridgeTalk vs modern cross-app orchestration

BridgeTalk (see extendscript-legacy.md) is the only in-process PS↔AE bridge, but it chains you to ExtendScript on both ends. The modern shape for PS→AE pipelines: an external orchestrator (Python/Node) drives PS via COM/Kevlar/.psjs-with-file-handoff, writes assets + a JSON manifest, then drives AE via `aerender`/ExtendScript — looser coupling, testable stages, and each app scriptable in its native idiom. For handoffs, the JSON manifest should carry frame-rate and duration as integer frame counts so the AE side applies frameDuration/Math.round conventions without re-deriving timing.

## Color-managed export rules (scripted output)

1. **Convert, then embed:** for web/social delivery, `convertProfile` to sRGB and embed the profile explicitly in every scripted export. Untagged wide-gamut renders desaturated in sRGB-assuming consumers.
2. **Distrust Export As in scripts:** documented history of silent sRGB conversion, anomalous "uRGB" profile embeds, and 16→8-bit ProPhoto shifts. Prefer Save As / Save for Web (Legacy) paths, or convert explicitly first. (Reported)
3. Broadcast delivery: color/spec authority lives in the team's own spec sheets — this file governs only the scripting mechanics; the specs govern targets.
4. PS 27.8 adds OCIO 2.5 / ACES 2.0 support — relevant for cine-pipeline interchange; scripted OCIO behavior is ⚠ untested.

## Data-driven graphics (native, no code)

Image > Variables + Data Sets: bind layer visibility/pixel/text to CSV rows; export data-set files as batch output. Known 2026 bug: typing "P" in Variables/Data Set text fields toggles the Preview checkbox (see pitfalls). For heavier templating, the same job is usually better served by .psjs iterating a JSON/CSV, or Firefly v2 `create-composite` at scale.
