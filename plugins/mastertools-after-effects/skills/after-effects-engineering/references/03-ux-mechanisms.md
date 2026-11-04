# 03 — UX Systems Library (the mechanism catalog)

> The principles live in `01-design-canon.md`; this is the **pattern catalog** — when the workflow analysis
> (`02`) says "hide this," "guide them here," or "make this instant," these are the proven mechanisms, with
> guidance on **which to use when**. Grounded in how the best AE tools actually behave. Works for ScriptUI and
> CEP alike (CEP gives you better tools to honor these, not permission to ignore them).

---

## §1 — PROGRESSIVE DISCLOSURE (mechanisms, in order of preference)

1. **Smart default + silent override** *(the best disclosure is no control at all).* If a value is right ~90% of
   the time, default it and let advanced users change it where it lives — don't add a visible option for the
   10%. Hiding a *decision* beats hiding a *control*.
2. **Gear / "More…" dialog** — set-once-and-forget configuration. A small gear/"More…" opens a focused secondary
   dialog; it closes, the panel remembers. Best for preferences that rarely change. Keeps the primary surface
   pristine.
3. **Secondary mode (tab / segmented control)** — an entire *alternate workflow* with its own identity
   ("Sequence" vs "Find + Replace"). Use when the second path is common enough (≥ ~1 in 5 sessions) to deserve
   one click and has enough controls to justify its own view. Each tab should feel like a real place.
4. **Right-click / power menu** — advanced *actions* (not settings) power users want and novices should never
   trip over. Invisible until invoked; zero surface cost. (Double-click for the single most likely action — e.g.,
   reveal the layer.)
5. **Inline contextual reveal** — show a control only when the mode that needs it is active, **but only if it
   doesn't change panel height** (use fixed-height mode panels; a layout jump is worse than a slightly-irrelevant
   control). Tie the reveal to an explicit user action, never to hover.
6. **Expandable / collapsible section** — *last resort.* Collapsed sections waste space; expanding causes layout
   instability. A tab is almost always better.

**The discoverability caveat (non-negotiable):** hiding only works if users can still *find* it. Every
disclosure entry point must be visibly present (a real gear icon, a labeled "More…", a tab) — hidden-and-findable,
never hidden-and-lost.

> **CEP note:** prefer a **top tab bar** over per-density-tier `display:none` of interactive surfaces. A drawer/
> popover that lives in normal flow can inflate panel height → trigger a density downgrade → vanish the very
> control you opened. If you must use a popover, make it a `position:fixed` overlay. See `06` for the full lesson.

---

## §2 — THE LAUNCHER INSIGHT

The most successful AE tooling at the *suite* level isn't a mega-panel — it's a **launcher** (KBar, Tool
Launcher, Quick Menu) where users place only the buttons they use. A focused single-purpose tool that does one
thing brilliantly is often *more* valuable than a sprawling suite, because users compose focused tools into
exactly the workspace they want. When a request is really "a bunch of small utilities," consider shipping them
as **separate, launchable actions** rather than one crowded panel — unless they share state and a workflow.
Expose your tool's discrete actions as clean, separately-invokable entry points.

---

## §3 — BUILT-IN GUIDANCE (the tool teaches itself)

- **Empty state as onboarding** — the hero zone, when empty, says exactly what to do first, contextual to *why*
  it's empty ("Select layers in the timeline" vs "Open a comp" vs "Type in Find to preview"). Map every empty
  condition (`05` §4.1). This replaces a tutorial.
- **helpTips with examples, not definitions** — *"Find: text to search in layer names — e.g., 'BG' matches
  'BG_sky'"* teaches more than *"search string."*
- **The preview is the lesson** — `Old → New` before commit teaches the transform by demonstration, risk-free.
- **Labels in the user's language** — the verb they'd use ("Rename", "Fix"), never the API's ("Execute batch
  transform"). The label *is* the instruction.
- **A discreet "?" / info affordance** — a small `i` button (the one place an `alert()` is acceptable) for
  version, a one-line "what this does," and a support link. Never a wall of text.
- **First-run nudge (optional, restrained)** — at most one dismissible inline hint on first open, persisted as
  dismissed. Not a multi-step wizard, not a modal tour.
- **Spatial layout as manual** — top-to-bottom = order of operations; the reading order teaches the workflow.

Guidance hierarchy: **make it obvious (layout/labels) → explain on hover (helpTips) → explain on demand (info
button).** Never force explanation into the user's way.

---

## §4 — DEFAULT INTELLIGENCE (the tool decides so the user needn't)

The highest-leverage UX system — every good default is a decision the user never makes.
- **Context-inferred defaults** — scope from selection, target from active comp, mode from what's selected. The
  "do nothing" state should already be the most likely correct answer.
- **Remembered defaults** — persist last-used values (`app.settings`); reopening resumes where they left off.
- **Sensible cold defaults** — on true first run with no context, pick the most common value, not empty/neutral.
- **Optimistic pre-fill** — pre-populate fields with the best guess (highlighted so it's clearly editable).
- **One reset** — a single explicit "restore defaults." Never *auto*-reset their state as a side effect of an
  operation; preserve context, reset only on request.

---

## §5 — FEEDBACK SYSTEMS (the user always knows what's happening)

- **Instant preview** (< 400 ms) for anything being configured — drive it off the JS cache, never live DOM
  (`04` §perf). Lag reads as brokenness.
- **Progress for anything slow** — the moment an op crosses ~0.4–1 s, a real per-iteration progress bar with a
  label and a cancel path (`04` §threading). A frozen-looking AE is the fastest way to lose trust.
- **Post-action confirmation** — verb + count + noun in success colour ("✓ Renamed 12 layers"), edge cases
  appended ("(2 locked, skipped)"), next step hinted ("Cmd+Z to undo"). This is the peak-end moment.
- **Momentary colour, then calm** — success/error colour is a *flash*; reset to neutral on the next interaction.
  Persistent coloured status becomes noise.
- **Errors that coach** — inline, never `alert()` for expected conditions; say what went wrong, why, and the fix
  ("✓ Fixed 8 — ✗ 3 failed (locked) — unlock and retry").

---

## §6 — FORGIVENESS & SAFETY (confidence to act fast)

- **Undo-first design** — every operation in one clean undo group; tell the user ("Cmd+Z to undo").
- **Non-destructive by default** — prefer operations that add/modify recoverably. When you must overwrite (e.g.,
  expressions), back up first (`04` §expressions-from-scripts).
- **Scale confirmation to real risk** — *no* confirmation for undoable actions; confirm *only* when destructive
  *and* hard/impossible to undo, and make the confirm useful (offer "save first").
- **Show before you do** — preview/plan → execute → confirm, never execute → hope → undo.
- **Validate before acting** — re-check refs just-in-time so a stale click can't corrupt the project (`04`
  §undo); flag mismatches instead of plowing on.

---

## §7 — THE PATTERN PICKER (analysis result → mechanism)

| The workflow analysis (`02`) says… | Use this pattern |
|---|---|
| "right ~90% of the time" | Smart default + silent override (§1.1) — no control at all |
| "rare config, set once" | Gear / "More…" dialog (§1.2) |
| "second common workflow, ≥1-in-5" | Secondary tab with real identity (§1.3) |
| "advanced *action* power users want" | Right-click / power menu (§1.4) |
| "control only relevant in one mode" | Inline reveal, fixed-height panel (§1.5) |
| "a bunch of unrelated small utilities" | Separate launchable actions, not one panel (§2) |
| "user won't know how to start" | Empty-state onboarding + example helpTips (§3) |
| "the common task takes too many clicks" | Infer + remember + auto-advance (§4, `02` §2) |
| "operation could surprise them" | Live preview / plan before execute (§5, §6) |
| "operation is destructive & permanent" | Scaled confirmation + save prompt (§6) |
| "operation might take a while" | Per-iteration progress + cancel (§5) |

> Validate the finished design against the **Test Battery** in `01-design-canon.md` before writing more code.
