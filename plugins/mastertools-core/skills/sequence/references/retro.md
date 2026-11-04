# Retro and the lessons ledger (Full only)

Read in Phase 1 (before building) and in Phase 8 (after Gate D, or when a build
parks or stops).

## Log lessons at every gate

Each build keeps its own `LESSONS.md` in the project. Every gate ends by adding what that stage taught:
one line plus why, each with its enforcer (a check, a tool, a skill section or
a memory). A lane adds to it in the same turn it learns something.

## Read before building (Phase 1)

Always search both ledgers for this area:
`grep -i "<area or key word>" ~/.claude/build/LESSONS.md <project>/LESSONS.md`.
Apply each matching lesson's enforcer in
the plan, and list them in the Brief under "Lessons applied", one line each.
None found: say so in one line.

## Write the retro (Phase 8)

`buildplan/RETRO.md` is five lines or fewer:

```
Rework after build lock: <count, each in a few words> · User checked the count: yes | <their number>
User's attention: <minutes> min · <questions> questions · rework <n>
Worked: <one thing to keep>
Lesson: <what went wrong or slow> · Enforcer: <the check, template line or rule that stops it next time>
Skill edit proposed: <one edit, or none>   (goes through the user's rule-change process, never straight into the skill)
```

Then promote at most one lesson from the project's `LESSONS.md` to the shared
ledger, `~/.claude/build/LESSONS.md`, in this form:

```
### D-<next number> · <date> · <area>: <lesson in a few words>
<project> · <what happened, one line> · Enforcer: <the enforcer> · User: "<their words, when given>"
```

- One promoted lesson per build at most; a build with nothing to learn promotes none.
- Every lesson carries an enforcer. A lesson without one is a wish: leave it
  out.
- The area word comes from the list in `attention.md`, so the next build in
  the area finds it.
- The ledger is a log, like the build log: append only. A lesson that changes
  a rule or this skill goes through the user's rule-change process as well
  (the one their profile or CLAUDE.md names; otherwise straight to the user).
