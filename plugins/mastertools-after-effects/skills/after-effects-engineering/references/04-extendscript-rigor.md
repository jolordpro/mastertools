# 04 — ExtendScript Rigor (the engineering that survives every machine)

> The deep discipline that separates code that works on the author's machine from code that survives every
> machine, every language, every project, and a user mashing Cmd+Z. All code here is **strict ES3** (see `00`
> §4 for the language rules + the phantom-polyfill trap + the guarded-polyfill list). For CEP hosts this all
> still applies — the host is ES3 too.

---

## §1 — LOCALIZATION: matchName, never display name

The most common "works for me, broken for them" defect after the phantom-polyfill trap. AE ships in many
languages; **display names are localized, matchNames are not.**

- **matchName** = the stable, language-independent internal ID (`"ADBE Gaussian Blur 2"`,
  `"ADBE Transform Group"`, `"ADBE Position"`). Identical on every language/build.
- **name / displayName** = what the user sees, translated per language.

**Rules:** address effects/properties by **matchName**; iterate groups by **index + matchName check**, never by
`.name`; read `.name` for *display only*, never branch logic on it; menu commands by **numeric command ID** (not
localized `findMenuCommandId("text")`). Never guess a matchName — verify against the docsforadobe match-name
pages, or have the user print `selectedProperties[0].matchName`.

```javascript
// language-independent effect lookup
function findEffectByMatchName(layer, mn) {
    var fx = layer.property("ADBE Effect Parade");   // null on cameras/lights — guard upstream
    if (!fx) return null;
    for (var i = 1; i <= fx.numProperties; i++) {
        var e = fx.property(i);
        if (e && e.matchName === mn) return e;
    }
    return null;
}
```

---

## §2 — THE UNDO PROBLEM: state ExtendScript can't see

ExtendScript **cannot detect Cmd/Ctrl+Z** (or any manual edit while your panel is open). Your cached model
silently diverges the moment the user undoes one of your operations; acting on a stale cache corrupts the
project. This is the defining hazard of long-lived panels.

1. **Validate every stored reference immediately before acting on it.**
   ```javascript
   function isRefValid(rec, comp) {
       try {
           if (rec.layerId != null && comp) {                 // best: stable ID (AE 22+)
               var l = app.project.layerByID(rec.layerId);
               return l != null && l.containingComp === comp;
           }
           var byIdx = comp.layer(rec.index);                  // fallback: index+name
           return byIdx && byIdx.name === rec.name;
       } catch (e) { return false; }
   }
   ```
2. **Prefer `Layer.id` + `Project.layerByID()` (AE 22+) over index** for anything stored across time. Capture
   `layer.id` at scan time; resolve at action time.
3. **Provide an explicit Refresh** as a first-class affordance (the user's only way to reconcile after an undo);
   auto-refresh the cache from the DOM after every operation.
4. **Re-read on focus** (`onActivate`) — the user may have undone/edited between interactions.
5. **Never hold a live `Layer`/`Property` across a mutation** that changes the layer collection — re-resolve by
   ID after.

*Mental model: your cache is a photo, not a mirror. Every action that trusts the photo must first check it still
matches the room.*

---

## §3 — THE SINGLE-THREADED REALITY & RESPONSIVE LONG OPS

ExtendScript runs on AE's **main thread** — no real async, no `setTimeout`, no workers. A long loop **freezes
the whole app**; "it looks hung" is the #1 cause of users force-quitting mid-batch. For ops over ~100 items or
~1 s:

1. **A real progress window, updated every outer-loop iteration** (one heavy item can take seconds; a stale bar
   reads as a hang). `panel.update()` **alone is often insufficient — pair it with `$.sleep(1)`** so the OS
   actually paints (the documented trick).
   ```javascript
   function makeProgress(title, total) {
       var w = new Window("palette", title, undefined, {closeButton:false});
       w.bar = w.add("progressbar", undefined, 0, total); w.bar.preferredSize = [320, 8];
       w.txt = w.add("statictext", undefined, "");        w.txt.preferredSize = [320, 16];
       w.show();
       w.tick = function (i, label) { this.bar.value = i; this.txt.text = label || (i + " / " + total);
                                      this.update(); $.sleep(1); };
       return w;
   }
   ```
2. **A cancel path** — a "palette" progress window can host a Cancel button; check a flag each iteration and bail
   cleanly (still closing the undo group in `finally`).
3. **Debounce expensive recompute** with `app.scheduleTask(fn, delayMs, false)` (AE 2024+ — the only timer-like
   mechanism) to coalesce rapid input.
4. **Yield periodically** in very long loops (`if (i % 25 === 0) progress.tick(i);`).
5. **Suppress dialogs around batch work** so one modal AE warning doesn't stall a 500-item run:
   `app.beginSuppressDialogs()` … `app.endSuppressDialogs(false)` in `finally`. Pair every begin with an end.

---

## §4 — PERFORMANCE (where the milliseconds actually go) — `perf`

The cost is in **DOM reads**, not JS logic. Each property read can trigger evaluation; each `activeItem` lookup
is a call.

- **Cache `app.project.activeItem` once** at the top; don't call it in a loop. Same for `comp.numLayers`,
  `comp.selectedLayers`, `comp.layers`.
- **Read once, compute in JS.** Build a plain-object snapshot (`{id,name,index,enabled,locked}`) in a single
  pass, then filter/sort/preview on the JS array. **Never re-read the DOM inside a preview or `onChanging`
  handler.**
- **Target specific property groups, never walk from the layer root.** A complex shape layer exposes 10,000+
  nodes; go straight to `layer.property("ADBE Effect Parade")`, `"ADBE Transform Group"`, `"ADBE Text
  Properties"`, etc.
- **Skip barren groups** (Material Options, Audio, Data, irrelevant Layer Styles). **Depth-limit recursive
  walkers (≤25)** — shape/text trees overflow ExtendScript's shallow call stack.
- **Cap work per layer** (e.g., 5,000 properties); report a monster layer as skipped rather than hanging.
- **Deselect in O(1)** with `app.executeCommand(2004)` (Deselect All), not a loop.
- **Hide the ListBox during population** (`visible = false` → add → `true`); cap visible rows ~200, force
  filtering above.
- **Batch undo, not per-item undo** — one `beginUndoGroup` around the whole batch (faster + one clean undo step).

---

## §5 — ROBUST PROPERTY & EFFECT APPLICATION

Real projects contain cameras where you expect AVLayers, missing plugins, hold keyframes, third-party effects
with quirky matchNames.

- **Null-guard group access** — `layer.property("ADBE Effect Parade")` is **null** on camera/light layers.
- **Check `canAddProperty(matchName)` before `addProperty`** — and fall back matchName → displayName for some
  third-party effects (try matchName, catch, retry with displayName).
- **Check interpolation type before `setTemporalEase`** — hold keyframes throw; read
  `keyInInterpolationType`/`keyOutInterpolationType`, skip or convert first.
- **Guard `canSetExpression`/property reads** in try/catch — some PropertyGroup children throw on access;
  absence is a skip, not an error.
- **Verify the effect applied** after `addProperty` (a missing plugin is a silent no-op on some builds).
- **Version-gate new APIs** (`parseFloat(app.version)`), degrade gracefully, tell the user what they're missing.

```javascript
function addEffectSafely(layer, matchName, displayName) {
    var parade = layer.property("ADBE Effect Parade");
    if (!parade) return null;                      // camera/light/etc.
    if (!parade.canAddProperty(matchName)) {
        if (!displayName || !parade.canAddProperty(displayName)) return null;
        matchName = displayName;                   // 3rd-party fallback
    }
    try { return parade.addProperty(matchName); } catch (e) { return null; }
}
```

---

## §6 — WRITING EXPRESSIONS FROM SCRIPTS — `expressions-from-scripts`

Treat it like surgery — it touches user data that's expensive to recreate.
- **Back up before overwrite** — log the old `prop.expression` to your file log (an `EXPR_BACKUP` line) so a
  mistake is recoverable beyond AE's undo.
- **Set both when clearing**: `prop.expression = ""` **and** `prop.expressionEnabled = false` (some builds need
  both).
- **Mind the target engine** — read `app.project.expressionEngine` (`"javascript-1.0"` or `"extendscript"`),
  write matching syntax, warn on mismatch (see `08-expressions.md`).
- **Escape strings correctly** — the expression is a JS string in your ES3 source; build with concatenation and
  `\n`, not template literals.
- **`prop.canSetExpression` must be true** — not all properties accept expressions.

---

## §7 — STRUCTURED RESULTS & PARTIAL SUCCESS

A batch op rarely fully succeeds or fully fails. Return a **result object**, not a bare count.

```javascript
function newResult() {
    return { ok: 0, skipped: [], failed: [],   // skipped/failed hold {ref, reason}
             note: function () {
                 var s = this.ok + " done";
                 if (this.skipped.length) s += ", " + this.skipped.length + " skipped";
                 if (this.failed.length)  s += ", " + this.failed.length + " failed";
                 return s;
             } };
}
```
Distinguish **skipped** (expected: locked, wrong type, already-done) from **failed** (unexpected: threw); surface
reasons grouped ("3 failed (locked layers) — unlock and retry"); keep failed refs for a **Retry Failed** button.
**Idempotency:** design ops so re-running is safe — detect already-applied state and count it as skipped, not
re-applied. Re-runnable tools are trusted tools.

---

## §8 — PLAN → PREVIEW → EXECUTE (the dry-run architecture)

For batch tools, compute the entire plan as data first, show it, then execute — don't interleave "decide and do."
```
SCAN    → snapshot []         (pure DOM read, cached)
PLAN    → operations []       (pure JS: {ref, action, from, to, willSkip, reason})
PREVIEW → render plan         (pure JS → UI; shows exactly what will happen, incl. skips)
EXECUTE → walk plan in one undo group, validating each ref just-in-time (§2)
REPORT  → result object (§7), auto-refresh snapshot
```
Benefits: the preview is *exactly* what executes (no drift); skips are visible before commit; the plan is
testable in isolation; execution is a simple, auditable loop.

---

## §9 — PRESETS, CONFIG & TEAM SHARING — `presets`

Beyond `app.settings` (per-user/per-machine key/value for last-used UI state):
- **Named presets to disk** as JSON (polyfilled `JSON`) in `Folder.userData/<ToolName>/presets/` — a snapshot of
  the option set the user can name, recall, and **export/import as a file** (key for teams).
- **Schema-version your config** (`{ "schema": 2, … }`). On load, if `schema` is older, **migrate forward** in
  code rather than failing. This is how a tool evolves without orphaning saved setups.
- **File I/O correctness:** set `f.encoding = "UTF-8"` before read/write (handle a possible BOM on read); build
  paths with `Folder` joins (`Folder.fs` awareness), never hard-code `/` or `\`; **write to a temp file then
  rename** so a crash mid-write can't corrupt the existing preset; wrap I/O in try/catch and surface failures
  inline ("Allow Scripts to Write Files" off, disk full, perms).
- **Store the AE version settings were written under** — so a later downgrade doesn't replay settings for APIs
  that no longer exist.

---

## §10 — DOCKABILITY, ENGINE PERSISTENCE & LIFECYCLE

- **Dockable wrapper:** `(function (thisObj) { … })(this)` + `thisObj instanceof Panel ? thisObj : new
  Window("palette", …)`. A panel in `ScriptUI Panels/` is passed a `Panel`; a menu-run script gets a window.
- **Persistent-engine caution:** dockable panels can survive across runs; with `#targetengine "name"` globals
  persist between invocations — initialize defensively (don't assume a clean global scope), don't leak listeners.
- **Clean teardown:** remove event listeners and stop any `scheduleTask` loops when the panel closes, so a
  re-open doesn't double-wire handlers.

---

## §11 — THE EXPERT QC ADDENDUM (beyond the Quality Standard §7)

- [ ] All effects/properties addressed by **matchName**, never localized display name; menu commands by numeric ID.
- [ ] Stored refs use `Layer.id`/`layerByID` where they persist; every stored ref re-validated just-in-time
      before mutation.
- [ ] Long ops show **per-iteration** progress (`update()` + `$.sleep(1)`); cancelable; dialogs suppressed.
- [ ] No DOM reads inside preview/`onChanging`; one snapshot pass, JS-only after.
- [ ] Recursive walkers depth-limited (≤25); scans target specific groups; barren groups skipped; per-layer cap.
- [ ] Expression overwrites backed up to log; engine match checked; clear sets both `""` + `expressionEnabled=false`.
- [ ] Batch returns a **result object** (ok/skipped/failed + reasons); Retry-failed possible; op is idempotent.
- [ ] Config JSON is **schema-versioned** with a migration path; I/O is UTF-8, temp-then-rename.
- [ ] Panel teardown removes listeners and cancels scheduled tasks.
