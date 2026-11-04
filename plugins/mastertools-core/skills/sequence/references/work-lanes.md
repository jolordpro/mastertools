# Work lanes and render slots (Full only)

Read in Phase 3 when the plan is written, and again at the start of Phase 6.
Not the user's lanes of tools and stacks (that's `templates/lanes.md`): these are
the pieces of the build that can run side by side.

## The lane plan (Phase 3, a "## Lanes" section in PLAN.md)

A piece is its own lane only when all four hold: it needs no other piece's
result; no other piece needs its result first; it touches no file another
piece touches; it doesn't have to land in one change with another piece.
Everything else stays on the main thread, in order.

One line per lane:
`<lane> · <who: helper type, or its own session> · files it owns · its check · gate before merge`

- **Helper** (a subagent: `opus-builder`, `sonnet-worker`) for a piece that
  comes back inside the sitting.
- **Own session** for a piece of a sitting or more that ends in its own branch
  or file set. Propose it as a session card; it starts when the user starts it.
- **The coordinator wins.** A `COORDINATOR.md` or a coordinating session
  (for looks and QC, or for GPU and render slots) sets holds, slots and file rules. Lanes ask it; none route
  around it.

## Running lanes (Phase 6)

- Brief each lane fully: its files, its check, what done means, where it
  could go wrong, and `buildplan/OUTCOME.md`. A lane can't change scope.
- Lanes never poll the user. Their questions come to the main thread, which
  searches for a settled answer first and asks the user itself.
- **Gate each lane before it merges:** its own check passes, and a reviewer
  that didn't build it (`opus-reviewer`) passes it. Merge one lane at a time,
  then rerun the whole build's check.
- A lane that fails its gate twice comes back to the main thread.

## Renders

- Never start a render on a shared GPU yourself. Book the slot with the
  coordinator, when there is one.
- Drafts first: small draft stills for Claude's checks, full-size hero stills
  for the user. Estimate a long render's time from the draft and tell the user
  before an hours-long one.
- **A render lane's check has two parts:** the first frame lands on disk
  within the time the draft predicts, and the last frame lands. Watch for the
  first frame before reporting any render as running. No first frame in time
  means the render failed: stop it, read the log, and say so at once.
