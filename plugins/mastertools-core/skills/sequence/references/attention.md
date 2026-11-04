# The user's attention, and gates that show the work (Full only)

Read at the start of Phase 1 and again before every gate. Spend the user's minutes
where a wrong guess would cost most, and show them the work itself, never a
report about it.

## What to ask

- **No daily cap.** Ask whenever a wrong guess would be expensive to fix or
  redo: taste the user hasn't ruled on, scope, money, people, anything public or
  hard to undo, anything later work will stand on.
- **Rank before asking.** When several questions are open, ask the one whose
  wrong guess costs most first. A guess that's cheap to undo stays Claude's:
  decide it and log the undo.
- Asking more never means asking worse: one decision per poll, context first,
  the recommended option first, never a question a ruling already settled.
- **Gate cards can wait for the user.** When other work can go on
  without the gate, and the user isn't in the thread (overnight, "run to the end",
  away), write the card to `buildplan/GATE.md` with a first line
  `Gate <X> · status: open · <date>`, and keep working on what doesn't
  depend on it. The card waits for the next session here (the start hook
  names it), and for a daily brief, when one reads `GATE.md`. When the user answers, set `status: answered` and log their words.
  Work that depends on the gate waits; a one-way door always waits.
- **Track the user's time** in the checkpoint's attention line:
  `User: <minutes> min · <questions> questions · rework <n>`.
  Minutes are an estimate: about 1 per poll question, 3 per gate card, 5 per
  prototype they try, or the real gap between asking and their answer when
  it's shorter. Rework counts each time the user said, in effect, "that's not what I
  meant". The retro reports the totals: more questions with less rework is
  the trade this skill makes.

## Before every question

`<calls>` below is the decisions ledger's command, when the ledgers module
is installed (it names the command at session start). Without it, use the
fallback.

1. **Look for a settled answer first:**
   `<calls> find <the question's key words> --area <area>`
   Areas include `motion`, `design-taste`, `copy-writing`, `apps-code`,
   `files-delivery`, `process`.
   Fallback (no decisions ledger), search instead:
   `buildplan/DECISIONS.md`, the project's decision log, `~/.claude/build/LESSONS.md`
   and memory.
2. A ruling, a precedent or a past answer that fits settles it: apply it,
   name its id on the Applied line, and don't ask. A poll
   answer holds only in its own project and for 30 days.
3. Still open, and expensive to fix or redo if guessed wrong? Ask. Anything
   cheap to undo, at 90% sure or more and not seen by others, is Claude's:
   decide it and log it (below).

## Claude's own calls

- Calls cheap to undo, at 90% sure or more and not seen by others, are
  Claude's (always-on rule). Log each so the user can reverse it:
  `<calls> decide --area <area> --call "<the call, as an outcome>" --why "<one line>" --undo "<how to undo it>" --confidence <0.90-1.00>`
  It prints an S-number. Put it on the `DECISIONS.md` line. The user says
  "reverse S-<n>"; `<calls> reverse` records their words and prints the undo.
- Exit code 2: read the line it prints. "PAUSED" or "Below 90%": ask the user
  instead. "Left out" (health, family or money details): don't ask; log the
  call in the project's `DECISIONS.md` only. An `error:` line instead means a
  bad command: fix it and rerun.
- Without the decisions ledger, log the line in `DECISIONS.md` as
  `Claude decided (solo) · undo: <how>`, and list those lines on the next gate
  card as "My picks: say 'reverse <date> <call>' to undo".

## Gates show the real work

The user judges by reading the work, one piece at a time.

- **Context first, with no poll:** what the piece is, where it will live,
  what it has to do. Then the pieces. The poll comes after the user says ready.
- **Show the thing itself:**
  - images inline, labelled, two or three across;
  - real excerpts, the actual lines, ten or fewer per piece;
  - a screenshot of the running page or tool, plus its local path to open;
  - for code, the check's real output lines, never the diff.
- **Never stand-ins:** no summaries in place of the work, no scores, counts or
  codes (M2, S-3, P1.1) as the content. An id may trail a line as a
  pointer, never replace it.
- **One absolute question per piece:** "Is this the opening you want?", not
  "Rate A against B" or "Approve the 6 items?".

| Gate | Shows |
|---|---|
| A | The outcome card, the five "ask, tested" lines and the inferred answers, word for word |
| B | Each direction as a real sample: a sketch, a board image, a draft paragraph or a dry-run output |
| C | The prototype running in the user's real moment: screenshot plus the local file |
| D | The finished work, piece by piece, plus each measure's check output |
