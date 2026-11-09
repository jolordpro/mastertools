# Governance: versioning, contribution, deprecation, changelog

Governance exists to catch high-impact drift while letting practitioners move quickly. It is not a committee
that approves every animation (KB-C 126). Motion systems age like APIs: a one-frame duration change can alter the
perceived character of dozens of experiences, so versioning has to track *perceptual* compatibility, not only
code compatibility (KB-C 125).

## Contents
1. Lifecycle
2. Semver rules for motion
3. Change control: four questions
4. Contribution template
5. Exception record (with expiry)
6. Review levels and decision rights
7. Deprecation and migration procedure
8. Changelog format
9. Cadence and health metrics
10. Motion debt and entropy
11. Solo and portfolio-scale governance
12. Roadmap: an investment mix
13. After handoff

## 1. Lifecycle
```
PROPOSED -> EXPERIMENTAL -> ACTIVE -> PREFERRED -> DEPRECATED -> RETIRED
```
- PROPOSED: hypothesis, no adoption evidence. Not usable in production.
- EXPERIMENTAL: limited pilot; semantics may change without a major version.
- ACTIVE: approved, documented, supported.
- PREFERRED: the recommended implementation for a class of problem (optional step; use it when two ACTIVE tokens overlap).
- DEPRECATED: no new usage; `replacedBy` and migration note required.
- RETIRED: removed after migration or explicit sunset date.
Why the middle states: they stop every successful experiment from silently becoming permanent infrastructure
(KB-C Part XXVII).

## 2. Semver rules for motion
| Change | Bump | Why / response |
|---|---|---|
| Docs clarification, new example, typo | PATCH | no behavior change |
| New token, new verb, new optional parameter | MINOR | additive; run the four questions first |
| Value refinement judged perceptually safe (e.g. 200 -> 190ms on a utility token, curve nudged) | PATCH or MINOR with note | but see next row |
| Duration change on a high-use token, any easing change, any spring parameter change | **MAJOR for the token** (or MINOR with a perceptual-impact review and sign-off if inside a declared tolerance) | duration shifts perceived responsiveness; easing shifts perceived weight; springs shift settle and interruption behavior. Test high-use components and signature patterns |
| Semantic rename | MINOR (alias) then MAJOR at removal | alias + deprecate + migrate |
| Pattern behavior change (state graph, choreography order, interruption policy) | MAJOR for the pattern | changes learned behavior and hierarchy |
| Reduced-motion strategy change | MAJOR + accessibility review | changes the accessible experience |
| Runtime/platform mapping change | adapter version bump | validate semantic equivalence across targets |

Declare a **tolerance** in the governance doc (e.g. +-10% duration, +-0.02 on curve control points on
tokens tagged utility). Changes inside tolerance may ship as PATCH with a changelog line; outside it they are
breaking. The point is that "behaviorally significant" is decided by a written rule, not by whoever is editing.
Version the artifacts separately: token file, each pattern contract, each toolkit, each platform adapter.

## 3. Change control: four questions (CMP C21.01)
**Diagnose before proposing (DR 5.1-5.2).** Collect several examples, not the first complaint. Cluster them by
user impact, team friction, technical cause and organizational cause. Separate the symptom from the root cause,
the constraint and the policy choice. Cost the status quo (user friction, duplicated work, inconsistency,
accessibility risk, maintenance). Pick the smallest intervention that changes the pattern at its source, and check
the diagnosis with the people who live with the problem. The skill is naming the mechanism that produces the
inconsistency, not noticing it.

**Evidence ladder for a proposal (KB-S 18.2).** Expert review, then a task-based prototype in a real workflow,
then a controlled comparison (A/B or timed task), then production telemetry (adoption, defects, performance,
recurring exceptions), then longitudinal review (is it still coherent a year on). State which rung a proposal
stands on. Higher reach and lower reversibility need a higher rung.

Every new behavior must answer: (1) Why does the existing system fail here? (2) What semantic value does the new
behavior add? (3) Can an existing behavior be parameterized instead? (4) How will it affect existing outputs?
This is API design review for motion. Most proposals die at question 3, which is the point.

## 4. Contribution template (KB-C 126.1, extended with evidence from KB-S 14.3)
```markdown
# Motion change proposal: {{title}}
1. Problem / user need:
2. Existing behavior considered (and why it does not fit):
3. Why existing behavior is insufficient (evidence, screenshots, usage data):
4. Proposed semantic role:
5. Proposed token or pattern (IDs, values only after roles are agreed):
6. Invariant behavior:
7. Allowed variation (ranges):
8. Reduced-motion and instant behavior:
9. Runtime targets and platform mappings:
10. Performance class and considerations:
11. Example implementation(s) or prototype:
12. Evidence (research, critique, A/B, stress-test results):
13. Migration impact (what existing outputs change, perceptual description):
14. Proposed status (PROPOSED/EXPERIMENTAL), owner, review date:
15. Decision owner (who decides, from the decision-rights table in section 6):
16. Criteria, agreed before options are compared:
17. Evidence split: facts / assumptions / preferences:
18. Reversibility: two-way (cheap to undo) or one-way (migration, learned behavior, public brand):
```
Intake outcomes: accepted as experimental / needs evidence / parameterize existing / **declined, with a local
path** (name the local variant or override the team may use, inside guardrails) / rejected with reason. Decline
before engineering starts. Keep the contribution path cheaper than the workaround: if filing a proposal costs more
than forking locally, teams will fork (DR 9.3, 10.4). Many disputes are ownership or sequencing problems, not
quality problems; settle the owner and the criteria first (DR 6.2).
Record the decision in `decision-log/` with the date and rationale; a rejected proposal with its reason prevents re-litigation.

## 5. Exception record (with expiry)
A good system allows principled exceptions and makes divergence visible, justified, and reviewable
(KB-S 14.4, 25.5). Exceptions must expire or be promoted; otherwise they are permanent debt.
```yaml
exception: EXC-2026-014
title: Lower-third uses overshoot on a Utility-tier move
requested_by: show-graphics
approved_by: motion-system-owner
type: brand-expression          # perceptual-mismatch | platform-mismatch | brand-expression | accessibility-adaptation | performance-constraint | experimental
rule_broken: "No overshoot on utility motion"
rationale: "Season finale needs added punch; scoped to one episode package."
evidence: prototype-link, reviewer-notes
scope: "Finale package only, 6 comps, no reuse"
reduced_motion: "Overshoot removed; fade + position snap"
created: 2026-10-04
expires: 2026-12-31             # required
on_expiry: revert              # revert | promote-to-experimental | renew-with-justification
status: approved
```
Review exceptions on a cadence; cluster them. Many exceptions of the same type are evidence the system is too
rigid or too generic and should change (KB-C 128.1 "exception rate").

## 6. Review levels and decision rights (KB-C 126)
| Artifact | Default review | Why |
|---|---|---|
| Primitive token | system owner + engineering validation | low semantic complexity, broad blast radius |
| Semantic token | motion-system review | defines organizational vocabulary |
| Reusable behavior / pattern | motion + product/UX review | affects multiple experiences |
| Brand signature | brand + motion leadership | high identity value |
| New runtime or tool | engineering + motion systems | platform dependency |
| One-off campaign | project-level review | local unless promoted |
| Accessibility exception | accessibility + motion owner | high user impact |

Roles (KB-C 137.1): motion system lead (language, semantics, quality), design systems lead (contracts,
integration), engineering lead (runtime, performance), brand design lead (distinctiveness, signature),
creative technology (tools, generators), accessibility partner (policy, exceptions), product teams (application
and feedback). Model: hybrid is the most common among well-adopted systems (central foundations, distributed
contribution) (KB-S 14.2).

**Ownership by layer (KB-S 26.4, DOS 4.7).** Component motion belongs to the component system. Screen-level
choreography belongs to the page or product pattern. Global navigation behavior belongs to the system layer.
Ambiguous ownership creates competing rules. Write a **scope boundary** into the system doc: what the system owns,
and what it deliberately leaves to product teams or campaigns. A system can govern component semantics without
owning the whole experience.

**Routing by reach, urgency and reversibility (DR 13.2).** The artifact table above sets the reviewer; these
inputs set the lane.

| Lane | Example | Owner | Pace |
|---|---|---|---|
| Foundation / brand | thesis, signature verb, core curve family | system + brand leadership | scheduled review |
| Cross-product pattern | a shared transition or loading behavior | system + affected teams | biweekly or monthly |
| Local variant | one product's override inside guardrails | product team | as needed, logged |
| Emergency defect | flash risk, broken reduced motion, a regression on air | domain owner | immediate; review after |
| Deprecation / migration | retiring a verb or token | system, as a planned program | section 7 |

Tighter ownership for global reach; faster lanes for local, reversible changes.

**Operating models (KB-S 14.2).** Centralized: high coherence and fast policy, risk of bottleneck and weak local
ownership; fits early or small systems. Federated: broad contribution, risk of drift and unclear decisions; needs a
strong governance culture. Hybrid: central foundations, distributed contribution; needs clear roles and
communication.

**Governance failure modes (KB-S 14.5).** Check for each on the quarterly review:
- Central bureaucracy: every small change needs an expensive committee.
- Invisible ownership: teams don't know who answers or approves.
- Unbounded contribution: patterns ship without semantic review, so the system fragments.
- Local optimization: teams solve their own case with custom motion and never feed it back.
- Frozen authority: the system adapts too slowly, so teams route around it.
- No exception path: teams fork quietly instead of asking (section 5 exists to prevent this).

**New tool gate (DOS 33.3).** Before the "New runtime or tool" row applies, the tool has to earn building. Build
when the task repeats, inputs are structured, outputs stay inside known bounds, manual work is expensive and the
variation can be parameterized. Do not build when the work is bespoke, inputs can't be standardized, exploration
is still the goal, or the tool would constrain more than it speeds up. Name a maintenance owner before the first
release.

**Generated variants (CMP C20, C37.06).** When a generator or AI produces variants, the governed asset is the
selection and rejection criteria, written so someone other than the author can apply them: curated exemplars, the
reasons a variant is rejected, and a deterministic check where one exists. Without them, variation drifts to
the average.

## 7. Deprecation and migration procedure
1. Mark `status: deprecated`, set `$deprecated`, add `replacedBy`. Keep the old token as an alias for at least one minor cycle.
2. Write the **perceptual** migration note: what will feel different (faster, heavier, less overshoot), where the old behavior is still appropriate, whether choreography needs retuning (KB-S 15.4).
3. Add a lint rule or codemod that flags the old ID; announce in the changelog.
4. Track migration completion (count of remaining usages). Set a sunset date.
5. At the date, mark `retired`; the validator will error if an active token still references it.
Also circulate the update through templates: orphaned toolkits (old MOGRTs, stale Lottie) are the most common way
retired behavior survives (KB-C 138).

**Migration as a change program (MKB4, change management).** For anything larger than a token rename:
inventory the patterns in use, one-offs included; group them by intent, not appearance; define the new semantic
model; map old to new; name the true exceptions; pilot with one or two teams and measure friction; publish docs and
examples; classify each change as breaking or not; announce early and hold office hours; deprecate with a
compatibility window; then audit production for drift.

**Behaviors retire too (DOS 9.3, 14.3).** A system defines when motion disappears, not only when it appears.
Give each behavior a "stop using when" condition tied to measured harm (it confuses, slows reversal, starts
unintentionally). When evidence shows harm, constrain or deprecate the behavior through this same procedure.

## 8. Changelog format
Keep `releases/CHANGELOG.md`, newest first; each entry names the artifact and the *felt* change.
```markdown
## 2.0.0 - 2026-11-02
### Breaking
- semantic.verb.reveal: duration medium 300ms -> 240ms, easing enter tuned. Feels snappier; dialogs and toasts affected. Migration: none required; review signature opens. (PR-45)
### Added
- semantic.verb.confirm (EXPERIMENTAL)
### Deprecated
- semantic.fast -> use semantic.duration.micro. Sunset 2027-01-15.
### Accessibility
- Reduced strategy for shift changed from fade to reduce-amplitude. Reviewed by A11y 2026-10-28.
### Notes
- Tolerance policy unchanged (+-10% duration on utility tokens).
```

## 9. Cadence and health metrics (KB-S 35, KB-C 128.1)
Weekly: triage questions, exceptions, QA defects. Biweekly: review contributions. Monthly: adoption and quality
review. Quarterly: taxonomy/token review and debt reduction. Semiannual: platform, accessibility, performance
audit. Annual: principles and architecture refresh.
Metrics that tell the truth (avoid vanity counts): time to first correct implementation (the "golden path" test),
number of undocumented decisions, raw values in production, reuse rate of approved patterns, exception rate,
migration completion, broken-reference rate, developer questions per implementation. Pinterest's lesson: measure
what teams actually use in recent handoff files, not that the library exists (KB-S 29.8).

**Health warning signals (KB-S 17.4).** Read these before the numbers:

| Dimension | Warning signal |
|---|---|
| Discoverability | teams ask the same questions repeatedly |
| Trust | teams bypass the system by default |
| Stability | frequent breaking changes |
| Performance | motion causes jank or battery cost |
| Accessibility | reduced motion handled ad hoc |
| Contribution | the system team works in isolation |
| Governance | either bureaucracy or chaos |
| Evolution | forks accumulate |

**Adoption is a causal signal, not a compliance score (DR 13.3-13.4, MKB4).** A system can be highly adopted and
still poor; low adoption may mean a coverage gap, not resistance. Ask what behavior produced the number. Useful
signals: detach rate and duplicate local versions, coverage (share of eligible interaction states using an
approved pattern, inside a stated scope), request turnaround, repeated questions, version drift. Measure design
adoption (handoff files) and code adoption apart. Before evangelizing, diagnose: friction, discoverability,
contribution cost, implementation gaps, docs that don't match the code. Keep a small set of measures, each tied
to a decision it informs.

**Value measures (CMP C23).** When the case for investment is needed: outputs per week or hours per output;
deviation rate; time to first correct output for a new contributor; share of outputs made without central art
direction (partner or vendor self-serve); cycle time per locale or format; hours per global update; share of team
time moved to exploratory work. Report saved and enabled work separately (motion-evidence-audit metric forensics).

**Productive autonomy (CMP C33.05).** The top-level test: does the system raise the number of competent authors
outside the original team without making their work less distinctive? Output volume alone, or consistency alone,
doesn't answer it.

## 10. Motion debt and entropy
Motion debt (KB-C Part XXVII, CMP C33): one-off values without rationale, duplicate near-synonym behaviors, brand
and product motion evolving separately, design/code drift, old templates still circulating, vendor versions newer than
canonical, accessibility patched in late, shadow libraries, no deprecation path. System entropy (CMP C33.04):
the rate exceptions and variants accumulate compared to the system's ability to explain them. Monitor: unique
behaviors / total behaviors, number of aliases, local overrides, time to explain a standard behavior to a new
contributor.

System-level failure patterns not covered by the SKILL.md anti-pattern table (CMP C32):
- Toolkit without language: assets ship, rules don't, so teams copy assets and drift.
- Master-comp-first: one perfect master built before the responsive logic, so every derivative format is expensive.
- Logo-centric identity: motion lives only around the mark; the rest of the package has no behavior.
- Automation-first: automation built before the behavior is understood; bad rules get faster.
- Motion as polish: motion added after layout and IA are locked, so choreography can't shape hierarchy.
- Generative wallpaper: variation with no semantic purpose.

## 11. Solo and portfolio-scale governance
A single-author public system (a portfolio "Motion Language") still needs governance to be credible: a lifecycle
status on every verb and token, a changelog with dated releases, at least one recorded exception, one deprecation
or rename with its migration note, and a "what I refused to add and why" log. These are the maintenance evidence
that distinguishes a system from a showcase (KB-S 32.2: artifact, adoption, decision, outcome, maintenance,
teaching evidence). Do not invent adoption numbers; label unknowns as unknown.

## 12. Roadmap: an investment mix (DR 9.2)
Balance five classes and name the evidence for each:

| Class | Question | Evidence |
|---|---|---|
| Product demand | What repeated need is visible now? | requests, usage, audits |
| Health / debt | Where is inconsistency or friction rising? | detaches, defects, accessibility issues, implementation variance |
| Strategic capability | What will future work need? | prototypes, platform bets |
| Migration | What must be retired or consolidated? | duplicates, legacy versions, drift |
| Enablement | What does the organization need to self-serve? | doc gaps, onboarding time, repeated questions |

Two failures: a roadmap that only reacts to requests becomes a ticket queue; one that only builds abstractions
loses touch with the product. The split is the authors' synthesis, not a standard; adjust the weights to the stage.

## 13. After handoff (RES R06.06, R06.16; "no post-launch test")
For a brand or toolkit system delivered to others (an agency to a client, a lead to vendors or affiliates), the
quality test is what happens after the authors leave. Audit real outputs at about 30, 90 and 180 days: where did
people improvise, where did a rule fail, which new rule or example is needed? The strongest positive signal is
unplanned variation that still reads as the brand. The failure is launch-only: a launch film that internal teams
can't reproduce. Record the findings in the changelog as rules, not as notes.

