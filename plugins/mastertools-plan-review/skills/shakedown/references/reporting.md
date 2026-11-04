# Shakedown — Report Reference

Moved word for word from SKILL.md (2026-10-14): the report order, the work order format, the steelman clause, the worked work order, confidence classes in full, the Challenger handoff packet, and the anti-patterns. Load before writing the report.

## Report order, in full

Produce, in this order:

1. **Executive verdict** — five lines max: blocker count, top three risks,
   overall readiness against the stated milestone, the reproduction rate
   (Full tier), and the single most important thing to do next.
2. **Calibration block** — tier (with its shape cell verbatim), mode,
   milestone, verification ceiling, execution mode, depth budget, and a
   degraded-mode statement if the references were unreachable. A few lines.
3. **Coverage map** — deep / skimmed / not examined.
4. **Findings** — severity-tiered, each written as a **self-contained work
   order** (format below). Surface at most the top 3 Blockers, top 7 Highs,
   top 7 Mediums, top 5 Lows in the main report; overflow goes to an
   appendix with one-liners. The cap is structural nitpick-theater
   prevention — the reader must be able to see the two findings that matter.
5. **Sweep result** — what the gap-hunt added, or the one-line empty result.
6. **Punch list** — the recommended fix sequence, dependencies noted.
7. **Decisions for the human** — judgment calls, accepted-risk candidates,
   one-way doors, and anything that bends a stated parameter.
8. **Ledger append** — see Ledger in SKILL.md.

## Work order format, in full

Every surfaced finding contains all six fields. The reader may be routing
these to another agent or session verbatim — each must stand alone as a
ticket:

- **Where:** exact location (file:line, section, screen+state, message).
- **What:** the defect or gap, stated plainly, with the failure consequence —
  the cost the owner or user actually eats.
- **Severity:** Blocker / High / Medium / Low — scored as likelihood ×
  impact × exposure *against the stated milestone*. Boundaries: **Blocker** —
  the milestone fails if this ships (demo breaks, data loss, security hole,
  legal exposure). **High** — the milestone is damaged but survives; fix
  before ship if at all possible. **Medium** — real defect, tolerable for this
  milestone, fix soon after. **Low** — quality gap, no milestone impact.
- **Confidence:** Verified / Traced / Hypothesis (see below).
- **Verify:** repro steps, the failing input, or the specific contradiction —
  whatever lets someone confirm it independently.
- **Fix:** the concrete change, plus an acceptance test ("done when X") and a
  one-line **blast radius** note — what the fix touches, what to re-check
  after.

## Steelman clause

Open the findings section by naming, in two or three lines, what the build
gets right — the decisions worth keeping and the parts that are already at
the bar. Not flattery: calibration. The report should read as an ally's punch
list, not a rival's takedown. A report that's all wounds trains the reader to
stop opening it.

## Worked work order

**Worked example (Traced-class):**

- **Where:** `api/export.js:47`, the CSV export handler.
- **What:** the user-supplied `filename` param is interpolated into the
  response header without sanitization; a crafted value injects a second
  header (response-splitting).
- **Severity:** High — traced against a pilot milestone with authenticated
  users; not Blocker because it needs an authenticated session to reach.
- **Confidence:** Traced — followed the param from route to header; not
  executed in this environment.
- **Verify:** call `/export?filename=x%0d%0aSet-Cookie:evil=1` and inspect the
  response headers for the injected line.
- **Fix:** strip CR/LF and quote the filename before it reaches the header;
  done when the crafted input appears inert. Blast radius: touches only the
  export handler; re-check any other handler using the same header-building
  helper.

### Confidence classes

- **Verified** — reproduced or executed; the failure was observed.
- **Traced** — the logic was followed end to end and the defect is
  demonstrable on paper, but not executed (environment ceiling or budget).
- **Hypothesis** — plausible given what was read; the included Verify steps
  are the test. Never dress a Hypothesis as Verified; miscalibrated
  confidence is how audits burn trust.

These are the report-facing names of Phase B's verdicts: CONFIRMED arrives as
Verified or Traced, PLAUSIBLE arrives as Hypothesis, REFUTED never arrives.

## Root-cause clustering, in full

While compiling findings, cluster by underlying cause. **If three or more
High-or-above findings trace to the same design decision, stop enumerating
symptoms.** Report the cluster as a single frame-level finding, name the
design decision, and recommend a Challenger pass on that question before any
symptom-level fixes are executed. Counting deck chairs comes after the hull
is sound.

## The Challenger handoff packet

Emit the cluster as this packet, so the receiving Challenger pass starts from
the finding instead of from zero:

```
HANDOFF → challenger
- Cluster: <the repeated defect pattern, one line>
- Evidence: <2–4 finding locations that demonstrate it>
- Suspected frame assumption: <the plan-level choice producing these>
- What a re-challenge should answer: <the one question>
```

## Anti-patterns (do not do these)

- **Findings from vibes.** No location, no finding. No repro or trace, no
  Verified label.
- **Judging while finding.** "Could be a bug… probably fine" inside the FIND
  pass is the silent killer. Candidates with a nameable consequence reach the
  judge; the phases stay separate.
- **Refutation by doubt.** "Speculative," "unlikely," and "probably handled"
  are not verdicts. REFUTED quotes its evidence or the candidate survives.
- **Coverage dishonesty.** Pronouncing on the whole after reading a part.
  The coverage map is mandatory and leads the report.
- **Unstated degradation.** Running from the embedded core lists without
  saying so, or claiming Full-tier sign-off without the references.
- **Fan-out theater.** "Independent" finders that share a context, or a
  verifier confirming its own finder's candidate, launder one opinion into
  many.
- **Nitpick theater.** Fifty trivial findings burying two real ones. The
  caps and severity rubric exist for this; respect them.
- **Sweep abuse.** Skipping the sweep at Standard+ — or padding an empty one
  to look thorough. Both are the same sin in opposite directions.
- **Silent rewrites.** Shakedown reports; the human decides. Never quietly
  fix, restructure, or "improve while I was in there."
- **False confidence.** Hypothesis dressed as Verified. Label at or below
  the verification ceiling, always — and at Full tier, no Blocker ships
  unreproduced without saying the attempt failed.
- **Research theater.** Claiming "X is deprecated" or "the modern approach
  is Y" without having actually checked. Sources or silence.
- **Fashion-chasing.** Recommending churn because newer exists. The churn
  guard's three bars are the only doors in.
- **Re-litigating the ledger.** Accepted risks stay accepted unless the
  milestone moved. A nagging audit is an ignored audit.
- **Symptom enumeration past the cluster threshold.** Three High findings,
  one root cause → one frame finding + Challenger handoff, not thirty
  tickets.
- **Uniform shallow coverage.** Depth goes where risk lives. An audit that
  reads everything a little audits nothing.
