# ExtendScript (.jsx) — Legacy Reference

Volatility: LOW (frozen platform). Stamp 2026-07-10. Status/removal-date facts → `current-versions.md`.

Load this file only for maintaining existing .jsx or when a required API has no UXP equivalent. New Photoshop automation defaults to UXP/.psjs.

## Engine constraints (ES3-era)

- No `let`/`const`/arrow functions/template literals/classes/Promises/JSON (native). Use `var`, functions, string concat.
- Safe polyfills: `JSON` (json2.js), `Array.prototype.forEach/map/filter/indexOf`, `String.prototype.trim`, `Object.keys`. NOT polyfillable: Proxy, Symbol, async/await, getters via defineProperty semantics differ.
- `#include "path.jsx"` / `//@include` for composition; `$.evalFile()` at runtime.
- `$` utilities: `$.writeln` (console), `$.hiresTimer`, `$.os`, `$.locale`.
- Everything is synchronous — the app blocks while a script runs. Long batches: no UI updates unless you pump progress via a ScriptUI palette.

## Two API layers

**Classic DOM** — readable, covers common ground:
```jsx
var doc = app.activeDocument;
doc.activeLayer.name = "Hero";
doc.saveAs(new File("/out/hero.psd"), new PhotoshopSaveOptions(), true);
```
**Action Manager** — reaches everything the DOM doesn't (the .jsx analog of batchPlay):
```jsx
function s2t(s){ return app.stringIDToTypeID(s); }
var d = new ActionDescriptor();
var r = new ActionReference();
r.putProperty(s2t("property"), s2t("layerID"));
r.putEnumerated(s2t("layer"), s2t("ordinal"), s2t("targetEnum"));
d.putReference(s2t("null"), r);
executeAction(s2t("get"), d, DialogModes.NO);
```
Prefer `stringIDToTypeID` over `charIDToTypeID` (readable, greppable). `executeActionGet` for reads. Descriptor discovery: the **ScriptingListener plug-in** logs every UI action as AM code to `ScriptingListenerJS.log` on the desktop; clean the verbose output with **Clean SL** (rendertom). Alchemist descriptors translate conceptually (actionJSON ↔ AM) — `ps-es-to-uxp` converts the other direction.

## Units gotcha

`app.preferences.rulerUnits` silently changes what numeric values mean. Bulletproof pattern:
```jsx
var saved = app.preferences.rulerUnits;
app.preferences.rulerUnits = Units.PIXELS;
try { /* work */ } finally { app.preferences.rulerUnits = saved; }
```
Or use `UnitValue("100 px")` everywhere.

## History

```jsx
doc.suspendHistory("My Operation", "main()");  // one undo step; string is EVALUATED
```
The second argument is a code string, not a function reference — scope accordingly.

## Debugging in 2025+

ESTK is dead (32-bit, killed by macOS 10.15; deprecated 2020). Use the **VS Code ExtendScript Debugger** (`Adobe.extendscript-debug`): attach to host, breakpoints, eval-in-host. Known flaky (Reported) — most reliable on self-contained scripts; ScriptUI panel debugging is painful. Fallbacks: `$.writeln` to the debug console, `alert()` checkpoints, try/catch with `e.line`/`e.message` written to a log file.

## BridgeTalk (cross-app, incl. Photoshop↔After Effects)

```jsx
var bt = new BridgeTalk();
bt.target = "aftereffects";
bt.body = "app.project.activeItem.name;";   // code STRING evaluated in target
bt.onResult = function(res){ $.writeln(res.body); };
bt.onError  = function(err){ $.writeln(err.body); };
bt.send();
```
- Target app must be running (or use `BridgeTalk.launch("aftereffects")`).
- Payloads are strings — serialize data as JSON text both ways.
- Asynchronous-ish: results arrive via callbacks; a script that exits immediately may drop them — pump with `BridgeTalk.pump()`/timed loops when waiting.
- Specifier can pin versions (e.g. `aftereffects-2026`); bare name targets the newest.
- This remains the only in-process PS↔AE scripting bridge; modern alternatives orchestrate externally (see psd-tooling-and-external-control.md). For PS→AE handoffs, apply AE frame-math discipline on the AE side — integer frame counts on `item.frameDuration`, Math.round conversions, verified across NTSC and non-NTSC rates.

## ScriptUI in one paragraph

`new Window("dialog"|"palette")`, add controls (`statictext`, `edittext`, `button`, `dropdownlist`, `progressbar`), `.show()`. Palettes need `#targetengine "session"` to persist. Dated but functional; do not invest — UI work belongs in UXP.

## File I/O quirks

- `File`/`Folder` use URI-ish paths; `File.fsName` for native, `~` expands home.
- Set `file.encoding = "UTF-8"` before text writes; default encoding is platform-dependent.
- `File.openDialog`/`Folder.selectDialog` for pickers.
- Network volumes and long Windows paths are historic pain points — test on production storage.

## When ExtendScript still wins (short list, shrinking)

- Maintaining a proven .jsx pipeline where a rewrite has no payoff yet.
- BridgeTalk-dependent cross-app steps not yet externalized.
- The odd API corner UXP hasn't wrapped — verify against the UXP changelog at preflight before assuming a gap still exists.
