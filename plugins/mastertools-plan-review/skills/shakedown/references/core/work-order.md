# Work orders

Shared by challenger, shakedown and stress-test. Edit in `core/`, never in a copy.

Every surfaced finding is a self-contained ticket. The reader may route it
to another agent or session verbatim, so each stands alone.

## Fields, every finding

- **Where** — exact location: `file:line`, section and paragraph, screen and
  state, control and panel state, or message.
- **What** — the defect, stated plainly, with the failure consequence the
  owner or user eats.
- **Severity** — Blocker / High / Medium / Low (`severity.md`), with the
  score or condition shown.
- **Confidence** — a rung of the ladder (`evidence.md`).
- **Verify** — repro steps, the failing input, or the contradiction:
  whatever lets someone confirm it independently.
- **Fix** — the concrete change and a "done when" test. Copy fixes give the
  exact new text; layout fixes give the exact move.
- **Blast radius** — what the fix touches and what to re-check after.

## Tool lane adds

Stress Test's tool lane adds **Who hits it** (personas, and the everyday
suite if it applies), **Repro** (fixture, selection, steps), **Expected**
(what a pro expects, with its oracle) and **Actual** (what happened, with
screenshot references).

## Enhancements

An Enhancement carries **Effort** and **Value** instead of Severity, and
names the concrete move, never "improve X."
