# 02 — Workflow-First Design (think before you build)

> The most important file for tool *quality* (as opposed to code *correctness*). A technically flawless panel
> optimized for the wrong workflow is a bad tool. This analysis happens **before any UI is sketched or any code
> is written** — inside build Phase 1, mandatory for any non-trivial tool. The goal: the tool does the user's
> *most common* task in the fewest interactions, and never makes them wade through options they rarely touch.

---

## §0 — THE CORE BELIEF

A tool is not a collection of features. It is the **shortest path between an intent and a finished result.**
Every option you add is a tax on every user who didn't need it. The design question is never "what could this
tool do?" — it's "what does this specific user do *over and over*, and how do I make that one thing feel
effortless?"

Two failure modes this file prevents: **The Everything Panel** (every capability visible at once, so the common
task is buried) and **The Wrong Optimization** (a beautiful UI around a workflow performed twice a year, while
the daily task takes six clicks).

---

## §1 — THE WORKFLOW INTAKE (answer before designing)

From the user's words, reasonable inference, or **one or two targeted questions** if genuinely unknowable. Write
the answers down — they become the design's success criteria.

**A. The Job** — (1) In one sentence, what is the user trying to accomplish? (Their words: "rename my selected
layers in sequence," not "batch string transformation.") (2) What triggers them to reach for it? (3) What does
"done" look like — how do they know it worked?

**B. Frequency & Distribution (the heart)** — (4) List every distinct task the tool might handle; estimate how
often the user does each (*every session / daily / weekly / rarely / once*). (5) Which **one** is performed
most? That is the **Primary Path**. (6) What % of total uses does it represent? (Find the 80/20.)

**C. The User** — (7) Novice (needs guidance, mouse-driven, infrequent) or power user (knows the domain,
keyboard-driven, daily)? Often both → plan two tracks (§4). (8) What do they already know? (Don't re-teach AE;
do explain the tool's own concepts.) (9) State of mind at the moment of use? (Deadline at 2 AM → ruthless speed,
zero ambiguity. Exploring → discoverability.)

**D. The Context** — (10) What's *selected/open* when they invoke the tool? Can scope/intent be **inferred** from
that instead of asked? (A layer selected ⇒ scope = selected.) (11) What did they *just* do, and what next? (Pick
up where the prior step left off; tee up the next — auto-advance.) (12) Destructive vs non-destructive actions?
(Sets confirmation policy.)

**E. The Constraints** — (13) Which inputs are *required* vs *optional with a sensible default*? (Defaults
eliminate decisions.) (14) What can go wrong in a real project (locked/missing/wrong-type/empty)? Each becomes an
empty-state or guard, not a crash.

---

## §2 — PRIMARY-PATH OPTIMIZATION (the click budget)

**Count the interactions** between "I want X" and "X is done," then drive it toward the minimum:
1. Write the Primary Path as a literal step list (open panel → … → result).
2. For each step ask: *essential to the user's intent, or can the tool make it?* Eliminate, infer, or default
   every non-essential step.
3. Target: **the common case is one obvious action**, ideally with smart defaults pre-filled from context.

**Techniques to remove steps (priority order):** infer from selection/context → remember last-used (persist via
`app.settings`) → smart default per context → auto-advance (after a scan show results; after an action refresh
state and point at the next move) → collapse confirmations (non-destructive ⇒ just do it; undo exists).

**The test:** a competent stranger completes the Primary Path in under ~15 s with zero reading. If not, it's too
long — cut.

---

## §3 — THE 80/20 SURFACE & THE PERMANENT-REAL-ESTATE TEST

For every control, ask: *"What workflow does this save, and is that workflow common enough (≥ ~1 in 5 sessions)
to justify occupying screen space and attention every session, including the ones where it's not used?"*

- **Used most sessions** → primary surface, prominent (the hero + its direct controls).
- **Used sometimes** → primary surface, secondary weight (smaller, grouped, dim).
- **Used rarely (< ~1 in 5)** → **behind disclosure** (gear, "More…", Advanced tab).
- **Used almost never** → consider cutting it entirely.

**Visibility ≠ complexity.** Six clearly-labeled, grouped controls are *simpler* than three where one is a
mode-dropdown hiding four behaviors. The enemy is ambiguity and choice-density, not element count. Don't hide
things to look minimal — hide things that are genuinely rare, and make what remains unmistakable.

---

## §4 — TWO TRACKS IN ONE PANEL (novice + power user, no compromise)

Layer the *same* tool instead of building one "medium-complexity" interface that serves neither:
- **Discoverable track (novice/infrequent):** visible labels, an obvious primary button, helpTips, empty-state
  guidance — the mouse path works end-to-end with no hidden knowledge.
- **Fast track (power user), layered on top:** keyboard triggers (Enter = primary; Ctrl/Cmd+F = focus search;
  Space = toggle), remembered defaults so repeat use is near-zero-input, multi-select for batch, a right-click /
  power menu for advanced actions novices never see.

The fast track must never *cost* the novice anything; the discoverable track must never *slow* the expert
(no forced wizards, no re-confirming what they set last time). Progressive disclosure (`03`) is how they coexist.

---

## §5 — ANTI-PATTERNS (smells that mean you skipped this file)

- **Feature parity with the menu** — "it can do everything AE can." A tool's value is *focus*, not coverage.
- **Mode soup** — one dropdown reconfiguring the whole panel into 5 unrelated tools. Usually two/three should be
  separate tools, or tabs with real identity.
- **Asking what you can infer** — a "Scope: [Selected ▾]" dropdown when a selection already exists.
- **Required input with no default** — every empty required field is a forced decision.
- **Dead-end states** — a result screen with no suggested next action.
- **Confirmation theater** — "Are you sure?" on a non-destructive, undoable action.
- **Option creep** — a checkbox for every conceivable preference until the common task is surrounded by noise.

---

## §6 — WORKED EXAMPLE (rename layers)

**Intake (compressed):** Job = rename selected layers, usually numbered (`Layer_01…`). Frequency: sequential
rename = every session (Primary, ~70%); Find+Replace = weekly (~20%); prefix/suffix = occasional (~8%);
case/regex = rare (~2%). User = both junior (mouse) and senior (keyboard). Context = layers already selected ⇒
scope inferable; next step is back to the timeline.

**Design that falls out:** Primary surface = sequential rename — one "Name" field + a live preview
(`Layer → Layer_01 … Layer_12`) + one "Rename" button; scope **inferred from selection** (no scope dropdown);
Enter triggers Rename. Find+Replace = a **secondary tab** (20% earns one click). Prefix/suffix/case/regex →
behind **"More…"/Advanced**. Last-used base name + padding **remembered**. Non-destructive ⇒ no confirmation;
post-action "✓ Renamed 12 layers — Cmd+Z to undo"; locked layers skipped with a count. **Click budget:** a
six-decision form → **one field + Enter**. That delta is the difference between a $5 script and a tool people
recommend.

---

## §7 — THE ONE-PAGE BRIEF (produce before coding any substantial tool; confirm with the user)

```
TOOL: <name>
JOB (user's words): …
PRIMARY PATH (≈__% of use): step → step → result   | click-budget target: __
SECONDARY PATHS (on-surface, secondary weight): …
ADVANCED (behind disclosure): …
CUT (considered, rejected — why): …
INFERRED FROM CONTEXT (not asked): scope=…, target=…, mode=…
REMEMBERED (persisted defaults): …
AUTO-ADVANCE: after scan → …; after action → …
CONFIRMATIONS: destructive=…(confirm)  others=(none, undoable)
EDGE STATES → MESSAGES: no comp→… / none selected→… / empty→… / zero results→…
TWO TRACKS: novice path = … ; power path = …
```

**Workflow first, interface second, code third.** Only after this brief is settled do you move to spatial
hierarchy, labels (`05` §3), and the multi-pass build.
