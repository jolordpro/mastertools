# design-taste: roadmap

Future updates, with the evidence behind each. Not loaded by the skill; read it when planning the next version.
Written after v0.7. Each user's own grading notes and round data sit in their evidence folder, not here.

## Rules that hold for every update
- No edits to the user's `taste-profile.md` while a round is locked and unscored (`score_round.py DT round-N` first).
- Made-up products only in tests and rounds.
- Every fix ships with a test that fails on the old text or script.
- A session keeps the skill text it started with. Test each version in a new session, and check `VERSION` first.
- Improve mode proposes; the user approves every profile edit.

## v0.8: fixes from a real-project run
Source: a run of the full loop on a personal finance app's home and goals screens.

1. **The judge must stay blind to the user's words.** One run handed the judge the user's correction quote, so its "this answers the note" wasn't independent.
   - Fix: judge.md says a correction goes in the brief line as a requirement ("more polish, no clutter"), never as a quote. Check the quote in the reply step instead.
   - Test: one run with a correction; the judge prompt must contain no quoted words.
2. **Fix every option before ranking.** Only the top pick got its judge fix, so the third option was graded unfinished and looked worse than it was.
   - Fix: apply each option's one fix, recheck, then judge again. Costs one rebuild per option.
3. **Every mark on screen says what it means.** The winning option had coloured month dots with no key. They read as decoration.
   - Fix: judge.md adds "a mark that needs a key you can't see is a fix." Possible check.mjs heuristic: small coloured shapes repeated with no nearby text label.
4. **`--dial` optional on corrections.** `log_choice.py` requires it, so the logging session invented one.
5. **Don't cite rules from another job.** The judge cited a homepage rule on an app screen. judge.md: cite only the rule rows for this job, plus the every-page rules.

## Untested since v0.6 (need a fresh brief in a new session)
- The Proven rule on a brand-new brief (leave Proven out when its fix would turn it into another option).
- The same-screen rule, comma rule ids and the dashboard job row coming from the text, not session memory.
- The VERSION guard on the desktop app (folder overwritten in place). It cannot fire for an old terminal session, which keeps one cache folder per version.

## Where the skill runs, and gaps
- Code tab: the full loop (screenshots, judge agent, logs).
- claude.ai chat (uploaded zip): designs and judges, but cannot reach the evidence folder (nothing logged) and check.mjs needs Chrome. Re-upload on each version and replace the old upload, so there is one copy.
- Idea: in chat, print the log line the user would paste into a Code session, so chat picks still count.

## Beyond design-taste: a UX studio
Goal: Claude excellent at UX and UI end to end: flows, direction, components, layouts, critique. design-taste is the taste layer; these are the other parts.

**Critique engine (next).** A blind bench of planted problems:

| Set | Claude critic | Impeccable (rule scanner) |
|---|---|---|
| 1: 20 plain problems, 30 pages | 17/20 | 8/20 |
| 2: 19 subtle problems, 30 pages | 12/19 | 5/19 |

- Both missed small tap targets and vague link text, twice. check.mjs now covers tap targets (v0.7); link text is still open.
- False alarms on clean pages, graded blind: wrong 26% for Claude (7 of 13 were complaints about placeholder images), 7% for Impeccable. Valid about a third for both.
- Impeccable works only through a browser URL (`detect <url> --viewport 1280x800|390x844`); file mode gave 46 false contrast alarms. It misses dot-separated meta text and small monospace labels.
- Plan: Impeccable checks + Claude critique + tap-target and link-text checks. The critic cites the HTML or screenshot, ignores placeholder images, ranks findings (top 5 first). Target: 15+/19 on set 2 and under 10% wrong.
- A human check of about 20 findings would settle "Claude judged Claude".

**Next parts after the critic.**
- Flows: multi-screen journeys judged as a whole (steps to done, dead ends), not screen by screen.
- Components and systems: tokens and a small component set per project, so options share one system and only the layout varies.
- States: empty, loading, error and success for every option, checked like layout.
- Copy in UI: link text, button verbs, labels, scored with the critic.

## Lessons from building it
- Batch file reads in zsh with `echo =====` drop files silently (`=word` is a command lookup). Read each file on its own.
- A green log line is not proof a step ran: logging was "on" for days before the first line was ever written.
- When the skill moves or is copied, compare files byte for byte against the newest branch, not against main.
- Two sessions should never write the same skill branch. One owns it; the other sends a change list.
