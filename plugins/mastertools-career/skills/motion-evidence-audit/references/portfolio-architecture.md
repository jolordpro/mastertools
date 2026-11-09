# Portfolio architecture, artifact library and red flags

Read this when mapping a surface to dimensions, reviewing a case study's structure, choosing artifacts for the work-order list, or scanning for red flags. Rubric and gates are in `rubric.md` and `evidence-and-gates.md`.

Source codes: **FW1**, **FW0**, **FR**, **PA**, **WB**, **HI** as defined in `rubric.md`; new: **DR** = staff_principal_design_research, **DOS** = motion_systems_dossier ("Motion Systems at Scale"), **RES** = motion_systems_research, **MKB4** = staff_motion_designer_master_knowledge_base_v4.

## 1. What each surface can prove

Decide this first. Most inputs are text, and text cannot evidence craft or behavior. Marking those dimensions U is correct, not harsh.

| Surface | Can evidence | Cannot evidence | Typical ceiling |
|---|---|---|---|
| Resume bullet | Claims about D5 to D13 | Anything observable | D (claim) unless it links to an artifact |
| LinkedIn headline, About, Experience | Positioning, scope, vocabulary, claims | Behavior, craft, adoption | D, C if linked proof |
| Portfolio site page or case study (text only) | Structure, reasoning, attribution clarity, claimed outcomes | Craft, interruption, real behavior | C |
| Case study with video | D1, D14, part of D2 | State logic, accessibility, adoption | B on craft, C elsewhere |
| Interactive prototype or live site | D3, D4, D8, part of D7 | Adoption, governance, production fidelity | A on behavior |
| System docs, token files, spec pages | D5, D6, D7, D11 (existence) | Whether anyone used them | B, A with usage evidence |
| Code repository, shipped product | D7, D9, D5 as implemented | Strategy and influence | A |
| Metrics, testimonials, decision records | D10, D12, D13 | Craft | B to A depending on independence |

Linear and broadcast work (reels, on-air packages, launch films) are strong D1 and D14 evidence and silent on D3, D4, D8. Do not treat that as weakness. Do advise showing the bridge (section 5 below).

## 2. Review order (halo control)

Visual portfolios create a halo: a cinematic opening inflates product and systems scores; a plain systems page deflates craft scores. PA's order controls both directions, so this skill uses it (FW0 starts by not scoring craft at all; PA scores craft first and sets it aside. Both aim at the same bias; PA's is easier to follow with mixed media).

1. **Craft pass.** View the strongest media without reading the narrative. Record craft impressions only: D1, D2, D14.
2. **One shipped interaction in detail,** including states and repeated use: D3, D4.
3. **One system artifact:** tokens, patterns, spec, state model, docs: D5, D6, D7, D11.
4. **Implementation and accessibility evidence:** D7, D8, D9.
5. **Read the narrative** for decision quality, trade-offs, outcomes: D10, D12, D13.
6. **Score each dimension separately,** citing evidence and confidence.
7. **Apply gates;** separate "not demonstrated" from "weak".
8. **Red-team:** state the strongest alternative reading of the work and test it against the evidence.

For media: watch once with sound off, again at half speed, freeze at 20, 50 and 80 percent, and note anything moving at the edges of the frame.

## 3. The 13-step case-study spine

Use this to judge whether a case study exposes its own mechanism, and to restructure one. It merges FW0's 14-step template, PA's 13-part anatomy and FR's required structure. Rule that rides on all of it: every major claim has a nearby artifact (FW1 §26). If it cannot be shown for confidentiality, the person should still describe its structure, decision logic and downstream effect. Confidentiality lowers the visual detail required, not the evidentiary standard.

| # | Step | Passes when it shows | Fails when it shows | Feeds |
|---|---|---|---|---|
| 1 | Context and constraints | Product, users, platform, team shape, why motion mattered | A title card and a logo | D10 |
| 2 | Systemic problem, baseline, diagnosis | A specific inconsistency, cost or scale problem with an inventory or audit | "The company wanted better motion" | D2, D10 |
| 3 | Role and decision rights | Exact decisions owned, collaborators named (attribution panel) | "Led the project" | D13, all |
| 4 | Principles and rejected alternatives | A small rule set, options tried and why they lost | Adjectives; a story with no losing option | D1, D2 |
| 5 | Behavior model | States, transitions, interruption, async, who is source of truth | Happy path only | D3 |
| 6 | Craft decisions | Timing, easing, choreography, continuity with reasons | A reel with no rationale | D1, D4 |
| 7 | System architecture | Tokens, patterns, component mapping, exceptions | A gallery or a table of numbers | D5, D6 |
| 8 | Prototype and validation | The question each prototype answered; what it changed | A final polished prototype only | D9 |
| 9 | Implementation | Engineering contract, compromises, performance, parity QA | "Engineering built it" | D7, D9 |
| 10 | Accessibility | Default and reduced variants, essential versus decorative | One sentence of intent | D8 |
| 11 | Adoption and enablement | Who used it, first outside adopter, mechanism, governance | "Available to everyone" | D11, D12 |
| 12 | Outcome and limits of the claim | Baseline, denominator, method, caveats | A bare percentage | D10, D12 |
| 13 | Evolution and durability | What changed after launch, what was deprecated, what persists | System presented as finished forever | D11 |

Above the fold (PA 15.3): a reviewer under time pressure should see the product problem and the motion outcome within the first screen or two, not a generic title card. The deeper reasoning follows. High signal early, without shrinking the case study to a marketing reel.

Media balance (PA 15.4):

| Medium | Best use | Failure mode |
|---|---|---|
| Video | Feel, timing, choreography, polish | Replacing explanation |
| Interactive prototype | Behavior, state, interruption, responsiveness | So complex nobody can reproduce it |
| State diagram | Logic and edge cases | A technical diagram with no perceptual evidence |
| Token table | Abstraction | Raw numbers with no semantics |
| Annotated frames | Cause and effect | Clutter |
| Code snippet | Implementation literacy | Code theater with no product relevance |
| Before and after | Improvement and trade-off | Simplifying the "before" unfairly |
| Metrics | Outcome | Attribution inflation |

## 4. Portfolio-level structure

**Project mix** (PA 15.1). Across the portfolio, at least one project proving each of: exceptional craft; product interaction (a shipped flow with real states); a system case; implementation; accessibility; cross-team leverage. Also useful: a prototype or concept, a cross-platform project, an enablement or toolkit project.

**Five proofs** (PA 20.3): proof of craft; proof of product behavior; proof of systems; proof of implementation; proof of leverage. A Staff portfolio holds all five. Name which are present, thin or missing.

**Three-Case Portfolio Test** (FR §14.3). Three cases can carry a Staff portfolio: Case A, system builder (architecture, abstraction, implementation, governance, adoption). Case B, cross-boundary solver (ambiguity, influence without authority, engineering and product negotiation). Case C, organizational multiplier (enablement, standards, teaching, adoption, measurement, durable behavior change). The person need not label them this way; the reviewer checks that the evidence types exist.

**Minimum credible portfolio by level** (FR §14.2): Senior, two or three strong projects with clear personal decisions and one reusable practice. Staff, at least two system-level cases, one cross-team system, adoption evidence, engineering partnership, observable leverage, influence without authority. Principal, several independent examples of organization-level leverage, a durable system or platform effect, strategy or roadmap influence, and capability that persisted beyond direct involvement.

**Single-peak caution** (FR §9.2): one extraordinary project proves the person can work at that level. Repeated evidence across situations shows they reliably do. Staff and Principal calls prefer the pattern.

**Read the posting.** List each requirement with an ID, in its own words, as must-have, nice-to-have or trait. For each, name the proof in the material (piece, page, line) or the gap. A role's lens changes what counts: a live or broadcast motion role is judged on 2D and 3D range, concept to finish, toolkits and templates, delivery and file discipline, and directing a look under time pressure; it barely asks about state models or token architecture, so do not mark those down there. A product or Staff systems role is the reverse. Tooling (scripts, toolkits) is strong evidence for the first and weak for the second unless it shows adoption. Say which lens you used.

**Reel and case-study rules** (motion-hiring §6.3, career reference §8.4).
- Reel 60 to 90 seconds, strongest 10 to 15 seconds first, above the fold, no password unless an NDA requires one; the person's role credited on every collaborative piece.
- Separate cuts for brand or marketing roles and for product or UI roles.
- Studio and broadcast roles are decided by the reel; product and Staff roles are decided by written case studies, with the reel in support.
- Three or four case studies: problem, constraints, personal role, system built, scale (markets, languages, deliverables, aspect ratios), outcome, rejected routes.
- Localization is proof worth showing when the role ships globally: text expansion, right-to-left scripts, CJK type, versions across languages and aspect ratios.
- Spec or fan work for a company the person doesn't work for: labelled a personal study, kept free of that company's marks, never sent to them unasked.

## 5. Translating broadcast, campaign and studio evidence

This table is this skill's synthesis, not a source finding. It shows where non-product motion work earns systems credit and where product evidence is still needed.

| Evidence from broadcast, brand or studio work | Can support | Still needs |
|---|---|---|
| Modular template or toolkit that editors assemble without the author | D6, D12 (WB: BUCK, Vucko "common behavior over common visuals") | Count of independent users, rules that make it modular, version history |
| Motion language for lower thirds, transitions, alerts, identity | D2, D6, D11 | Written rules, exceptions, who applied them later |
| Live data graphics where there is no second take | Analogue for D3 (timing under real-time input, failure behavior) | State and failure handling shown, not just the result |
| Pipeline automation, render and delivery tooling | D9, D12 | Named users, measured work removed, maintenance owner |
| Vendor specs and package standards | D7, D11 | The spec itself and what vendors did with it |
| Mentoring a junior to proficiency | D12 | The independent capability that resulted |
| On-time delivery and throughput gains from workflow redesign | D12, D13, D9 | Baseline, method, attribution |

Not enough on its own for a product-motion Staff role: no UI state model, no runtime or token evidence, no accessibility variants. Say so plainly, and keep the "close the gap" advice on artifacts that supply exactly those.

## 6. The 20-artifact library (the work-order catalogue)

From FW1 §31. Use the IDs in the work-order list. Columns:
**Closes:** dimensions it supplies evidence for. **Effort** is this skill's estimate: S is up to about a week of part-time work from material that already exists; M is two to six weeks; L is a quarter or needs other people's cooperation. **Move:** Surface (it likely exists, show it), Build (can be made independently), Earn (needs real-world signal that a document cannot create). **Cares:** PM staff product motion, DS design-systems or design technology, BR brand or studio craft, CL creative leadership.

| ID | Artifact (what it proves) | Closes | Effort | Move | Cares |
|---|---|---|---|---|---|
| A01 | Motion architecture map (layers from principles to adoption) | D5, D6, D11 | S | Build | PM, DS, CL |
| A02 | Motion principles with anti-examples and exceptions | D1, D2 | S | Surface | PM, DS, BR, CL |
| A03 | Semantic motion taxonomy (meaning to behavior) | D2, D6 | S to M | Build | PM, DS |
| A04 | Token architecture (primitive, semantic, component, modes) | D5 | M | Build | PM, DS |
| A05 | Pattern library with use-when, avoid-when, states, accessibility | D6 | L | Build | PM, DS |
| A06 | State and transition matrix with interruption and fallbacks | D3 | S | Build | PM, DS |
| A07 | Motion specification with acceptance criteria | D7 | S to M | Build | PM, DS |
| A08 | Motion inside canonical design-system components and variables | D6, D7 | L | Earn | PM, DS |
| A09 | Runtime prototype (code, Rive, native) with real input | D3, D4, D7 | M | Build | PM, DS, BR |
| A10 | Engineering contract (constraints, boundaries, trade-offs) | D7 | M | Earn | PM, DS |
| A11 | Accessibility matrix (default, reduced, essential versus decorative) | D8 | S | Build | PM, DS, BR, CL |
| A12 | Motion QA matrix and regression approach | D9, D8 | S to M | Build | PM, DS |
| A13 | Working tooling with a usage signal | D9, D12 | M to L | Surface or Earn | DS, PM, CL |
| A14 | Governance model (contribution, review, versioning, exceptions) | D11 | M | Build | DS, PM, CL |
| A15 | Adoption scorecard with denominators | D12 | M | Earn | DS, PM, CL |
| A16 | System roadmap and debt register | D11 | M | Build | DS, CL |
| A17 | Enablement kit (workshop, critique rubric, onboarding) | D12 | M | Build | DS, PM, CL |
| A18 | Change record (one decision, alternatives, trade-offs, consequences) | D11, D13 | S | Surface | PM, DS, CL |
| A19 | Before and after production audit across real surfaces | D10, D12 | M to L | Earn | PM, DS |
| A20 | Leadership narrative (why the investment, what it changes) | D13, D10 | S | Build | CL, PM, DS |

Additions beyond FW1 §31:

| ID | Artifact (what it proves) | Closes | Effort | Move | Cares |
|---|---|---|---|---|---|
| A21 | Migration simulation: an old-to-new mapping, pilot plan, compatibility window and drift audit for a real or public system (MKB4) | D11, D12 | S to M | Build | DS, PM, CL |
| A22 | Removal case: motion that looked better at first, evidence of harm, then changed or removed, and the rule fed back into the system (DOS 9.4, 14.5) | D1, D10, D11 | S | Surface | PM, DS, CL |

A21 made independently is honest when labelled a simulation; it proves change-management thinking, not adoption.

Rules for using the library:
- **Never advise manufacturing evidence.** A Build artifact made independently (a public teardown, a personal token set, a recreated interaction) is honest if labelled as such. It proves the capability, not adoption. Adoption, outcome and durability gaps are Earn moves. If no document can close a gap, say "cannot be closed by a document" and name the real-world move (release the tool to colleagues, run the audit on a live product, ask a partner team to adopt a pattern and record the result).
- **Check ownership before recommending a tool artifact.** Employer-built code may not be publishable. Offer a method-only write-up or a clean-room rebuild instead.
- **Surface before Build.** Many gaps are visibility gaps (PA 2.3). Ask whether the artifact already exists in old work before recommending a new one.
- A work order names one library artifact per item. Combine only when one deliverable truly serves two.

## 7. Consolidated red-flag list (RF-xx)

Use the IDs in your working; in the report, describe each flag in plain words with a quote from the input. Claim-level distortions I1 to I6 are in `evidence-and-gates.md` §6; together they feed part (c), "Things a panel will notice".

| ID | Flag | The tell | Probe or fix |
|---|---|---|---|
| RF-01 | Hero animator | Exceptional craft, no reusable system | Ask for tokens, states, specs, implementation, adoption |
| RF-02 | Library collector | Hundreds of examples, no semantic taxonomy | What decision does each pattern enable, who governs it |
| RF-03 | Token theater | Many tokens named by value | Semantics, modes, accessibility, migration |
| RF-04 | Prototype specialist | Brilliant prototypes, little shipped | Runtime implementation, edge cases, QA, adoption |
| RF-05 | Tool maker | Interesting plugin, no users | Who used it, how much work it removed, who maintains it |
| RF-06 | Documentation specialist | Handsome docs or a huge manual, no evidence of good motion produced or consumed | Did engineering use it, what changed in code, show the rule and the result |
| RF-07 | Governance gatekeeper | Consistency at the cost of friction | Contribution flow, effect on delivery speed |
| RF-08 | Evangelist | Strong workshops, weak mechanics | Actual architecture and shipped implementation |
| RF-09 | Executive storyteller | Strategy language, thin artifacts | Reconstruct one decision end to end |
| RF-10 | AI or tool innovation theater | Fast variations, experiments never integrated | Quality, semantics, accessibility, provenance, workflow integration |
| RF-11 | Spectacle trap | 3D or reel spectacle read as interaction skill | Product evidence of equal weight alongside it |
| RF-12 | Label trap | A "motion system" page of finished animations | Abstraction, rules, reuse model |
| RF-13 | Tool-list trap | Software names as proof | What problem, what behavior, did it survive production |
| RF-14 | Logo and award proxy | Client logos, awards, stakeholder logos as evidence | Who made the decisions, what changed, what standard remained |
| RF-15 | Adjective trap | Premium, fluid, delightful, immersive, elegant, cinematic | Convert to observable rules (see `claim-rewrites.md`) |
| RF-16 | Happy-path trap | One perfect interaction | Repeat input, failure, loading, reduced motion, back navigation |
| RF-17 | Hero dependence | Quality needs the candidate's personal touch, or every decision appears to originate with them | What another designer did successfully without them |
| RF-18 | Outcome borrowing | A team or company result with no personal slice | Attribution ledger |
| RF-19 | Metrics theater | One percentage, no baseline, denominator, method or causal link | Metric forensics in `claim-rewrites.md` |
| RF-20 | Case-study compression | No disagreement, failed approaches or trade-offs; consensus-only story | Rejected alternatives; a lost decision |
| RF-21 | Impact without persistence | Launch results, nothing about what survived | What remained, what was deprecated |
| RF-22 | Breadth without depth | Dozens of logos and projects at the same narrow scope | Which projects show expanding scope |
| RF-23 | Strategy or framework inflation | "Strategy" means a moodboard or vocabulary with no changed decisions | Strategy chain: which decision changed |
| RF-24 | Artifact accumulation | Many systems, few consuming teams | First outside adopter, usage trend |
| RF-25 | Title inflation | Staff or Principal title with feature-level examples | Scope, not title |
| RF-26 | Output obsession | Volume of screens, shots or components, not changed behavior | What other people can now do |
| RF-27 | Over-standardization | Cannot say what should stay contextual | Ask what was deliberately not standardized |
| RF-28 | System for its own sake | Premature abstraction, no real recurring problem or usage | The recurring problem and its evidence |
| RF-29 | Craft absolutism | Cannot explain speed, accessibility, engineering or business trade-offs | A trade-off where craft lost |
| RF-30 | Single-peak evidence | Only one project shows Staff-grade behavior | A second, independent situation |
| RF-31 | Territory protection | The domain is presented as personal authority; others need permission | Who else changed the system, and how |
| RF-32 | Vision without craft proximity | Strategy and direction, no hands-on reasoning about behavior | Reason through one behavior decision in detail |
| RF-33 | Standardization that suppresses local learning | Org-wide rules with no path for product-specific discovery to flow back | What a product team taught the system |
| RF-34 | Executive-only alignment | Leadership sign-off, no practitioner buy-in | What practitioners did with it unprompted |

Craft signals that look impressive but should score lower (WB §18.1) also belong here when seen: long choreographed intros on ordinary interactions; dramatic easing on high-frequency controls; 3D or WebGL as stand-in for state logic; no cancel, reversal or async example; no reduced-motion variant; specs with many timing values and no semantic taxonomy; a clip delivered where runtime state changes are required.
