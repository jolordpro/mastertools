# Claim compressor: verb-to-evidence, resume upgrades and rewrite examples

Read this when rewriting a resume bullet, LinkedIn line, case-study sentence or site copy. Evidence rules and the strip test are in `evidence-and-gates.md`.

Source codes: **FR** Forensic Rubric (§7.1, §6.2, §12.2), **FW1** Assessment Framework (§27), **PA** Portfolio Audit (§16.5, §12.2).

Every example below is invented, and every number is a letter or a bracketed placeholder on purpose. Do not copy example wording into someone's real material. For the user's own work, facts come only from their verified source (see SKILL.md).

## 1. The rewrite procedure

1. **Strip** (strip test, `evidence-and-gates.md` §8): remove adjectives and prestige verbs, keep the proposition.
2. **Classify** the proposition: system creation, leadership, engineering, adoption, tooling, accessibility, outcome, mentoring, strategy.
3. **List the slots** that class needs (table below).
4. **Fill only from known facts.** Unknown slots become `[CONFIRM: what is needed and from whom]`. Never estimate a slot to make a line read better.
5. **Downshift if a slot cannot be filled truthfully.** Rewrite to the smaller claim that is true. A modest claim with an artifact beats a big claim with none, because the reader will test the big one.
6. **Check the voice:** numbers over adjectives, concrete nouns (token layers, teams, platforms, states), no filler verbs.

Bullet formula: *what you made* (named artifact) + *who consumed it* (count and type) + *what it changed in their work* + *measure with baseline* (X to Y, how measured).

## 2. Verb-to-evidence table

| Claim phrase | Slots the claim must be able to fill (FR §7.1, §6.2) | Upgrade pattern (FW1 §27) |
|---|---|---|
| Led | Who followed; formal versus earned authority; which decision was yours | "Influenced [N] teams without formal authority by establishing [standard, ritual, pattern]" |
| Owned | Which decisions were yours versus PM, engineering, management | Name the decision rights: "approved [x], decided [y]" |
| Drove | What changed direction because of you; the record that shows it | Cite the decision record or roadmap change |
| Influenced | Who changed behavior or decision; before and after | "[Team] changed [decision] after [artifact]" |
| Established | What standard, system or process now exists | Name it and its consumers |
| Created motion system | Layers present, teams, platforms, governance | "Established semantic motion architecture (tokens, state models, guidance, governance) used by [N] teams across [platforms]" |
| Standardized | What stayed flexible, what the exception path is | "Standardized [x]; left [y] contextual; exceptions via [path]" |
| Scaled | From what scope to what scope; adoption evidence | "Grew from [A teams] to [B teams] through [mechanism]" |
| Transformed | Measurable or durable before and after | Replace with the concrete difference, or cut |
| Partnered with engineering | What architecture, API, tooling or workflow changed | "Co-designed runtime behavior and constraints with engineering, cutting handoff iterations and standardizing state behavior" with the real change named |
| Built plugin or tool | Users, work removed, maintenance | "Built [tool] that cut [task] from [X] to [Y] for [N] users" |
| Championed accessibility | Requirement, component behavior, tests, reduced-motion variants, shipped use | "Embedded reduced-motion variants and motion QA in canonical patterns used across [N] products" |
| Drove adoption | Definition, denominator, period | "Raised adoption from [X percent] to [Y percent] of eligible [components or surfaces] via [migration, enablement]" |
| Improved efficiency | Baseline, intervention, population, measurement method, result | "[Task] from [X] to [Y] per [unit] across [N] people, measured by [method]" |
| Mentored | The independent capability that now exists | "[Role] went from [X] to independently shipping [Y]; rubric or kit now used by [N]" |
| Strategized | Priorities, trade-offs and decisions that changed | Show the strategy chain with the decision that moved |
| Evangelized | Who adopted the idea and how it became operational | Replace with the mechanism and the adopters |
| Delightful, premium, fluid | Observable rule or measured effect | Name timing, easing, state or outcome (section 4) |

## 3. Work-history questions (FW1 §27)

For resume and LinkedIn audits, these nine questions locate the missing slots. Ask them as the next probes:
1. What system existed before the person arrived?
2. What did they personally change?
3. Who adopted the change?
4. What artifact made it repeatable?
5. What did engineering implement?
6. How was accessibility represented?
7. How was adoption measured?
8. What happened after launch?
9. What evidence remains after they left or moved teams?

## 4. Turning adjectives into rules (PA §16.5, §12.2)

"Playful" is not a principle. A usable version names behavior and its limits: controlled overshoot on selection only, asymmetric entrance and exit timing, brief celebratory states reserved for completed goals, none on high-frequency controls. Do this for any brand adjective:

| Adjective | Rewrite to | Check |
|---|---|---|
| Premium, elevated | Timing class, easing family, motion density and what stays still | Can another designer apply it to a new component? |
| Fluid, smooth | Continuity rule (what identity persists), interruptibility, frame budget | Does it hold on reversal and low-end hardware? |
| Delightful | Where the expressive budget is spent and where it is not | Is the high-frequency path quiet? |
| Intuitive | What the user can infer (cause, state, origin) and how that was tested | Is there a comprehension result? |
| Cinematic | Craft claim only; say it is craft, and keep it out of product claims | Is it evidence for D1, not D3? |

## 5. Metric forensics (FR §12.2)

| Bad claim | Ask | Rewrite shape |
|---|---|---|
| "Saved 40 percent of production time" | 40 percent of what, which workflow, baseline, who measured, sample, quality held constant? | "[Task] from [X] to [Y] per [unit], timed by [who] on [N] runs" |
| "Adopted by 80 percent of the organization" | 80 percent of teams, files, components or surfaces, over what period? | "[X] of [Y] eligible [teams] by [date]; counted by [method]" |
| "Increased consistency" | Inconsistent how, measured how? | "Reduced [N distinct easing curves] to [M] across [surface count]" |
| "Used across 20 products" | Shipped products or exploratory files; was it the source of truth? | "Source of truth for [N] shipped [products]; [M] still on legacy" |
| "Reduced engineering time" | Which step got cheaper, measured or estimated? | Name the step and the measure, or state it as an estimate |
| "Improved accessibility" | Which requirement changed, how was compliance verified? | "Added reduced-motion variants to [N] patterns; verified by [method]" |
| "Animation increased conversion" | Correlation, contribution or causation; test design? | "Release correlated with [x]; [A/B or not]; [caveats]" |

Two further rules. **Saved versus enabled:** never claim hours saved on work that was never done by hand; report it as scope enabled (it could not be done before) and keep the two numbers apart. **Machine time is not designer time:** faster renders are a separate claim from reclaimed designer hours.

## 6. Worked examples (invented)

**System creation.** Original: "Led the creation of a motion system for the whole company."
Strip: a motion system exists. Missing: layers, consumers, governance. Rewrite: "Defined a three-layer motion token set (primitive, semantic, component) with a reduced-motion mode, adopted by [N] product teams on [platforms]. [CONFIRM: how adoption was counted and as of when.]"

**Tooling.** Original: "Built an After Effects plugin that saved the team hundreds of hours."
Strip: a plugin exists and some hours were saved. Missing: baseline, users, method, whether the work was done by hand before. Rewrite: "Built an After Effects panel that cut [task] from [X] to [Y] per [unit], used weekly by [N] designers. [CONFIRM: who timed it.]" If the panel produced work nobody did before, say "made [scope] possible that was not done before" and do not call it hours saved.

**Engineering.** Original: "Partnered with engineers to ship delightful micro-interactions."
Strip: collaboration happened. Missing: what changed in code or process. Rewrite: "Specified [component] as a transition matrix (idle, pressed, pending, success, error, interrupted) with acceptance criteria; engineering implemented it in [stack] and adopted the state names in the component API. [CONFIRM: defects found against the spec before release.]"

**Accessibility.** Original: "Accessibility-first motion."
Strip: an intention. Rewrite: "Every pattern ships a default and a reduced-motion variant; spatial transitions become crossfades; essential motion is listed and documented. [CONFIRM: QA method and number of patterns covered.]"

**Mentoring.** Original: "Mentored junior designers."
Rewrite: "Took [role] from [starting skill] to independently shipping [deliverable] in [period]; the critique rubric is now used by [N]. [CONFIRM: names or roles cleared for use.]"

**Metric.** Original: "Increased engagement 30 percent through animation."
Rewrite: "Shipped [change]; [metric] moved from [X] to [Y] over [period] against [baseline]; [A/B or not]; other releases overlapped, so treated as contribution, not sole cause. [CONFIRM: test design.]" If no baseline exists, downshift to the qualitative fact that is true.

**Broadcast to systems.** Original: "Designed an award-winning on-air motion package."
Craft credit stays, as craft. To add the systems layer, ask what rules, templates or tooling let other people produce it: "Built a modular template set of [N] variants assembled by [M] editors without the designer; revision rounds fell from [X] to [Y]. [CONFIRM: counts and period.]" If the modular layer does not exist, do not imply it.

## 7. LinkedIn and site copy

Headline and About lead with a scope noun and a system layer, not an adjective. The Featured section links to artifacts (a spec, a state matrix, a token page, a tool demo), because links raise confidence from D to B and a bare list of tools stays D. Keep the same facts everywhere; a number that differs between surfaces is a credibility cost larger than any gain from the bigger number.

**Application files that parse** (motion-hiring §6.1, §8). Text-based PDF or DOCX in one column; standard headings; nothing that matters in headers, footers, text boxes or tables; title, company and dates on their own lines; reel and portfolio URLs written out in full near the top and again in the application's link fields; links that open without a password. After upload, check the careers site's autofilled fields: garbled there means garbled for the recruiter. Flag as defects: hidden or white text, keyword dumps, pasted job descriptions, and any "instructions to the AI" line. Parsers extract all of it and recruiters see it. The "75 percent auto-rejected" figure is a myth from a defunct vendor; knockout questions are the real automatic filter.

**AI-workflow claims.** "Used AI tools" is a D-level claim until it shows a before and after with real numbers (time, versions, cost), names the tools and whether they were cleared for the employer's use, says how rights, data and likeness were handled, and makes plain that the final craft is the person's own. Rewrite toward that shape or leave `[CONFIRM: ...]` slots.
