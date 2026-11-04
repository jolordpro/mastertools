# Phases 3 and 4 · Plan and Prove

## Phase 3 · Plan

- Deep research on the chosen direction. Verify versions, prices and APIs live.
- Read again at the start of Phase 3 and of Phase 4, even after a compaction.
- **Mechanics, applied.** Claude makes each technical call, writes it as the
  outcome it sets ("built for one person a few times a week; room for a team
  later", not the tool), and lists them in `PLAN.md`. The Gate C card shows
  them as one Applied line; on "change" they become one multi-select change
  list. Calls that leave the user's lanes or can't be undone get their own question.
- Write `buildplan/PLAN.md` from `templates/PLAN.md`: two pages plus the task
  list at most. Order the phases by these rules:
  1. **Riskiest unknown first.** Spike it before building around it.
  2. **Walking skeleton next.** The thinnest path that runs end to end.
  3. **Then vertical slices.** Each slice ends usable and checked.
  4. **Dependencies before dependents. Reversible before irreversible.**
     Publishing, migrations, deletes and anything that spends money come last,
     each behind its own gate.
- Each phase carries: goal · done means · the check that could fail · size ·
  who builds it (main thread or a helper from the routing table) · effort ·
  `Delivers:` the measure numbers it serves (or `enabling`).
- Tasks fit one sitting and are written so a fresh helper with no context could
  run them: exact files, the change, the check.
- Also: top five risks, each with an early warning sign · cut list · premortem
  (it shipped and failed: the three likeliest causes and the guard for each).
- **Lanes.** Read `work-lanes.md` and write the `## Lanes` section: the pieces
  that can run side by side, who runs each, and the gate before each merges.
  Renders on a shared machine are booked through the coordinator, when there
  is one, never started here.

## Phase 4 · Prove (challenge it, then picture it)

1. Run `plan-review:challenger` (when installed; otherwise a main-thread
   challenge) on `BRIEF.md` and `PLAN.md`. It also marks which chunks go
   to helpers.
2. One red-team pass: push three to five real scenarios through the whole plan
   at once (crossing parts, conflicting goals, colliding clocks).
3. Build the cheapest prototype that tests the riskiest assumption and locks
   the experience. **Use the user's real data, staged in the real moment of use**
   (their Monday morning, their actual files, the real client). Never placeholder
   content.

   | Project | Prototype |
   |---|---|
   | App, site, dashboard | Clickable HTML click-through, phone-safe |
   | Script, pipeline, automation | Dry run on a real sample, output shown |
   | Creative-tool panel or script | Mock panel plus a persona walkthrough |
   | Document, deck, copy | Outline plus one finished section |
   | Process or workflow | Step-by-step walkthrough of one real case |

   Save every prototype as a local file in the project first. A hosted link is
   a second copy; links don't carry across accounts.
4. UX and design picks as polls with previews (`ui-design:design-taste` for UI, when installed).
5. Edge cases, ranked: which the build handles, which it defers.
6. **Trace check**, before the gate:

   ```
   python3 -I <this skill>/scripts/trace_check.py buildplan
   ```

   It maps every measure in `BRIEF.md` to a plan phase that delivers it, and
   every phase back to a measure or `enabling`. Exit 1 means an orphan on one
   side: fix it or raise it in the gate card. Paste its table into `PROVE.md`.
7. PLAN v2 with a change list, in `PLAN.md` and `PROVE.md`.
8. **Gate C, build lock.** Check the outcome card first (`outcome-card.md`).
   The card leads with the prototype running, shown as a screenshot plus its
   local file (`attention.md`), and one question:
   *"Picture <the real moment>. Would you use this?"* Then PLAN v2. From here,
   scope changes go through change control (Phase 6).
9. Explore mode ends here: the prototype and the lessons are the deliverable.
   Ship mode hands off the build to a fresh session (see SKILL.md).
