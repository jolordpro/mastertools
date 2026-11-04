# AE ExtendScript API gotchas — verified notes

Behaviour that is either undocumented, changed between versions, or contradicts the
obvious reading. Each entry records how confident the finding is and where it came
from, so a future reader knows what is established and what still needs a live test.

Verification levels used here:
- **CONFIRMED** — official scripting guide or changelog.
- **COMMUNITY** — consistent reports across independent forum sources, not in the docs.
- **UNVERIFIED** — reasoned or single-source; treat as a hypothesis and defend in code.

## Contents

- [Cache purging and `app.purge`](#cache-purging-and-apppurge)
- [Closing and opening projects](#closing-and-opening-projects)
- [Render queue isolation](#render-queue-isolation)
- [Single-frame stills and time spans](#single-frame-stills-and-time-spans)
- [Output modules and filenames](#output-modules-and-filenames)
- [Comp markers, and batching many renders](#comp-markers-and-batching-many-renders)
- [ScriptUI layout in a dockable panel](#scriptui-layout-in-a-dockable-panel)
- [ScriptUI windows: dialogs, scrolling, engines, real-input tests (2026-10-14)](#scriptui-windows-dialogs-scrolling-engines-real-input-tests-2026-10-14)
- [Suppression and error capture](#suppression-and-error-capture)
- [Text layers and TextDocument](#text-layers-and-textdocument)
- [Rendering frames from script](#rendering-frames-from-script)
- [Never concatenate an Array into a String](#never-concatenate-an-array-into-a-string)
- [Locked layers reject metadata](#locked-layers-reject-metadata)
- [Driving AE from the shell without losing errors](#driving-ae-from-the-shell-without-losing-errors)
- [Expression control names: the 39-byte limit](#expression-control-names-the-39-byte-limit)
- [Render queue hygiene](#render-queue-hygiene)
- [Headless testing of a builder script](#headless-testing-of-a-builder-script)
- [Colour properties](#colour-properties)
- [Effects and properties](#effects-and-properties)
- [Blending, Levels clipping, sampling and still depth at 16 bpc (2026-10-30)](#blending-levels-clipping-sampling-and-still-depth-at-16-bpc-2026-10-30)
- [Scripts Claude drives: no AE dialogs (2026-10-29)](#scripts-claude-drives-no-ae-dialogs-2026-10-29)
- [ffmpeg drops Rec.709 tags on raw pipes (ffmpeg 8.1, 2026-10-29)](#ffmpeg-drops-rec709-tags-on-raw-pipes-ffmpeg-81-2026-10-29)

## Cache purging and `app.purge`

**CONFIRMED — behaviour changed in AE 24.3.** From 24.3 onward,
`PurgeTarget.ALL_CACHES` purges the **disk cache as well as RAM**, and a new member
`ALL_MEMORY_CACHES` was added to give scripts the previous RAM-only behaviour. Before
24.3, `ALL_CACHES` was RAM only and the disk cache was unreachable from scripting.
Source: AE scripting guide changelog, ae-scripting.docsforadobe.dev.

Valid `PurgeTarget` members: `ALL_CACHES`, `UNDO_CACHES`, `SNAPSHOT_CACHES`,
`IMAGE_CACHES`, plus `ALL_MEMORY_CACHES` on 24.3+.

Write purges defensively so an unknown member is a no-op rather than a crash, and gate
version-dependent messaging on the actual version:

```javascript
function purgeTarget(name) {
    try {
        if (PurgeTarget[name] !== undefined) { app.purge(PurgeTarget[name]); return true; }
    } catch (e) {}
    return false;
}

function aeVersionAtLeast(major, minor) {
    var m = null;
    try { m = String(app.version).match(/^(\d+)\.(\d+)/); } catch (e) { m = null; }
    if (!m) { return false; }
    var maj = parseInt(m[1], 10), min = parseInt(m[2], 10);
    return (maj > major) || (maj === major && min >= minor);
}
```

**UNCERTAIN — the Purge menu command.** On pre-24.3 builds the only route to the disk
cache is `app.findMenuCommandId()` + `app.executeCommand()` for Edit ▸ Purge ▸ "All
Memory & Disk Cache". The exact literal string is not authoritatively documented and
the ampersand has been reported to defeat `findMenuCommandId` on some builds. Try
several forms and treat failure as non-fatal:

```javascript
var PURGE_MENU_CANDIDATES = [
    "All Memory & Disk Cache",
    "Purge All Memory & Disk Cache",
    "All Memory and Disk Cache",
    "All Memory &amp; Disk Cache"
];
```

Hardcoded numeric command IDs circulate in community lists; they are version-fragile,
so prefer name lookup. **COMMUNITY:** executing the purge via `executeCommand` appears
to clear the disk cache with no confirmation dialog, unlike the UI path.

**Purge at every hand-back in a shared or unattended run (CONFIRMED by measurement, 2026-10-30).**
`app.purge(PurgeTarget.ALL_CACHES)` took a 1.74 GB disk cache to 51 MB. A full disk cache raises a modal
disk-space warning that blocks the app until someone clicks it, and nobody may be there to click it.

## Closing and opening projects

`app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES)` is the reliable way to discard an
edited project without a prompt. Do not rely on dialog suppression to answer a
"Save changes?" prompt — suppression picks a default you do not control, and the wrong
default here overwrites the user's master.

`CloseOptions` members: `DO_NOT_SAVE_CHANGES`, `PROMPT_TO_SAVE_CHANGES`, `SAVE_CHANGES`.

The safe cycle for batch work is close → purge → open. Make one function the only place
`app.open` appears so the invariant is structural rather than a review question.

## Render queue isolation

**Opening a project reloads its render queue from disk.** If a user's master has queued
items enabled, they come back enabled on every open, so disabling must be re-applied
after each one. `renderQueue.render()` renders *every* enabled item, so skipping this
means rendering someone else's work.

Snapshot each item's `render` flag before the run and restore in a `finally`. Setting
`.render` on an item whose status is `DONE` can throw — wrap per-item access in
`try`/`catch` and treat a failure as benign.

`RQItemStatus` members: `WILL_CONTINUE`, `NEEDS_OUTPUT`, `UNQUEUED`, `QUEUED`,
`RENDERING`, `USER_STOPPED`, `ERR_STOPPED`, `DONE`.

## Single-frame stills and time spans

`RenderQueueItem.timeSpanStart` and `timeSpanDuration` are writable, in **seconds**.

**CONFIRMED — `RenderQueueItem.applyTemplate()` destroys the span; the output module's
`applyTemplate()` does not.** Measured on AE 26.3x87. Setting a one-frame span and then
applying "Best Settings" reset it to `start=0, dur=599 frames` — the whole comp.
Applying an *output module* template afterwards left the span untouched. So the only
safe order is:

```
item.applyTemplate(renderSettings)      // first — this one wipes the span
setOneFrameSpan(item, comp)             // then the span
item.outputModule(1).applyTemplate(om)  // safe, does not touch the span
```

This also rules out the obvious shortcut. **`Composition ▸ Save Frame As ▸ File…` builds
a correct single-frame queue item for you, but you cannot use it from script.**
`findMenuCommandId("Save Frame As")` returns 2233, which is the *submenu* — executing it
does nothing, adds no item, raises no error. The circulating id 2104 for the `File…`
child also did nothing on 26.3. And even if you got it, applying "Best Settings"
afterwards would wipe the span AE just set, while skipping it leaves Render Settings on
"Current Settings" — which follows the comp's current resolution, so a comp left at Half
silently exports at half size.

### Setting the span raises a modal *before* you ever call render()

**CONFIRMED — AE 26.3.** A one-frame span on the **last frame of a comp** necessarily
runs past the comp end, and AE puts up a modal at *assignment* time:

> After Effects warning: timeSpanDuration of 0.02 seconds will cause render to have
> frames outside of range defined by comp displayStartTime (0) and end of comp duration
> (2). Render will succeed, but may have blank frames.

The render itself is fine — the requested frame comes out correct, and the out-of-range
extra frame is the one you discard anyway. The problem is purely the dialog: grabbing
the last frame of an end card is an ordinary request, and a modal there hangs the tool
until somebody clicks OK.

The lesson generalises past this one warning: **the suppression triad has to open before
the first property assignment, not just around `render()`.** Wrapping only the render
call leaves every setup-time dialog unsuppressed. Open it as soon as the queue item
exists, and clear the captured `onError` string immediately before `render()` so a
harmless setup warning cannot be misreported as a render failure.

**COMMUNITY — a duration of exactly `comp.frameDuration` can throw a float-precision
range error** ("Value 0.03 out of range 0.03 to …"). This matters most at 59.94 fps
where `frameDuration` is 0.016683350016683. Nudge upward until one takes, staying under
1.5 frames so the span can still only round to a single frame, and verify by reading
back:

```javascript
var candidates = [fd, fd * 1.001, fd * 1.01, fd * 1.2];
for (var i = 0; i < candidates.length; i++) {
    try { item.timeSpanDuration = candidates[i]; } catch (e) { continue; }
    var got = item.timeSpanDuration;
    if (got > 0 && got < fd * 1.45) { return; }   // rounds to exactly one frame
}
fail("would not accept a one-frame span — refusing to render a whole sequence");
```

Failing loudly here matters: a span that silently stays at full duration renders the
whole comp as a still sequence, which at 59.94 fps over ten seconds is ~600 files per
item.

### A one-frame span renders two frames, and the counter lies about which

**CONFIRMED — measured on AE 26.3x87, macOS, 59.94 fps comp, Best Settings.** Three
findings that together mean a naive still export silently saves the wrong frame.

**Durations below `frameDuration` throw, and the failed write leaves the span at full
length.** Setting `fd * 0.25` through `fd * 0.99` all threw; each time
`timeSpanDuration` read back as the whole remaining comp (3.15 s) and the render
produced **190 stills**. Never nudge downward, and always re-read the span after
setting it — the readback check is what separates a still from a sequence.

**Exactly `fd` is accepted but quantised upward.** AE snaps time to a 1/10240 s grid
here, so `0.01668335001668` came back as `0.01669921875`, which straddles the next
frame boundary. Every single-frame export rendered **two** frames. This appears
unavoidable; plan to discard the extra rather than fight it.

**The filename counter is derived from the quantised span start rounded down, so it can
be one less than the frame it contains.** Measured, asking for each frame in turn:

| requested | quantised start | files written | actual content |
|---|---|---|---|
| 111 | 111.0002 (up)   | `00111`, `00112` | frame 111, 112 |
| 112 | 111.9992 (down) | `00111`, `00112` | **frame 112**, 113 |
| 250 | 249.9998 (down) | `00249`, `00250` | **frame 250**, 251 |

So matching the counter against the frame number returns the wrong frame whenever the
quantisation rounds down. What held on every frame tested (0, 7, 111, 112, 250): **the
lowest-numbered file is the frame that was requested.** Sort and take the lowest;
`Folder.getFiles()` order is arbitrary, so taking `[0]` is a coin flip.

Verify this class of bug by rendering a comp whose pixels encode their own frame — a
bar whose left edge sits at `x = frame` via
`[Math.round(time/thisComp.frameDuration) + 2, 50]` — then decode the PNG. A static
test comp cannot tell you which frame you got.

### AE appends its counter after the extension, not before it

**CONFIRMED — AE 26.3.** A still written as `NAME.png` lands on disk as
`NAME.png00112`. The documented `_[#####]`-before-extension form is not what happens
here. Deriving the extension with `/\.([A-Za-z0-9]+)$/` therefore yields `png00112` and
carries the counter into the saved filename. Match letters only and drop trailing
digits: `/\.([A-Za-z]+)[0-9]*$/`.

### Stringifying an AE error object can itself throw

**CONFIRMED — AE 26.3.** `"prefix " + err` and `String(err)` on an error caught from AE
can raise *"Object of type Error found where a Number, Array, or Property is needed"*.
Hit inside a `catch` block, this kills the script and puts up the modal the handler
existed to prevent — and it blocks the next `do javascript`, so it reads as a hang.
Guard every coercion and verify you got a primitive:

```javascript
function safeErr(e) {
    var s = null;
    try { if (typeof e === "string") { return e; } } catch (e0) {}
    try { s = e.toString(); } catch (e1) { s = null; }
    if (typeof s !== "string" || s === "") { try { s = e.message; } catch (e2) { s = null; } }
    if (typeof s !== "string" || s === "") { return "unknown After Effects error"; }
    return s;
}
```

**Timecode to frame number.** AE counts a 59.94 fps comp on a 60-frame timebase, so
`0:00:01:51` is frame `1 * 60 + 51 = 111`. Confirm the convention by reading the frame
counter under the comp's time display, then derive time from the comp's own
`frameDuration` rather than hardcoding seconds.

## Output modules and filenames

**Movie codec and format are read-only to scripting.** You cannot build an output
module from script. Validate that a named template exists on *this machine* and stop
with recreate instructions if it does not — templates are machine-local, so a script
that works on one workstation fails on the next.

Read the available names from a scratch queue item, then remove it:

```javascript
var probe = rq.items.add(comp);
probe.render = false;
var omNames = probe.outputModule(1).templates;   // machine-local
var rsNames = probe.templates;
probe.remove();
```

**Assign the file, then read it back.** Assigning `outputModule.file` lets AE rewrite
the extension to match the format the module actually writes. Reading `om.file` *before*
assignment gives you the template's stale path and the wrong extension.

**COMMUNITY — AE may append `_[#####]` to still filenames.** Whether it does appears to
depend on the queue's Output Info field reading "Single frame" versus sequence-eligible,
and there is no setting that reliably suppresses it. Do not fight it. Render to a
scratch path, glob for the variants, then copy to the exact destination name:

```javascript
// matches NAME.ext, NAME_#####.ext and NAME#####.ext — never NAMEX.ext
new RegExp("^" + escRe(base) + "(_?[0-9]{1,8})?\\." + escRe(ext) + "$", "i");
```

Clearing the destination first matters because `File.copy()` does not overwrite.

## Comp markers, and batching many renders

**CONFIRMED — AE 26.3.** `CompItem.markerProperty` behaves exactly as documented, which
makes markers the cheapest "which frames do you want?" input a tool can take — and the
only one that survives a Premiere handoff, since **Premiere sequence markers become AE
comp markers on `File ▸ Import ▸ Adobe Premiere Pro Project`** (Adobe helpx, "Share
markers between Premiere and After Effects").

```javascript
var mp = comp.markerProperty;          // null on some item types — guard
for (var i = 1; i <= mp.numKeys; i++) {          // 1-indexed, like everything in AE
    var t   = mp.keyTime(i);                      // seconds
    var cmt = mp.keyValue(i).comment;             // "" when unlabelled
    var idx = Math.round(t / comp.frameDuration); // the frame
}
```

Markers arrive in creation order, not time order, and two markers can land on one frame —
sort by time and dedupe by frame index before rendering, or you get out-of-order and
duplicate output.

Three rules for a batch that shares one render engine with a single-shot command:

**Park the user's queue once per run, not once per item.** Wrap the whole batch in a
`withParkedQueue(fn)` that snapshots every `render` flag, disables them, and restores in a
`finally`. Parking per item is N times the risk of leaving a flag wrong if something
throws mid-run. Verified against a 62-item live queue, and worth asserting in tests by
counting park transitions: a 3-frame batch over 52 items should park **52** times, not 156.

**Account per output, not per run.** One frame failing must not discard the frames that
succeeded — collect `{done, failed[], files[]}` and report "2 of 3 exported. Failed:
frame 40: …". The classic bug is wrapping the loop in one `try` so the first failure jumps
past everything already accomplished.

**Escape is the only cancel a blocking loop can offer.** ScriptUI cannot process a button
click while `renderQueue.render()` blocks, so a Cancel button is decorative. Poll the
keyboard between items instead:

```javascript
function escapePressed() {
    try { return ScriptUI.environment.keyboardState.keyName === "Escape"; }
    catch (e) { return false; }
}
```

## ScriptUI layout in a dockable panel

**CONFIRMED — AE 26.3, measured by reading `control.bounds` after each layout.** A
dockable panel gets resized to arbitrary shapes by the user, and ScriptUI has no reflow.
Six behaviours make "just make it responsive" much harder than it looks. Debug this by
dumping `bounds` for every control, not by squinting at screenshots — each of these was
invisible or misleading on screen and obvious in the numbers.

**`preferredSize` is frequently ignored; `maximumSize` is what gets honoured.** In a row,
ScriptUI handed *every* child an identical 231px regardless of the `preferredSize` set on
it, pushing the trailing controls past the panel edge. The one control that came out right
was the only one that also had a `maximumSize`. Cap every child explicitly.

**`visible = false` still reserves the child's slot.** A hidden label left a 71px hole and
squeezed the button beside it to zero width. Zero *both* sizes to actually reclaim it:

```javascript
c.visible = show;
c.preferredSize = show ? [-1, -1] : [0, 0];
c.maximumSize   = show ? [4000, 40] : [0, 0];
```

**`layout.layout(true)` resizes the CONTAINER to its preferred size.** Calling it from a
resize handler stretched a palette to 3059px wide in row mode, and grew a 52px-tall strip
back to 147px. Use `layout.layout(true)` exactly once at build; use `layout.resize()`
everywhere after.

**Read the size before touching the layout.** `layout.resize()` can itself grow a short
container up to its content height. A handler that calls `resize()` first and measures
second reads the *grown* size, so a short-and-wide arrangement can never be selected:

```javascript
w.onResizing = w.onResize = function () {
    var rw = 0, rh = 0;
    try { rw = this.size.width; rh = this.size.height; } catch (e) {}
    applyLayout(rw, rh);      // measure first, lay out second
};
```

**An intermediate group gets sized to its content and centred.** Wrapping the controls in
one group (the obvious way to flip orientation) sized that group to 247px inside a 420px
panel and centred it, indenting everything by ~86px. `alignment: ["fill","fill"]`,
`preferredSize` and `minimumSize` on the group all failed to override it. Add controls
**directly to the panel** — its size is always exactly the docked size — and flip
`w.orientation` between `"column"` and `"row"` instead.

**Only relayout when the arrangement actually changes.** Resize events fire continuously
while the dock edge is dragged. Derive a key from the chosen arrangement and return early
when it is unchanged, or the panel flickers.

Related: a docked panel is built **once at launch**, so anything it computed then goes
stale — a status line reading "no comp open" will still say that after a project is
opened. Refresh on `mouseover`, and guard it so a real result is not wiped:

```javascript
w.addEventListener("mouseover", function () { if (statusIsIdle) { sayIdle(); } });
```

Prefer short fixed labels over truncation-prone ones. Text that fits at every width needs
no measuring, and it is the only approach that cannot clip.

## Suppression and error capture

`app.beginSuppressDialogs()` / `app.endSuppressDialogs(alertMessage)`. Whether nested
calls are reference-counted or whether the first `end` clears suppression outright is
**undocumented** — count depth yourself so only the outermost pair toggles:

```javascript
var SUPPRESS_DEPTH = 0;

function beginTriad() {
    var st = { msg: "", prevOnError: null, hadPrev: false };
    try { st.prevOnError = app.onError; st.hadPrev = true; } catch (e) {}
    app.onError = function (err) { st.msg = String(err); };
    if (SUPPRESS_DEPTH === 0) { app.beginSuppressDialogs(); }
    SUPPRESS_DEPTH++;
    return st;
}

function endTriad(st) {
    SUPPRESS_DEPTH--;
    if (SUPPRESS_DEPTH < 0) { SUPPRESS_DEPTH = 0; }
    if (SUPPRESS_DEPTH === 0) { try { app.endSuppressDialogs(false); } catch (e) {} }
    try { if (st && st.hadPrev) { app.onError = st.prevOnError; } } catch (e) {}
}
```

Always restore `app.onError` to whatever this triad displaced, so an inner `end` hands
control back to the outer handler rather than clearing it.

Export errors on Apple Silicon are frequently transient and their codes are
non-diagnostic — 1, 10, 784, 9988 and 19972 are all the same vague failure. Do not
decode the number; retry with `$.sleep(800)` and report the string captured by
`app.onError`.

## Colour properties

Colour properties read back as **four components** `[r, g, b, a]`. A three-element
`setValue` is rejected on some builds, so write `[r, g, b, 1]`.

`setValue` writes into the project's **working colour space**. If that space is linear
or anything other than sRGB, a straight hex write lands visibly off a brand guide. Do
not try to detect or compensate automatically — isolate the conversion in one function
so a correction is a single edit, and have the user eyeball one item before a batch.

Before writing, check `prop.expressionEnabled`. A driver property carrying a live
expression will be overwritten every frame, so `setValue` appears to succeed while
changing nothing. Report it as a preflight warning.

## Effects and properties

Find effects by `matchName` (e.g. `"ADBE Fill"`), never display name — users rename
effects on layers and display names are localised.

Find a sub-property by **value type** rather than sub-matchName. It survives renames,
localisation and version differences:

```javascript
var parade = layer.property("ADBE Effect Parade");   // null on cameras/lights
for (var i = 1; i <= parade.numProperties; i++) {
    var fx = parade.property(i);
    if (fx.matchName !== "ADBE Fill") { continue; }
    for (var j = 1; j <= fx.numProperties; j++) {
        var p = fx.property(j);
        if (p.propertyValueType === PropertyValueType.COLOR) { return p; }
    }
}
```

Effect property groups such as `"Compositing Options"` report `propertyValueType` as
`undefined`, so compare with `===` against the specific type you want rather than
testing truthiness.

Check `fx.enabled` — a colour written to a disabled effect is invisible and looks like
total failure.

`layer.property("ADBE Effect Parade")` returns null for cameras, lights and other
non-AV layers; guard it.


## Text layers and TextDocument

Four traps, all verified by controlled experiment on AE 26.x (2026), all silent or fatal.

**`addText()` inherits the last-used character style from prefs.** `Prefs-text.txt` →
`["Text Style Sheet"]` carries whatever was last typed in the UI — on one machine that was
`BC Sklonar Medium, 18px, tracking 415, All Caps`. Every scripted text layer is born with it.
**Write every field the design depends on explicitly**: `text`, `font`, `fontSize`,
`tracking`, `applyFill`, `fillColor`, `justification`.

**`fontSize` may be applied at ~100×.** Setting `fontSize = 3` rendered as roughly 300pt.
Verified by setting 3 / 30 / 300 on one string and measuring rendered ink — at 3, the ink
measured 377 × 224 px and `sourceRectAtTime` independently reported 376.9 × 223.6, an exact
match. Do not assume; render one probe and measure before committing a size system.
**UNVERIFIED whether this is universal or machine/font specific** — treat the ratio as
something to measure per project, not a constant to hardcode.

**`tracking` must be an integer within −1000…1000.** Non-integers throw
`"13202.49 is not an integer"`; out of range throws `"Value 3000 out of range -1000 to 1000"`.
Round and clamp before every write.

**`allCaps` and `smallCaps` are read-only** and throw on assignment, killing the script at
that line. Writability of TextDocument fields varies by version, so set essentials directly
and wrap the rest:

```javascript
function tdSoft(td, field, val) {
    try { td[field] = val; } catch (e) { SKIPPED[field] = true; }
}
```

### Leading collapses multi-line text — use one layer per line

`fontSize` is applied at ~100× on this build but **`leading` is not**, and leading is also
inherited from prefs. Setting `leading = fontSize` therefore collapses every line of a
multi-line string onto a single baseline — measured: a 16-line block rendered **23px tall**,
about 1px per line. Asking for `autoLeading = true` did not rescue it either.

For anything that must be reliable — a README comp, an on-canvas legend — **build one text
layer per line and position each explicitly.** It sidesteps leading entirely, and it lets you
style headers and body differently, which a single text block cannot do anyway.

Verify it rather than eyeballing: read `sourceRectAtTime().height` back and assert it is at
least `lines × 10`. A collapsed block is obvious in that one number and easy to miss on screen.

### `sourceRectAtTime` does not see a same-pass `setValue`

This is the one that wastes hours. After writing a TextDocument, `sourceRectAtTime()` still
returns geometry for the **previously committed** state. A measure → adjust → measure loop
therefore compounds its own step and runs away — an observed fit loop reached tracking 13202
before AE threw.

**Never iterate on text metrics in-pass.** Split into two script runs: pass A writes and
saves, pass B reopens and measures. Reloaded geometry is accurate — the 3/30/300 probe above
matched rendered pixels exactly once the project had been reopened.

### Tracking-to-fit, closed-form

To track a small line out so its width matches a larger line (the common
kicker-over-headline lockup), do not iterate. Ink width is linear in both size and tracking:

```
W(size, t) = k * size + gaps * t * size * trackPerUnit
```

Measure `k` (natural width per unit size) and `trackPerUnit` from **two probes on a reloaded
project** — one at tracking 0, one at a known tracking. Then:

```
size = targetW / (k + gaps * t_target * trackPerUnit)
t    = ((targetW - k * size) / (gaps * size)) / trackPerUnit
```

`gaps` is `text.length - 1` — interior gaps only, because `sourceRectAtTime` returns the ink
box, which excludes trailing advance. This landed three lockups within 0.2px on the first
try. Deriving `trackPerUnit` empirically also sidesteps the question of whether the tracking
unit is 1/1000 em of the nominal or effective point size.

Character-panel tracking is a `TextDocument` field with **no `Property` object**, so no
expression can drive it. Live tracking needs a Text Animator
(`ADBE Text Tracking Amount` + `ADBE Text Track Type` set to Between Characters). For a baked
deliverable, solving at build time is simpler and exact.

**`ADBE Text Track Type` is hidden to scripts until you add it yourself** (AE 26.5, verified 2026-10-01). After
`animatorProps.addProperty("ADBE Text Tracking Amount")` the Tracking Type property exists and reads 1, but
`setValue(2)` throws "Can not set value with this property, because the property or a parent property is hidden".
Call `animatorProps.addProperty("ADBE Text Track Type")` (re-fetch the layer first), then setValue works:
1 Before & After, 2 Before, 3 After. To space ONE pair of letters, select the second letter (an Expression Selector
returning 100 for that `textIndex`) with Tracking Type Before. `sourceRectAtTime` includes the animator's tracking.

### AppleScript `do javascript` timeouts are not failures

Driving AE from `osascript` (`tell application "Adobe After Effects 2026" to DoScriptFile …`)
frequently returns `AppleEvent timed out (-1712)` **after the script has already completed
successfully**. Wrap in `with timeout of N seconds`, but more importantly: verify by checking
the artifact the script was supposed to produce — a log file, the saved project's mtime —
never by trusting the AppleEvent's return.


## Rendering frames from script

**`comp.saveFrameToPng()` writes ASYNCHRONOUSLY.** `File.exists` immediately afterwards
returns `false` and `File.length` returns 0, even though the file lands moments later. A
script that checks its own output will report total failure while every frame is fine.
Verify from **outside** the script — poll the filesystem until the count stops changing —
never with an in-script existence check.

It also fails **silently**: on error it throws nothing and simply writes no file. So a
missing frame means "investigate", not "the comp is empty".

**`comp.resolutionFactor` applies to `saveFrameToPng`.** A comp left at half resolution
writes half-size PNGs, so any pixel measurement against comp-space coordinates must scale by
`renderedWidth / comp.width` or every measurement lands in the wrong place. (Render Settings
templates override resolution for real renders, so this affects probes, not delivery.)

**Motion Tile has a hard 30,000px ceiling, and it is stricter than the arithmetic suggests.**
`ADBE Tile` with Output Width *N*% on a layer of width *W* asks AE for `W × N/100` pixels.

It fails in two different ways, which is what makes it expensive to diagnose:

- Far above the limit it fails **silently** — no error, no file, and *every* comp downstream
  produces no frame at all. A 14,311px layer at 400% (57,244px) killed every render in a
  project with nothing logged anywhere.
- Nearer the limit it throws a modal:
  `Motion Tile cannot allocate a buffer larger than 30000 pixels in either dimension. (516)`

**Correction to an earlier version of this note:** 200% of a 14,311px layer (28,622px) is
under 30,000 on paper and still threw, because the layer was offset by a drift expression and
the offset counts against the budget. Do not size to the arithmetic limit and assume headroom.

**For an infinite horizontal scroll, prefer no Motion Tile at all.** Scale one layer to
*overfill* the frame and move it with a Throw expression, guarding the scale so the travel can
never expose an edge:

```javascript
/* scale = max(user value, width the drift needs, full frame height) + pad */
var travel = (Math.abs(speed) + Math.abs(parallax)) * thisComp.duration * enabled;
var needW  = ((frameW + pad + travel) / srcW) * 100;
var needH  = ((frameH + pad) / srcH) * 100;
out = Math.max(userScale, needW, needH);
```

That has no plugin ceiling, no buffer allocation, and the guard makes an exposed edge
impossible by construction rather than by discipline. Verify it by rendering frames and
asserting `alpha == 255` at all four edges.

## Locked layers reject metadata

`layer.locked = true` makes `layer.comment`, `layer.label` **and every reordering method**
(`moveToEnd`, `moveToBeginning`, `moveBefore`, `moveAfter`) **throw**, which kills the script
mid-build:

> Can not call method "moveToEnd" on Layer "GROUND" because the Layer is locked.

Treat locking as the **last** thing you ever do to a layer. Any helper that locks a layer must take its metadata as arguments and
write them *before* locking:

```javascript
function markGuide(layer, label, comment) {
    try { layer.guideLayer = true; } catch (e) {}
    if (label != null) { try { layer.label = label; } catch (e1) {} }
    if (comment) { try { layer.comment = comment; } catch (e2) {} }
    try { layer.locked = true; } catch (e3) {}   /* lock LAST */
}
```

Related: a guide layer never renders, in its own comp **or** when nested, so
`saveFrameToPng` of a comp whose content is all guide layers returns an empty frame. That is
correct behaviour, not a bug — to inspect one, un-guide it, render, and do **not** save.

## Driving AE from the shell without losing errors

AE surfaces script errors as a **modal dialog**, which blocks the next `do javascript` and
looks exactly like a hang. When scripting a chain from bash, read and dismiss the modal
between steps so a failure is reported rather than silently stalling everything after it:

```bash
DLG=$(osascript -e 'tell application "System Events" to tell process "Adobe After Effects 2026"
  if exists window 1 then
    if exists static text 2 of window 1 then return value of static text 2 of window 1
  end if
  return ""
end tell')
[ -n "$DLG" ] && echo "MODAL: $DLG" && exit 1
```


## Expression control names: the 39-byte limit

`property(name)` refuses any name longer than **39 bytes**:

> After Effects error: Unable to call "property" because of parameter 1. The string is too
> long, it can only be 39 bytes after conversion.

The trap is that `effect.name = <long string>` **succeeds**. The control is created and looks
right in the UI; only the *lookup* fails. So the tempting pattern of inlining a legend —
`"Brand Pattern  [0=off 1=B1 odd 2=B1 even ...]"` (59 bytes) — builds cleanly and then every
expression that reads it throws at evaluation time.

Keep control names short and put the legend in `layer.comment`, which has no such limit and
shows in the Timeline's Comment column.

Guard it at build time, because the failure is otherwise invisible:

```javascript
var NAME_LIMIT = 39;
if (String(name).length > NAME_LIMIT) {
    throw new Error("Control name is " + String(name).length + " bytes, AE allows " +
                    NAME_LIMIT + ": '" + name + "'");
}
```

### Why safe-degrade hides this, and what to do about it

The recommended `try { … } catch (e) {}` wrapper turns a failed lookup into a silent fallback
to the property's static value. `expressionError` stays **empty**, so an error sweep reports a
clean project while nothing works. A brand-routing rig looked perfectly healthy — 190
expressions, zero errors — while every one of its lookups was throwing into the catch.

Two habits make it cheap to catch:

1. **Simulate the generated expressions in JavaScriptCore before they reach AE.** Build a fake
   `comp()`/`thisComp` whose `effect(name)` **throws on an unknown name**, run each generated
   expression, and assert on the returned value. This catches a bad lookup in milliseconds and
   also verifies the logic — including names built by concatenation
   (`"P" + pad(i) + " Brand"`), which no static grep over the source can see.
2. When something silently returns its fallback, re-attach the same logic **without** the
   catch to a scratch property and read `expressionError`. The real message appears
   immediately.

A static scan of the builder source is worth having too, but treat it as the weaker check: it
sees `effect("Literal")` and misses every computed name.


## Render queue hygiene

The queue is a **delivery hazard**, not just a build step. Two habits:

**Clear it before staging.** A stray item turned up in a freshly built project — a review comp
that must never be rendered. Someone hitting Render All would have burned an hour on a
14,090px comp and written a file with a delivery filename. Iterate backwards, because removing
shifts indices:

```javascript
var q;
for (q = rq.numItems; q >= 1; q--) { rq.item(q).remove(); }
```

**Audit after staging**, and put the result in the build log so it is visible without opening
the project:

```javascript
/* every item is a delivery comp, full length, enabled, and uniquely named */
for (qi = 1; qi <= rq.numItems; qi++) {
    var it = rq.item(qi), n = it.comp.name;
    if (!isDelivery(n))                                              strays.push(n);
    if (Math.round(it.timeSpanDuration * it.comp.frameRate) !== FRAMES) shorts.push(n);
    if (!it.render)                                                  offs.push(n);
}
```

Duplicate output filenames deserve their own check — two items writing the same path overwrite
silently and you ship eleven files of which two are identical.

## Headless testing of a builder script

Most of a builder is pure arithmetic — geometry, naming, role tables, timing. Run it in
JavaScriptCore before AE ever opens:

```
/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc test.js
```

Guard the entry point so the harness can `eval` the builder without executing it:

```javascript
if (typeof HARNESS === "undefined") { var RESULT = build(); }
```

**Strip ExtendScript directives first.** `#target illustrator` / `#include` are not valid
JavaScript — JSC reports *"Bare private name can only be used as the left-hand side of an `in`
expression"*, which does not sound like the actual problem:

```javascript
var SRC = readFile("builder.jsx").replace(/^\s*#.*$/gm, "");
eval(SRC);
```

Stub the few AE globals the file touches at load time (`ParagraphJustification`, `RGBColor`,
`File`, enum objects) and everything else is testable.

### Simulate the generated expressions too

This is the highest-value test in the set, because expression failures are otherwise silent
(see the 39-byte section). Build a fake `comp()` / `thisComp` whose `effect(name)` **throws on
an unknown name**, execute each generated expression, and assert on the returned value:

```javascript
function effectOf(store, where) {
    return function (n) {
        if (!(n in store)) { missed.push(where + " -> " + n); throw new Error("no such effect: " + n); }
        return function () { return store[n]; };
    };
}
var body = expr.replace(/\r/g, "\n") + "\nreturn out;";   /* AE's trailing `out` is not a return */
var fn = new Function("value", "comp", "thisComp", "time", "Math", body);
```

It catches names built by concatenation (`"P" + pad(i) + " Brand"`) that no static grep over
the source can see, and it validates the logic at the same time. In one session it found two
separate control-name bugs that a clean AE error sweep had reported as healthy.

**Derive test expectations from the builder's own constants**, never hardcode them. Retuning a
beat boundary or setting a real contract number should not leave three tests failing for no
reason.


## Never concatenate an Array into a String

```javascript
var a = [540, 1770];
$.writeln("pos=" + a);              // THROWS in ExtendScript
```

> After Effects error: invalid numeric result (divide by zero?)

In browser JS this yields `"pos=540,1770"`. ExtendScript instead attempts a **numeric**
coercion of the Array, fails, and raises an error whose text mentions division — which is
nowhere near the real cause. The reported line number is often the *logging* line, not the
line that built the array, so it reads like the log statement is at fault.

This is easy to introduce when generating expression source, because building coordinates
into an expression string is such a natural thing to write:

```javascript
"var A = [" + markAnchor(w, 1) + "];"          // BAD - markAnchor returns an array
"var A = [" + a[0] + ", " + a[1] + "];"        // fine
"var A = [" + a.join(", ") + "];"              // fine
```

Cost when missed: a builder that dies mid-run, and — in one case — After Effects itself
crashing shortly after, taking the scripting bridge with it.

**Guard it statically.** Keep a list of functions known to return arrays and assert none of
them ever appears immediately after a string concatenation in the source:

```javascript
re = new RegExp("[\"']\\s*\\+\\s*" + fnName + "\\s*\\(", "g");
```

**Bisect it with a logging probe.** Because the error names the wrong construct, the fastest
route is a throwaway script that logs each sub-expression on its own line — `PW`, `PITCH`,
`mid`, `cx`, then the array, then the concatenation. The last line printed is the answer.
That took three minutes after an hour of reading a misleading error.


## Verifying "nothing in the dead zone" needs variance, not alpha

On a panel array with physical gaps, the natural check is "is anything drawn in the gap
bands?" — but that fires on a harmless full-width background solid and reports a violation
that is not one. The gap is never sampled by the delivery comps, so a **flat** fill there is
free; what matters is whether *varied* content (footage, type, a logo) crosses it.

Measure the **standard deviation** of a channel across the band instead of alpha:

```python
sd = pstdev([px[x, y][0] for x in band for y in rows])
flat = sd <= 3.0          # a solid fill; harmless
```

Measured on a real build: gap bands read stdev **0.00** against the ground colour while a
neighbouring footage panel read **76.4**. The signal is unambiguous, and it stops the check
crying wolf every time you add a background.

The same reasoning applies to "is this panel opaque?" — check it against what the panel is
*supposed* to contain, not against a bare alpha threshold, or a deliberately transparent
overlay comp will look like a hole.

## Many queue items sharing one output path silently overwrite each other

**CONFIRMED — AE 26.5x89.** Queueing N items for the *same* comp and giving each the same
output path template (`.../f_[#####].png`) does not produce N renders. AE raises

> After Effects warning: The name of an output module for this render item is already in use.

for every duplicate, reports every item as `DONE`, and leaves **two files on disk from
sixteen items**. Nothing throws; `status === RQItemStatus.DONE` is true for all of them, so
the usual success check passes while 14/16 outputs are missing.

Two consequences:

- **Render one contiguous span per item, not N single-frame items.** Besides being correct,
  it was ~6× faster in measurement — 16 single-frame items cost 1592 ms/frame against
  252–517 ms/frame for one span, because per-item setup dominates.
- If you genuinely need several items on one comp, every output module needs a *distinct*
  path. Verify by reading `om.file.fsName` back and asserting your own token appears in it:

```javascript
om.file = new File(dest + "/" + basename + ".mov");
if (String(om.file.fsName).indexOf(basename) < 0) {
    throw new Error("name template won — output path is not what we asked for");
}
```

This is the same failure that makes a 60-file batch overwrite one deliverable: the stock
templates ship `File Template = [compName].[fileExtension]`, and every generated project
keeps the same render-comp name. Rename the render comp per output *and* assign `om.file`.

## Fonts: `missingFonts` reports zero while the font is silently substituted

**CONFIRMED — AE 26.5x89.** A project referenced `Knockout-HTF94-UltmtSumo`, which does not
exist; AE resolved it to `/System/Library/Fonts/Helvetica.ttc` and reported
`app.fonts.missingFonts.length === 0`. A wrong PostScript name is not a *missing* font to
AE — it is a resolved one. There is no warning anywhere in the UI or the API.

The only reliable check reads the resolved file per text layer:

```javascript
var sd = layer.property("Source Text").value;
var loc = String(sd.fontObject.location);      // the actual file on disk
if (loc.indexOf("/System/Library/Fonts") === 0) { /* substituted */ }
```

Two related traps:

- **`app.fonts.allFonts[i].postScriptName` returns `undefined`** on 26.5 — every property on
  those array elements does. Enumerating the system font list that way yields 419 objects of
  nothing. Enumerate via `fontObject` on real text layers instead.
- **`app.fonts.missingFonts` can itself throw**, not merely return empty. Guard the access.

Adobe-Fonts-activated faces live under
`~/Library/Application Support/Adobe/.User Owned Fonts/` and are per-user: a batch on
another workstation substitutes silently unless the same faces are activated there. Assert
the expected path, not merely that the family name matches.

## Animator tracking is pixels per gap — the unit question, answered

The closed-form fit above deliberately derives `trackPerUnit` empirically. For the record,
measured on AE 26.5x89 from two live samples of the same string at the same size
(`"DAVID"` @151px, tracking 67 → ink 867.35; tracking 154 → ink 1215.30):

    slope = (1215.30 - 867.35) / (154 - 67) = 3.9994 px per tracking unit
    "DAVID" has 5 characters → 4 interior gaps → 0.9999 px per gap per unit

So a **Text Animator** `ADBE Text Tracking Amount` is **1.000 px per gap**, independent of
font size — *not* 1/1000 em like the Character-panel field. `ink_width = W0 + T * (len - 1)`
predicted the second sample to 0.09 px. Still derive it empirically when precision matters,
but expect 1.0 and treat a wildly different slope as a sign you measured the wrong property.

Beware negative tracking on heavy display faces: Knockout 94 Ultimate Sumo has *negative*
sidebearings on A/V/W/Y, so `VA`, `AV` and `AA` already overlap at tracking 0. Compute the
per-pair headroom from the font's own metrics before assuming negative tracking is available.

## A modal makes `DoScriptFile` return `1` and run nothing

The reference already notes that an AE error dialog blocks the next `do javascript`. The
concrete symptom is worth knowing: `osascript … DoScriptFile` returns the string **`1`**
immediately, writes no log, and leaves no trace — indistinguishable from a script that ran
and did nothing. Meanwhile AE sits at ~0.4% CPU, so a "is it still rendering?" check says no.

Distinguish them from outside AE:

```bash
ps -o pcpu= -p "$(pgrep -f 'MacOS/After Effects' | head -1)"   # ~0.4% = idle, not rendering
screencapture -x -o /tmp/ae.png                                # then look at it
```

`System Events` window enumeration returns empty unless the calling terminal has
Accessibility permission, so it is not a reliable probe. A screenshot is.

**The fix needs no UI clicking: `with override`.** The dialog itself names it, and it works
even while the modal is still on screen — verified on 26.5x89. It applies to `DoScriptFile`
as well as `DoScript`, which the docs do not make obvious:

```bash
osascript -e 'with timeout of 900 seconds
tell application id "com.adobe.AfterEffects.application" to DoScriptFile POSIX file "/abs/x.jsx" with override
end timeout'
```

So never click through a stuck AE modal from a script — re-issue with `with override` and
have that script clean up whatever the killed one left behind. Which is the real hazard: a
script killed mid-run does not execute its `finally`, so **proxies stay attached, render-queue
items stay queued with `render = true`, and `bitsPerChannel` stays where you set it**. After
any AppleEvent timeout or abort, re-assert every piece of global state you touched rather
than assuming the cleanup ran. Identify your own queue leftovers by their output path:

```javascript
if (String(om.file.fsName).indexOf("/private/tmp/") === 0) { item.remove(); }
```

## Several `TextDocument` fields are read-only and throw on assignment

**CONFIRMED — AE 26.5x89.** The advice to set every `TextDocument` field explicitly (because
`addText()` inherits the last-used character style) collides with this: `allCaps` and
`smallCaps` raise

> After Effects error: Unable to set "allCaps". It is a readOnly attribute.

and the throw happens **before** your `setValue()`, so the layer keeps the placeholder string
from `addText("x")` and the failure looks like "the text never applied". Worse, a partially
built layer survives the failed run, so a re-run finds it by name, skips creation, and leaves
the placeholder in place — the second run reports success while the layer still says `x`.

Assign each field independently and report what was refused, rather than one straight-line
block:

```javascript
var FIELDS = [["text", str], ["font", face], ["fontSize", size],
              ["allCaps", false], ["smallCaps", false] /* ... */];
var skipped = [];
for (var q = 0; q < FIELDS.length; q++) {
    try { sd[FIELDS[q][0]] = FIELDS[q][1]; }
    catch (e) { skipped.push(FIELDS[q][0]); }
}
doc.setValue(sd);            // always reached
```

Corollary for any builder that creates layers: make it idempotent on *content*, not just on
existence. Check the value is what you intended, not merely that the layer is there.

## A Source Text expression keeps the layer's own styling

Driving `Source Text` with an expression that returns a plain **string** preserves the
layer's font, size and `allCaps` — verified across five layers in three different faces,
all rendering correctly from one shared source with zero expression errors. So one control
comp can feed differently-styled consumers:

```javascript
layer.property("Source Text").expression =
    'comp("_CONTROL").layer("LAST").text.sourceText';
```

Because `allCaps` is preserved and read-only, the case you type in the control comp does not
matter to the render. Storing proper case (`"Pastrnak"`) keeps the control panel readable.

## Ink height varies with which glyphs are present

`sourceRectAtTime` returns the **ink** box, so round letters' overshoot changes the height
even at identical cap height and size. Measured, Knockout 94 Ultimate Sumo @151px, all caps:

| string | ink height |
|---|---|
| `DAVID` (no round glyphs) | 101.28 |
| `SIDNEY` (`S` overshoots) | 108.88 |

That is 7.5% for a purely typographic reason. A fit solver that targets a measured ink
height therefore inherits a ~7% wobble between names. Target the font's cap height from
metrics if you need names to match exactly, or accept the overshoot and state the tolerance.

Related: a per-font PIL-vs-AE width correction derived from **one** string does not transfer
exactly to others — 0.0% error on the calibration string, 4.7% on a different one. Use an
offline estimate for planning and AE's own `sourceRectAtTime` for production values.

## Separate Dimensions: three traps in one layer

**CONFIRMED — AE 26.5x89.** When a layer has Separate Dimensions on (common in projects you
inherit), the Transform group exposes `Position`, `X Position`, `Y Position` and `Z Position`
together, and all three of the obvious moves fail.

**1. Writing to the combined `Position` is refused.** You get

> Can not "set expression" with this property, because the property or a parent property is hidden.

**2. `isHidden` cannot tell you that.** It returns `undefined` for *every* transform property
on 26.5, so branching on it silently picks the unwritable one. **`canSetExpression` is the
reliable test:**

```javascript
var tr = layer.property("ADBE Transform Group");
var pos = tr.property("ADBE Position");
if (pos && pos.canSetExpression) {
    pos.expression = COMBINED_EXPR;               // returns [x, y] or [x, y, z]
} else {
    tr.property("ADBE Position_0").expression = SCALAR_EXPR;   // returns a number
}
```

Note the expression's *return type* changes with the branch — a combined Position wants an
array, `ADBE Position_0` wants a scalar. Reusing one expression for both yields a type error.

**3. The combined `Position.value` is stale and never reflects the separated values.**
Measured with an expression driving X Position:

| TOP X NUDGE | `Position.value` | `ADBE Position_0.value` |
|---|---|---|
| 0 | `-517.39, -274.47, 0` | `-517.39` |
| 250 | `-517.39, -274.47, 0` | `-267.39` |

So a verification step that reads `Position.value` reports "the override did nothing" while it
is working perfectly. Read `ADBE Position_0` / `ADBE Position_1` instead. This one cost a full
round of false-negative debugging.

Also worth knowing: on a 2D layer, scripting reports **3** components for `Position.value`
(`x, y, 0`) while the expression-side `value` has only **2** — so `value[2]` inside an
expression throws "Undefined value used in expression (could be an out of range array
subscript?)". Branch on `value.length` rather than on `threeDLayer`.

## Guard expression divisions explicitly, not with try/catch

A fit expression that divides by a measured dimension raises

> invalid numeric result (divide by zero?)

the moment the text is empty — which happens for real during a batch, whenever a name field is
blank. The safe-degrade `try { } catch { }` wrapper is the wrong fix here because it hides real
errors. Test the measurement and state the fallback:

```javascript
var mw = sourceRectAtTime(time, false).width;
var ih = m.sourceRectAtTime(time, false).height;
if (mw < 1 || ih < 1) { [100, 100]; }      // nothing to measure -> neutral
else { /* the real solve */ }
```

Verified: with the first-name field emptied, the project reports **0 expression errors** and the
layer simply renders nothing, instead of throwing across every dependent property.

**And beware applying a "link" multiplier twice.** If a width-match expression already reads
`other.scale[0]`, then a global scale control that scales `other` reaches this layer *through*
that read. Multiplying by the same control again squares it — measured as a last name 896px
wide against a first name at 672px (= 896 × 0.75 again) when both should have matched.

---

## A property reference in a boolean context is an OBJECT, and always truthy

This one is nasty because it is silent, and because the idiom that breaks is the same idiom
that works everywhere else.

In an expression, `effect("NAME")("Param")` evaluates to a **property object**, not to a number.
It coerces to a number in *arithmetic* and *relational* contexts — which is why the ordinary
idiom reads fine:

```javascript
var lnk = C.effect("SCALE LINK")("Slider") + C.effect("S1 SCALE LINK")("Slider");   // fine
if (t == 1) { ... }                                                                 // fine, == coerces
```

But a ternary condition, `if (x)`, `!x`, `&&` and `||` all apply **ToBoolean**, and ToBoolean of
an object is `true` — no `valueOf` call. So a checkbox control used directly as a condition is
**always taken as checked**:

```javascript
var inv = comp("_CONTROL").layer("CTRL").effect("INVERT")("Checkbox");
inv ? A : B;        // ALWAYS A, even with the box unchecked
```

Measured on AE 26.5: with the checkbox at 0, a pair of swatches driven this way came out
**exactly swapped** — the background took the "inverted" colour and the text took the
background's. No expression error, no warning; both branches are valid colours, so the only
symptom is wrong output.

Fix by forcing coercion, or by reading `.value`:

```javascript
var inv = comp("_CONTROL").layer("CTRL").effect("INVERT")("Checkbox") > 0.5;   // real boolean
```

Comparing to a number invokes ToPrimitive → `valueOf`, the same mechanism the arithmetic idiom
relies on, so it is safe on any build where the ordinary idiom works.

**How it was caught, and the general lesson:** not by an error sweep (0 errors) and not by
reading the code, but by a verify step that compared each swatch's *evaluated colour* before and
after the edit against values read from the file. Any check of the form "does this still evaluate
to what it evaluated to before" would have caught it; no amount of "0 expression errors" could.
See also the safe-degrade wrapper note — these expressions are deliberately written to fail
quietly, so `expressionError === ""` proves nothing about correctness.

---

## Essential Graphics from script — what actually works on 26.5

**The EGP reaches into nested comps.** A property on a layer inside a *nested* comp can
be added to an ancestor comp's panel:

```javascript
var prop = comp("_CONTROL").layer("CTRL").property("ADBE Effect Parade")
             .property("FIT TARGET H").property(1);
prop.canAddToMotionGraphicsTemplate(renderComp);      // true, even though prop is nested
prop.addToMotionGraphicsTemplateAs(renderComp, "10 - Fit: first-name height px");
```

Verified: 20 properties living on one control layer in a `_CONTROL` comp, all added to
the render comp's panel, all confirmed. This is what makes the "one hidden control comp +
a panel on the comp the operator actually opens" pattern viable — the controls stay in
one place for scripting, and the panel is on the comp a `.mogrt` would export from.

**`canAddToMotionGraphicsTemplate` doubles as the only read-back.** There is no API to
enumerate what is in a panel. But the call returns **false once the property is already
there**, so it serves both as the pre-flight check and as the post-add verification — and
as the idempotency guard on a re-run. Treat `false` before adding as "already present",
and `false` after adding as "confirmed in".

Two more constraints worth knowing up front:

- **Order of addition is panel order, and there is no grouping API** (AE's EGP does have
  groups and comments, via Add Formatting, but only by hand — see "Essential Graphics,
  continued" below). Impose structure through the display names —
  `addToMotionGraphicsTemplateAs` with a numeric prefix (`"04 - Team"`, `"20 - Photo:
  scene 1 position"`) is the only lever you have.
- `addToMotionGraphicsTemplateAs` returns a boolean. Check it; it can return false
  without throwing.
- Set `comp.motionGraphicsTemplateName` explicitly — it defaults to `"Untitled"`.

**`getMotionGraphicsTemplateControllerName()` can kill the script engine outright.**
There *is* an enumeration API — `motionGraphicsTemplateControllerCount` plus
`getMotionGraphicsTemplateControllerName(i)` — and the name getter is not safe to call.
It does not throw: execution simply **stops dead**, `try/catch` does not catch, `finally`
does not run, and no output file is written. From the outside it is indistinguishable from
a hang, except that AE itself stays responsive and accepts the next `DoScriptFile`
immediately.

Measured on 26.5x89: the same loop read all 20 controllers fine, then killed the engine at
**index 0** once the panel held 33. Index 0 also returns `undefined` rather than the first
controller's name even when the call survives, so the indexing is not what it appears.

This is expensive because it kills scripts *after* their mutations have already landed: a
build script that adds controls and then enumerates to verify leaves the additions in
memory and dies before its `app.project.save()` — which looks exactly like a no-op but is
a half-succeeded run. Diagnose a silent death like this by flushing a log file after
**every** call (open/append/close per iteration); the trail then ends on the offending
index:

```javascript
function logLine(s) {                      // flush per call; survives a hard engine kill
    var f = new File(LOGP); f.open("a"); f.writeln(String(s)); f.close();
}
logLine("about to read [" + i + "]");      // this line lands
var n = rc.getMotionGraphicsTemplateControllerName(i);
logLine("  [" + i + "] = " + n);           // this line never does
```

So **never enumerate controller names in a script that also mutates.** Verify panel
membership with `canAddToMotionGraphicsTemplate` (false == present, per above) and read
the `Count` property only. To confirm the display *labels* landed, verify from outside
AE — save the project and grep the `.aep` for each label string, using a known label as a
positive control and a fabricated one as a negative control to prove the grep
discriminates.

Corollary for the ordering note above: because the panel cannot be safely enumerated, the
claim "order of addition is panel order" is only checkable via the `.aep` bytes. On 26.5
the controller list reads back **descending** by the numeric prefix with ascending index
(index 1 = `"42 - ..."`, index 19 = `"02 - Last name"`), i.e. the panel is ordered by add
order and *not* by display name — so a numeric prefix documents grouping for a human but
does not sort anything. Appending last is what puts a control at the bottom.

## `setPropertyParameters()` destroys and recreates the dropdown effect

Changing a Dropdown Menu Control's items is not an edit, it is a **replacement**. Verified on
26.5x89: after `setPropertyParameters([...])` the effect comes back

- **renamed** to `"Dropdown Menu Control"` (the author's name is gone), and
- with a **new `matchName`** (`Pseudo/@@0uVw5Rpv…` became `Pseudo/@@yysVwCj5…`, and a
  different one again on each run).

Three consequences, in increasing nastiness:

1. **The property reference you called it on is dead.** The very next `teamProp.value`
   throws `ReferenceError: Object is invalid`. Re-fetch from the effect parade.
2. **Every expression that addressed the effect BY NAME has lost its target** — and AE does
   not merely error those, it **permanently DISABLES** them. Renaming the effect back does
   *not* re-enable them. On a test project 4 expressions stayed dead, and they were the four
   opacity switches that drove the team-logo swap: the project looked fine and silently
   stopped switching logos.
3. Disabling happens **on evaluation, not on the destroy**. So the order matters enormously:

```javascript
app.beginUndoGroup("change dropdown items");
try {
    ctrl.effect("TEAM")("Menu").setPropertyParameters(ITEMS);
    parade.property(1).name = "TEAM";      // rename IMMEDIATELY, same undo group
    // …only now touch anything that evaluates expressions
} finally { app.endUndoGroup(); }
```

Renaming before anything forces an evaluation cost **0** disabled expressions on a project
where doing a health sweep in between cost 4. Belt and braces: snapshot the text of every
expression that mentions the effect first, then after the rename re-set any whose
`expressionEnabled` is false or whose `expressionError` is non-empty. Property objects on
*other* layers survive the destroy, so the snapshot can hold direct property references and
needs no path re-resolution.

Good news worth knowing: the **EGP controller survives**. `canAddToMotionGraphicsTemplate`
stays `false` and the controller count is unchanged, so the Essential Graphics panel keeps
working and does not gain a dead entry — which matters, because there is no
`removeFromMotionGraphicsTemplate` to clean one up with.

## `applyTemplate()` resets the render item's time span

Set `timeSpanStart` / `timeSpanDuration` **after** `rqi.applyTemplate(...)`, never before.
A render-settings template carries its own time-span fields, so applying it silently
discards the span you just set and you render the whole comp. The symptom is a render that
takes 4x longer than budgeted and an output whose duration is the comp length — easy to
misread as "the comp is longer than I thought" rather than "my span was overwritten".

## A regex literal that starts with `=` kills the script at load

`if (/==\s*5\b/.test(ex))` is a load-time death. ExtendScript's parser reads the leading
`/=` as the **divide-assign operator** and reports:

    Unable to execute script at line 24. /= does not have a value

The cost is not the error, it is the **modal**: that dialog then blocks every subsequent
`DoScriptFile`, which returns `1` and runs nothing (see the modal entry above). So one bad
regex literal looks like AE has hung, and stays that way until someone clicks OK — on a
machine you may only be reaching over AppleScript.

Build any regex whose first character is `=` with the constructor instead:

```javascript
var RE_TEAM5 = new RegExp("==\\s*5\\b");   // safe
if (RE_TEAM5.test(ex)) { … }
```

Only the *first* character matters — `/t\s*==\s*5/` is fine, `/==5/` is not.

`scripts/qc_gate.py` now catches this. Note *why* it could not catch it as an ordinary
pattern check: the sweep runs on source whose string and regex **bodies have been blanked**
(so the ES5 vocabulary sweep does not match its own error messages), and blanking the body
removes the very `=` that makes the construct fatal. The detection therefore lives inside
`strip_noncode`, at the one point that already knows a regex literal is legally starting —
which is also the only place the `/` can be told apart from division.

## A Source Text expression does NOT carry character styling

Worth stating because the opposite is very plausible and costs an hour to chase. Whether
a Source Text expression returns

```javascript
comp("_CONTROL").layer("CITY").text.sourceText      // another layer's sourceText object
String(a) + " " + String(b)                          // a plain concatenated string
```

the destination layer keeps **its own** font, size, tracking and leading. Verified by
bisection: six expressions rewritten from one source layer to another were bit-exact
across 600 frames despite the source and destination differing in font, size *and*
tracking (`ES Nein Extrabold 62pt` vs `Knockout 94UltmtSumo 77pt tracking 628`).

So a control comp's text layers can be created with plain `addText()` and left in
whatever style `addText` inherited from prefs — it never reaches the render. Do not
build `copyToComp` machinery to preserve styling that was never being passed.

Related: reading `.property("Source Text").value` on a property that *has* an expression
returns the evaluated result, so a field-by-field TextDocument comparison between a
source and an expression-driven consumer cannot tell you whether style is inherited.
Bisect and render instead.

## File output loses newlines unless you set lineFeed

`f.open("w"); f.write(lines.join("\n"))` writes a file with no line breaks — every line
runs together, which looks like the script concatenated its own output. Set the line
feed and write per line:

```javascript
function OUT(path, lines) {
    var f = new File(path);
    f.encoding = "UTF-8";
    f.lineFeed = "Unix";
    f.open("w");
    for (var i = 0; i < lines.length; i++) { f.writeln(String(lines[i])); }
    f.close();
}
```

Relatedly, **expressions authored in the AE UI use `\r` line endings**, so
`prop.expression.split("\n")` returns a single element containing embedded carriage
returns. Split on `/[\r\n]+/` when you need the lines.

## One balanced undo pair, with the save outside it

`qc_gate.py` enforces `beginUndoGroup`/`endUndoGroup` balance, and the obvious structure
— end it inline on success *and* in a `finally` — reads as 1:2 and fails. The shape that
satisfies both the gate and the "never leave a group open across a save" rule is a nested
try whose `finally` owns the only `endUndoGroup`, with verification and saving after it:

```javascript
var threw = null;
app.beginUndoGroup("...");
try {
    ...mutations...
} catch (e) { threw = e.toString() + " (line " + e.line + ")"; }
finally { app.endUndoGroup(); }          // the only end; closed before any save

...verify...                             // outside the group
if (threw || errs > 0) { /* report, do not save — Cmd-Z is intact */ }
else { app.project.save(); }
```

Refusing to save on a failed verify is what makes `Cmd-Z` a real rollback rather than a
hope. Pair it with a guard on anything the script must not persist — e.g.
`if (app.project.bitsPerChannel !== 16) { /* refuse */ }`.

## A layer used as a track matte reports `enabled === false`

Confidence: **high** — observed on AE 26.5x89, and it is how AE has always marked a consumed matte.

When layer N uses layer N-1 as its track matte (`trackMatteType` is e.g. `5015` for LUMA), the
MATTE layer's own `enabled` flag is set to **false**. It still renders — as the matte — but it
reads exactly like a layer someone switched off.

Two ways this bites:

- **An audit or orphan sweep will "helpfully" flag or delete it.** Anything that treats
  `enabled === false` as "unused" must first check whether some layer directly below it names it
  as a matte. Deleting it silently removes the matte and the matted layer renders unclipped.
- **A visibility toggle will not do what you expect.** Setting `enabled = true` on it makes it
  draw as a normal layer *in addition* to matting, which looks like a mysterious extra copy.

```javascript
// is this layer being consumed as a track matte by the layer above it?
function isTrackMatte(lay) {
    if (lay.index < 2) { return false; }
    var above = lay.containingComp.layer(lay.index - 1);
    return above.trackMatteType !== TrackMatteType.NO_TRACK_MATTE;
}
```

**Related trap: a track matte does NOT scale with the layer it mattes.** If you scale a text layer
by expression, its matte stays put and silently crops the new extent. Coupling the matte's scale to
the layer's is the fix, but compensate position too — scaling about the matte's own anchor
distributes the new coverage around that anchor, which is rarely where you need it. Derive the edge
you want pinned:

```javascript
// keep the matte's TOP fixed while it scales, so all new coverage goes downward.
// `off` uses the matte's DESIGNED scale, so at k = 1 this returns `value` exactly.
var k = thisComp.layer("Last Name").scale[1] / 100;
var r = thisLayer.sourceRectAtTime(time, false);
var off = (r.top - anchorPoint[1]) * 104 / 100;
[value[0], (value[1] + off) - off * k, value[2]];
```

## An expression driven by another layer's scale must be checked over TIME, not just at rest

Confidence: **high** — the failure mode is silent and a resting-frame check cannot see it.

Coupling property A to layer B's `scale` (or position, or rect) is fine when B is static, and
changes the ANIMATION when B is not. A no-op check at one frame passes either way.

`numKeys` is not the test. A property can carry keyframes whose effect an expression fully
overrides — a fit-solver returning a computed scale makes its 2 underlying keyframes inert, so the
evaluated value is constant despite `numKeys === 2`. Conversely a property with zero keys can vary
if its expression is time-dependent. **Sample the evaluated value across the comp's duration:**

```javascript
var lo = null, hi = null, i, v;
for (i = 0; i <= 10; i++) {
    v = prop.valueAtTime(comp.duration * i / 10, false);
    v = (v instanceof Array) ? v[1] : v;
    if (lo === null || v < lo) { lo = v; }
    if (hi === null || v > hi) { hi = v; }
}
// (hi - lo) < 0.01  =>  constant over the shot, safe to couple to
```

## `canAddToMotionGraphicsTemplate()` takes the COMP, not the project

Confidence: **high** — measured on 26.5x89, and it cost a whole phase.

```javascript
prop.canAddToMotionGraphicsTemplate(app.project);   // THROWS
// After Effects error: Unable to call "canAddToMotionGraphicsTemplate" because of parameter 1.
// [object Project] is not of the correct type.

prop.canAddToMotionGraphicsTemplate(renderComp);    // correct — the comp hosting the panel
```

Why it matters more than a normal signature slip: this call is the **only** safe read-back of
Essential Graphics membership (see the EGP section above), so it tends to be written inside a
`try/catch` that treats failure as "unknown". A swallowed throw then reports every property as
present, and a control genuinely missing from the panel looks fine. On this project exactly one
control of 45 had never been added, and an audit that passed `app.project` reported all 45 exposed.

**Audit the catch, not just the call.** If a probe's "unknown" branch and its "present" branch
produce the same output, the probe cannot fail visibly:

```javascript
var state;
try { state = prop.canAddToMotionGraphicsTemplate(hostComp) ? "ABSENT" : "present"; }
catch (e) { state = "UNREADABLE: " + e.toString(); }   // never collapse this into "present"
```

## `addProperty()` invalidates property references you are already holding

Confidence: **high** — reproduced on 26.5x89.

Adding an effect to a layer's `ADBE Effect Parade` staled every property object the script had
fetched earlier, including ones on *other* layers. The next access died with:

```
ReferenceError: Object is invalid
```

The expensive part is *when* it dies: after the mutations have landed. A script that adds controls,
then verifies, then saves will leave the additions in memory and never reach `app.project.save()` —
indistinguishable from a no-op run, but actually a half-succeeded one.

So treat any structural change (`addProperty`, `replaceSource`, layer add/delete) as a barrier, and
**re-fetch by name on the far side of it**:

```javascript
app.beginUndoGroup("...");
try { parade.addProperty("ADBE Slider Control"); /* ... */ }
finally { app.endUndoGroup(); }

// barrier crossed — everything fetched before this point is suspect
ctrl = findLayer(findComp("_CONTROL"), "CTRL");
myProp = ctrl.property("ADBE Effect Parade").property("MY CONTROL").property(1);
```

## A limit control probed upward looks dead

Confidence: **high** — a measurement trap, not an AE bug, but it produced 20 false alarms in one
sweep.

When sweeping controls to prove each one does something, the obvious probe is "nudge it up and see
what moves". For any control that is a **ceiling or a cap**, that is exactly the probe that cannot
work: raising a limit the content is already inside is correctly a no-op. Push it **down**, past
the current value, so it binds.

Two related traps in the same sweep:

- A control can be un-testable in the current state entirely. A "max uplift" ceiling does nothing
  while the uplift factor is 1, so it has to be tested as an **interaction** — engage the feature
  first (raise its trigger threshold), then vary the ceiling underneath it.
- **Build the control→consumer map before the behavioural sweep.** Scan every live expression for
  `effect("NAME")` and record the property paths. Without it, "nothing moved" is ambiguous between
  dead wiring and a witness in the wrong place — and the second is far more likely. Ten of those
  twenty false alarms drove layers the sweep never watched, and two drove a **separated** position
  axis while the sweep watched the composite `Position`, which on a separated layer reports a value
  nothing drives.

## `app.scheduleTask()` may never fire — do not build a run loop on it

Confidence: **high** — measured on AE 26.5x89, macOS arm64.

`app.scheduleTask(str, delayMs, repeat)` returns a task id and then, in at least some conditions,
**never executes the string at all**. Measured with three tasks scheduled together:

| task | fired in 8s |
|---|---|
| `"$.global.__tick();"` (global function) | **no** |
| `"$.global.__log('inline');"` (no function lookup of its own) | **no** |
| repeating task at 300ms | **no** |

Zero calls, no trail, ids returned normally. So this is not a scoping problem with the scheduled
string — the scheduler itself did not run. It appears to depend on AE's idle loop getting time,
which it does not reliably get when AE is driven from outside (AppleScript `DoScriptFile`) or is
otherwise not being interacted with.

**Why this is expensive.** It is the obvious way to keep a ScriptUI panel responsive during a long
batch: one work item per tick, so the panel repaints and a Stop button works. When the scheduler
does not fire, the batch **silently never starts** — no error, no output — while the panel sits
with its buttons disabled and Stop enabled, looking busy forever. It fails exactly like a hang.

**Use a blocking loop instead**, and be honest about it in the UI:

```javascript
function escapePressed() {
    try { return ScriptUI.environment.keyboardState.keyName === "Escape"; }
    catch (e) { return false; }
}

for (var i = 0; i < items.length; i++) {
    if (escapePressed()) { break; }          // the only cancel a blocking loop can offer
    status.text = "…" + (i + 1) + "/" + items.length;
    try { w.update(); } catch (e) {}          // repaint; does NOT dispatch clicks
    doOneItem(items[i]);
}
```

Two consequences worth designing around rather than hiding:

- **A Stop button cannot work.** `w.update()` repaints but does not dispatch input events, so a
  button sits there looking clickable and does nothing. Ship a label that says "Esc stops", not a
  dead button.
- **Tell the operator how long the freeze will be.** Multiply a measured per-item cost by the item
  count and put it in the confirm dialog. The difference between "it froze" and "it is working" is
  entirely whether they were warned.

If you do use `scheduleTask`, verify it fires *in the environment you will ship into* by having the
scheduled string append to a file (open/write/close per call, so the trail survives), then check the
file after an idle period. Do not infer from the returned id that anything will run.

## `FootageItem.replace()` silently refuses a path that does not exist

Confidence: **high** — measured on 26.5x89.

```javascript
item.replace(new File("/nonexistent/GHOST/logo.png"));
// no throw, no error, and item.footageMissing stays FALSE — the item still points at the old file
```

Eight items were "repointed" this way and **zero** of them changed. So `replace()` cannot be used
to simulate missing footage for a test, and more importantly, **a relink routine must verify the
result rather than assume the call worked**:

```javascript
item.replace(candidate);
if (item.footageMissing) { /* the replace did not take — report it */ }
```

To genuinely produce missing footage (for a test, or to understand the state): point the item at a
file that DOES exist, then delete that file and call `item.mainSource.reload()`. AE caches
footage state, so without the reload the project keeps reporting the file as present.

**Collect Files is not scriptable.** `app.project.collectFiles` and `app.project.collect` are both
`undefined`; only `consolidateFootage()`, `removeUnusedFootage()` and `reduceProject()` exist. A
script therefore cannot make a project self-contained — it can only *verify* that it is, and relink
what is not. Verification worth doing, since it is cheap: count items where
`mainSource instanceof FileSource`, check `footageMissing`, and check each file's path sits under
one known root.

**Why this matters on any cloud-synced (CloudStorage) project:** AE stores ABSOLUTE footage paths, and a
CloudStorage path contains the user's own home folder
(`/Users/<name>/Library/CloudStorage/Dropbox-…`). Open the same project as a different user, on a
different machine, or after the client re-mounts, and *every* path is wrong at once. Relinking by
filename against an operator-set search root is the practical fix; where a filename occurs more
than once, prefer the candidate sharing the most trailing path segments with the original.

## Concatenating an Error object throws, so a catch block can escape as a modal

*Confidence: measured on 26.5x89, macOS arm64.*

```javascript
} catch (e) {
    log("failed: " + e);        // THROWS
}
```

> `Unable to execute script at line NNN. Object of type Error found where a Number, Array, or
> Property is needed`

String-concatenating an `Error` invokes a conversion ExtendScript refuses. The consequence is out
of all proportion to the mistake: the throw happens **inside the catch block**, so it escapes the
script entirely, AE puts up its own error modal, and that modal **blocks the next
`DoScriptFile`** — which from a shell harness looks exactly like a hang. The reported line number
is the catch block, so the original failure is never recorded at all. One of these cost two
timed-out runs before the modal was seen on screen.

Guard every access individually, because `e.line` and `e.toString()` can each be absent:

```javascript
} catch (e) {
    var msg = "unprintable error", where = "";
    try { msg = e.toString(); } catch (e9) {}
    try { where = e.line ? ("  @line " + e.line) : ""; } catch (e8) {}
    log("failed: " + msg + where);
}
```

Related: give `$.evalFile()` its own `try` rather than letting a load failure fall through to an
outer catch. The line number inside the loaded file is the entire diagnostic value, and an outer
catch reports only that *something* threw.

## Set mtimes with `touch` when testing anything that compares timestamps

*Confidence: measured; `File.modified` is read-only on 26.5x89.*

A build/staleness model is a comparison of timestamps, so a test that cannot *control* the
timestamps is only asserting that nothing threw. `File.modified` cannot be assigned, but
`system.callSystem("/usr/bin/touch -t YYYYMMDDhhmm '<path>'")` works, and reading the value back
with `new File(p).modified.getTime()` avoids doing timezone arithmetic in the test — which is
itself a rich source of tests that lie.

That makes states like "built from an old master", "hand-edited since it was built" and "stills
predate the project" directly constructible, one fixture per state, instead of hoped for.

## ScriptUI sizing: four rules that decide whether a panel can be resized at all

*Confidence: all four measured on 26.5x89, macOS arm64, by laying a real panel out at four window
sizes and reading `size` and `location` back.*

Panel layout is the one area where reading the code tells you nothing — the container decides, and
several of its decisions contradict the obvious reading. Measure it: build the panel, set
`w.size`, call the resize path, then walk the tree reading `.size`/`.location`. A layout bug that
only appears at sizes nobody tried is otherwise invisible.

**1. A `statictext`'s natural width is its ENTIRE string, and that becomes the panel's floor.**
One long sentence — a warning notice, an absolute path — silently sets the minimum width of the
whole window. Measured: a panel that could not go below 802pt wide, traced to three labels.
`preferredSize` overrides this; **`minimumSize` does not.** The fix is one helper applied to every
long label:

```javascript
function fluid(ctrl) {
    ctrl.alignment = ["fill", "center"];
    ctrl.preferredSize.width = 220;      // can shrink to this, expands to fill
    ctrl.helpTip = String(ctrl.text);    // the full text stays reachable
    return ctrl;
}
```

The same applies to an `edittext` holding a long path, and to a multiline `edittext` whose content
sets the natural *height*.

**2. A `tabbedpanel` ignores vertical `alignment: "fill"`.** It sizes to the selected tab's
content and leaves the remainder of the window empty. Measured: the window grew 440pt, the
tabbedpanel took 146 of it. If a fixed-height tabbedpanel sits above a control aligned `"bottom"`,
every extra pixel falls into the gap *between* them — a hole in the middle of the panel that is
invisible at the one size it was built at.

**3. A nested `panel` will not hand vertical slack to its children.** A control aligned
`["fill","fill"]` inside a `panel` inside a tab stayed at its initial height across a 440pt window
growth, while the same control as a direct child of the tab grew correctly. Prefer a header
`statictext` plus a 1px `panel` as a rule, plus a `group` — which also looks more like native AE,
since AE's own panels group with labels and rules rather than GroupBox borders.

**4. `layout.resize()` does not re-read a `preferredSize` changed after construction;
`layout.layout(true)` does, but recomputes the window's natural size as a side effect.** So a
"fitter" that ends with `layout(true)` undoes the resize that triggered it — measured, a window
asked for 560pt settled at 908pt, growing on every pass. Read the size *before* touching the
layout, and end with `resize()`:

```javascript
w.onResizing = w.onResize = function () {
    var h = w.size.height;               // read FIRST
    tabs.preferredSize.height = h - CHROME;
    w.layout.resize();                   // never layout(true) here
};
```

Derive `CHROME` by measuring (`w.size.height - tabs.size.height` at natural layout) rather than
counting margins by hand — hand-counted chrome is wrong the moment a section is added, and wrong
silently.

The practical consequence of 2–4 together: making a listbox track the panel height means
hand-positioning every control below it. That is a rewrite, not a tweak. Give it a sensible fixed
height, and reserve the growing control for one that is the only child of its container.

## Findings from the Signature Draw test run (AE 26.5x89, 2026-09-23)

**CONFIRMED — Simple Choker is not linear and has a dead zone.** Measured on ~5px antialiased
strokes in an 8bpc project, choke values −0.35…+0.35 change the stroke width by ≤0.04px, and
either side the response curves (−1 → +1.68px, +1 → −1.44px, −3 → +4.10px, +3 → −3.30px). A
formula that assumes "choke c changes width by 2c" was off by up to 1.2px. The good news: the
curve was the same for every signature tested (within ~0.2px), so invert a measured table in the
expression, then close the loop — render one still, measure, correct. One pass landed ten players
within 0.02px of target. Blur-then-choke has the same dead zone; choking at 2x resolution is
erratic. Measure stroke width as 2 x coverage area / iso-0.5 contour length (marching squares);
a boundary-PIXEL count overcounts diagonals and is direction- and scale-dependent.

**CONFIRMED — removing every Time Remap key hides the property.** After
`layer.timeRemapEnabled = true`, removing both automatic keys makes the next `setValueAtTime`
throw "Can not set value at time with this property, because the property or a parent property
is hidden". Write your keys first, then remove any key that is not yours.

**CONFIRMED — a "10 second" comp at 59.94 is 599 frames.** `addComp(..., 10, 60000/1001)` gives
599 frames (9.9933s); 00:00:10:00 is 600 frames. Specify durations as `frames * 1001/60000`.

**CONFIRMED — render progress reaches `app.onError` with a timestamp prefix and continuation
lines.** Messages look like `9/23/26 11:52:21 AM EDT: Starting composition "X".` followed by
separate `Output To: …` and blank messages, so a `^(Starting composition|…)` filter matches
nothing. Don't classify onError text; judge success by `RQItemStatus.DONE` only and keep the
text for the log.

**CONFIRMED — new projects on this machine default to 16 bpc.** Set `app.project.bitsPerChannel`
explicitly when a job specifies a depth.

**CONFIRMED — iPad screen recordings are variable frame rate (1/60s while drawing, 1/20s idle).**
Resample them onto an exact 60000/1001 grid (AVAssetWriter with `mediaTimeScale = 60000`; the
default 600 cannot represent 1001/60000 and yields 16.7/18.3ms alternating frames) and AE reads the
result as exactly 59.94 with the exact frame count, so helper frame n == AE frame n.

**CONFIRMED — `system.callSystem` copes with non-ASCII paths** (a non-ASCII symbol in the scripts path) when
each path is single-quoted for the shell.

**CONFIRMED — AE caches footage by path for the whole session.** Rewriting a file in place and
re-importing it (even into a brand-new project) gave AE's OLD frame count for 17 of 22 files. Give
regenerated media a new path (content/settings fingerprint in the name) and check the imported
frame count against what you wrote.

**CONFIRMED — `Folder.temp` is `$TMPDIR/TemporaryItems/`**, and a shell outside AE gets
"Operation not permitted" listing it. Processes AE launches (`system.callSystem`) can read it.
Don't diagnose a render by `ls`-ing AE's temp from Terminal.

**CONFIRMED — `app.settings` live in memory until AE quits** (the prefs .txt on disk had no trace
of values set minutes earlier). Read them back through AE, not from the prefs file.

**CONFIRMED — `File.name` is URI-encoded** (`Penguins%20Signatures.aep`); use `decodeURI()` or
`displayName` for anything a person reads.

**Test hooks passed as globals outlive the run.** `$.global` persists for the AE session, so a
test flag set by one driver silently changes every later run of the same script (here: a real panel
would have auto-answered its own confirm dialogs). Read such globals once and clear them.

## Essential Graphics, continued: removing controllers, red rows, ranges, groups (26.5, 2026-09-23)

**There is no API to remove a controller — but deleting the property removes it.** A controller
disappears from the panel when the property behind it is deleted. So to empty or rebuild a panel whose
controls all live on one control layer, replace that layer with an exact duplicate:

```javascript
var idx = orig.index;
orig.duplicate();            // lands directly above, same name, effects, values, expressions
orig.remove();               // its controllers vanish from the panel
var dup = comp.layer(idx);   // re-fetch: the stack shifted
// rc.motionGraphicsTemplateControllerCount drops by that layer's share; repeat per source layer
```

Safe only if nothing addresses that layer **by index** (grep every expression for `layer(\s*\d`)
and nothing is parented to it (a duplicate does not inherit children). Measured on a 48-controller
panel: 4 layers held all 48; count went 48 -> 0; expression count and errors unchanged; renders
bit-identical. Re-adding afterwards gives full control of order. **It also wipes any groups, comments
and slider ranges the user built by hand** — do it before they finish the panel, never after.

**Red rows = "unrelated property".** The EGP paints a property red when its comp is not inside the
primary comp's hierarchy (a `_CONTROL` comp reached only by expressions, `usedIn` 0). They still work
inside AE, but a `.mogrt` export drops them, and users read red as "broken". Fix: nest the control comp
into the primary comp as a disabled + guide + shy layer (it never renders); the rows turn normal.

**Not scriptable at all:** EGP groups, comments ("Add Formatting"), and **slider ranges** (neither the
Slider Control's own range nor the EGP's Edit Range). Clamp in the consuming expression
(`Math.max(-50, Math.min(50, v))`) and ask the user to set the range once in the master — builds inherit it.

**A control that feeds a solver can be cancelled by it.** A "name size" factor fed into a fit solver
did nothing for most names, because the solver's own floors/limits re-fit the result. Operator-facing
size controls should scale the FINISHED result (a parent null, after the solver), not an input to it.
If a sibling that must follow is not a child of that null (e.g. a track-matte rig), apply the same
similarity transform about the same pivot: `pos' = pw + k*(pos - pw)`, `scale' = k*scale`, where
`pw = thatNull.toComp(pivot)` — the pivot is invariant, so `toComp` is safe to read at any `k`.

**`openInEssentialGraphics()` exists on 26.5** (`typeof comp.openInEssentialGraphics === "function"`).
Open the comps that need attention with `openInViewer()` first and the primary comp LAST — the project
is saved with those viewers, so it reopens with them as tabs and the primary in front.

## Relinking footage by script: layered PSD/AI, sequences, interpretation

**`FootageItem.replace()` on a layered PSD/AI item swaps in the FLATTENED file.** Several items imported
as layers of one PSD (named `"Layer/file.psd"`) each become the whole merged PSD. There is no API option
to keep the layer. What works: import the new file as layers once and route each old item to its twin by
name, then drop the old item.

```javascript
var io = new ImportOptions(new File(newPath));
io.importAs = ImportAsType.COMP;                 // or COMP_CROPPED_LAYERS — keep whichever matches the
var holder = app.project.importFile(io);         //   old items' width/height
var byName = {}; for (j = 1; j <= holder.numLayers; j++) { byName[holder.layer(j).source.name] = holder.layer(j).source; }
// for each old item: for each comp in old.usedIn, each layer whose source === old -> layer.replaceSource(twin, false)
// then old.remove(); move the twins where the old items lived; remove holder and the unused layer items
```

The layer items land in their own "<file> Layers" folder, **not** next to the returned comp — find the
folder via a layer item's `parentFolder`, not `holder.parentFolder`. Detect a layered item by a `/` in
its name plus a layered extension (psd/psb/ai/eps/pdf).

**Sequences:** `mainSource.isStill === false` with an image extension. Copy every frame sharing the
first frame's prefix, digit count and extension, then `item.replaceWithSequence(firstFrame, false)`.
**Interpretation:** save and reapply `alphaMode, premulColor, invertAlpha, conformFrameRate,
fieldSeparationType, highQualityFieldSeparation, removePulldown, loop` and `pixelAspect` around a
replace. Proven on a 55-file template (18 EXR/PNG sequences, one PSD as 7 layers) by rendering the
relinked build against the un-relinked one.

**A self-contained ("collected") project, done by script.** Copy every file-backed item into
`<projectFolder>/(Footage)/...`, relink, and save the .aep in `<projectFolder>`. AE stores a relative
path too and falls back to it when the absolute path fails — so the folder can be renamed, moved or
shared. Prove it: rename the folder, reopen, and check every `mainSource.file.fsName` resolves inside the
NEW folder. Drop `usedIn.length === 0` footage first so replaced art is not shipped. Never overwrite: same
size = reuse, else a numbered sibling. Fonts cannot be collected.

## A 0%-opacity layer is skipped by the renderer — use it to switch between live and pre-rendered

AE does not render a layer whose opacity evaluates to 0: measured, a heavy precomp at 0% cost the same as
the precomp switched off (260 vs 276 ms/frame, noise). So a pre-rendered copy can sit above the live layer
with an expression that shows it only while it is still valid, and the live layer's opacity expression
drops to 0 while the copy is shown. Encode the validity inputs in the movie's FILE NAME
(`BGPATTERN_<TEAM>_<RRGGBB>.mov`) and parse `thisLayer.source.name` in the expression — self-describing,
so swapping the source at build time needs no expression rewrite, and a wrong or stale movie hides itself.
A colour read in the same script pass as the `setValue` that changes it returns the OLD value — read it in
the next `DoScriptFile`.

## Four traps from the team-package build (AE 26.5, 2026-09-23)

- **`File.name` is URL-encoded** (`"Card%20-%20base.psd"`); `fsName` is not. Compare names with
  `decodeURI(f.name)` or use `fsName` throughout, or a match on a name with spaces silently fails.
- **A PSD's layer GROUPS import as nested comps.** Importing as `COMP` / `COMP_CROPPED_LAYERS` gives a
  holder comp whose layers are footage items AND group comps; the grouped layers are inside those. Walk
  them recursively when matching items by name. The group comps keep the Photoshop group names — one
  here was `"Main Texts"`, the name of an existing template comp — so delete everything the import
  created that ends up unused (track item `id`s from before the import, and loop until stable), or
  `comp("Main Texts")` becomes ambiguous.
- **2D rotation is `"ADBE Rotate Z"`**, not `"ADBE Rotation"`. `property("ADBE Rotation")` returns null
  and the next `.setValue` throws "null is not an object" — halfway through building a layer.
- **Fonts under `/System/Library/Fonts` read as substitution** to a font check that tests
  `fontObject.location` (Arial Bold lives in `.../Fonts/Supplemental`). Script-created text (notes,
  banners) should use a face the project already depends on.

Also: **a failed build leaves the template open with unsaved changes**, which blocks the next batch's
"unsaved changes" precheck. If builds never save the template and a batch cannot start while it has
unsaved work, the dirty state after a failure is always the build's own, so discard it in a wrapper.


## Packaging / collect: file size is not identity (Example PNI, 2026-09-24)

**Confidence: measured.** A re-render of a ProRes 4444 clip with the same frame count and size came out
byte-for-byte the SAME LENGTH as the previous render, with a different checksum (ProRes pads frames to
fixed sizes). A "same size means same file, skip the copy" collect rule therefore silently keeps stale
media. `File.copy()` stamps the copy with the time it was copied, so compare dates as well: a source
modified after the destination copy is a newer version, so refresh it (remove, then copy, because `copy()`
does not overwrite). Only fall back to size (or a hash) when the dates don't settle it.


## The Fill effect's "Opacity" at 0 hides the whole layer (AE 26.5, measured 2026-09-24)

**Confidence: measured.** To make a Fill conditional (for example, grey only while a placeholder is the source),
do NOT drive the Fill's own `Opacity` parameter to 0. That rendered the layer fully transparent, and a real photo
in that layer vanished. Drive the effect's mix instead, which is the same for any effect:
`effect.property("ADBE Effect Built In Params").property("ADBE Effect Mask Opacity")` (Compositing Options ▸
Effect Opacity, 0–100). At 0 the layer renders untouched. Verify with a render; the expression shows no error either way.


## Chained ternaries associate LEFT in ExtendScript (AE 26.5x89, measured 2026-09-25)

**Confidence: measured.** `a ? X : b ? Y : Z` is parsed as `(a ? X : b) ? Y : Z`, not the standard
`a ? X : (b ? Y : Z)`. When `a` is true and `X` is truthy, the result is **`Y`**, silently. Measured on a
comp: `it.typeName === "Composition" ? "COMP" : it.typeName === "Folder" ? "FOLDER" : "FOOT"` returned
`"FOLDER"`; the parenthesised form returned `"COMP"`. It never throws, and when `a` is false the answer is
right, so it passes any test that happens to exercise only the later branches. A probe built on it
classified every comp as a folder and dropped every comp section from its report.

Never chain ternaries. Parenthesise the inner one, or use `if / else if`. It parses fine in JSC and
any normal checker, so only a review or a gate rule catches it.

Seen again in AE 2026 (2026-10-31): `v === L ? "LINEAR" : v === H ? "HOLD" : v === B ? "BEZIER" : String(v)` returned
"BEZIER" for LINEAR and HOLD alike while the raw values read right (KeyframeInterpolationType LINEAR 6612, BEZIER
6613, HOLD 6614) and plain `===` worked. It cost two failed probes, because a "type" gate read mislabelled names.
So readers log the raw number next to any mapped name.


## Output file name templates: `File Template` needs `Base Path` in the same call (AE 26.5x89, measured 2026-09-25)

**Confidence: measured.** To make a queue item's file name follow the comp name, set
`om.setSettings({"Output File Info": {"Base Path": dir, "Subfolder Path": "", "File Template": "[compName].[fileextension]"}})`.
Passing `File Template` (or `File Name`) without `Base Path` throws *"With either File Name or File Template, must also
pass Base Path"*. AE then stores the base as `/Volumes/<boot volume>/Users/...` even when you pass `/Users/...`. It's the
same folder, but it won't string-match items made in the UI (those keep `/Users/...`). Assigning `om.file` instead keeps
`/Users/...`, but it turns the template into a literal name. Brackets in a comp name such as `[Name Project]` expand
literally; they are not re-parsed as tokens.

Comparing two output modules with `getSettings`: `"Resize to"` differs by comp size even when `"Resize"` is `false`.
It's a label, so compare `Resize` rather than the label.

## Appending a line to point text: set `leading` explicitly (measured 2026-09-25)

**Confidence: measured.** A one-line text layer can carry a near-zero `leading` with `autoLeading = false` (seen: 2.52)
that nobody notices until a second line exists. Appending `"\r..."` then stacks the new line on top of the first:
`baselineLocs` shows a y of 0 and 2.5. When adding lines, set `td.autoLeading = false; td.leading = <house value>`, and read
`baselineLocs` back to confirm the lines are spaced. `sourceRectAtTime` reports one line's height in this state, which
is the hint.


## `replaceSource()` renames a layer whose name was never customised (measured 2026-09-25)

**Confidence: measured.** A precomp layer still named after its source, such as `02b - TXT - Top Line`, takes the
NEW source's name after `layer.replaceSource(newComp, false)`. Any expression doing `layer("02b - TXT - Top Line")`
then breaks with "layer named ... is missing". Test copies built by duplicate+replaceSource therefore need the layer
name as a parameter. Renaming a comp renames those layers too, so name-based expressions in a template depend on
producers never renaming the nested comps.

## Auto-fit must sit BELOW any matte that should stay fixed (measured 2026-09-25)

**Confidence: measured.** A shrink-to-fit on a parent null in the outer comp (`02d > RESIZE TYPE`) also shrank the
circle track matte inside the nested comp. Long text got smaller but stayed clipped in exactly the same place,
because the matte shrank with it. Put the fit on a transform that is inside the matte's comp and parents only the
type (here each option comp's `CNTRL ALL`). The failure is invisible in the numbers (the fit factor looks right)
and obvious in a frame, so look at a frame.


## Early frames can differ between two renders of the SAME state (AE 26.5x89, measured 2026-09-25)

**Confidence: measured.** In the Pro Pack title (Magnify + Add Grain + Gaussian/Radial blur active over f0–47), purging
all caches and re-rendering an unchanged project moved up to ~110 px by as much as 8/255 at f0–f30, while f60+ stayed
bit-identical. Two renders WITHOUT a purge in between matched exactly, which is why an earlier "deterministic" check
passed. So a before/after pixel gate over animated-effect frames needs a same-state control pair (render, purge,
render) to set the noise floor. Otherwise a harmless edit gets blamed for the noise, as happened here with a
COLOR CORRECT change. Gate the frames where the effects are static at 0 tolerance, and the intro frames against the
measured floor.


## Removing a temp comp leaves its solids behind (measured 2026-09-25)

**Confidence: measured.** `comp.remove()` does not delete the footage items that `layers.addSolid()` and
`layers.addNull()` created. Those land in the project's Solids folder and stay there, unused. A probe that built
throwaway comps leaked `a`, `a`, `b` and `Null 6` into a delivered template, and they survived a Collect Files.
Before removing a temp comp, collect `layer.source` from every solid/null layer and remove those items after the
comp. Or end the probe with an unused-footage sweep (usedIn.length === 0), matched on the exact names/sizes/colours
you created, never on "unused" alone.


## `TextDocument.allCaps` is read-only; set caps with `fontCapsOption` (AE 26.5x89, measured 2026-09-25)

**Confidence: measured.** `d.allCaps = true; prop.setValue(d)` throws `Unable to set "allCaps". It is a readOnly
attribute.`, and an unguarded script dies on the first text layer it builds. Use
`d.fontCapsOption = FontCapsOption.FONT_ALL_CAPS` instead (AE 24+). `allCaps` still READS correctly afterwards.
In the same probe, text-style expressions all worked on AE 26.5 with no expression errors:
- per-character ranges: `style.setText(s).setFontSize(10, 11, 2).setTracking(10, 11, 2)`, `.setBaselineShift(3, i, n)`,
  `.setFillColor([r,g,b], i, n)`
- paragraph leading: `.setAutoLeading(false).setLeading(23.1)`
- the layer's all-caps survives `setText()`, so lowercase input still renders in caps
- `sourceRectAtTime()` read by ANOTHER layer's expression reflects the per-character sizes
- a cross-comp read of `comp("X").layer("Y").enabled` works, so an eye toggle in one comp can drive expressions in
  another

Measure widths in a second script run (create in pass 1, measure and remove in pass 2), or through an expression
reporter layer. `sourceRectAtTime` read by script in the pass that set the text can be stale.


## `copyToComp()`: three traps (AE 26.5x89, measured 2026-09-25)

**Confidence: measured.**
1. It refuses while an undo group is open if the layer has a parent or a linked expression: "Can't copy a layer with a parent or with a linked expression, while an Undo Group is open". Run the copy phase without an undo group.
2. It drags the layer's track-matte layer along. So `dst.layer(1)` can be the matte copy, not your layer. Diff `layer.id` before and after the copy, pick the new layer by name, and remove the extras.
3. A parented layer arrives with its parent BAKED IN: comp-space position, and scale multiplied by the parent's. `setParentWithJump(newNull)` afterwards doubles the transform. Leave it unparented, or parent it with compensation (`layer.parent = x`).
Also: a scripted `app.executeCommand(16)` (Undo) did nothing here. Build scripts must be re-runnable, with explicit cleanup, rather than relying on undo.


## `copyToComp()` from an imported reference project can alter a same-named layer (AE 26.5x89, observed 2026-09-28)

**Confidence: observed once, mechanism unknown.** Copying a reference project's `darken` adjustment layers (Levels IB .14 / G .6 / OW .55) from a
temp-imported .aep into a comp that already had its own layer named `darken` left the EXISTING `darken` with the reference's Levels
values after the copies were removed — and that top-of-stack adjustment (blend 5227) then warm-tinted all the type through the Lumetri
below. Found by diffing the live comp against the pre-change auto-save (import the .aep, walk every property, compare). Rules: never
copyToComp from a reference into a comp with same-named layers — rebuild the effect values on new layers instead; after any prototype,
re-measure a known-neutral pixel (white type) against a pre-change grab. Auto-saves are the cheapest baseline for a property diff.


## Small measured facts (AE 26.5x89, 2026-09-28)

- `comp.workAreaDuration` refuses a 1-frame value at 59.94 ("out of range 0.02"): the script minimum is 0.02 s, so use 2 frames.
- To SEE a UI built from guide layers, clear `guideLayer` for the grab and restore it afterwards (tag the layers in `comment` so the
  restore pass finds exactly those). `saveFrameToPng` also returns transparency, so composite on the comp bg colour before judging.
- `comp.layers.precompose(indices, name, true)` keeps every attribute, but the new precomp layer lands at the top index of the moved
  set, so guides that sat below that index end up BELOW it. Restack guides (and toggles) explicitly afterwards.
- Renaming a comp by script does NOT rewrite `comp("old name")` in expressions. Rewrite every expression string first (a REPL
  table walked over all properties), rename second, then re-enable: AE auto-DISABLES any expression that errored on the way.
- A layer marker's label shows about 30 characters in a normal timeline zoom. Keep marker text to 2–8 words and put the
  full sentence in `layer.comment` (the timeline's Comments column).

## AE 26.5: script can't READ 2D values on shape-layer properties (2026-09-28, confirmed)
Reading `.value` / `.valueAtTime()` of any 2D shape property (group `ADBE Vector Position`/`Anchor`/`Scale`, gradient
`ADBE Vector Grad Start Pt`/`End Pt`) throws "invalid numeric result (divide by zero?)" — even on a brand-new shape group.
Path (`ADBE Vector Shape`) values, layer transforms and 1D values read fine; `setValue` on 2D shape props works.
If uncaught it raises a modal that blocks the next DoScriptFile. Workaround: read through an expression on a temp text
layer's Source Text (`content("Group 1").transform.position.value`, `gradientFill.startPoint.value`; groups by index are
`group(k)` in expressions, not `.property(k)`), then remove the layer — see `Pro-Pack L3/tools/l3_xread.jsx`.
Also: in a catch, log `String(e.message)`, not `"…" + e` — the concatenation itself threw ("Object of type Error found
where a Number, Array, or Property is needed") and surfaced as a second modal.

## AE 26.5: implicit Array → String in a script throws "invalid numeric result (divide by zero?)" (2026-09-28, confirmed)
`"x " + [1.5, 2]` (or `"" + prop.value` for an array value) threw in this build, both for layer-transform values and plain number arrays;
`arr.join(",")` and per-element `String(Math.round(v))` are fine. Always format arrays explicitly in logs.
Also: a Project-panel FOLDER and a COMP can share a name ("4 - Style + Banner" folder + comp) — an item-by-name lookup must check the type
(`instanceof CompItem`), or it returns the folder and `.layer` is undefined.

## Re-runnable builders: never read `.value` of a property that has an expression (2026-09-28, confirmed — cost a visible bug)
`prop.value` returns the EXPRESSION RESULT. A builder that does `p.setValue([x, p.value[1]])` on a property whose expression is
`value + offset` adds the offset again on every re-run (a day/time crept 14 px per run until it hit the lockup). Use constants for design
values, or `p.valueAtTime(t, true)` (pre-expression — but NOT for Source Text, see the 2026-10-07 correction below). Same for TextDocument: `.value` of an expression-driven Source Text is the result.

## Restoring `comp.motionBlur = true` switches it ON in nested precomps too (AE 26.5x89, measured 2026-09-29)

A cost probe set `04c - REVEAL.motionBlur = false`, rendered, then restored it to `true`. Afterwards the precomps nested inside it
(`04a - LAYOUT`, and `04g - LOCKUP` inside that) had their comp motion-blur switch **on**, although they had been off and were never
touched. A bare render without the toggle changed nothing, so it's the `true` assignment that propagates downwards.
- Any tool that flips a comp's motion-blur switch must snapshot `motionBlur` for **every** comp first and put them all back
  (loop until they match), not just the comp it touched.
- Catch it with a before/after project audit diff — an expression sweep or a render check won't notice (layers inside had MB off,
  so the picture didn't change).
- **Superseded in part (AE 26.2.1, measured 2026-10-30):** the `false` assignment propagates too. Setting a comp's
  `motionBlur` from a script, on or off, sets every comp nested inside it to the same value; a nested comp set afterwards
  keeps its own. So a restore loop that sets a child before its parent gets undone by the parent. Generators: never set
  the switch while building. After every comp exists, one pass sets each switch in reverse build order (parents first,
  each child last), on only where the comp has a blurred layer or its spec asks for blur. Then assert every comp
  matches and gate on the reopened file's readout. The render queue's default Motion Blur setting ("On for Checked
  Layers") still blurs those layers with the comp switch off; "Current Settings", saveFrameToPng and the viewer don't.

## Pre-rendering a subtree as a plate: four traps (AE 26.5x89, measured 2026-09-29)

Replacing a heavy background (a 4500×3840 ring precomp + adjustments) with a pre-rendered plate cut a 16x9 render by a third, but it only
matched the live render (max 1/255) after these were handled:
- **Render the plate at the parent's time, not inside a time-remapped precomp.** A plate taken in the precomp's own time, played back under
  a slowing time remap, stepped between whole frames and carried the wrong (full-speed) motion blur: max 90/255 off mid-motion.
- **A collapsed precomp's adjustment layers reach the parent's layers below it.** Switching those adjustments off, with the precomp's
  visible layers already off, still changed the frame (mean 4.3, max 80). They and whatever they touch below belong in the plate.
- **Superseded (see the 2026-10-27 retest below): ProRes 4444 is not a lossless round trip here.** Rendered from a 16-bpc sRGB project
  and re-imported, it came back 3–7 levels darker in the shadows (brights unchanged), with no colour-profile keys exposed on the output
  module. An 8-bit PNG sequence re-imported bit-exact.
- **Replacing a file on disk under the same path keeps AE's cached metadata.** A re-rendered plate imported as its old 320-frame length.
  Remove the footage item first, or use new file names.
- **Superseded follow-up (2026-09-29), kept as history: "it is AE's *import* of ProRes, not the encode."** macOS (QuickLook/AVFoundation)
  decodes the same AE-written ProRes 422 HQ / 4444 file at the right level (mean 8.80 vs 8.76 rendered); AE's re-import read it at 3.51
  (shadows crushed). The rule drawn then, "plates must not be ProRes", is wrong. The retest below explains the 3.51.
- **Retest (AE Beta 27.1x23, measured 2026-10-27): AE decodes ProRes exactly. The darkening is an sRGB working space.** With no working
  space (16 or 32 bpc) and under OCIO at 32 bpc, ProRes 422 HQ and 4444 read within 0.1 level of an ffmpeg decode in the shadows (≤ 0.8 in
  the highs, AE's 10-bit legal-range scale). Tagged and untagged files read the same. With an **sRGB working space**, AE treats ProRes as
  Rec.709 Gamma 2.4 and converts it: −12.6 levels at level 24, −6.5 at 128. The old crush was AE writing sRGB values into ProRes, then
  reading them back as Rec.709 2.4.
- **Rule: no sRGB working space in a project with ProRes plates, or convert back on output.** No working space, or OCIO pass-through, keeps
  code values unchanged. A Rec.709 Gamma 2.4 working space keeps the plate exact but lifts sRGB graphics (PNGs, logos) by up to 13 levels.
  32 bpc keeps sub-black and super-white; 16 bpc clips them. `P.workingSpace` is settable by script in Adobe mode
  (`P.workingSpace = "sRGB IEC61966-2.1"`) and reads `None` under OCIO. An invalid profile name raises a modal (seen with "None" and
  "HDTV (Rec. 709)"). Not covered: AE 2026 release builds, OCIO with a real config loaded.
- **Per-footage colour interpretation is not scriptable** (mainSource exposes no colour/profile property, and Interpret Footage › Preserve
  RGB is a manual check). The project working space is scriptable (above).
- **JPEG plates need the ICC profile.** A Pillow JPEG made from AE's PNG without `icc_profile=` came back 2.7 levels darker in the shadows;
  with the PNG's embedded profile copied in, JPEG q95 4:4:4 matched the live render to mean ≤ 0.5 level — at 15 % of the PNG size.
- **16-bit PNG from a script (2026-09-29):** `om.setSettings({"Depth": …})` throws "Property is read-only". Use a template that is already
  16-bit — AE ships `_HIDDEN X-Factor 16` (PNG Sequence, Trillions of Colors+, RGB + Alpha, straight). Rendering each PSD-layer footage item
  in a comp of its own size and swapping with `layer.replaceSource(png, false)` was pixel-identical (max 0) and cut a 552 MB PSD to 55 MB.

## String + Date / Error throws in AE 26.5 scripts (2026-09-29, confirmed 4 times)
`"text " + someDate` and, inside a catch, `"THREW " + e` raise **"Object of type Date (or Error) found where a Number,
Array, or Property is needed"** as a modal — even inside `try` when it is the catch block itself. Always wrap:
`String(file.modified)`, `String(e)`. A catch that concatenates `e` hides the real error behind this one.
Also: reading `keyTime()` of a COMBINED Position whose dimensions are separated throws an uncatchable modal; read
`Position_0/_1/_2` instead, and check `dimensionsSeparated` first.

## A 3D layer's "Y" is not always vertical
A parent with Rotate X 90 (child Orientation 270 to face the camera) turns the child's Y into depth: moving it "up"
resizes it on screen. Check the whole parent chain's Rotate/Orientation before wiring a position control to a 3D
layer, or put the offset on a 2D layer inside the precomp instead. Verify with `toComp` through a temporary null.

## Every object answers operator names ("-", "+", "|" …) with a FUNCTION (found 2026-09-30, AE 26.5)

ExtendScript supports operator overloading, so `obj["-"]`, `obj["+"]`, `obj["|"]`, `obj["*"]`, `obj["<"]` … return a
built-in function on ANY plain object, including `{}` used as a lookup map. `map[ch] !== undefined` is therefore TRUE for
a hyphen, and `out += map[ch]` throws "Object of type Function found where a Number, Array, or Property is needed". This
crashed an accent-folding table on hyphenated names (Kiner-Falefa). JavaScriptCore does NOT reproduce it, so a JSC
harness passes. Use `map.hasOwnProperty(key)` for every lookup keyed by arbitrary text. Confidence: verified in AE.

## A panel's first refresh runs on the operator's real prefs (found 2026-09-30)

`$.evalFile(panel)` builds the UI and runs its first refresh IMMEDIATELY, with the saved prefs. Overriding the panel's
config through a test hook afterwards is too late: that first refresh already read — and, for a panel that migrates
files, WROTE — the operator's real folders. Give the panel a pre-load override (`$.global.<X>_TEST_CFG`, applied where
the config object is built) and set it before evalFile; clear it after. Fingerprint the folder the PREF names, not a
remembered path (the operator may have moved it).

## `property.value` is AFTER the expression — read the raw value with `valueAtTime(t, true)` (AE 26.5x89, measured 2026-09-30)

**Confidence: measured.** On a property with an enabled expression, `prop.value` returns the evaluated result. A script
that reads it, transforms it and writes it back with `setValue()` bakes the expression's contribution into the static
value, and the expression adds it again. Seen on a photo layer whose Position expression adds an Essential Graphics
offset: a -59 px nudge became -118 after one re-size. Use `prop.valueAtTime(time, true)` (`preExpression = true`) for the
value `setValue()` actually owns. Harness stubs that return one `value` hide this; the gate caught it only because it
checked the exact rendered position of a file that had a nudge.

## `"text" + prop.value` can throw "invalid numeric result (divide by zero?)" (2026-09-30, AE 26.5)
Concatenating the array an AE property returns (e.g. a Point control's `.value`) straight onto a string threw
"Invalid numeric result (divide by zero?)" inside a gate, while the same values printed fine through `String(v)`.
Confidence: observed twice in one session, not isolated further. Always `String(v)` (or `v.join(",")`) property
arrays before concatenating. It surfaces as a modal if uncaught, which blocks the next DoScript.

## aerender: renders while the AE window is open; don't run several at once (2026-09-30, AE 26.5, M5 Max)
`/Applications/Adobe After Effects 2026/aerender -project X.aep -comp NAME -RStemplate "Best Settings" -OMtemplate "T"
-output out.mov` launches its own `aerendercore` and renders while the GUI stays usable. It leaves a `X.aep Logs` folder
beside the project, so render from a temp copy. Missing preset: "aerender ERROR: No output module template was found
with the given name." Each instance uses every core: 3 in parallel gave ~90 frames/min total vs ~200 for one.
Launch from ExtendScript with `system.callSystem("/bin/bash -c '… nohup … > /dev/null 2>&1 & echo PID=$!'")`: it
returns at once (38 ms).
Update 2026-10-01: the same happens with a **Date** (`"saved " + file.modified`) and an **Error** (`"THREW: " + e` inside
a catch, which then escapes as a modal). The message is "Object of type Date/Error found where a Number, Array, or
Property is needed". In gates: `String(e.message)`, `String(file.modified)`, `String(arrayValue)`.

## `"text" + e` inside a catch raises an AE modal (AE 26.5, 2026-10-01) — always `String(e)`
AE's ExtendScript overloads `+` for vector maths. `"ERR " + e` where `e` is an Error object throws a SECOND error *inside the catch
handler* — "Unable to execute script at line N. Object of type Error found where a Number, Array, or Property is needed" — and that one
is uncaught, so it lands as a modal on the user's screen and blocks every later DoScriptFile (aerun then reports "NO LOG"). Three
modals hit in one session from this; each was first misread as "some getter is uncatchable" (the line number points at the catch).
**Rule:** in every handler write `String(e)`, `String(e.message)`, `String(e.line)` — never `"…" + e`. (`"…" + e.message` is safe:
it's a string.) When a modal says "Object of type Error found where…", look at the catch line first.

## `copyToComp` of a parented layer fails inside an undo group (AE 26.5)
"Can't copy a layer with a parent or with a linked expression, while an Undo Group is open." Copy outside the undo group (or unparent first).

## An expression's `value` is the PRE-expression value
Appending `;value + [0, d];` to an existing expression throws its result away. To adjust a result, rewrite the final statement
(`var __R = <last array literal>; add(__R, [0, d]);`) — or, when the expression itself is `value + …`, just change the static value.

## `expressionError` stays stale after the cause is fixed (AE 26.5, measured 2026-10-02)
Renaming a comp that expressions named (or creating it after writing them) makes AE disable those expressions. Setting
`expressionEnabled = true` is not enough: `expressionError` keeps the old message ("comp named … is missing") until the expression is
re-evaluated. **Re-assign the text** (`p.expression = p.expression`) and read `expressionError` again — 20 "errors" dropped to the 5 real ones.
Order that avoids it: rewrite the expression strings first, rename second, then one re-enable + re-assign sweep (L3 `tools/expr_enable.jsx`).
Confidence: high (seen on the L3 text-bar conversion).

## Reading another layer's opacity can render stale when it depends on another comp's eyes (AE 26.5, 2026-10-02)
L3 banner text had `thisComp.layer("BANNER · BOTTOM").transform.opacity`; the tab's own opacity read `comp("…step 4").layer("BANNER - TOP").enabled`.
After switching the banner position, the RENDER (saveFrameToPng and the render queue path) showed the BOTTOM text while scripting
(`valueAtTime(t, false)`) returned 0 and the tab itself rendered correctly. Forcing the text's expression to `0;` removed it; restoring the
chained read brought it back. **Fix: every layer reads the eyes directly (same `pos` logic), never another layer's eye-driven opacity.** Verify
with a switching sequence (BOTTOM → TOP → OVER → none → TOP) rendered at the same frame, not with scripting values. Confidence: high.

## A precomp made with `addComp(…, duration 2, …)` ends its layer at 0:02 — check the LAST frame (2026-10-02)
`P.items.addComp(name, w, h, 1, 2, fps)` for a small helper precomp (a lockup) gave a 2 s comp; added into a 32 s comp, its layer's out-point
was 0:02 and the lockup vanished from every render after two seconds. Every frame check in that session stopped at the landed frame (f60),
so nothing caught it until the producer saw a sample. **Create helper precomps with the parent's duration, set the layer's out-point to the
parent's duration, and gate on it** (L3 `tools/choice_check.jsx` fails any layer/precomp shorter than its comp). Always include the last frame
in render checks. Confidence: high.

## Gradient Ramp on a parented SHAPE layer reads its points in COMP space (AE 26.5, measured 2026-10-02)
A ramp on a shape layer (parented to a null, position/anchor 0) with points from `fromComp(L.toComp([0, -32]))` (= layer space, which
for a shape layer equals its content space) rendered flat (all end colour). The same points as plain comp coordinates
(`thisComp.layer("ROW").toComp([0, -32])`, no `fromComp`) gave the gradient. Use comp coordinates for effect points on shape layers
and verify on a render (sample a column), not by reading the property value. Confidence: high for this setup.

## A text Expression Selector must not read its own layer's sourceRectAtTime (AE 26.5, measured 2026-10-02)
Inside `ADBE Text Expressible Amount`, `sourceRectAtTime(...)` on the SAME layer is circular (the animator changes the rect it would read). AE
does not report it usefully: the selector silently falls back and every character takes the animator at full amount — with an Opacity 0
animator, all the text vanished, on every frame including the landed one, while the build's error sweep reported nothing on that property.
Estimate character positions instead (layer x + `textIndex × ~0.62 em` for caps), or read a width another layer already measures.
Corollary: if layout elsewhere reads `sourceRectAtTime` (chained positions, ink-centred anchors), keep text animators to opacity / colour —
position or scale animators move the measured rect and fight the layout. Verify with a landed-frame pixel diff before/after adding animators.
Match names (probed): `ADBE Text Animator` > `ADBE Text Animator Properties` > `ADBE Text Opacity`; `ADBE Text Selectors` >
`ADBE Text Expressible Selector` > `ADBE Text Expressible Amount` (return `selectorValue * k`). Linear Wipe: `ADBE Linear Wipe-0001` completion,
`-0002` angle (270 = reveals left → right as completion falls 100 → 0), `-0003` feather. Shape-group opacity lives under
`ADBE Vector Transform Group` > `ADBE Vector Group Opacity` (not `ADBE Transform Group`).

## Importing an .aep into a fresh project: the HOST's project settings win (AE 26.5, measured 2026-10-02)
`app.newProject()` starts at 8 bpc (sRGB, gamma 2.4 here). Importing 16-bpc kit projects into it keeps their comps but renders them at the
host's 8 bpc — every gradient / fog frame drifted 3–39 levels. Set `P.bitsPerChannel`, `P.workingSpace`, `P.workingGamma`,
`P.linearBlending` to the source projects' values BEFORE importing (diff every reflectable project property: `P.reflect.properties`).
Even then, frames where a Gaussian Blur is animating differed by ≤ 11 levels on blurred edges in the merged project while each source
re-rendered bit-identically on its own — gate those frames as a named exception, keep everything else at ±1.
Also: importing an .aep brings its render-queue items with it.

## A text layer's sourceText `.value` is the EXPRESSION RESULT — restyling with it bakes the result in (AE 26.5, found 2026-10-02)
`var d = tdoc(L).value; d.font = …; tdoc(L).setValue(d);` on a layer whose Source Text has an expression writes the expression's CURRENT
OUTPUT as the layer's own (pre-expression) text. If the expression is "own typed text if any, else Setup", that silently turns into a stuck
override (the L3 day field froze on SATURDAY 6). **CORRECTION 2026-10-07 (measured, AE 26.5):** `p.valueAtTime(t, true)` does NOT give the pre-expression text for Source Text — it
returns the expression RESULT, same as `.value` (3 fields tested: typed '' read back as 'SATURDAY 6' / 'FLYERS'). The only reliable
read of what was typed is to switch the expression off, read, switch it back on (layer unlocked):
`var lk = L.locked; L.locked = false; p.expressionEnabled = false; var d = p.value; p.expressionEnabled = true; L.locked = lk;`.
Use that in every restyle / "write every field" helper and in any test tool that SAVEs and RESTOREs typed fields — a save/restore
through `.value` or `valueAtTime(t, true)` silently turns "follow Setup" fields into stuck overrides. Not yet re-tested for
non-text properties (Position etc.) — verify before relying on `valueAtTime(t, true)` there either.
Also: a dropdown effect's `setPropertyParameters()` invalidates the effect object and can drop its custom name — add the effect, call
setPropertyParameters via `parade.property(n).property(1)`, then re-fetch by INDEX and name it.

## Render Queue: output File Template does NOT survive a duplicate or a render (AE 26.5, measured 2026-10-07)
- `RQItem.duplicate()` (= Render Queue › Edit › Duplicate) resets the copy's File Template to AE's default
  `[compName]/[compName]_[#####].[fileextension]` (or `[compName].[fileextension]`) and its folder to the LAST folder AE rendered to on this
  machine — possibly another project's folder. `renderQueue.items.add(comp)` does the same.
- After an item renders, its "File Template" reads back as the RESOLVED relative name (`Renders/PP_X_<project>.mov`), so a later Save As does not
  re-name it — and the item is Done anyway.
- Rendering to a path that exists replaces the file silently (no prompt, even without suppressDialogs).
- Test rule: a test that duplicates an RQ item must re-apply its output path/template BEFORE rendering, or it writes into someone else's folder.
- `app.onError` also receives the render log lines ("Starting composition…", "Finished…", "Output To…") — filter them before counting errors.
- Save As fails ("File couldn't be opened for writing") once the project name is ~230+ characters (AE adds a temp suffix).

## Queue in AME ignores the AE output module (measured AE/AME 26.5, 2026-10-07)
`renderQueue.queueInAME(true)` (and the Queue in AME button) keeps the RQ item's folder + file name but encodes with Media Encoder's
own current preset: a ProRes 4444 + alpha .mov item came out H.264 .mp4 (no alpha), and a PNG still item became a 1-frame MP4 named
literally `…_[#####].mp4`. There is no project-side setting that carries the output module across. If a template's deliverables need a
specific codec or alpha, tell the operator to use Render, not Queue in AME. Confidence: high (one run, both item types).

---
**CONFIRMED 2026-10-08 (AE 26.5) — `layerByID` lives on the PROJECT: `app.project.layerByID(id)`, not `CompItem.layerByID`.** Calling it on a
comp throws (a try/catch made a "put back" restore 0 of 959 layers silently). Store `layer.id`, look it up with `app.project.layerByID`, fall
back to scanning `comp.layer(i).id`. `app.project.itemByID(id)` finds comps.

**CONFIRMED 2026-10-08 — screenshot a ScriptUI window from the shell:** `screencapture -x -o -l <CGWindowID> out.png` captures the window even when
it is on another Space (the computer-use window tools could not). Find the id with JXA `CGWindowListCopyWindowInfo` (kCGWindowName === the
window title). A closed palette can still be listed with kCGWindowListOptionAll — check `.visible` in ExtendScript instead.

**Script security setting (read-only check):** `app.preferences.getPrefAsLong("Main Pref Section", "Pref_SCRIPTING_FILE_NETWORK_SECURITY")` = 1 when
Settings › Scripting & Expressions › "Allow Scripts to Write Files and Access Network" is on. Read it to warn the user; never set it.

## ScriptUI windows: dialogs, scrolling, engines, real-input tests (2026-10-14)

*AE 26.5x89, macOS arm64. Found building the ProPack form and Signature Draw v3. Confidence per item.*

### A file dialog started from a palette can lock AE (CONFIRMED, reproduced twice)
`File.openDialog`, `Folder.selectDialog`, `.openDlg/.saveDlg/.selectDlg`, or `app.executeCommand` of Open/Import, started
from a button in a `"palette"` window, can open **off-screen or behind** while the script waits on it. AE then refuses every
open (Finder, File › Open, Recent) and even Quit ("User canceled"). Nothing is visible; only a force-quit frees it.
- In a palette, take footage from the **Project panel selection** ("Use selected") and folders from a **modal `"dialog"`
  window with a paste-path field** (Finder: Option-Command-C copies a path). Both proven with real input + an open test.
- **NOT proven:** a Finder picker started from inside a modal ScriptUI window. Don't assume it is safe.
- Recovery: look for a hidden dialog; if Quit is refused and nothing shows, force-quit (save is impossible anyway).
- Never send a second script (ping, test) while a script waits on a dialog: AE answers "a second script while another
  script was already running".
- Check that AE still opens files after any dialog change: `open -a "Adobe After Effects 2026" file.aep`, then ping until the
  project name comes back.

### ScriptUI has no scrolling; build it from a scrollbar (CONFIRMED with real drags, resizes, wheel)
Pattern: `w` (row) → `view` group (clips its children) + `scrollbar`; content group inside `view`; on scroll set
`content.location = [0, -bar.value]`; on resize set `view.size`, `bar.maxvalue = contentH - H`, hide the bar when it fits.
Reference implementation: `Example Scripts/_tools/example_scroll.jsxinc` (`exampleScroll`). What the tests found:
- Moving a group's `location` to negative y redraws correctly on Mac, and a group clips children outside its bounds.
- **`w.layout.layout(true)` snaps a Window back to its natural size** (a squeezed 320 px window jumped to 782). After any
  relayout, restore `w.size` and re-apply the scroll offset.
- **A container's layout ignores a changed `preferredSize` once sizes are set:** `list.preferredSize.height = 120;
  content.layout.layout(true)` left the list at 260. Grow/shrink a control by setting `.size` and moving the controls below
  it by hand (record their natural y after the first layout).
- **Measure natural content height from the children** (max of `location.y + size.height`, plus the bottom margin), never
  from a container's `.size`: once you set it, it reports what you set.
- **`scrollbar.notify("onChanging")` does nothing; `notify("onChange")` fires.** Use onChange in tests; real drags fire both.
- **The mouse wheel reaches only the scrollbar itself.** Script windows receive no wheel events (listener test on window,
  group and content for `mousewheel`, `wheel`, `scroll`: none; `mousemove` arrived, the positive control). Tell users.
- Size the window to the screen at open: `$.screens[0]` bottom-top minus ~120, so a laptop starts with a bar.
- Setting `w.size` from a script does not reliably run your fit: call it yourself in tests.

### Engines: who keeps a window alive (CONFIRMED)
- A palette created by `osascript … DoScriptFile` in the main engine disappeared when the script ended, even with
  `#targetengine` at the top when run through a runner that wraps the file. Through the Example Scripts panel's engine
  (`run.py` / host.jsx `run`) the same palette stayed open. Test palettes through the panel engine.
- `$.global` is per engine. A probe for a script that declares `#targetengine "propack"` must declare the same engine,
  or it sees nothing.

### Testing with real input (CONFIRMED, macctl / CGEvent)
- Real mouse **drags** reach a palette's scrollbar and the window's resize edge. Real **clicks and typing** reach a modal
  `"dialog"` window (field, buttons). Earlier finding still holds: real clicks on **buttons inside a palette** did nothing,
  and an accessibility "press" flips a checkbox without firing `onClick`. Prove palette buttons with `notify("onClick")`.
- Wheel: `CGEventCreateScrollWheelEvent` (examplepy + Quartz) posted at a point works as a real wheel.
- A modal dialog opened by `notify("onClick")` blocks that script: start the runner in the background, drive the dialog,
  then read the result.
- In a modal dialog, Return submitted the default button while the field had focus from `ed.active = true`; after the
  field was clicked, Return did nothing (seen once). Don't rely on Return alone.
- Screen coordinates: `macctl shot --max N` prints image px per point; divide.
- Never drive the mouse or keyboard while the user is typing on the Mac (screenshot first; if another app is in use, stop).
- A script error in AE shows a **modal alert** that makes every following `DoScriptFile` silently not run ("NO LOG").
  Dismiss with `osascript -e 'tell application "System Events" to tell process "After Effects" to keystroke return'`.

### Small traps found on the way (CONFIRMED)
- `"text " + w.size` (or `.location`, `.bounds`) throws "Object of type Dimension found where a Number, Array, or Property is
  needed". Concatenate `.width` / `.height` / `[0]`, never the object. Same family as the Array/Error concatenation entries.
- A `// comment` appended by sed inside a one-line `{ … }` block comments out the closing brace: the file fails to parse.
  Put the comment after the `}` or use `/* */`. The ES3 gate catches it; run it after every scripted edit.

## Blending, Levels clipping, sampling and still depth at 16 bpc (2026-10-30)

Measured in AE 2026 (26.x) and Beta 27.1, 16 bpc, no colour management, linearBlending false.
Each fact was predicted, then measured on a 16-bit ramp that carries every 15-bit code.

- **Subtract clamps before the opacity mix (CONFIRMED by measurement).** out = dst + α·(max(0, dst − src) − dst).
  With src > dst the blend clamps to 0 and the result is dst·(1 − α), not dst − α·src. Add with opacity is linear
  (dst + α·src, within 1 code). So a weighted negative term built from Subtract opacity is lost wherever the source
  is brighter than what's under it. To subtract w·src, scale the source first (a gain at 100 % opacity), then Subtract.
- **Pro Levels "Clip To Output White" (ADBE Pro Levels2-0039) values (CONFIRMED by measurement):** 1 = clips,
  2 = no clip, 3 ("Off for 32 bpc Color") clips at 8 and 16 bpc. Don't infer the order from the menu text;
  assert the value and prove it with a pixel row.
- **Easy Levels doesn't survive save (CONFIRMED by measurement, 26.2.1).** Script-set values read correctly in memory,
  then come back as defaults after save and reopen. Pro Levels survives. Gate on the reopened file, never on memory.
- **saveFrameToPng truncates 16 bpc to 8 bit (CONFIRMED by measurement).** About 0.4 levels darker than a render-queue
  PNG of the same frame (72 % of px differ by 1). At 8 bpc they match. Gate proofs go through the render queue.
- **Motion-blur sampling (CONFIRMED by measurement).** shutterPhase takes whole degrees (−83.57 becomes −84).
  Samples sit at phase + k·angle/N. On 2D layers the adaptive limit is 128, so only 3D layers hold an exact sample
  count, and a 3D layer draws differently from a 2D one even with blur off.
- **samplingQuality (Bicubic/Bilinear) applies only at Best quality.**
- **Draft at 50 % scale is not a point sample (CONFIRMED by measurement).** It filters with a fixed tent, [1 2 1]/4 per
  axis, centred on the even source pixel. A least-squares fit on two renders gave weights of exactly 1/16, 2/16 and 4/16,
  residual 0 on every interior px. Linear ramps pass through a symmetric tent unchanged, so a ramp test reads "exact"
  and hides the filter. Measure a resample kernel on random-valued input. At the layer edge the tent reaches off the
  layer and blends with transparency; a transparent margin doesn't help, the margin has to be opaque content.
- **Vector strokes widen under layer scale.** A 2.502 px stroke rendered as 2.565 and 2.631 at 2.6 % and 3.5 % scale.
  To match a raster pipeline, draw at scale 1 in a precomp and scale the rendered layer.
- **Linearizing every layer before compositing changes edges.** Blending overlaps and anti-aliased edges in linear light
  read +1.4 to +3.3 levels against a pipeline that composites in gamma and linearizes only to average blur samples.
- **`instanceof SolidSource` (UNVERIFIED, open).** True on a fresh solid, false on 406 solids in a reopened project.
  Test `mainSource` with more than one method before trusting a type check.


## Scripts Claude drives: no AE dialogs (2026-10-29)

**The rule.** An ExtendScript error that popped AE's "Unable to execute script" dialog during a build was "a sloppy
error": the modal blocks AE for every lane until someone clicks it away, and it means the script's own catch and log
failed. Every `.jsx` that Claude runs:

- runs inside one wrapper: `app.beginSuppressDialogs()`, a `try / catch` that only logs, and
  `app.endSuppressDialogs(false)` in `finally`. Never call `app.open` while dialogs are suppressed;
- is linted (`scripts/qc_gate.py` or es3lint) **after** its placeholders are filled. On Oct 29, JSON with quotes
  pasted into a `"%X%"` string passed the template's lint, then reached AE as a syntax-error modal that background
  control could not dismiss. Pass data through files, never inside string literals;
- never keeps a property handle across `addProperty` on the same group: AE invalidates the siblings, so re-fetch;
- logs append-and-close per line, because `saveFrameToPng` can end a script silently mid-run.

## ffmpeg drops Rec.709 tags on raw pipes (ffmpeg 8.1, 2026-10-29)

**Confidence: measured.** Frames piped in as `-f rawvideo -pix_fmt rgb24` keep only
one of `-color_primaries`, `-color_trc` and `-colorspace` when those are set only on the output: two tags read
unknown (`bt709,unknown,unknown`). Set all three **before `-i`** as well. To retag a finished file without re-encoding:

- ProRes: `-c copy -bsf:v prores_metadata=color_primaries=bt709:color_trc=bt709:colorspace=bt709`
- H.264: `-c copy -bsf:v h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1`
  (use `matrix_coefficients=6` if the source had no colorspace)
- WebM: `-c copy -color_primaries bt709 -color_trc bt709`

Check with `ffprobe` that all three tags read `bt709` before delivery.
