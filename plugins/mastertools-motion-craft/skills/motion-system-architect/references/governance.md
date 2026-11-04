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
```
Intake outcomes: accepted as experimental / needs evidence / parameterize existing / rejected with reason. Record the
decision in `decision-log/` with the date and rationale; a rejected proposal with its reason prevents re-litigation.

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

## 7. Deprecation and migration procedure
1. Mark `status: deprecated`, set `$deprecated`, add `replacedBy`. Keep the old token as an alias for at least one minor cycle.
2. Write the **perceptual** migration note: what will feel different (faster, heavier, less overshoot), where the old behavior is still appropriate, whether choreography needs retuning (KB-S 15.4).
3. Add a lint rule or codemod that flags the old ID; announce in the changelog.
4. Track migration completion (count of remaining usages). Set a sunset date.
5. At the date, mark `retired`; the validator will error if an active token still references it.
Also circulate the update through templates: orphaned toolkits (old MOGRTs, stale Lottie) are the most common way
retired behavior survives (KB-C 138).

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

## 10. Motion debt and entropy
Motion debt (KB-C Part XXVII, CMP C33): one-off values without rationale, duplicate near-synonym behaviors, brand
and product motion evolving separately, design/code drift, old templates still circulating, vendor versions newer than
canonical, accessibility patched in late, shadow libraries, no deprecation path. System entropy (CMP C33.04):
the rate exceptions and variants accumulate compared to the system's ability to explain them. Monitor: unique
behaviors / total behaviors, number of aliases, local overrides, time to explain a standard behavior to a new
contributor.

## 11. Solo and portfolio-scale governance
A single-author public system (a portfolio "Motion Language") still needs governance to be credible: a lifecycle
status on every verb and token, a changelog with dated releases, at least one recorded exception, one deprecation
or rename with its migration note, and a "what I refused to add and why" log. These are the maintenance evidence
that distinguishes a system from a showcase (KB-S 32.2: artifact, adoption, decision, outcome, maintenance,
teaching evidence). Do not invent adoption numbers; label unknowns as unknown.
