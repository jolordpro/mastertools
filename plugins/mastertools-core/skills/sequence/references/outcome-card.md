# Outcome card (Full only)

Read when Phase 1 writes the Brief, and again at every gate. The card is
`buildplan/OUTCOME.md`, from `templates/OUTCOME.md`: five lines under its
title, never more.

## Write it (end of Phase 1)

- **Done, in the user's words.** Quote them. If they haven't said it, the Gate A poll
  asks for it, with Claude's draft as the recommended option.
- **Measures.** Three to five, the same M-numbers as `BRIEF.md`, a few words
  each.
- **Out of scope.** What this build will not do, from the Brief's "Not doing".
- **Tripwires.** Each one is a fact a script or a date can check, never a
  feeling:
  - **Cost cap**: money spent, or the user's minutes on this build (see
    `attention.md`), past a set number.
  - **Date**: past it with Gate D not passed.
  - **Failed demand test**: the cheapest proof from "The ask, tested" came back
    no, or no answer by its date.
  A build with no payer but the user has no demand tripwire; write "none, the
  user's own tool" so the gap is on purpose.
- The card is most of the Gate A card. The user's yes on Gate A is their yes on it.

## Check it at every gate

The gate card gets one line, first: `Outcome card: holds` or `Outcome card:
<what moved>`. Check three things against the work in hand:
1. Every measure still has a phase that serves it.
2. Nothing out of scope got built.
3. No tripwire has tripped.

## Scope changes

Any change to the done line, a measure or the out-of-scope line is a scope
change. It needs the user's yes again, as its own poll, before work on it starts.
Log it on the card's last line and in `DECISIONS.md`. Phase 6 change control
counts: "add now" on an out-of-scope item is a scope change.

## A tripwire trips

Park the build at once, without asking:
1. Snapshot the work (a commit, branch or dated copy).
2. Set the status on BRIEF.md's first `Sequence:` line to
   `status: parked (<date>) · tripwire: <which one, in a few words>`, and the
   same on the checkpoint's first line.
3. Leave the user one line in the next message (the start hook stays quiet
   for a parked build; a daily brief can carry it, when one reads build
   status):
   "Parked <project>: <tripwire>. Say 'resume' to go on, or 'stop'."
4. Do no more work on it. Only the user's word restarts it; log that word in
   `DECISIONS.md`.
