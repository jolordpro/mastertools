# 05 — ScriptUI Premium Quality Standard

> What "commercial grade" means concretely for a **ScriptUI** panel — the bar is aescripts.com top-10: users
> open it and immediately know what to do, never hit a crash, and wonder how they worked without it. The design
> *philosophy* + Test Battery live in `01-design-canon.md`; the workflow analysis that precedes any UI here is
> `02-workflow-first.md`; the engineering rigor behind §7 is `04-extendscript-rigor.md`. **Confirm ScriptUI is
> the right vehicle first** (`00` §3). For CEP the carry-over is in `06-cep-extensions.md`. All ExtendScript here
> is **strict ES3** (`00` §4 — the phantom-polyfill trap is why guarded polyfills are mandatory).

---

## §1 — SPATIAL HIERARCHY BUDGET (implements canon Principle 3)

- **Tier 1 — The Hero (55–65%):** the primary content (a ListBox or large preview/input zone). Always
  `alignment: ["fill","fill"]`. It dominates.
- **Tier 2 — The Controls (20–30%):** actions/filters operating on the hero. Compact, horizontal, directly
  above/below the hero. Plain groups with dividers, not framed panels.
- **Tier 3 — The Context (5–10%):** status, counts, mode indicators. Small, dim (`DS.dimText`). Glanceable.
- **Tier 4 — The Settings (≤5%):** set-once config. Behind a gear, a secondary tab, or a "More…" dialog. Never
  on the primary surface.

---

## §2 — VISUAL DESIGN SYSTEM (one `DS` object → a consistent brand across tools)

```javascript
var DS = {
    // Brand (AE-sympathetic, muted)
    accent:    [0.25, 0.56, 0.85], accentDim: [0.20, 0.44, 0.68],
    success:   [0.30, 0.72, 0.45], warning:   [0.85, 0.68, 0.25], error: [0.82, 0.30, 0.30],
    // Text hierarchy
    dimText:   [0.55, 0.55, 0.55], faintText: [0.40, 0.40, 0.40], white: [1, 1, 1],
    // Structure
    divider:   [0.28, 0.28, 0.28],
    isMac:     ($.os.indexOf("Mac") !== -1),
    // Spacing
    winMargins:[8,8,8,6], winSpacing:2, groupGap:4, labelW:55, minW:250,
    btnH:26, fieldH:24, divH:8, tabBtnH:24, tabBtnHWin:27,
    // Safe Unicode (verified cross-platform)
    ok:"✓", arrow:"→", dash:"—", bullet:"•",
    // UNSAFE → ASCII substitutes
    fail:"X", warn:"(!)", gear:"*"
};
```

**Safe-Unicode rule (don't "optimize" it away):** `✓ → — •` are safe; `⚠ ✗` and similar symbols render as a box (□) on some
**Windows DPI/codepage** configs — this is about rendering, not aesthetics. For interactive affordances drawn as
text (checkbox states, toggles), prefer ASCII `[X]`/`[ ]` over any Unicode box-drawing character — it never
breaks.

**Custom draw pattern (always: try styled draw, catch with functional fallback so the control still works):**
```javascript
function applyAccentDraw(ctrl) {              // primary action button (accent fill)
  try { ctrl.onDraw = function () { try {
    var g = this.graphics, w = this.size[0], h = this.size[1];
    var c = this.enabled ? DS.accent : DS.accentDim;
    g.rectPath(0,0,w,h); g.fillPath(g.newBrush(g.BrushType.SOLID_COLOR, c));
    if (this.text) {
      var pen = g.newPen(g.PenType.SOLID_COLOR, DS.white, 1);
      var m = g.measureString(this.text, g.font);
      var tw = (m && m[0]) ? m[0] : (this.text.length * 7);   // measureString can be null on Win DPI
      g.drawString(this.text, pen, (w - tw) / 2, (h - 14) / 2);
    }
  } catch (e) {} }; } catch (e) {}
}
```
Tab buttons are **platform-aware** (Mac: accent fill when active; Windows: text + a colored bottom-bar
indicator, DPI-safe). Every `g.measureString()` must be null-guarded. Helpers worth keeping: `setColor(ctrl,
arr)`, `setBold(ctrl)` (via `ScriptUI.newFont`), `makeDivider(parent)` (a `customview` + `applyDividerDraw`).

---

## §3 — LABEL DOCTRINE

- **Labels describe what the USER does, not what the CODE does.** "Fix selected", not "Execute Batch Process".
- **Verb-first for actions** ("Scan", "Fix", "Export"); **noun-first for displays** ("Active Comp", "Found
  Issues").
- **Max 2 words for buttons** (3 only when 2 is ambiguous; more → decompose). **Max 4 words for section/tab
  labels.**
- **No colons on field labels** ("Find", not "Find:"). **No jargon** ("Apply to all", not "Propagate"; "Save",
  not "Serialize"). **No abbreviations** unless universal in AE ("Comp" ok; "Sel."/"Expr" not).
- **Button suffixes:** `…` = opens a dialog; `▸` = reveals more; no suffix = acts directly.
- **The 2-AM test:** would a designer on deadline understand it without pausing? If not, rewrite.

| Pattern | Good | Bad |
|---|---|---|
| Action buttons | "Rename", "Scan", "Fix" | "Execute Rename", "Run Scan" |
| Scope | "Selected layers", "All layers" | "Selected Layers Only", "Process All" |
| Status | "✓ Renamed 5 layers" | "Operation completed successfully: 5 layers renamed." |
| Error | "X No comp open" | "Error: ActiveItem is not a CompItem instance" |

---

## §4 — UX PATTERN LIBRARY (mechanisms catalogued in `03`; ScriptUI specifics here)

**4.1 Empty-state map (mandatory, designed BEFORE the UI).** Each "nothing to show" condition gets its own
contextual message, evaluated top-down: no project → "Open a project to begin"; no comp → "Select a comp"; comp
empty → "Add layers first"; scope=selected/none → "Select layers in the timeline"; input empty → "Type in Find
to preview"; zero results → "[what was searched] — [suggestion]". Dim text, shown in the **hero zone**. The
empty state *is* the onboarding.

**4.2 Live preview = cache layer, not live reads.** `onChanging` reads ONLY the JS cache, never `app.project`/
`comp.layers`. DOM reads happen on: init, scope change, field focus (`onActivate` — catches "selected layers
then clicked into the panel"), post-action, manual refresh. Format: `"OldName  →  NewName"` (batch:
`"BG_01 … BG_12"`).

**4.3 Selection sync by tool type.** *Transform tools:* cache refreshes on field `onActivate` (zero polling).
*Scan/audit tools:* explicit Scan button; results are a snapshot (show comp name/timestamp); re-validate stored
refs before acting. *Hybrid:* scan on demand, validate each record before executing (prefer `Layer.id`/
`layerByID` — `04` §2).

**4.4 Post-action feedback:** verb + count + noun ("✓ Renamed 5 layers") + edge cases ("(2 locked, skipped)") +
next step ("Cmd+Z to undo"). Colors are **momentary** — reset to `DS.dimText` on the next interaction.

**4.5 Settings persistence module (versioned section name; also store the AE version written under):**
```javascript
var SETTINGS_SECTION = "ToolName_v1";        // namespaced, versioned
var Settings = {
  _defaults: { mode:"0", scope:"0" },
  get: function (k) { try { if (app.settings.haveSetting(SETTINGS_SECTION,k)) return app.settings.getSetting(SETTINGS_SECTION,k); } catch(e){} return this._defaults[k] !== undefined ? this._defaults[k] : ""; },
  set: function (k,v) { try { app.settings.saveSetting(SETTINGS_SECTION,k,String(v)); } catch(e){} },
  getInt: function (k) { return parseInt(this.get(k),10) || 0; },
  getBool: function (k) { return this.get(k) === "true"; }
};
```
Persist active tab, dropdown/checkbox state, field values. Don't persist transient state (results, preview,
status). Store `parseFloat(app.version)` alongside feature-tied settings so a downgrade doesn't replay settings
for absent APIs (and a rebuild can migrate — `04` §9, `07` §9).

**4.6 About/version:** a small `i` button → a one-line dialog or `helpTip` ("Tool Name v1.0 — yoursite.com").
**This is the ONLY place `alert()` is acceptable.**

**4.7 Error communication:** inline, never `alert()`; tell the user what went wrong (user terms), why, and the
fix. `previewText = "Open a comp to start"` not `alert("No CompItem found")`.

---

## §5 — ARCHITECTURE TEMPLATE (search `§` to jump; dependencies flow downward, no forward refs)

```
§0  HEADER (name, version, AE-compat range, description, author/site, settings-migration note, CHANGELOG)
§1  DESIGN SYSTEM CONSTANTS (DS object)
§2  POLYFILLS (guarded JSON, Array.indexOf/forEach — assume native absent; 00 §4)
§3  SETTINGS PERSISTENCE (stores AE version written under)
§4  UTILITY FUNCTIONS (draw helpers, color setters, label helpers)
§5  BUILD UI (window/panel, all visual elements, layout)
§6  STATE MANAGEMENT (cache, flags, active mode)
§7  EMPTY STATE MAP (context-aware message function)
§8  DATA LAYER (cache management, scan engine)
§9  PREVIEW / DISPLAY LOGIC (reads cache, never DOM)
§10 ACTION ENGINE (guarded operations with undo groups)
§11 EVENT WIRING (onChange/onClick/onActivate)
§12 INIT (set initial mode, first preview, show window)
```
The §0 header carries provenance so the next rebuild is cheap (`07` §9): name, version, AE-compat, one-line
purpose, author/site, settings section (+ migration note), CHANGELOG.

---

## §6 — MULTI-PASS BUILD (complex panels in passes, not monolithically)

- **Pass 1 — Architecture & shell:** DS → guarded polyfills → Settings → UI elements (all laid out) → empty
  states → resize handling → init. Buttons present, handlers stubbed. *Verify:* layout correct at min size,
  mode switching works, empty states display.
- **Pass 2 — Data & preview:** cache → preview → `onChanging` wiring → scope change → `onActivate` refresh.
  *Verify:* preview updates on keystroke; no DOM reads in `onChanging`.
- **Pass 3 — Action engine:** guarded handlers → undo groups → locked-layer handling → batch ops → post-action
  feedback → color management. *Verify:* locked skipped with count; undo groups in `finally`; colors reset.
- **Pass 4 — Polish & QC:** helpTips on every element → keyboard shortcuts → settings persistence → about/version
  → run §7.
- **Pass 5 — Stress test:** the adversarial fixtures (`00` §6) + the **cold-start test**.

For simple tools (<~300 lines) combine passes 1–3; for 500+ lines follow them strictly.

---

## §7 — MANDATORY QC CHECKLIST (each item exists because a real test revealed a bug)

**7.1 ES3 compliance (scripts only — NOT expressions)**
- [ ] Zero `let`/`const`, arrow functions, template literals, destructuring, spread/rest, default params,
      `for…of`, `Promise`/`async`, `Set`/`Map`.
- [ ] No ES5 Array methods (`forEach`/`map`/`filter`/`reduce`/`some`/`every`/`find`/`includes`) **unless a guarded
      polyfill is shipped at the top**.
- [ ] No `String.trim`/`includes`/`startsWith`/`endsWith`/`padStart` (or guarded polyfill); no `Object.keys`/
      `values`/`entries`/`assign`/`create`; no `Date.now`/`toISOString`.
- [ ] **`Array.indexOf` and `JSON`: ASSUME ABSENT** — Adobe panels inject them, so reliance fails cold-start.
      Ship guarded polyfills, each `if (!X)` so a native/injected version is never clobbered.
- [ ] `RegExp` uses only `g`/`i`/`m` (no dotAll/lookbehind/named groups/`u`/`y`). No reserved words as object keys.
- [ ] **Cold-start test passed** (quit AE, reopen with NO Libraries/Learning panels, run).

**7.2 Structural integrity**
- [ ] Every `beginUndoGroup()` matched by `endUndoGroup()` in a `finally`; same for `beginSuppressDialogs()`/`end`.
- [ ] All brackets/parens/braces balanced; every referenced function/variable defined/declared.
- [ ] `(function (thisObj) {…})(this)` wrapper + `thisObj instanceof Panel` check (dockable vs palette).

**7.3 UI quality**
- [ ] `minimumSize` set; `onResizing`/`onResize` calls `layout.layout(true)`.
- [ ] `helpTip` on every edittext/button/checkbox/dropdownlist/listbox column.
- [ ] Zero `alert()` for expected conditions; `alert()` only for the About box / truly unrecoverable error.
- [ ] Empty-state messages cover every condition; labels follow §3; primary action uses accent draw.
- [ ] Mode panels use fixed `minimumSize` height (no layout jump on tab switch).
- [ ] Enter triggers the primary action from input fields (check both `"Enter"` AND `"Return"` keyName).
- [ ] **Vehicle confirmed ScriptUI** (not a request that needed CEP) before building (`00` §3).
- [ ] Any API newer than the user's AE version is **version-gated** (`parseFloat(app.version)`) with graceful
      degradation/warning.
- [ ] **"Allow Scripts to Write Files and Access Network" requirement stated** if the tool does I/O.

**7.4 Interaction safety**
- [ ] `_actionInProgress` guard on every action handler; primary button disabled during execution.
- [ ] `_suppressOnChange` flag wraps every programmatic ListBox mutation; `onChange` on ListBox NEVER toggles
      checkboxes (use Space key or a Toggle button — toggling on `onChange` breaks arrow-key nav).
- [ ] Batch removals sorted **index-descending**; `layer.locked` checked before any modification.
- [ ] Stored DOM refs validated before action (`Layer.id`/`layerByID`, or `comp.layer(idx).name === storedName`).
- [ ] IIFE closure capture in deferred loops: `(function (rec) {…})(records[i])`.

**7.5 Performance**
- [ ] `onChanging` handlers never read `app.project`/`comp.layers`/any DOM.
- [ ] ListBox `visible = false` before population, `true` after; capped ~200 rows with forced filtering.
- [ ] Scans target specific property groups, never the layer root; recursive walkers depth-limited; barren groups
      skipped.

**7.6 Feedback & state**
- [ ] Post-action feedback = verb + count + noun; skipped items reported with reason; undo hint after destructive ops.
- [ ] Post-action colors reset to `DS.dimText` on next interaction; settings persisted for tab/dropdown/checkbox.
- [ ] Long ops (>~1 s or >~100 items) show per-iteration progress (`update()` + `$.sleep(1)`) + a cancel path.

**7.7 Cross-platform**
- [ ] Safe-Unicode subset only; `g.measureString()` null-guarded in every `onDraw`.
- [ ] Tab active state platform-aware (Mac accent fill / Win bottom bar); Enter check covers `"Enter"` + `"Return"`.
- [ ] File paths use `Folder.fs` separator awareness; effects/properties by **matchName**, menu commands by
      numeric ID.

**7.8 Deployment & handoff**
- [ ] Exact install path for the user's OS + AE version (`00` §7); dockable wrapper present.
- [ ] Header block: name, version, AE-compat range, description, site/support, settings-migration note, changelog.
- [ ] If file logging: buffered writes, session ID, rotation ~500 KB, `Folder.userData` path.
- [ ] Adversarial fixtures listed for the user to test; required prefs stated ("Allow Scripts to Write Files…").

Then run the canon **Test Battery** (`01`) — the 5 gut checks — and the expert addendum (`04` §11).

---

## §8 — INTERACTION MODEL

**Keyboard:** Enter/Return = primary action; Cmd/Ctrl+Z = native undo; Cmd/Ctrl+A in ListBox = select all
visible; Space on a highlighted ListBox item = toggle (NOT `onChange`); Cmd/Ctrl+F = focus search; Esc = close a
dialog (no-op for dockable). **ListBox:** `onChange` updates preview only (never toggles state); `onDoubleClick`
navigates to the item in AE; a dedicated `[Toggle]` button for mouse users; multi-select on by default; status as
a text prefix on existing columns (saves horizontal space). **Tabs:** `custombutton` + `applyTabDraw`; an
`_isActive` flag toggled by the mode switcher; all mode panels in the DOM at once (visibility toggled), consistent
`minimumSize` height; active mode persisted.

**Action handler skeleton:**
```javascript
function doAction() {
  if (_actionInProgress) return;
  var comp = app.project.activeItem;
  if (!(comp instanceof CompItem)) { showStatus(DS.warn + "  Open a composition first", DS.warning); return; }
  _actionInProgress = true; actionBtn.enabled = false;
  app.beginUndoGroup("Operation Name");
  try {
    var count = 0, skipped = 0;
    // batch op: check layer.locked (skip+count), sort removals index-descending, validate refs first
    var msg = DS.ok + "  Verbed " + count + " noun" + (count !== 1 ? "s" : "");
    if (skipped > 0) msg += " (" + skipped + " locked, skipped)";
    showStatus(msg + " " + DS.dash + " Cmd+Z to undo", DS.success);
  } catch (e) { showStatus(DS.fail + "  " + e.toString(), DS.error); }
  finally { app.endUndoGroup(); _actionInProgress = false; refreshPreview(); }  // refresh re-enables the button
}
```

---

## §9 — PROGRESSIVE DISCLOSURE (ScriptUI essentials; full catalog in `03`)

Primary surface serves the 80%; advanced options behind disclosure (gear / Settings tab / "More…" dialog). **Rule
of thumb:** a control used in fewer than ~1 in 5 sessions belongs behind disclosure (the Permanent-Real-Estate
Test, `02` §3). Mechanisms in order: smart default + silent override → gear/"More…" dialog → secondary tab →
(avoid) expandable group. Context-adaptive controls may show/hide **only** if it doesn't change panel height, the
transition is tied to an explicit action, and the hidden controls are genuinely irrelevant in the current mode.

---

## §10 — WHAT PREMIUM TOOLS DO (the $5-vs-$50 details)

They remember you · never crash (locked/missing/camera/0-dur/guide layers handled, degrade not die) · show
before they do · speak your language · know when to shut up (no confirmation theater) · guide without lecturing
(empty states + helpTips + layout) · respect your screen (compact, the hero gets the real estate) · feel fast
(cached reads, ListBox behind `visible=false`, progress on long ops) · handle the edge cases you forgot · look
like they belong (AE-sympathetic colors, platform-aware rendering).

---

## §11 — APPLYING THIS STANDARD

0. Confirm vehicle is ScriptUI (`00` §3); if it needs HTML/CSS it's CEP (`06`); never UXP for AE. If it's a
   rebuild, route through `07` first.
1. Run the workflow analysis (`02`) → the one-page brief → confirm before designing.
2. Identify the tool type (Transform / Scan / Hybrid, §4.3).
3. Design the empty-state map (§4.1).
4. Plan the spatial hierarchy (§1).
5. Write the label set (§3).
6. Build in passes (§6), applying `04` rigor throughout.
7. Run §7 + the canon Test Battery (`01`).
8. Verify & hand off (cold-start + adversarial fixtures + exact install path + required prefs — `00` §6–§7).

---

## §12 — CEP UI BASELINE (only when Phase 0 selected CEP)

Full detail in `06-cep-extensions.md`. In brief: scaffold with **Bolt-CEP** (don't hand-roll manifest/signing/
HMR); frontend = a framework + a real design system that **honors the host theme** (`CSInterface.getHostEnvironment()
.appSkinInfo`); **the host (`host.jsx`) is STILL ES3** — every §7.1 rule applies; the **bridge** is async JSON-
over-string (`evalTS()`/`evalScript()`), keep calls small, never assume ordering; persistence via `localStorage`/
`cep.fs`/`Folder.userData`; errors inline, never a blocking host `alert()`. Every canon principle and UX mechanism
still applies — CEP gives you better tools to honor them, not permission to ignore them.
