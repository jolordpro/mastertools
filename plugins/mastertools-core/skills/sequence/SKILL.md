---
name: sequence
description: >-
  Runs a build that will take more than one sitting, from idea to finished
  work, sized to the job. Use when a thread starts a new project, product,
  app, tool, plan, study or feature (a new feature for an existing app
  counts) that will take more than one sitting ("let's build...", "I want to
  make...", "plan out a new..."), when the start hook says a build is in
  progress, or on /sequence. It sizes the job first: small jobs step aside in
  one line; Lite writes one plan card, then builds and checks; Full tests the
  ask, researches, plans, prototypes and builds through four stops, holding
  state in files that survive compaction and new sessions. Not for questions,
  explanations, single edits, one-file changes, bug fixes or compiling code
  ("full build" or "run the build" meaning compile), not for critiquing a
  plan alone (challenger), and not for auditing finished work (shakedown).
---

# Sequence

If `~/.claude/overlays/sequence/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

## Key rules (these hold at every phase, and after any compaction)

1. **Size the job first, in one line, with no poll about process.**
   "Applied: Full build, four stops. Say 'change' to see why." Just do it steps
   aside in that one line and the always-on rules carry the work.
2. **The user gets only money, people, taste and risk calls.** Size, tools, stack and
   mechanics are Claude's: apply them and show them as one "Applied:" line on
   the plan card or gate card. "Change" opens them.
3. **Context first, then the poll after the user says ready.** A stop is ten
   lines or fewer. The user never reads a whole file to approve one. One "ready" per stop:
   after it, each piece goes in chat with its one question in the same turn.
4. **The coordinator wins.** A `COORDINATOR.md` (or another process file) in the
   project or a folder above it beats this skill on holds, slots and file
   rules. Say so in one line.
5. **Label every answer's source:** *User said · Claude inferred · Claude
   decided (user delegated) · Claude proposed*. A proposal becomes the user's
   decision only when the user picks it. "Proceed" is never the user's own
   pick of an outcome.
6. **Escalate with a snapshot.** When small work gains stakes mid-way (personal
   data, money, a one-way step, more users), snapshot the work first (a commit,
   branch or dated copy), then stop and poll before writing more.
7. **Look before asking.** Search files, memory, the project and the machine
   before asking the user for anything, and settled calls in the decisions
   ledger, when the ledgers module is installed. Never poll what they answer.
8. **Files hold the state, not the conversation.** `buildplan/` plus the
   `## Now` section of `PROGRESS.md`. Each phase starts by reading its
   reference file again, even if it was read before.
9. **One-way doors, lane breaks and Gate D always stop for the user,** whatever was
   delegated. A stop never closes with an open decision.
10. **Nothing is running until its first output is seen.** A render, export,
    batch, chain or probe counts as started only when its first output lands
    and is looked at: not blank, not grey clay, the right size, inputs not
    empty. Empty output is a failure, never "nothing found". Watch for it
    before reporting any time or result.

## Size the job (Phase 0, never a stop of its own)

1. **Coordinator.** Rule 4. If it puts build files elsewhere, follow it and say
   in one line that the start hook won't see them there.
2. **Resume.** A `buildplan/` folder holding `CARD.md` or `BRIEF.md` means
   resume, not restart: read it and `PROGRESS.md` `## Now`, open with one line
   ("Resuming Full build at Phase 3 · Plan."), and re-ask nothing a stop
   approved. A `build/` folder is some tool's output, never build state.
3. **Reuse.** Search past parts before planning anything new: one quick search
   of the project and its siblings, said in one line.
4. **Pick the size.** The first row that fits wins.

| Size | When | What happens |
|---|---|---|
| Full | Any one: money, sign-in, personal data or public reputation at stake · a step can't be undone · more than about two sittings · other people use it and it's more than one sitting | Test the ask, research, plan, prove, build. Four stops (Gates A–D). |
| Lite | Up to about two sittings, low stakes; or one sitting that other people will use | Plan card, build, a check that can fail. One stop at most. |
| Just do it | Fits in one sitting, can be undone, nobody outside sees it | One line, then the work, under the always-on rules. No files. |

   - Lite that others will use adds a **pre-handover check**
     (`plan-review:shakedown` when installed; for creative-tool scripts and
     panels, also a walkthrough as real users would run it).
   - Novelty and taste never force Full alone; taste adds a quick prototype
     to Lite.
   - Explore mode (only the user uses it, the lessons are the point): Lite, or Full
     that ends after Phase 4 with the prototype as the deliverable.
5. **Say it in one line** (rule 1): the size, the stops, the signal in a few
   words. "Applied: Lite build, one plan card. Say 'change' to see why."
   "Applied: Just do it (one sitting, undoable). Say 'sequence' to plan it."
   On "change", show the signals and offer the other sizes as one poll.

### Commands

- `/sequence <idea>` sizes the job. `/sequence lite|full <idea>` sets the size
  (coordinator, resume and reuse still run).
- Any time: `status` (size, phase, last stop, open decisions) · `go lite` ·
  `go full` · `back to <phase>` (voids every later gate, said in one line) ·
  `run to the end`.
- **"Proceed"** answers an open poll with the recommended options and approves
  the current stop. In Phase 1 it records the answers as *Claude inferred, user
  delegated*, and Gate A still needs one explicit yes after the playback.
- **"Run to the end"** lets Claude make the calls from Gate B through Gate C,
  each logged as *Claude decided (user delegated)*, with the scope written in the
  checkpoint. Rule 9 still holds.

## Just do it

One line (rule 1), then the work. No `buildplan/`, no card, no checkpoint.
If the work grows past the row mid-way, rule 6: snapshot, then size it again.

## Lite (alignment in under five minutes)

Read `references/templates/CARD.md` first.

- **L1 Align.** At most one question in all, and only a
  money, people, taste or risk call where a wrong guess costs more than
  redoing the build. Often none.
- **L2 Plan card.** Write `buildplan/CARD.md` and show it: outcome · steps · not
  doing · the check that proves it works · Applied line · status. Every guess
  is on the card, so a wrong one is caught at a glance. The user's go ends it; a
  "proceed" in the request counts.
- **L3 Build.** Then run the check. It must be able to fail: name what a broken
  result looks like and why the check would catch it.
- **L4 Close.** What changed, the check result, Next steps. Mark the card
  `status: done`.
- **Escalate** the moment the work meets the Full row (rule 6):
  1. snapshot the work so far;
  2. name the signal in one line, and poll *Switch to Full · Stay Lite*;
  3. on a switch, write `buildplan/BRIEF.md` from the card, listing every file
     already touched, and poll only the gaps;
  4. Phase 5 marks each touched file keep, rework or revert. Never restart.

## Full

Each phase opens with one status line: name, goal, what ends it. Between stops,
work without stopping. **Read the phase's reference file when the phase starts,
every time, never before.**

| Phase | Ends with | Read (in `references/`) |
|---|---|---|
| 1 · Align | reuse, past lessons, test the ask, `BRIEF.md`, `OUTCOME.md` · **Gate A:** is the Brief right? | `align-explore.md`, `attention.md`, `outcome-card.md`, `retro.md` |
| 2 · Explore | ranked directions, a fresh reviewer's attack · **Gate B:** pick one | `align-explore.md` |
| 3 · Plan | `PLAN.md` with lanes, mechanics applied as outcomes | `plan-prove.md`, `work-lanes.md` |
| 4 · Prove | prototype, trace check, PLAN v2 · **Gate C:** build lock | `plan-prove.md` |
| 5 · Foundation | walking skeleton whose check fails when broken | `build-verify.md` |
| 6 · Build | every lane and slice built, checked and gated | `build-verify.md`, `work-lanes.md` |
| 7 · Verify | every Brief measure graded · **Gate D:** the user accepts | `build-verify.md` |
| 8 · Ship and learn | delivery note, five-line `RETRO.md`, a ledger lesson, build-log line | `build-verify.md`, `retro.md` |

Before every gate, read `attention.md` and `outcome-card.md` again, then
confirm each line of the gate check. Any "no" is fixed before the card goes out:

1. The outcome card still holds, or the change has its own poll.
2. Each question was searched for a settled answer first.
3. Only the user's kind of call is left; the rest is applied and logged with its undo.
4. Every open question that would be expensive to redo is on the card; cheap ones were decided and logged.
5. The card shows the work itself: images, real excerpts, a screenshot, check output.
6. Every job started since the last gate showed its first output, and it was checked.
7. Nothing the user approved has changed without their word.
8. What this stage taught is in the project's `LESSONS.md`, each lesson with its enforcer.

In Full, ask whatever would be expensive to fix or redo if guessed wrong (no
daily cap); when the user is away, a gate can wait in
`buildplan/GATE.md` while other work goes on. It waits for the next session
here (and a daily brief, when one reads `GATE.md`). A tripped
tripwire (cost, date, failed demand test) parks the build without asking.

**Gate card** (ten lines or fewer, then the work itself: images inline,
real excerpts, a screenshot of the running page; never a summary or codes in
its place; the poll comes after the user says ready):

```
Gate <X> · <what the user is approving>
Outcome card: holds | <what moved>
Calls inside it: 1) ... 2) ... 3) ...   (one to three, the user's kind only)
Applied: <size and mechanics, as outcomes>. Say "change" to see them.
If no: <what changes>
Full file: buildplan/<FILE>.md
Say "ready" for the poll.
```

Where the surface can't wait for "ready" (an eval, a helper, "run to the end"),
show the card and the poll together.

**Hand off after Gate C.** Update the checkpoint, then start a fresh session at
medium effort whose whole brief is "Continue the build from `buildplan/`."
Where this surface can't start sessions, give the user that line to paste into a new
one. If the fresh session has to ask anything a gate settled, log it in
`DECISIONS.md` as a state-file miss and fix the template, not only the answer.

## Polls

- One to four questions per call, two to four options each, header twelve
  characters or fewer. `multiSelect` only for change lists and non-exclusive
  picks.
- The recommended option is first, its label ends "(Recommended)", and its
  description gives the why in one line. Other options say what they gain and
  what they give up. `preview` when options are visual or structural, never
  for a passage the user has to read (send that in chat first).
- Phase 1 asks outcomes, never tech, unless the outcome itself is technical.
  Ask "how many people will use it", never "which backend".
- **Change list** (only when the user says "change" on an Applied line, Phase 3 on):
  one multi-select poll of the applied calls, each written as the outcome it
  sets ("Built for one person a few times a week; room for a team later", not
  "SQLite"). Every option is already applied. The first option is "Keep all
  as applied (Recommended)"; the user ticks it, or what to change.
- Never ask "should I proceed?" outside a stop.
- **No AskUserQuestion** (a helper, an eval run, a surface without it): append
  the poll to `buildplan/polls.jsonl` as one JSON line, `{"phase": "<0-8 or
  L1-L4>", "kind": "poll|gate|veto|escalate", "questions": [<the exact
  AskUserQuestion questions array>]}`, show it as a numbered list with the
  recommendation marked, and stop for the answer.

## State on disk

- Folder: `buildplan/` in the project, never `build/`. Files: `CARD.md` (Lite) ·
  `OUTCOME.md` · `BRIEF.md` · `PLAN.md` (versioned) · `PROVE.md` ·
  `DECISIONS.md` (decision-log form, sources apart) · `GATE.md` (a gate waiting
  for the user) · `RETRO.md` · `polls.jsonl` (fallback only). Templates are in
  `references/templates/`.
- **The build's status lives in `buildplan/`:** the `status:` field on the
  first `Sequence:` line of `BRIEF.md` (Full) or `CARD.md` (Lite): `building`,
  `done (<date>)` or `parked (<date>) · tripwire: <which>`. Parked holds the
  build until the user's word.
- **The checkpoint is the `## Now` section of the project's `PROGRESS.md`.**
  During a Full build its first line is `Sequence: Full · Phase <n> · <name> ·
  last gate <X> (<date>)`; the rest follows `references/templates/NOW.md`.
- This plugin's start hook finds an open build (status planned or building) from
  the project or any folder below it and prints "A build is in progress here.
  Use Skill(sequence) to resume it." with the checkpoint, plus any gate card
  open in `GATE.md`. Done, parked or no status: it prints nothing. Load this
  skill when you see it.
- At every stop: update the checkpoint and add one dated line to
  `DECISIONS.md`. A `handoff` at any moment is then cheap.

## Other skills and helpers

Sequence calls these at the right moment and never copies them. When one is
missing, the fallback runs and is said in one line.

| When | Use | If missing |
|---|---|---|
| Phase 0, Phase 1 | a quick search of the project and its siblings | none needed |
| Phase 1 | the domain's kit (After Effects: `after-effects:after-effects-engineering`) | one line, go on |
| Renders | the coordinator's slot booking, when the project has one (rule 4) | none: never start a render on a shared GPU unbooked |
| Phase 2, before Gate B | a fresh reviewer (`opus-reviewer`) that didn't write the directions | a fresh general subagent given only the Brief and the ranking |
| Phases 2, 4 (UI) | `ui-design:design-taste` | the user's taste notes in the Brief |
| Phase 4 | `plan-review:challenger` on BRIEF and PLAN | main-thread challenge |
| Phase 4 red team | one main-thread red-team pass | none needed |
| Pre-handover, Phase 7 | `plan-review:shakedown`; creative tools: also a real-user walkthrough | one main-thread audit pass |
| Any moment | `threads:handoff` | the checkpoint plus `buildplan/` |
| Helpers | the routing rules' table (`opus-builder`, `sonnet-worker`, `opus-reviewer`) | main thread or a general subagent |

- Effort per phase comes from the routing rules. A session can't change its
  own effort, so name the right level in one line at each phase change.
- Domain skills load in their own right during build phases.

## User defaults

These apply wherever the user's always-on rules are loaded.

- **Lanes:** `~/.claude/build/lanes.md` (the user's preferred tools, stacks,
  hosting, formats, look). It is a standing rule file, so changes go through
  the user's rule-change process if their profile or CLAUDE.md names one;
  otherwise straight to the user. If it's missing, draft it from
  `references/templates/lanes.md` (only what the user has stated, a source on
  every line) inside `buildplan/`, and ask to install it that way. Until
  then, the draft guides this build. Leaving a lane is a **lane break**: its own poll
  before building.
- **Changes to this skill** (the RETRO's proposed edit, the two-"no" review)
  go the same way, one line each, never straight into the skill.
- **Copy passes** for documents and site copy: `writing:copywriting` and
  `writing:tighten` when installed, plus `career:motion-evidence-audit` for
  portfolio and case-study work.
- Boards and prototypes are phone-safe. Proofs go one at a time, one poll each.
- **When the user judges work** (any size): a context message first, with no
  poll; then the work itself, one piece at a time, with one plain question per
  piece. No codes, counts or summaries in its place. A passage to read goes in chat, never in a poll
  preview.
- **Approved is locked.** A check that fails on something the user approved raises a
  flag on the next card; it never changes the approved piece by itself.
- **When the user asks to change a look or draft** they liked: their words are
  the target and the approved version is the anchor. Move about a third of the
  gap per draft, check each draft against their words line by line before
  showing it, and treat any metric or bar as a check, not the goal.
- Suggest `/compact` after Gate D.
- **Lessons:** each build logs lessons at every gate in the project's
  `LESSONS.md`, each with its enforcer. The
  retro promotes at most one to `~/.claude/build/LESSONS.md`, append only.
  Phase 1 of the next build greps both (`references/retro.md`).
- **Build log:** `~/.claude/build/LOG.md`, one line per finished build:
  `date · project · size · rework count · the user's verdict`. Two "no"
  verdicts in a row: stop and review this skill with the user before the next
  build.
