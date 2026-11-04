# Shakedown — Modes Reference

Moved word for word from SKILL.md (2026-10-14): the ledger and handoff check, delta mode and re-verification mode. Load for any delta or re-verification run. The ledger spec itself is `references/core/ledger.md`.

## Ledger and handoff check (Calibrate step 6), in full

If a `.ledger/ledger.md` exists in the
   project (or a prior Shakedown report exists in the conversation), read it
   first. Prior findings marked `accepted-risk`, `closed`, or `deferred` are
   not re-reported unless their severity has changed under the current
   milestone — and then name what changed. Re-litigating accepted decisions
   turns the audit into a nag and gets it ignored.

   Then look for a `HANDOFF → shakedown` block, in context or beside the
   ledger. If present, adopt its milestone, audience, bar, and tier as
   defaults (owner statements still override), and treat its **watch items as
   top-priority risk concentrations** in Inventory — those are the places the
   plan's author already suspected the build would break.

## Ledger

The ledger spec (prefixes, run line, coverage line, entries, statuses, misses) is shared by all review skills: `references/core/ledger.md`.

## Delta mode

When a ledger with a run anchor exists and the ask is "what changed" or "what
broke since" — or the artifact has moved only modestly since the last full
run — audit the delta, not the world. Full audits are for milestones and
first contact; delta keeps the habit affordable in between.

Scope, from the last run line's anchor:

1. **Everything changed since the anchor** — `git diff <anchor>..HEAD` plus
   the working tree for code; revision compare or dated sections for
   documents.
2. **Open findings whose locations fall inside the changed zone** — did the
   change fix, worsen, or move them?
3. **The blast radii of fixes made since** — the adjacent things each fix
   touched, per the work orders' blast-radius notes.

Run the two-phase hunt on that scope only. The removed-behavior discipline
from `code.md` earns its keep here: for every guard, check, or promise the
delta deletes or rewrites, find where it is re-established. Sweep narrowed to
the same scope. Report with a **DELTA** label, a coverage map scoped to the
delta, and a new run line in the ledger. Severity still anchors to the
current milestone.

A delta run never discharges a full-audit obligation: if a milestone is
approaching and the last full run predates major work, say so in the verdict.

---

## Re-verification mode

When the human returns after executing fixes ("fixed SD-003 and SD-007,
re-check"), do not re-run the full audit. Instead:

1. Re-run the **Verify** steps for each fixed finding; confirm and mark
   `fixed` in the ledger.
2. Sweep the **blast radius** noted on each fix — the adjacent things the
   change touched. Low-tier fixes introduce Blocker-tier regressions more
   often than anyone admits.
3. Report a short delta: confirmed fixes, regressions found, ledger updated.
