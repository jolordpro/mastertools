# Independence

Shared by challenger, shakedown and stress-test. Edit in `core/`, never in a copy.

One context that finds, judges and approves its own work launders one
opinion into a verdict. These rules keep the roles apart.

## The roles

- **Finders** hunt candidates. They are blind to each other: no finder sees
  another's list.
- **The judge** rules on each candidate from evidence only. It runs in a
  fresh context, never a finder's context, and never judges a candidate it
  produced.
- **The checker** (claim check) verifies factual claims with receipts. It did
  not write the work it checks.

## Fresh agents

- **When the author is in the session** (this session wrote or built the
  work), finding and judging go to fresh agents that never saw the build.
  This session only briefs them and collates.
- **Models, in Claude Code:** finders run on Sonnet, the judge on Opus, at
  every tier. At Full, extra Opus finders may be added; the judge then
  reports "same model as some finders."
- **The checker** runs on a different model from the author where one is
  available.

## Without helper agents

In claude.ai chat or anywhere subagents are missing, run the roles one after
another with an explicit role reset between them ("you are a second auditor
handed this list"). Write the full candidate list before the first verdict;
the written list is the firewall. The report says **"lower independence"**
in its calibration block, with why.

## Tools that exist only in Claude Code

Use them when present and skip them with a note when not: subagents, the
built-in `/code-review`, the Workflow tool. Never launch a billed or cloud
review (such as `/code-review ultra`) yourself; that is the user's to launch.
