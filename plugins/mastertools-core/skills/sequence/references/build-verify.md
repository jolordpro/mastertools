# Phases 5 to 8 · Foundation, Build, Verify, Ship

A fresh build session starts here. Read `buildplan/` and the checkpoint, then
build. Ask nothing a gate settled; a needed answer missing from the files is a
state-file miss (log it in `DECISIONS.md`). Read this file again at the start
of each phase from 5 to 8, even after a compaction.

## Phase 5 · Foundation

- Build the walking skeleton with real wiring, end to end. For non-code builds,
  the skeleton is the full structure with every part stubbed.
- Files touched before an escalation from Lite: mark each keep, rework or revert.
- **Leave room, don't build rooms.** Name the two or three likeliest growth
  paths (more users, more data, features parked for later) and leave a clear
  seam for each. Build none of them now.
- Usability: simple defaults, power revealed as needed, error states designed
  on purpose.
- **Lanes.** Follow the user's lanes. When a better route exists, raise a lane break
  before building: the lane · the recommended route · why · what staying costs.
  Poll it. Never depart silently.
- Put the check in place on day one, by project type:

  | Project | The check that could fail |
  |---|---|
  | Code | Tests run, and one fails when the code is broken on purpose |
  | Creative-tool panel or script | The domain skill's QC gate, run in the host app |
  | Pipeline or data | A known-answer sample that must match |
  | Document, deck, copy | Each Brief measure tested on the draft, plus the copy passes |
  | Process or workflow | One real case walked through, every step logged |

- Exit: the skeleton runs end to end, and its check fails when broken on
  purpose. One gate check at high effort here (say so in one line).

## Phase 6 · Build

- Read `work-lanes.md` again. Run the lanes from PLAN v2; gate each before it
  merges.
- Re-verify any Sourced fact older than seven days before building on it.
- Slice by slice from PLAN v2: build → run its check → update the checkpoint,
  including the attention line, and check the tripwires. A tripped tripwire
  parks the build (`outcome-card.md`).
- Fan independent chunks to helpers. Route high-stakes slices (sign-in, data,
  money, migrations) through `opus-reviewer`.
- Keep going until the plan is done. Stop only when blocked, for a lane break,
  for the user's decision, or for a finding that changes the plan or the outcome.
  Raise that last one at once.
- **Change control.** New ideas wait for the end of the slice, then go out
  together in one poll: *add now · add to Later · drop*. Anything that raises
  the cost of fixing later is raised at once instead.

## Phase 7 · Verify

- Grade every success measure in `BRIEF.md` with its named check. A measure
  without a passing check is not met.
- Run `plan-review:shakedown` on the built artifact (when installed;
  otherwise one main-thread audit pass); for creative tools, also a persona
  walkthrough in the host app. One gate check at high effort.
- **A fresh reader** that wasn't told of any earlier finding reads or uses
  the finished work the way the user will meet it (the pages, the frames, the
  panel), not the reports about it. Counts like "320 checks passed" never
  stand for "it's right".
- Fix the must-fix items. List worth-doing items apart.
- Show the user only what needs their ruling, one proof at a time: the work itself,
  piece by piece, with each measure's check output (`attention.md`).
- **Gate D:** the user accepts. The card opens with the outcome-card line.

## Phase 8 · Ship and learn

- Deliver: where it lives, how to run it, how to undo it.
- Read `retro.md`. Write `buildplan/RETRO.md`, five lines or fewer: rework
  after build lock (each time the user said, in effect, "that's not what I meant"),
  the user's minutes and questions, what worked, one lesson with its enforcer, and
  one proposed edit to this skill. Promote at most one lesson from the
  project's LESSONS.md to `~/.claude/build/LESSONS.md` (`retro.md`).
- One poll: *Was this build better than it would have been without sequence?*
  Show Claude's rework count so the user can correct it; a self-count runs low.
- Write the build-log line with the user's verdict and the confirmed count. Set
  BRIEF.md's `Sequence:` line to `status: done (<date>)`, and the checkpoint's
  first line to `Sequence: done (<date>)`.
