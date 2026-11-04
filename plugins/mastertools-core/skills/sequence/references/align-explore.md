# Phases 1 and 2 · Align and Explore

## Phase 1 · Align (the outcome, not the tech)

- Read again at the start of Phase 1 and of Phase 2, even after a compaction.
- **First, before any question,** read `attention.md` (what's worth asking, the
  settled-answer search, gates that show the work).
- **Reuse and past lessons.** Search the project and its siblings once for
  each part the build needs; a part that fits is used or extended and named in
  the Brief. Load the matching domain kit once, when installed: After Effects
  → `after-effects:after-effects-engineering`. A kit that isn't installed:
  one line, go on. Then read past lessons
  in this area (`retro.md`, "Read before building").
- Two rounds is the target, three the cap. At most four questions per round,
  each its own question. Ask only the user's kind of call: money, people, taste and
  risk. No technical questions unless the outcome itself is technical. No
  change lists. Context first; the poll after the user says ready.
- Question bank. Pick only what this build needs, and skip what the request
  already answers:
  - Who is it for, and who touches it first?
  - If it worked, what's true a month after it ships?
  - What does it replace or fix today?
  - Explore or ship? Any date?
  - How should it feel? Which references does the user like?
  - What must it never do?
  - Where must it live (and still work) if the user changes jobs?
  - How much use: one person weekly, or hundreds daily?
  - What does it cost if it's wrong?
- After each round, a three-line playback:
  `User said: ... · Claude inferred: ... · Still open: ...`
- **Test the ask** (after round one, before the Brief). Write it into the
  Brief's "The ask, tested" section, five lines:
  - **The goal behind the request.** Why the user wants this; what it serves.
  - **Limits, sorted.** Fixed (the user said, law, money, a hard dependency) and
    assumed (habit, a default, "how it's usually done"). Assumed ones are
    fair game in Phase 2.
  - **What nobody has asked yet.** The question that would change the plan.
  - **People missing from the plan.** Who uses, pays, approves, maintains or
    is affected, and isn't in the request.
  - **Who pays, and the cheapest proof they will,** before anything is built
    (a pre-order, a refundable deposit, a signed yes, a hand-run trial). For
    a tool only the user uses, the payer is the user's time: name what it saves.
  Each line carries its source label. Any line that is the user's call (money,
  people, taste, risk) goes in round two; the rest is Claude's, applied.
  The cheapest proof becomes a success measure or Phase 1 of the plan.
- A "proceed" answers with the recommended options, and each answer goes into
  `BRIEF.md` and `DECISIONS.md` marked *Claude inferred, user delegated*.
- Still fuzzy after round three? Stop asking and show a rough sketch.
- Write `buildplan/BRIEF.md` from `templates/BRIEF.md`, one page at most. Three
  to five success measures, each in the When / Checked by form and numbered
  M1, M2, ... so the trace check can find them.
- Then write `buildplan/OUTCOME.md`, the five-line outcome card (read
  `outcome-card.md`): done in the user's words, measures, out of scope, tripwires.
- **Gate A:** is the Brief right? Always one explicit yes, even after
  "proceed". The gate card leads with the outcome card, then the inferred
  answers, then the Applied line (size and why).

## Phase 2 · Explore (the solution space)

- Light research: how others solve this, two or three existing tools, what's
  current. Label each claim *Sourced* (with date), *Recalled* or *Inferred*.
  Independent topics can fan out to `sonnet-worker` helpers.
- Pitch two or three directions that differ in kind, not degree. Rank them.
  Show the strongest one you'd reject and why it lost. When the difference is
  visual or structural, add an HTML comparison board (phone-safe).
- A sketch plan for the top pick, five to eight lines.
- **Outcome check.** If research changed what success looks like, say so
  plainly, re-poll only those items, and update `BRIEF.md`.
- **Fresh reviewer, before Gate B.** One reviewer that didn't write the
  directions (`opus-reviewer`, or a fresh subagent) gets only `BRIEF.md` and
  the ranking, and attacks the ranking: which direction it would pick and
  why, what the ranking missed, which assumed limit it leans on, and whether
  the cheapest proof of demand comes early enough. Fix the ranking or say
  why not. The gate card names one line of what the reviewer changed.
- **Gate B:** pick the direction. The card opens with the outcome-card line
  and shows each direction as a real sample (`attention.md`). Log the pick and the reason in
  `DECISIONS.md`, the user's words when they give them.
