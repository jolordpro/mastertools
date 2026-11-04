# Evidence, gates and claim integrity

Read this when assigning confidence, deciding gate status, checking attribution, or running the strip test. Scoring mechanics and the dimensions are in `rubric.md`.

Source codes: **FW1**, **FW0**, **FR**, **PA**, **WB**, **HI** as defined in `rubric.md`.

The reason this file exists: the most common audit failure is mistaking visible sophistication for systemic sophistication. A polished reel, a handsome docs site and confident language all look like Staff work. The rules below force the audit to ask what exists, who used it, and what changed.

## 1. Evidence confidence: A, B, C, D, U

Rate every dimension's evidence separately from its score. Confidence says how far to trust the score; it does not lower the score.

| Code | Meaning | Examples | Score behavior |
|---|---|---|---|
| A | Observed directly | Shipped behavior you can inspect; live prototype; production code or token package; adoption data you can read | Score normally. Only A can support a 5 |
| B | Strongly corroborated | Several aligned artifacts; spec plus prototype plus described implementation; documented adoption with named teams | Score normally. Supports up to 4 |
| C | Plausible but incomplete | Detailed case study with no artifact; credible context; a prototype judged on shipping or adoption (a prototype is B for the behavior it demonstrates) | Cap at 3. Name what is missing. Gates: provisional pass only |
| D | Asserted only | Resume bullet, headline, "I led", tool lists, awards without artifacts | Cap at 2, show in brackets as "claimed", and it cannot satisfy any gate |
| U | Not demonstrated (the surface is silent) | A reel says nothing about accessibility | **Never scored.** Record as a next probe |

Unknown is not weak. Accessibility, performance, governance and adoption are often absent from visual portfolios even when the person did the work. Scoring silence as failure punishes how the portfolio was packaged. Report U, say which probe would resolve it, and keep it out of the total.

The corpus lets a conflict stand here: PA says "do not convert a claim into score", FW0 says "cap claim-only at 2 unless an interview corroborates". This skill follows FW0 (a bracketed 2) because a claim still tells the reader something, but keeps D out of every gate, which is PA's point.

### Crosswalk to the source tiers

| This skill | FW1 tier | FR / HI evidence level | PA tier |
|---|---|---|---|
| A | A shipped + adopted + measured, B shipped | E3 to E5 | Tier 1 direct |
| B | B shipped artifact, C artifact without production proof | E2 to E3 | Tier 2 corroborated |
| C | D prototype or concept | E1 narrative | Tier 3 circumstantial |
| D | E claim | E0 assertion | Tier 4 self-asserted |
| U | "not tested" | n/a | Absence: mark not evidenced |

Independence matters too (FR P1 to P5): a claim, then a candidate-authored artifact, then an artifact in a shared organizational workflow, then independent usage evidence, then independent testimony plus artifact plus outcome. Prefer the higher rung when two items tie.

### Optional sensitivity check

FW1 offers confidence multipliers: 0.25 uncorroborated claim, 0.5 portfolio assertion, 0.65 prototype, 0.80 detailed case study, 0.90 shipped system artifact, 1.00 shipped implementation, 1.15 shipped plus adoption, 1.25 shipped plus adoption plus measured impact. FW1 itself calls them a calibration signal, not a law. Use them only to show a user how much of their total rests on proof quality. Never use them for the headline score.

## 2. Triangulation

A Staff-level score on any dimension should rest on at least three evidence classes: an artifact, an implementation or adoption signal, and an explanation that shows causal understanding (FW0 §2.3). A Principal-level score adds organizational persistence or evolution. One source alone caps the score at 3.

Do not count one artifact as independent evidence for many dimensions (FW1). A token file can support D5; it supports D12 only if usage evidence travels with it.

## 3. Leverage ladder and adoption ladder

Leverage (FR §16): L0 self, L1 a reusable artifact, L2 a team materially better, L3 several teams gained capability, L4 the organization changed how it works, L5 the capability persists and evolves without the author. Staff evidence lives at L3; Principal at L4 and L5.

Adoption (FR §11.1): awareness (not adoption), tryout, routine use, default behavior (teams reach for the system first), embedded infrastructure (in tooling, templates, code, review, planning), self-governing ecosystem. "Default behavior" is the first Staff-grade signal.

Rough test: 30 excellent animations with no reuse is high craft and low leverage; a system used by 15 designers is more; a system built into product code, used by four product groups, measured and maintained by several people is a lot more.

## 4. Gates

A total never awards a level on its own. Gates exist so exceptional craft cannot hide a systems gap. Report each gate as **pass**, **fail** or **not tested**. Fail means evidence at A, B or C shows the bar missed. Not tested means the surface was silent; it blocks a Staff call just as hard, but the fix is different (show the evidence, not build the capability).

### Staff, dimension gates (default mode)
Score of at least 3 on D3 (state and interruption), D5 (tokens), D6 (patterns and design-system integration), D7 (specs and engineering translation), D8 (accessibility). These are FW1's structural requirements: token architecture, state modeling, design-system integration, engineering partnership, technical literacy and accessibility.
Also: high craft cannot offset missing implementation or adoption evidence, and high leadership cannot offset inability to reason precisely about motion behavior (FW1). Check D1 or D3 at 3 or more when the leadership dimensions are strong.

### Staff, mandatory evidence gates (FR §15.2)
1. **Leverage beyond own output:** measurable or strongly observable effect on people or teams other than the candidate.
2. **Influence outside design:** a decision changed in engineering, product, research or leadership.
3. **Inspectable system artifact:** at least one, not a slide about one.
4. **Adoption by others:** people other than the candidate use it.
5. **Downstream outcome:** something changed because of it, beyond finishing the artifact.
6. **Separable personal contribution:** the candidate's decisions can be told apart from the team's.

Also check (FW0 §26.3): a Staff call wants at least two independent signals from implementation, governance, adoption or enablement at A or B.

### Principal
Everything above, plus score of at least 4 on D11 (governance and evolution), D12 (adoption and enablement) and D13 (influence and strategy), plus durability: evidence the capability survived launch or the author's reduced involvement. Also the FR 12-point threshold, condensed: a systemic problem across more than one team; an inspectable system artifact with rules rather than examples; a changed engineering decision or workflow; influence on product strategy or roadmap; an adoption mechanism others used; a real adoption signal; an outcome signal; a hard trade-off where a locally attractive answer lost to system health; a failure or revision that changed the system; a durable effect after reduced involvement; a clean attribution ledger; and the same behavior in more than one major situation. FR's closing test: does the evidence make it reasonable to expect this person to produce the same leverage in a new, ambiguous setting?

### Staff versus Principal calibration

| | Senior | Staff | Principal |
|---|---|---|---|
| Unit of impact | Project or feature | System, several teams | Ecosystem, organization, next platform generation |
| Question | How do we make this excellent? | How do we make excellent behavior repeatable? | What should excellent mean across the organization? |
| Time horizon | Months | Quarters to years | Multi-year |
| Risk managed | Craft and delivery | Fragmentation and adoption | Organizational, architectural, strategic, platform |
| Proof | Strong projects | Shipped system plus adoption | Repeated system change plus durable organizational change |

Staff comes in more than one valid shape (FR §2.2): system architect, cross-team lead, solver of the hardest ambiguous problem, organizational steward. Do not require all four. Do not mistake a missing management title for missing seniority, or a Principal title for Principal scope.
Principal red flags (FW1 §25): broad strategy with no prior system teams actually used; governance as authority rather than distributed decision-making; large craft range with weak technical or organizational leverage; a system that needs the principal to approve every decision; standards created faster than the organization can adopt them; executive presence covering thin implementation evidence.

## 5. Attribution ledger

Use when a case study says "we". Score the candidate's separable part, not the prestige of the environment (FR §8, FW0 §2.2).

| Contribution | Candidate role | What would show it |
|---|---|---|
| Problem framing | originated / reframed / inherited | problem statement, research synthesis |
| System architecture | designed / co-designed / implemented | diagrams, token schema, prototypes |
| Motion craft | primary / collaborative / reviewed | working files, shot ownership |
| Engineering translation | specified / prototyped / paired / reviewed | specs, code, implementation decisions |
| Stakeholder alignment | facilitated / influenced / informed | decision records, partner testimony |
| Adoption | drove / enabled / inherited | usage data, rollout, training |
| Outcome | caused / contributed / correlated | measurement and attribution logic |
| Governance | created / co-created / operated | process docs, review forums |

Rules: if the candidate cannot name their own decisions, score the case as team evidence. If the result belongs to a larger program, require the share they influenced. If they inherited a mature system, call it stewardship; it can be Staff-grade, but it is different evidence from authorship. A primary implementer is not a strategic owner.

## 6. Six inflation patterns (I1 to I6)

These are claim-level distortions (FW0 §2.4). Track them by ID internally; report them in plain words in part (c).

| ID | Pattern | Test |
|---|---|---|
| I1 | Role inflation: "led" when one contributor among many | Who followed? Which decisions were theirs? |
| I2 | System inflation: a component library or asset set called a motion system | Where are the abstractions, rules, states and reuse model? |
| I3 | Adoption inflation: one team or one flagship called organization-wide | How many teams, measured how, against what denominator? |
| I4 | Tooling inflation: a preset or script called infrastructure | Who used it, how much work did it remove, who maintains it? |
| I5 | Governance inflation: a document called governance with no owners, reviews, versioning or exceptions | Show the contribution path and a decision it resolved |
| I6 | Engineering adjacency inflation: attended handoffs, did not influence implementation architecture | What changed in code, API or workflow because of them? |

The wider list of artifact-level and portfolio-level red flags (RF-xx) is in `portfolio-architecture.md`.

## 7. Anti-conflation list

Never infer the right side from the left (FW0 AI.8). When a claim leans on an equation, flag it.

beautiful animation is not a motion system · motion tokens are not token architecture · a component library is not a pattern system · a handoff meeting is not engineering influence · documentation existing is not documentation being usable · publishing a system is not its adoption · adoption is not value · team leadership is not system architecture · a tool created is not infrastructure · a reduce-motion toggle is not accessible motion · a large system is not a mature one · many rules are not good governance · central control is not scalable governance · more systematization is not better design · AI generation is not AI-ready motion architecture.

## 8. The strip test ("would this still be true?")

For any claim, delete the adjectives and the prestige verbs, then check whether the remaining proposition is true and checkable (FR §7.3).
1. Strip: "spearheaded a transformative organization-wide motion overhaul" becomes "a new motion system was adopted by several teams and changed implementation".
2. Test: is the remainder specific enough to be verified or falsified? Which teams? Changed what?
3. List the missing slots (who, how many, what changed, baseline, artifact, date).
4. Rewrite to the smaller true claim, or leave the slots as bracketed placeholders. Never fill a slot with a guess.

Examples and the full rewrite procedure are in `claim-rewrites.md`.

## 9. The nine-link evidence chain

Reconstruct this chain for each major case (HI Part V). A missing link lowers confidence on every dimension that case supports.
1. **Before-state:** what was broken, ambiguous, expensive or inconsistent?
2. **Systemic cause:** why did it recur across projects or teams?
3. **Scope:** who and what were affected?
4. **Influence map:** who had to change behavior, and what did each protect?
5. **Strategic intervention:** the model, principle, architecture, standard or mechanism introduced.
6. **Durable artifacts:** what remains after the project ends?
7. **Conflict and trade-offs:** what was resolved, what was deliberately not done?
8. **Adoption:** how others used, migrated to, contributed to or depended on it.
9. **Outcome:** what changed, and what separates causation from correlation?

Two cross-checks. The **counterfactual test** (FR §1.3): if this person had not taken part, what would be materially different? "The animation would look worse" is a craft contribution; "three teams would still be building incompatible motion and engineering would have implemented each separately" is a systemic one. The **layer trace** (FW0 §24.2): pick one interaction and ask the candidate to show where its behavior lives at every layer, from rule to token to pattern to component to state model to spec to implementation to accessibility path to QA to maintenance, without inventing the system on the spot.

## 10. Probes for polished material

When the material looks finished but the evidence chain is thin, these are the questions a panel will ask (FW1 §30). Use them as next probes and as interview prep:
1. Show me the artifact that made the decision reusable.
2. Where did engineering consume this?
3. What happened when a team disagreed?
4. What broke after launch?
5. How did you measure adoption?
6. What did you deprecate?
7. What did you intentionally not standardize?
8. What did another designer do successfully without you present?
