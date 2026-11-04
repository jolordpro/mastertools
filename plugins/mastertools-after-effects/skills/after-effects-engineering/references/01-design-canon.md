# 01 — Design Canon (the single source of truth for UX judgment)

> The one place the design philosophy lives. Everything else (the workflow process `02`, the UX mechanism
> catalog `03`, the visual constants in `05`, the engineering rigor `04`) is *implementation* of these
> principles. Read this once; it's short on purpose. Run the **Test Battery** on every finished design.

---

## THE SIX PRINCIPLES

**1. Cognitive load is the enemy. (The Prime Directive.)**
Every decision the tool can make for the user *without removing meaningful control*, it must. The complexity of
a task is fixed — the only question is who absorbs it, the tool or the user; make it the tool (Tesler's Law).
Fewer choices is faster, not weaker (Hick's Law). *In practice:* smart defaults, scope inferred from selection,
last-used settings remembered, no confirmation for anything undoable.

**2. One job, minimum surface. (MVI.)**
Name the single thing the user is doing; build the smallest interface that nails it; add back only what earns
*permanent* space — used in roughly ≥ 1 in 5 sessions. This means minimum **cognitive load**, not minimum
controls: six clearly-labeled, grouped controls are simpler than three where one is a mode-dropdown hiding four
behaviours. The enemy is **ambiguity and choice-density**, not element count (Miller's Law: a few labeled
clusters, never a flat field of options).

**3. Hierarchy is importance; there is one obvious action.**
Visual weight maps to importance. The hero content dominates (≈55–65% of the panel); the primary action is the
largest, closest, most prominent target (Fitts's Law); status and context are small and dim. At a glance,
exactly one thing should pull the eye. If two controls fight for attention, the hierarchy has failed.

**4. The tool teaches itself.**
The UI is the manual. Empty states say what to do first; labels use the user's verbs, not the API's nouns;
helpTips give a concrete *example*, not a definition; preview shows what will happen *before* it happens;
feedback confirms what happened *after*. Show options rather than make users remember them, but organise them so
showing doesn't overwhelm (recognition over recall). Behave like the host app the user already knows — Window-menu
docking, native-looking controls, Cmd+Z works, Esc closes a dialog (Jakob's Law). No readme required for basic
operation.

**5. Show, then do — and be forgiving.**
Preview or plan → execute → confirm. Never execute → hope → undo. Default to non-destructive operations; wrap
each in one clean undo group and tell the user ("Cmd+Z to undo"). Scale confirmation to *actual* risk: none for
undoable actions (confirmation theatre erodes trust and speed), a real confirm only when an action is both
destructive *and* hard to reverse. Speed comes from users trusting that nothing they click can break their work.

**6. Respond instantly; end cleanly.**
Keep interaction under the ~400 ms flow threshold (the Doherty Threshold) — drive previews off a cached
snapshot, never live DOM reads (`04` §perf). The moment anything exceeds that, show real per-iteration progress.
Make completion specific and reassuring ("✓ Renamed 12 layers — 2 locked, skipped — Cmd+Z to undo"): people
judge the whole experience by its peak and its end (Peak–End Rule), so the end must feel clean.

**One-line synthesis:** *absorb the complexity, reduce the visible choices, keep the response instant, behave
like the host app, and make finishing feel effortless.*

---

## THE TEST BATTERY (run on every finished design — fix before writing more code)

These are far cheaper to satisfy on paper than in a rebuild.

1. **Squint test** — blur your eyes; is there exactly *one* obviously dominant action? (Principle 3.)
2. **Cold-stranger test** — a competent artist who's never seen the tool finishes the primary task in under ~15
   seconds with zero reading. (Principles 2, 4.)
3. **Count-the-decisions** — tally every choice between "I want X" and "X is done"; every non-essential one is a
   defect to eliminate, infer, or default. (Principle 1.)
4. **"Now what?" test** — at every state (empty, mid-task, post-action) the UI tells the user the next move. No
   dead ends. (Principles 4, 6.)
5. **2-AM test** — would an exhausted pro on a deadline understand every label without pausing to think? If a
   label makes them stop, rewrite it. (Principle 4.)

---

## AUTHORITY

This doctrine owns the *why* and *what* of design and does not change per tool. `02-workflow-first.md` owns the
*process* of applying it before building; `03-ux-mechanisms.md` owns the *mechanisms* that realise these
principles; `05` owns the visual constants/labels/ScriptUI conventions; `04` + `00` own the technical means
(instant response via caching, safe execution via validation/undo). When canon and an implementation file seem
to disagree, **canon decides the principle; the implementation file decides the mechanic.**
