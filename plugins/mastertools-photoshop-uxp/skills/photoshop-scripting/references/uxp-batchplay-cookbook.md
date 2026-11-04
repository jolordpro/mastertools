# UXP & batchPlay Cookbook

Volatility: LOW (grammar/semantics stable since apiVersion 2). Stamp 2026-07-10. Version facts → `current-versions.md`.

## Contents
1. Module map
2. executeAsModal discipline
3. History hygiene
4. batchPlay grammar
5. Descriptor discovery workflow
6. Imaging API
7. .psjs scripts
8. Action recording from UXP
9. Manifest v5 permissions
10. Debugging & diagnostics

## 1. Module map

```js
const ps = require("photoshop");
ps.app        // documents, activeDocument, layers (typed DOM)
ps.core       // executeAsModal, isModal, performance getters
ps.action     // batchPlay, addNotificationListener, recordAction
ps.imaging    // getPixels/putPixels/getSelection (was imaging_beta)
ps.constants  // enums incl. newer layerKind values (Grain, Clarity)

const uxp = require("uxp");
uxp.storage.localFileSystem   // sandboxed fs per manifest permission
uxp.shell                     // openExternal/openPath (launchProcess)
uxp.host / uxp.versions       // feature detection
```
DOM properties read synchronously (async under the hood); methods return Promises — `await` everything. apiVersion 2 collections are Proxies: spread to `[...app.activeDocument.layers]` before array ops.

## 2. executeAsModal discipline

Every state-modifying operation (document, app state, preferences, UI) must run inside:
```js
await require("photoshop").core.executeAsModal(async (executionContext, descriptor) => {
  // all mutations here
}, { commandName: "My Operation" });
```
Rules that prevent the classic failures:
- **Always `await` it.** Fire-and-forget causes interleaved modal states and silent drops.
- **One plugin modal at a time.** A collision throws an error naming the holder — catch and queue/retry.
- **Cancellation:** user Escape / Plugins → Cancel Plugin Command interrupts the scope. Poll `executionContext.isCancelled`, register `onCancel`, and return fast; batchPlay throws if called after cancellation.
- **Nested scopes** share one global modal state and progress bar. `executionContext.reportProgress({value, commandName})` drives the bar.
- **Interactive mode** exists for flows needing user input mid-scope (dialogs, Select-and-Mask style).
- While modal (non-interactive), Photoshop **silences event notifications** — other plugins can't observe your batchPlay.
- Read-only work (get descriptors, DOM reads) does NOT need modal scope — keep reads outside to stay responsive.

## 3. History hygiene

One script action = one undo step:
```js
await core.executeAsModal(async (ctx) => {
  const docID = app.activeDocument.id;
  const s = await ctx.hostControl.suspendHistory({ documentID: docID, name: "Batch Export Prep" });
  try {
    // ... edits ...
    s.finalName = "Batch Export Prep (12 layers)"; // optional rename
  } finally {
    await ctx.hostControl.resumeHistory(s);
  }
}, { commandName: "Batch Export Prep" });
```
Semantics: on normal return, suspended states commit as one entry; on an uncaught exception they are cancelled (automatic rollback); Photoshop auto-resumes suspension when the scope ends regardless. `Document.suspendHistory(name, fn)` is the light wrapper for single-doc cases. The old batchPlay history/UI options are deprecated — suspension is the mechanism.

## 4. batchPlay grammar

```js
const result = await require("photoshop").action.batchPlay(
  [ { _obj: "hueSaturation",
      _target: [ { _ref: "layer", _name: "Hero" },
                 { _ref: "document", _id: 42 } ],   // innermost → outermost
      adjustment: [ { _obj: "hueSatAdjustmentV2", hue: 10, saturation: -20, lightness: 0 } ],
      colorize: false } ],
  { modalBehavior: "execute" }
);
```
- **`_obj`** — the command/class (required everywhere).
- **`_target`** — reference chain of `{_ref, ...selector}`; selectors: `_id` (stablest), `_name`, `_index`, `_enum:"ordinal", _value:"targetEnum"` (current selection), `_property`.
- **`_unit` values** — `{_unit:"pixelsUnit"|"percentUnit"|"angleUnit"|"distanceUnit", _value: n}`.
- **Batching** — the first argument is an ARRAY: put serial steps in one call for fewer redraws and simpler history.
- **Options** — `modalBehavior: "wait" | "execute" | "fail"` (how to behave if the app is modal); `synchronousExecution: true` blocks the JS thread (the DOM uses it internally; avoid in new code).
- **Recording control** — `dontRecord`, `forceNotify`, `_isCommand` on descriptors.
- **Reads** — get descriptors are non-modifying and legal outside modal scope:
```js
const [doc] = await action.batchPlay([{ _obj: "get",
  _target: [ { _property: "title" }, { _ref: "document", _enum: "ordinal", _value: "targetEnum" } ] }], {});
```
- **Bulk reads** — one multiGet beats N DOM property hits by orders of magnitude on deep layer trees:
```js
const [tree] = await action.batchPlay([{ _obj: "multiGet",
  _target: { _ref: "document", _id: doc.id },
  extendedReference: [ ["name","layerID","visible","layerKind"],
                       { _obj: "layer", index: 1, count: -1 } ],   // all layers
  options: { failOnMissingProperty: false, failOnMissingElement: false } }], {});
// tree.list = flat array of {name, layerID, visible, layerKind}
```
(See uxp-toolkit's UTLayer for a maintained tree-parsing wrapper.)

## 5. Descriptor discovery workflow (the professional loop)

1. Perform the operation once by hand with **Alchemist** (jardicc) listening — copy the emitted descriptor.
2. Or: record an Action → panel flyout **"Copy as JavaScript"** → UXP-ready batchPlay.
3. Trim the descriptor to essentials (recorded output over-specifies); prefer `_id` targets over `_name`.
4. For legacy .jsx conversion: `adobe-uxp/ps-es-to-uxp` translates executeAction → batchPlay.
Never hand-invent descriptors from memory — grammar drifts per version; capture, then edit.
UXP can play/duplicate/delete/rename actions but **cannot create** an action set programmatically.

## 6. Imaging API

```js
const { imaging } = require("photoshop");
const { imageData } = await imaging.getPixels({
  documentID: doc.id, layerID: layer.id,
  sourceBounds: { left:0, top:0, right:512, bottom:512 },
  targetSize: { width: 256 },        // pyramid-level downscale
  componentSize: 8,                  // 8 | 16 | 32
  applyAlpha: false
});
const buf = await imageData.getData();  // typed array
// ... process ...
await imaging.putPixels({ documentID: doc.id, layerID: layer.id, imageData: newData });
imageData.dispose();                    // free promptly — don't wait for GC
```
Knowns: colorSpace RGB/Grayscale/Lab; 16-bit defaults to Photoshop's [0..32768] range unless the full-range flag is set; `getSelection()` returns the selection as a mask buffer; `encodeImageData` produces jpeg/base64 (required to display in a UXP `<img>`; quality can trail `saveAs.jpg`). **Bug:** Grayscale/LAB `getPixels` omits the alpha component (issue #501) — pull transparency separately via batchPlay channel selection + `getSelection`, aligning bounds yourself. Tight per-pixel loops belong in a C++ hybrid addon, not JS.

## 7. .psjs scripts

Modern-JS standalone scripts (File > Scripts / double-click). Full DOM + batchPlay + Imaging + localFileSystem + shell. Constraints: **no persistent storage** (each run is a fresh throwaway context — no plugin-data folder, no localStorage; persist to user-chosen files), no panels/entrypoints, `recordAction` unsupported. Debug via UXP Developer Tool 1.7.0+. For team batch tools: .psjs is the default target; if the timecard skill is installed, add its instrumentation block (timecard's bash/Python blocks don't run in-app — use the JS adaptation, same invariants). Any .psjs that exports images also follows the color rules in `psd-tooling-and-external-control.md` (convert duplicate to sRGB, embed profile).

## 8. Action recording from UXP (plugins only)

`action.recordAction({name, methodName}, info)` inserts a step into an in-progress Actions-panel recording; playback re-invokes the **global-scope** function `methodName` with the recorded `info`. Recognized `info` keys surface in the panel and shift across PS versions — prefix private keys reverse-URL style. Menu recording needs the manifest opt-in. Community reports playback reliability complaints (Reported) — test before shipping recordable steps.

## 9. Manifest v5 permissions (least-privilege reference)

| Permission | Values | Notes |
|---|---|---|
| `network` | `{domains:[...]}` or `"all"` | No top-level wildcards; list localhost AND 127.0.0.1 explicitly (flaky — see pitfalls) |
| `localFileSystem` | `plugin` / `request` / `fullAccess` | `request` = user-picks-folder; prefer over fullAccess |
| `launchProcess` | `{schemes:[...], extensions:[...]}` | Gates shell.openExternal/openPath; runtime consent dialog |
| `clipboard` | `read` / `readAndWrite` | |
| `webview` | `{domains:[...], enableMessageBridge:"no"|"localOnly"|"localAndRemote"}` | Bridge value gates postMessage |
| `allowCodeGenerationFromStrings` | bool | eval/new Function; Marketplace scrutiny |
| `enableAddon` | bool | C++ hybrid |
| `ipc` | `{enablePluginCommunication:true}` | plugin↔plugin |
| `enableUserInfo` | bool | anonymized CC user GUID |
Install-time grant for everything except launchProcess/anchor-open (runtime consent). Start from `assets/manifest-v5.template.json` and escalate deliberately.

## 10. Debugging & diagnostics

- **UXP Developer Tool (UDT)**: load unpackaged plugin, console, inspect, package .ccx. Required 1.7.0+ for .psjs and hybrid.
- **Alchemist**: live descriptor listener + inspector — the UXP-era ScriptingListener.
- **Runtime health getters** on `core`: `mainThreadTimeOutCount` (calls that timed out — usually missing modal scope), `v8HeapSize`, `isModal`, `isHistorySuspended`.
- **Feature detection**: `require("uxp").versions.uxp`, `uxp.host.version`; branch rather than assume.
- TypeScript: `@types/photoshop` (official; imperfect — Reported), `@adobe-uxp-types/*` (community), uxp-toolkit Zod schemas; scaffold with bolt-uxp (Vite + TS + React/Svelte/Vue, hot reload, .ccx packaging).
