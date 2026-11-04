# Runtime gotchas (UXP 9.3, measured unless marked)

## Manifest v5 that installs and runs
```json
{
  "manifestVersion": 5,
  "id": "com.nesn.mypanel.ps",
  "name": "My Panel",
  "version": "1.0.3",
  "main": "index.html",
  "host": { "app": "PS", "minVersion": "24.0.0" },
  "entrypoints": [{ "type": "panel", "id": "main", "label": { "default": "My Panel" },
    "minimumSize": {"width": 200, "height": 220}, "maximumSize": {"width": 1200, "height": 2400},
    "preferredDockedSize": {"width": 300, "height": 520}, "preferredFloatingSize": {"width": 300, "height": 520},
    "icons": [{"width": 23, "height": 23, "path": "icons/icon.png", "scale": [1, 2], "theme": ["all"], "species": ["generic"]}] }],
  "requiredPermissions": {
    "localFileSystem": "fullAccess",
    "allowCodeGenerationFromStrings": true,
    "launchProcess": { "schemes": ["file"], "extensions": [".jsx", ".js"] }
  },
  "icons": [{"width": 48, "height": 48, "path": "icons/plugin.png", "scale": [1, 2], "theme": ["all"], "species": ["pluginList"]}]
}
```
- `host` is a single object per package (we build one package per app). `version` must be `x.y.z`.
- Floating panel opened at its **minimumSize** in Premiere, not the preferred size (observed).
- Ask only for permissions the code uses; `uxp_check.py` flags code that needs one you didn't declare.

## Files (`localFileSystem: "fullAccess"`)
```js
const lfs = require("uxp").storage.localFileSystem;
const folder = await lfs.getEntryWithUrl("file:" + "/Users/<you>/My Projects/...");   // spaces and symbols fine unencoded
const entries = await folder.getEntries();          // e.isFolder, e.isFile, e.name, e.nativePath
const text = await entries[0].read();               // utf-8 string
const out = await folder.createFile("x.txt", { overwrite: true });
await out.write("data");                            // write("") THROWS: "writeToFile: data cannot be null"
const sub = await folder.getEntry("Shared");        // throws if missing → wrap in try
```
- `require("os").homedir()` works. Fallback: slice `(await lfs.getDataFolder()).nativePath` at `/Library/`.
- `lfs.getTemporaryFolder()` = plugin temp; `lfs.getFolder()` = user folder picker (returns null on cancel).
- `/tmp` is a symlink; use `file:/private/tmp` for log/receipt files.
- `uxp.shell.openPath(path)` needs `launchProcess`; it returns an error string ("" on success) rather than throwing (docs; our
  panel treats a non-empty return as failure).

## Running script files from a plugin
```js
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const fn = new AsyncFunction("require", "__filename", "__dirname", code);   // needs allowCodeGenerationFromStrings
await fn(require, entry.nativePath, dir);       // top-level await works inside the script
```
Errors come back as normal JS errors (`ReferenceError: x is not defined`). Line numbers are offset by the wrapper; don't
promise them for UXP scripts.

## Photoshop
- Anything that changes a document must run inside `require("photoshop").core.executeAsModal(fn, {commandName})`. We wrap
  user UXP scripts in it so they don't have to.
- **Legacy `.jsx`**: batchPlay with a session token. Photoshop raises its own modal on an uncaught ExtendScript error, even with
  `dontDisplay`, and batchPlay returns only `-128`. Wrap it:
```js
async function runJsxPhotoshop(entry) {
  const ps = require("photoshop");
  const tmp = await lfs.getTemporaryFolder();
  const res = await tmp.createFile("result.txt", { overwrite: true });
  await res.write("-");                                         // not "": empty write throws
  const wrap = await tmp.createFile("run.jsx", { overwrite: true });
  await wrap.write("(function(){var r;try{$.evalFile(new File(" + JSON.stringify(entry.nativePath) + "));r='ok';}" +
    "catch(e){r='ERR|'+(e.line||0)+'|'+(e.message||e);}" +
    "var f=new File(" + JSON.stringify(res.nativePath) + ");f.encoding='UTF-8';f.open('w');f.write(r);f.close();})();");
  const token = lfs.createSessionToken(wrap);
  await ps.core.executeAsModal(() => ps.action.batchPlay([{
    _obj: "AdobeScriptAutomation Scripts", javaScript: { _path: token, _kind: "local" },
    javaScriptMessage: "undefined", _options: { dialogOptions: "dontDisplay" } }], {}), { commandName: "Run script" });
  const got = String(await res.read());
  if (got.indexOf("ERR|") === 0) { const p = got.split("|"); const e = new Error(p.slice(2).join("|")); e.line = +p[1]; throw e; }
}
```
  `$.fileName` and relative `$.evalFile`/`#include` inside the target still work. Measured: good script 24–36 ms, error shown as
  "noSuchFunction123 is not a function (line 3)", no modal.

## InDesign
```js
const id = require("indesign");
const r = String(id.app.doScript(
  "(function(){try{$.evalFile(new File(" + JSON.stringify(path) + "));return 'ok';}catch(e){return 'ERR|'+(e.line||0)+'|'+(e.message||e);}})()",
  id.ScriptLanguage.JAVASCRIPT));
```
Synchronous; returns the ExtendScript value. Measured 230 ms first run.

## Premiere Pro
- `require("premierepro")` only; no route to ExtendScript from UXP. CEP + ExtendScript (`app.project`, `app.openDocument`, …)
  remains the way to run existing `.jsx` in Premiere.

## Lifecycle
- `require("uxp").entrypoints.setup({ panels: { <entrypointId>: { show() {…}, hide() {…} } } })` must be called during the
  first synchronous tick, before any `await`. Wrap in try/catch; it's optional.
- Plugins load at app launch. After installing a new version, **restart the app**.
- `uxp.host.name`, `uxp.host.version`, `uxp.versions.uxp` (e.g. `uxp-9.3.0-uxp`) are worth logging at start-up.
- `localStorage` works for per-panel settings (pins, last folder).
