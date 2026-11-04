# ExtendScript authoring and QC (merged from ae-extendscript)

Merged word for word from the ae-extendscript skill. Its headless harness is in assets/, its QC gate in scripts/.

Most AE script failures are not logic bugs. They are load-time syntax deaths, silent
no-ops from suppressed dialogs, and resource exhaustion during long batch runs. This
skill covers the failures you cannot reason your way to, and hands the mechanical
checks to a script so they cost you nothing.

You already know ES3 and the AE object model. What follows is deliberately only the
part that bites.

## Use the tooling

**`assets/probe-project.jsx`** — run this FIRST, before writing any tool code. One
`DoScriptFile` round trip reports comps, grouped layer geometry, audio/lock/solo flags,
footage sources, render-queue state and the template lists that exist *on this machine*.
It aggregates in-script, so a 63-layer comp is ~12 lines rather than 63, and a 77-comp
project indexes instead of dumping. Four separate exploratory probes and a 39 KB read is
the failure mode it exists to prevent. Set `CFG.comps` for full detail on named comps.

**`scripts/qc_gate.py <file.jsx>`** — run this on every script before delivering. It
parses the file and enforces the ES3 rules mechanically: no ES5+ syntax or methods, no
reserved words as bare object keys or member accesses, balanced suppression and undo
pairs, guarded polyfills. Reserved words are the one to care about — `{ in: 1 }`,
`.delete`, `{ default: … }` parse fine in any normal checker and then kill the script
at load in ExtendScript. Let the gate carry that so you can think about behaviour.

**`references/api-gotchas.md`** — read before using any AE API you have not used in
this session. It records behaviour that is version-dependent, undocumented, or actively
contradicts the obvious reading, with sources and confidence levels. Several entries
are not in Adobe's docs at all. Guessing here is how a 32-item render fails on item
one, or on all thirty-two.

**`references/scale-and-proxies.md`** — read when one template must produce dozens of
outputs, when asked to make renders faster, or before deleting anything from a project
you did not build. Covers timing renders so the number survives a cache purge, pricing
an individual precomp, buying that cost back with comp proxies, and the whitelist that
stops a prune from deleting the ~30% of disabled layers that are load-bearing. Also has
the ±1 tolerance a pixel-diff regression gate needs, without which the gate fails every
time and you learn to ignore it.

**`assets/harness-template.js`** — stubs the AE object model and ScriptUI so script
logic runs headlessly. Extend it for anything with real logic and run it before
delivering. Testing against deliberately broken projects is the only way to know
preflight *reports* rather than throws, and it costs minutes rather than an AE session.

§1b covers the render path specifically: `system.callSystem` backed by the virtual
filesystem (so `mv`/`cp` publishing is testable), `app.scheduleTask` + `pump()` for an
async run loop, output-module `getSettings`/`setSettings` with knobs for a setting that
silently refuses to change and a file path that loses to the module's name template,
`importFile` for verifying a rendered file's duration and audio, and a flat ScriptUI
registry so a test can click a control by its label (`findW("button", "Preflight")`).
`assets/harness-selftest.js` proves those stubs still behave — run it after editing the
template.

## The suppression triad

`app.beginSuppressDialogs()` alone is a silent-failure trap: errors vanish and the run
reports success. Detection alone lets a modal block an unattended batch. You need all
three parts together:

1. `beginSuppressDialogs()`
2. `app.onError = fn` capturing the real error string
3. checking `item.status === RQItemStatus.DONE` after `render()`

Pair every `begin` with an `end` in a `finally`, and restore the previous
`app.onError`. Triads nest — a render inside a batch — and AE does not document whether
`endSuppressDialogs` decrements or clears outright, so count depth and let only the
outermost pair toggle suppression. `references/api-gotchas.md` has the working
implementation.

Export errors on Apple Silicon are frequently transient and their codes are
non-diagnostic — 1, 10, 784, 9988 and 19972 are all the same vague failure. Do not
decode the number. Retry with a short sleep and report the string `app.onError` caught.

## Keep expected conditions out of modals

No project open, nothing selected, an empty field, a name collision — these are
expected, and each one behind an `alert()` is a nuisance interactively and a hang in an
unattended batch. Report them inline in the panel, in a status control the user can
read at a glance. Reserve `alert()` for the About affordance and genuinely fatal
surprises; a script with more than one or two is escalating normal states to modals.

The same instinct applies to preflight generally: a long-running button should stay
disabled until everything checkable has been checked — comps resolve, targets exist,
named templates are present *on this machine*, folders are writable. A 40-item render
is hours, and every check is seconds.

## Bulk runs and project cycling

Long batches fail from resource exhaustion, not logic. The cycle is
`app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES)` → purge → `app.open(next)`.
Enforce it structurally by making one function the only place `app.open` appears; then
`grep -c 'app\.open('` returning 1 turns "did we purge before every open?" from a
review question into a fact. See `references/api-gotchas.md` for what purging actually
covers, which changed in AE 24.3.

Three things that bite at scale:

- **Opening a project reloads its render queue from disk.** Queue-isolation disabling
  must be re-applied after *every* open, not once per run. `renderQueue.render()`
  renders every enabled item, so a user with queued work from another job will have it
  rendered by your script. Snapshot the states, park them, restore in a `finally`.
- **Never leave an undo group open** across a save, a render or a project open.
- **A ScriptUI panel's batch must BLOCK.** `app.scheduleTask` has been measured never to fire —
  see `references/api-gotchas.md`. Loop, repaint the status line with `w.update()`, cancel on
  Escape, ship a label saying so rather than a Stop button that cannot be clicked, and tell the
  operator up front roughly how long the freeze will be.
- **Track success per output, not per unit of work.** An item that saves a project and
  then fails its render has one success and one failure. Wrapping both in one `try` so
  the failure jumps past the recorded success is the classic bug here.

## Smaller traps worth knowing

- **Floating windows (palettes):** never open a file/folder dialog from one (it can vanish and lock AE: no open, no
  quit). Every resizable window must scroll when squeezed: ScriptUI has none, use the scrollbar pattern. AE sends no
  wheel events to script windows, and `layout.layout(true)` snaps a window to full size. Details + test recipes:
  `references/api-gotchas.md` › "ScriptUI windows: dialogs, scrolling, engines, real-input tests".

- **Whitelist, never blacklist, when toggling layers.** Touch only layers whose names
  are in the known set. A blanket disable silently kills guides, adjustment layers,
  mattes and structural layers the comp needs.
- **Renders go local-then-move; project files do not.** Render to `Folder.temp`, verify
  non-zero, then copy — `File.copy()` does not overwrite, so clear the destination
  first. But save `.aep` files directly to their destination, because moving a project
  file can break footage paths.
- **Never fabricate an output module.** Movie codec and format are read-only to
  scripting. Validate the named template exists and stop with recreate steps if not.
- **Report what you skipped.** If a run caps, samples or drops anything, say so.
  Silent truncation reads as "covered everything" when it did not.

## Silent failures — the ones that cost hours

AE's expensive bugs do not raise errors. Each of these built cleanly, reported success, and
was wrong. Details and code in `references/api-gotchas.md`.

- **`addText()` inherits the last-used character style from prefs** — font, size, and
  tracking you never set. Write every `TextDocument` field explicitly.
- **`sourceRectAtTime()` ignores a `setValue` made in the same pass.** Measure-adjust-measure
  loops compound their own error and run away. Write and save in one pass, reopen and measure
  in the next.
- **Effect names over 39 bytes break `property(name)` lookup** — but *setting* the long name
  succeeds, so the control looks right and every expression reading it throws.
- **`try { … } catch (e) {}` in an expression hides all of the above.** `expressionError`
  stays empty, so an error sweep reports a clean project while nothing works. Keep the
  safe-degrade wrapper — it is still correct — but never treat "0 errors" as proof.
- **`saveFrameToPng` is asynchronous and fails silently.** A missing frame means investigate,
  not "the comp is empty". Poll from outside the script.
- **A locked layer throws on `.comment` and `.label`.** Write metadata first, lock last.
- **AE reports script errors as a modal**, which blocks the next `do javascript` and looks
  exactly like a hang. When chaining from bash, read and dismiss it between steps.

**So verify from outside the model AE gives you.** Re-parse the saved `.aep`, render frames
and measure pixels, and simulate generated expressions in JavaScriptCore against a fake AE
that *throws* on unknown names. That last test found two control-name bugs in one session
that a clean AE error sweep had passed.

## Design the verification, not just the change

The expensive mistakes in AE work are rarely the edit. They are verifications that could not have
failed. Three separate times in one session a change was "proved" safe by a check that was
structurally incapable of catching the bug:

- A first-name alignment change was verified as a 0.02px no-op **on a player whose two names are
  the same width** — the one case where centred and flush-left are identical placements. The change
  was wrong for every other name.
- A short-name uplift was verified on the reference player whose uplift factor is **pinned to 1 by
  design**, so the feature under test never engaged.
- A control sweep nudged every control **upward**, which for a ceiling or cap is correctly a no-op.
  It reported 20 dead controls, all of them alive.

So before trusting a check, ask **what value of the input would make this fail?** If there isn't
one, the check is decorative. Concretely:

- **State the objective in words before choosing a metric, and check the metric can fail when the
  objective is violated.** "The two names are the same width" cannot fail when the type is far too
  big for its container — and a solver driven to a perfect 0.0 width delta produced lockups that
  overflowed the card. A pixel diff proves determinism and change-isolation; a measurement gate
  proves one invariant you chose. Neither can tell you the frame looks wrong, so for anything with
  a visual result, look at frames — at the extremes, not the happy path.
- **Pick a witness that can fail.** The reference/approved case is usually the worst choice — it is
  reference precisely because everything about it is neutral. Pick the input that exercises the
  thing you changed: a short name for a fit solver, a limit pushed *down* past the current value,
  a differently-shaped asset for a framing rule.
- **A skip is not a pass.** A check that `continue`s when a comp or layer is missing passes
  vacuously on a typo, and reports reassurance it never earned. Absent targets should FAIL.
- **Audit the catch, not just the call.** If a probe's "unknown" branch prints the same as its
  "healthy" branch, it cannot report a problem. One swallowed throw
  (`canAddToMotionGraphicsTemplate(app.project)` throws — it takes the comp) hid a control that
  was missing from Essential Graphics for an entire phase.
- **Map dependencies before sweeping behaviour.** Scan every live expression for `effect("NAME")`
  and record which properties read which control *first*. Without that map, "nothing moved" is
  ambiguous between dead wiring and a witness in the wrong place — and the second is far more
  likely.
- **Set expected counts from a measurement, never from a changelog.** "I added three expressions"
  is wrong the moment one of them replaced an existing one. Walk the project and count.
- **Beware the property that reports a value nothing drives.** With Separate Dimensions the
  composite `Position` is read-only and reads back a figure no expression produces; watch
  `ADBE Position_0/_1` instead.

And one that only a real run catches: **drive the actual UI**. A headless harness tests what the
code does, not whether the button reaches it. Walking a built ScriptUI window and invoking its
handlers is what exposed that `app.scheduleTask` never fires — a bug in how work was *scheduled*,
which no amount of testing the work itself could have found.

### Gated builds: rules that cost a run when skipped (2026-10-30)

From a multi-session AE build with frozen gates. Each one was learned from a real slip.

- **Freeze every reader before the first render.** Log its sha in the runner's preamble, and stop if it's missing.
  Once outputs exist, a reader written afterwards can be fitted to them, even by accident.
- **Self-tests run in the real data's regime.** A synthetic case that never reaches the real range proves nothing:
  test frames that never overshoot missed a library's clamp, and an alpha check tuned for A ≥ 0.6 failed real
  files at A 0.12–0.19. Add one counter-test on a real frame.
- **Fit against AE renders of the thing itself, never only against an offline model of AE.** Keep fit frames apart
  from gate frames: once a gate frame's AE output has been seen, no fit may use it.
- **Prove a setting's meaning on pixels before a gate depends on it.** An effect option's value order was inferred from
  its menu text and was wrong; a pixel row caught it.
- **When the real implementation is available, it is the reference.** A model of it is a diagnostic row.
- **Compare like with like.** 8-bit against 8-bit, one rounding rule (half-up; numpy's round is half-to-even).
- **A counter-test reads on the same instrument as the gate it protects.**
- **Log input shas at start (GEN) and at end (GEN-END).** A mismatch voids the run. Never edit a file a running job reads.
- **The lint gate fails loudly when its script is missing.** A runner that passes a skip flag "for now" ends up skipping
  it on every build.
- **A shell helper can shadow a real command.** A helper named `cut` made a sha check that could never match.
  Prove each check on a known miss.
- **Snapshots keyed by name throw on duplicate names.**
- **Purge caches at every hand-back.** A disk-space dialog can't be cleared remotely; keep it from appearing.

## Delivery notes for the user

- Dockable panels install to
  `~/Library/Application Support/Adobe/After Effects <year>/Scripts/ScriptUI Panels/`,
  then AE must restart; the panel appears at the bottom of the **Window** menu.
- Preferences ▸ Scripting & Expressions ▸ **Allow Scripts to Write Files and Access
  Network** must be on for any file output.
- AE caches script panels in memory. If a panel behaves like an older version, fully
  quit and reopen AE, or run via `File ▸ Scripts ▸ Run Script File…`.
