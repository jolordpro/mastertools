# 00 — AE Platform Facts (ground truth + the freshness protocol)

> The dated, authoritative snapshot of the After Effects extensibility landscape. When another reference or
> your prior knowledge conflicts with this file, **this file wins** — but anything version-dependent is
> *provisional*: verify it against the live source below before relying on it.
> **Last verified: June 2026, against AE 26.2.1.** (Re-date this when you re-verify.)

---

## §0 — THE FRESHNESS PROTOCOL (do this so the skill never goes stale)

Your training data and this file both drift. Treat the facts here as a strong prior, not gospel.

**Stop and verify the live source before you:**
1. state a version number, or attribute a feature to a specific version;
2. assert an API/method exists, or claim its signature/parameters;
3. claim something "isn't possible" or "isn't shipping yet" — **especially UXP-for-AE**;
4. finalize any non-trivial tool design.

**Also ask every time: has a newer *native* AE feature obsoleted the scripted approach?** Adobe periodically
ships natively what people used to script (e.g., AI/SVG → editable shape import, parametric 3D meshes,
selectable track mattes, `Property.valueText` readouts, `Layer.id`). If a native path now exists, prefer it or
flag it — don't ship a workaround the app does for free.

**Never invent an API.** If unsure a method exists in the user's version, say "verify against the scripting
changelog" and give the link. Version-gate anything newer with `parseFloat(app.version)` and degrade gracefully.

### Live sources (cite/verify against these, not memory)
- AE Scripting Guide: https://ae-scripting.docsforadobe.dev/
- **Scripting changelog (authoritative for which API exists in which version):** https://ae-scripting.docsforadobe.dev/introduction/changelog/
- ExtendScript guide + VS Code debugger: https://extendscript.docsforadobe.dev/
- What's new in AE: https://helpx.adobe.com/after-effects/using/whats-new.html
- AE release notes: https://helpx.adobe.com/after-effects/release-note/release-notes-after-effects.html
- matchName reference: docsforadobe "Match Names" pages (layers, effects, layer styles)
- CEP resources (Adobe): https://github.com/Adobe-CEP/CEP-Resources
- Bolt-CEP: https://github.com/hyperbrew/bolt-cep
- UXP-for-AE status: Adobe Tech Blog + Creative Cloud Developer Forums + UXP Developer Tool changelog
- Expressions: https://www.motionscript.com/ (Dan Ebberts)

---

## §1 — ONE-PARAGRAPH SUMMARY

As of mid-2026, **ExtendScript (ES3) + ScriptUI is still the correct default** for AE automation and panels.
**UXP panels have *not* shipped for After Effects** — they exist only in Photoshop, InDesign, and (historically)
XD. **CEP** (HTML/CSS/JS client + ExtendScript host) remains the path for rich UI and has multi-year runway
(CEP 12 is the last major version — frozen, not dead; security fixes, no new features, no announced EOL). So:
don't "modernize" an AE request into UXP — it isn't an option. Build ScriptUI for native-feel tooling; choose
CEP when the UI genuinely exceeds ScriptUI. Treat ExtendScript as **strict ES3** regardless of what seems to
work on a given machine (see §4, the phantom-polyfill trap).

---

## §2 — VERSIONS & RELEASE STATE (verify live before quoting)

| Track | Family | Notes |
|---|---|---|
| After Effects 2026 | **v26.x** | 26.0 (Jan 2026), 26.2.1 (Apr 2026, current stable at last verify). Native parametric 3D meshes, Substance 3D materials, **native SVG import**, new lighting model, built-in audio FX, Windows-on-ARM native, AI Object Matte/Mask. |
| After Effects 2025 | **v25.x** | CEP 12 shipped with 25.0. `app.restart()` added in 25.4. |

**Version-gating rule.** `app.version` returns e.g. `"26.2.1x..."`; `parseFloat` gives `26.2`. Guard any
method added in a specific version: check `parseFloat(app.version)` and degrade/warn rather than throw on older
builds. Ask the user's version when writing version-dependent code.

---

## §3 — THE FOUR VEHICLES (choose FIRST — Phase 0)

Picking the wrong vehicle is the most expensive mistake in the project.

1. **Script (.jsx / .jsxbin)** — ExtendScript (ES3) on the AE DOM. UI: none (run-once) or **ScriptUI** (dockable
   when placed in `ScriptUI Panels/`). Strengths: simplest, no signing, one-file, instant install, full DOM on
   the main thread. Limits: ES3 only; fixed ScriptUI widget set (no HTML/CSS; limited custom draw via `onDraw`).
   **This is the default and the subject of the Quality Standard (`05`).**
2. **CEP Extension (.zxp)** — HTML/CSS/JS client in embedded Chromium (CEF) + an ExtendScript host, bridged by
   `CSInterface.evalScript()`. Strengths: arbitrary web UI, Node.js, multi-host. Limits: two engines across a
   string bridge; manifest + signing + packaging; **the host that touches the DOM is still ES3.** Choose when the
   UI genuinely exceeds ScriptUI. Full detail: `06-cep-extensions.md`.
3. **UXP Plugin (.ccx)** — modern JS UI, the intended successor. **NOT AVAILABLE FOR AFTER EFFECTS PANELS** (as
   of last verify — confirm live). Don't propose it as an AE build target; mention only as future direction.
4. **C/C++ Plugin (AEGP / effect SDK)** — native code; the only path to rendered pixels, effects, file formats,
   render engines. Out of scope for scripting/tooling — flag it and point to the AE SDK.

**Decision procedure (top-down, first match):**
```
Modify rendered pixels / add an effect / add a file format?     → C/C++ plugin (out of scope; flag it)
UI satisfiable with ScriptUI widgets (listbox/buttons/fields/
  dropdowns/tabs/basic onDraw)?                                  → SCRIPT + ScriptUI   [DEFAULT, ~85%]
UI needs real HTML/CSS — rich tables, charts, drag canvas,
  themed multi-view, web auth, heavy async network?             → CEP extension       [co-equal]
One-shot action, no persistent panel?                            → SCRIPT (run-once, no UI)
```
**Never UXP for AE. Never call ScriptUI "outdated."**

**Frontend/backend/middleware — map honestly:** a *ScriptUI script* has no such split (it's one ES3 program; the
"architecture" is the internal section model — `05` §5). A *CEP extension* does: **client** (HTML/CSS/JS in CEF)
↔ **host** (`host.jsx`, ES3, touches `app.project`) ↔ **bridge** (`evalScript` UI→host; `CSXSEvent` host→UI, or
files on disk). The bridge is async and passes **strings** — JSON-marshal (polyfilled on the ES3 side), keep
calls small, never assume ordering.

---

## §4 — EXTENDSCRIPT IS ES3 (and the phantom-polyfill trap)

ExtendScript is **ECMAScript 3** (1999) plus Adobe extensions (`File`/`Folder`, `$`, reflection, operator
overloading, E4X). That's the whole language for scripts.

**The phantom-polyfill trap (why ES3 discipline is non-negotiable):** Adobe's own panels inject polyfills into
the **shared global scope** when they load — opening **Libraries** adds `Array.indexOf/filter/map` + `JSON`;
**Learning** adds `Array.indexOf`; others add more. They persist until AE quits. So a script using `JSON.parse`
or `arr.forEach` can **work on the dev machine** (a panel is open) and **fail cold** on a clean machine, a
different version, or a different panel-load order. Invisible unless you test from a cold start.

**Therefore:** never rely on any ES5+ method. Either avoid it or **ship a guarded polyfill** at the top of the
file (`if (!Array.prototype.indexOf) { … }`) so behavior is identical everywhere and you never clobber a faster
native/injected version.

**Do NOT use (will throw or behave unreliably in ES3):** `let`/`const` · arrow functions · template literals ·
destructuring · spread/rest · default params · `for…of` · `Promise`/`async`/`await` · `Set`/`Map`/`WeakMap` ·
`Array.from`/`Array.of` · `Array.prototype` {`forEach`,`map`,`filter`,`reduce`,`some`,`every`,`find`,
`findIndex`,`includes`,`fill`,`indexOf`*} · `Object` {`keys`,`values`,`entries`,`assign`,`create`,
`defineProperty`*,`freeze`*} · `String.prototype` {`trim`,`includes`,`startsWith`,`endsWith`,`repeat`,
`padStart`/`padEnd`} · `Number.isInteger` · `Date.now`/`toISOString` · `JSON`* · native getters/setters · ES3
also **rejects reserved words as object keys** (`in`, `class`, …) — and `node --check` won't catch that (modern
parser), so grep for it. (* = may *appear* present due to injection — treat as absent anyway.)

**Genuinely safe in ES3:** `var`, function declarations/expressions · `try`/`catch`/`finally` · `throw` ·
`typeof`/`instanceof`/`delete`/`in`/`with` · `hasOwnProperty` · `arguments` · `String` {`replace` (incl. regex),
`match`,`search`,`split`,`substring`,`substr`,`slice`,`indexOf`,`lastIndexOf`,`charAt`,`charCodeAt`,
`toLowerCase`,`toUpperCase`} · `Array` {`push`,`pop`,`shift`,`unshift`,`splice`,`slice`,`concat`,`join`,
`reverse`,`sort`} · `RegExp` (**flags `g`/`i`/`m` only** — no `s`/dotAll, no lookbehind, no named groups, no
`u`/`y`) · `Math.*`,`parseInt`/`parseFloat`/`isNaN`/`isFinite` · `new Date()` + getters · `encodeURI*` · Adobe:
`$.sleep`,`$.os`,`$.fileName`,`$.global`,`$.writeln`,`File`,`Folder`,`$.evalFile`,`app.scheduleTask` (AE 2024+,
the only setTimeout-like debounce).

**Polyfills to keep on hand (paste at top, each guarded `if (!X)`):** `Array.indexOf`, `Array.forEach`,
`Array.filter`, `Array.map`, `String.trim`, and a minimal `JSON` (Crockford `json2` is the canonical safe
choice). Deeper ES3 discipline + the matchName/undo/perf rigor live in `04-extendscript-rigor.md`.

---

## §5 — SCRIPTING API ADDITIONS (v22→v26 — use only with a version guard; verify live)

Anything **not** listed here for the user's version → treat as possibly-nonexistent; verify against the
changelog, do not invent.

- **26.x:** `Property.valueText` (read a property's *displayed* text — great for readouts), `Property.propertyParameters`, `PropertyGroup.addVariableFontAxis()`; native parametric meshes (`LayerCollection.addParametricMesh()`, beta — guard hard).
- **25.4:** `app.restart()`.
- **25.1:** text/font scripting (`CharacterRange.pasteFrom()`, `FontObject.hasGlyphsFor()`, default-font-for-script hooks).
- **24.x:** box-text `TextDocument` controls (24.6); `Project.replaceFont()`/`usedFonts` (24.5); `ThreeDModelLayer` (24.4); full `CharacterRange`/`ParagraphRange` text API + `app.purge(PurgeTarget.ALL_CACHES)` (24.3); `getEnumAsString()` + the `app.fonts`/`Font` model (24.0).
- **23.0:** selectable track mattes — `AVLayer.setTrackMatte()`/`removeTrackMatte()`/`trackMatteLayer` (legacy `trackMatteType`-only scripts fall back to "layer above").
- **22.x:** **`Layer.id` + `Project.layerByID()`** (stable refs that survive reordering — prefer over index where persisted); `app.setMultiFrameRenderingConfig()`; render-queue notifications.
- **18.0:** Media Replacement + Essential Properties. **17.0.1:** scripted Dropdown Menu Control items. **16.0:** `Project.expressionEngine` (read/set!), `app.disableRendering`, guide scripting. **15.0:** `.mogrt` export.

---

## §6 — DEVELOPMENT, TESTING & DEBUGGING

There is **no real unit-test framework for the AE DOM** — code runs inside AE against a live project. The
professional loop:

- **Editor/debugger:** VS Code + the official **ExtendScript Debugger** extension (Adobe). ESTK is deprecated +
  32-bit (won't run on modern macOS). Open the **folder/workspace** (not a lone file) → `launch.json` with an
  `extendscript-debug` config → attach to the host → "Eval in host app" or breakpoints + F5. **Limitation:**
  reliable for self-contained run-once scripts, **awkward for ScriptUI panels** (quits when the script
  "finishes"; misses `#targetengine`). So: develop panel *logic* as pure functions you can eval headlessly, test
  the shell live in AE.
- **Logging that survives a crash:** `$.writeln` goes to the debugger console only. For real diagnostics (and
  cold-start bugs), write a **buffered file logger** to `Folder.userData`: session-ID prefix, append, flush
  every N lines (per-write I/O is slow on Windows), rotate ~500 KB. A persisted log is the only way to debug
  "works for me, fails for the user."
- **The cold-start test (mandatory before shipping):** quit AE → reopen with **no Libraries/Learning/other
  panels** → run. If it depends on an injected polyfill, it fails only here.
- **Adversarial fixtures:** keep a junk project — locked layers, missing-footage placeholder, 0-duration comp,
  camera + light, guide layer, shy layer, 500+ layer comp, names with `()[]/\."'` + Unicode, a deeply nested
  shape group. Most DOM-edge crashes only appear against hostile input.

---

## §7 — DEPLOYMENT & INSTALL PATHS

**ScriptUI panel:** drop the `.jsx`/`.jsxbin` into the per-version **`ScriptUI Panels`** folder → appears at the
bottom of **Window** menu, dockable.
- macOS: `~/Library/Application Support/Adobe/After Effects <ver>/Scripts/ScriptUI Panels/` (or the app dir's `…/Scripts/ScriptUI Panels/`)
- Windows: `C:\Users\<user>\AppData\Roaming\Adobe\After Effects <ver>\Scripts\ScriptUI Panels\` (or `…\Program Files\…\Support Files\Scripts\ScriptUI Panels\`)
- **"Allow Scripts to Write Files and Access Network"** (Preferences ▸ Scripting & Expressions) must be ON for I/O.
- Run-once scripts (no panel) → `…/Scripts/`, run from **File ▸ Scripts ▸ Run Script File…**.

**CEP extension:** user scope (no admin) — macOS `~/Library/Application Support/Adobe/CEP/extensions/<bundleId>/`,
Windows `…\AppData\Roaming\Adobe\CEP\extensions\<bundleId>\`. Unsigned dev panels need `PlayerDebugMode = 1`
under the matching `CSXS.<n>` key (macOS `defaults write com.adobe.CSXS.<n> PlayerDebugMode 1`). Sign → `.zxp`
for distribution. Full CEP install/sign detail (cert immutability, timestamping, the two-CEP-folder hygiene
trap): `06-cep-extensions.md`.

**Modern CEP scaffolding:** **Bolt-CEP** (Vite + TypeScript + React/Vue/Svelte, HMR for both layers, type-safe
`evalTS()` bridge, one-command ZXP). Don't hand-roll CEP boilerplate. The host layer it builds is still ES3.

---

## §8 — EXPRESSIONS vs SCRIPTS (two engines — don't conflate)

- **Scripts (.jsx):** ExtendScript **ES3**. Run on demand, manipulate the DOM, stop.
- **Expressions:** live on properties, re-evaluate every frame. AE's default engine has been the **JavaScript
  engine** (modern, ES6-ish) since AE 16/2019; the **Legacy ExtendScript** engine is opt-in per project
  (`Project.expressionEngine`). So expression code may use `const`/arrow/etc. — the opposite of script code.
- **Always state which engine an expression targets**, and flag constructs that differ between the JS and Legacy
  engines. Default expressions to the **JS engine** and say so. Full detail: `08-expressions.md`.
