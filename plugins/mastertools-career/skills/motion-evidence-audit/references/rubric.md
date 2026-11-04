# Master rubric: 14 dimensions

Read this when scoring. It holds the scale, the weights, the axis map, the two mode weightings, and one entry per dimension. Gates and evidence rules live in `evidence-and-gates.md`.

Everything here is a synthesis of five research documents. The weights, the axis map and the score bands are this skill's own consolidation, not an industry standard and not a hiring predictor.

Source codes used below: **FW1** = Staff/Principal Motion Systems Assessment Framework (C01 to C22, the spine). **FW0** = the earlier forensic edition of that framework. **FR** = Forensic Rubric. **PA** = Portfolio Audit Manual. **WB** = World-Class Motion and Interaction Benchmark. **HI** = Horizontal Influence knowledge base, Part V.

## 1. Scale

Score the level the evidence demonstrates, never the level the person could probably reach.

| Score | Meaning | Maps to |
|---|---|---|
| 1 | Weak or purely local. Taste-led, happy path only | FW1 Mediocre, PA Weak |
| 2 | Competent. Reliable inside someone else's system | FW1 Competent |
| 3 | Senior. Deliberate decisions, edge cases considered, still works inside an existing framework | FW1 Strong Senior |
| 4 | Staff. Defines or materially upgrades the framework; other people reuse it; shipped | FW1 Staff |
| 5 | Principal. Durable, multi-team or multi-generation, changes how the organization works | FW1 Exceptional |
| U | Not demonstrated. **Not a score.** Becomes a next probe | PA "U", FW0 "missing is not absent" |

A score of 4 needs confidence A or B. A score of 5 needs confidence A plus durability evidence. Confidence ceilings are in `evidence-and-gates.md`.

## 2. Weights, axes and totals

Default mode is `staff-product-motion`. Weights sum to 100.

| # | Dimension | Weight | Axis |
|---|---|---|---|
| D1 | Craft and perceptual command | 8 | Craft |
| D2 | Semantics and decision framework | 5 | Craft |
| D3 | Interaction and state modeling (incl. interruption, async) | 12 | Product Interaction |
| D4 | Direct manipulation and continuity | 5 | Product Interaction |
| D5 | Token architecture | 8 | Org Leverage |
| D6 | Patterns, choreography and design-system integration | 8 | Org Leverage |
| D7 | Specs and engineering translation | 11 | Org Leverage |
| D8 | Accessibility as architecture | 5 | Product Interaction |
| D9 | QA, validation and tooling | 8 | Org Leverage |
| D10 | Product reasoning and outcomes | 8 | Product Interaction |
| D11 | Governance and evolution | 6 | Org Leverage |
| D12 | Adoption and enablement | 8 | Org Leverage |
| D13 | Cross-functional influence and strategy | 6 | Org Leverage |
| D14 | Expression, originality and emerging modalities | 2 | Craft |

Axis totals in default mode: Craft 15, Product Interaction 30, Org Leverage 55. The axes stay separate so exceptional craft cannot mask thin product or leverage evidence (PA 18.5).

**Axis score** = weighted mean of the scored dimensions on that axis, on the 1 to 5 scale. Skip U dimensions and say how many were skipped.
**Weighted total** = sum over scored dimensions of (score / 5 x weight), divided by the weight that was scored, times 100. Report **coverage** = scored weight as a share of 100.
A portfolio of all 3s totals 60; all 4s totals 80.

**Bands** (FW1 §29, kept as is). Apply a band only when coverage is at least 60 percent; below that, show the total as "provisional, no band". The "under 60" row below is a score band, unrelated to the 60 percent coverage rule.

| Total | Reads as |
|---|---|
| 90 to 100 | Principal-range evidence |
| 80 to 89 | Staff-range evidence |
| 70 to 79 | Staff-capable, emerging Staff |
| 60 to 69 | Strong Senior |
| under 60 | Senior or below on the evidence shown |

**Axis targets for a Staff profile** (calibration from PA 18.5, not gates): Craft 4.0, Product Interaction 4.0, Org Leverage 3.8. Exceptional profiles approach 4.5 to 5.0 on all three.

**Why Org Leverage carries 55.** FW1 and FW0 put about two thirds of their weight on system, engineering, adoption and governance competencies, because craft alone does not separate Staff from Senior. PA weights craft heavily because it audits the portfolio as a motion artifact. This skill sides with FW1 for the default mode and offers the craft-weighted view below when the role is craft-led.

### Craft-weighted alternative view (WB §19)

For roles led by brand, 3D or launch-film craft, also compute this view and show it beside the default. It never replaces the gates.

| WB group | Weight | Dimensions (weighted mean inside the group) |
|---|---|---|
| Motion craft | 25 | D1, D2, D14 |
| Interaction logic | 20 | D3, D4 |
| Product reasoning | 15 | D10 |
| Systems thinking | 15 | D5, D6, D11 |
| Implementation fluency | 10 | D7, D9 |
| Accessibility | 5 | D8 |
| Cross-functional influence | 10 | D12, D13 |

### `creative-leadership` mode

For Head of Creative, Creative Director and similar. The weights shift toward leverage, influence, governance and craft; technical dimensions drop to a literacy floor.

| D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | D14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | 6 | 5 | 2 | 3 | 5 | 4 | 4 | 7 | 8 | 12 | 12 | 14 | 8 |

Axis totals in this mode: Craft 24, Product Interaction 19, Org Leverage 57.

Gates in this mode: the mandatory gates in `evidence-and-gates.md` still apply. Dimension minimums become 3 on D1, D10, D11, D12 and D13, and 2 on D3, D5, D7 and D8 (enough literacy to direct technical work and spot a bluff). Principal-equivalent (Director and above) needs 4 on D11, D12 and D13 plus durability.

**Limit of the scoring, for your own use:** the research corpus is thin on people leadership. It has no dimensions for hiring, team design, performance management, budget ownership, vendor management or executive stakeholder work, so the numeric scores in this mode cover only creative-systems, governance and influence evidence. That limit applies to the numbers, not to the audit: in the report, assess people leadership directly as claims (what is stated, what would prove it, what a panel will ask), because for these roles it is the core of the job. Do not label it "outside the rubric" or route it elsewhere.

## 3. The dimensions

Each entry gives: what to look at, the Senior (3), Staff (4) and Principal (5) signatures, the artifacts that prove it, and the false positive to watch for. The merged sources are cited so you can trace a finding back.

### D1. Craft and perceptual command (8, Craft)
Merges FW1 C01, C03, C07 craft; PA 4.2 to 4.4 and 4.10; WB §3 to §5; FW0 §5.
Look at: duration as a function of frequency, distance and importance; easing as meaning; springs as a physical model (stiffness, damping, mass, interruptibility); choreography and focal hierarchy; restraint as an attention budget. Judge the motion itself: mute it, play it at half speed, freeze at 20, 50 and 80 percent, repeat it ten times.
- **3:** Varies duration by frequency and context; compares alternatives; sequences have a clear lead element.
- **4:** Craft judgment is written down as rules others use: temporal classes, distance-to-duration logic, spring families, choreography rules that prevent collisions, recorded decisions not to animate.
- **5:** An organization-level motion grammar that balances utility, expression, accessibility, platform and brand across very different surfaces.
Proof: three or more competing timing and easing studies with trade-offs; a distance-to-duration table; a spring guide; focal maps; a before/after simplification.
False positive: hero animator; one polished example with one timing value; springs because they are fashionable; every curve 200 to 300 ms.
Text-only inputs cannot evidence this dimension. Mark U.

### D2. Semantics and decision framework (5, Craft)
Merges FW1 C02; FW0 §4 principles; PA 4.1; FR 4.1 behavioral grammar; WB causality and intent.
Look at: motion as information (cause and effect, state, hierarchy, continuity, progress); productive versus expressive; turning an adjective into an observable rule ("confident" becomes timing, easing and spatial behavior); when the same meaning must always behave the same.
- **3:** Each movement is tied to comprehension, feedback or continuity, and the maker can explain trade-offs.
- **4:** A short durable set of principles plus a state-to-motion taxonomy and a decision framework (what moves, what stays still, in what order, with what fallback) that another designer can apply. Exceptions are documented.
- **5:** The language resolves new problems without central review and stays coherent across products, platforms and new modalities.
Proof: semantic motion taxonomy; principles with anti-examples; a motion audit showing contradictions in an existing product; a decision matrix.
False positive: a moodboard labelled "motion language"; "motion tells a story"; "delight".

### D3. Interaction and state modeling, including interruption and async (12, Product Interaction)
Merges FW1 C04; FW0 §8; PA 4.5, 4.8, 4.9; WB §7 and §24.1.
Look at: the state graph (idle, hover, focus, pressed, pending, success, error, disabled, interrupted); repeated input; reversal mid-flight; retargeting; cancellation; async truthfulness (intent registered, optimistic, pending, confirmed, failed, retried); who is the source of truth. Motion represents state; it must never define it.
- **3:** Explicit state behavior for individual flows, with reversal and common async cases handled.
- **4:** Reusable state models and behavior primitives across components, with a transition matrix covering interruption, cancellation, concurrency and precedence, and a contract engineers implement.
- **5:** The state architecture becomes the product's behavior model, contradictory states drop away, and new interactions get cheaper to design.
Proof: state diagram or transition matrix; runtime prototype with edge cases; interruptibility spec; loading, error and empty states.
False positive: one beautiful click animation shown as a whole interaction; a success animation before the backend confirms.
Broadcast and linear work cannot evidence this. Mark U, not weak.

### D4. Direct manipulation and continuity (5, Product Interaction)
Merges PA 4.6, 4.7; FW1 C07 spatial and C02 continuity; FW0 §20; WB §5, §6, §12, §13.
Look at: identity and origin carried across a change (shared element, container transform); direction as meaning; gesture coupling across the whole 0 to 100 percent range, release velocity, cancel thresholds, seekability; behavior with real content, other viewports and keyboard-only input.
- **3:** Persistent objects keep recognizable continuity; gesture position, direction and release affect the motion.
- **4:** Transitions teach the product's structure; direct manipulation and velocity transfer are modeled; continuity holds for long text, narrow screens and input variants.
- **5:** Motion acts as dynamic information architecture and feels physically coupled across input methods and spatial contexts.
Proof: gesture prototype showing slow drag, fast fling, reversal and cancel; shared-element mapping; keyboard-only run-through.
False positive: a swipe that is really a prebuilt timeline; random directional slides; continuity that is only visual and ignores task priority.

### D5. Token architecture (8, Org Leverage)
Merges FW1 C05; FW0 §6; PA 4.13; WB §11, §24.4.
Look at: primitive, semantic and component layers; aliases; modes (reduced motion, theme, platform); names by meaning not value; versioning and deprecation; whether the tokens exist outside one design tool (DTCG or equivalent, consumed in code); distance, stagger and spring tokens; a rule for reuse versus a new token.
- **3:** Separates primitives from semantic intent and maps them to components or patterns.
- **4:** A layered architecture across design and code with modes, exceptions, deprecation and accessibility mapping, so a value change propagates without editing every component.
- **5:** Interoperable across products, platforms, brands and stacks, still legible and governable, and says where tokens are deliberately not used.
Proof: token hierarchy diagram; DTCG-compatible package; variable and mode setup; platform mapping matrix; migration plan.
False positive: token theater ("50 motion tokens", a table of milliseconds, one token per animation, tokens that live only in one Figma file).

### D6. Patterns, choreography and design-system integration (8, Org Leverage)
Merges FW1 C06, C07 rules, C10; FW0 §7 and §9; PA 4.13; WB §14, §15.
Look at: a library organized by recurring product problem; for each pattern the intent, use-when, avoid-when, states, accessibility and tokens; anti-patterns; a contribution template; motion living inside canonical components rather than a parallel library; cross-platform matrix; what a theme change does.
- **3:** Adds context, variants and usage guidance; motion takes part in component states.
- **4:** A decision framework rather than a gallery, integrated with components, tokens, variables, code, docs and governance, reused by unrelated teams.
- **5:** A shared behavioral vocabulary that cuts bespoke motion yet leaves room for expression; motion is a first-class system layer.
Proof: pattern taxonomy or decision tree; component-motion anatomy; variable and mode structure; design-to-code mapping; anti-pattern gallery.
False positive: library collector; named after technique instead of user intent; a standalone motion library disconnected from source components.

### D7. Specs and engineering translation (11, Org Leverage)
Merges FW1 C08, C12, C13; FW0 §10, §11, §15; PA 4.15; WB §10 and §24.5; FR 3.8.
Look at: a spec as a contract (triggers, states, properties, tokens, interruptibility, constraints, fallbacks, acceptance criteria, ownership boundary); runtime prototypes in code, Rive or native instead of timelines; a compromise that protected perceptual intent; runtime literacy (layout versus compositing, frame budget, asset weight, which of CSS, native, Rive or Lottie fits); design and code parity; an engineering decision or API that changed.
- **3:** States, timing, sequencing and edge cases are defined; works with engineers during implementation.
- **4:** Specs act as repeatable contracts that cut live interpretation; behavior and architecture are co-designed with engineering; fidelity versus cost is negotiated with evidence; the shipped implementation is inspectable.
- **5:** Shapes the technical foundation or API through which several teams implement motion, changing the design/engineering interface itself.
Proof: motion spec or pattern contract; acceptance criteria; runtime prototype; implementation notes or PR threads where shareable; performance test; the compromise story (what stayed invariant, what changed).
False positive: a GIF or video as the whole API; "partnered closely with engineers"; "technical motion designer"; After Effects keyframes only; "GPU means faster".

### D8. Accessibility as architecture (5, Product Interaction)
Merges FW1 C14; FW0 §14; PA 4.11; WB §9.
Look at: essential, functional, expressive and ambient motion kept apart; reduced motion as a semantic fallback (crossfade, highlight, static state) rather than zero; vestibular, peripheral and flashing risks; non-motion alternatives; keyboard and screen-reader behavior; accessibility wired into tokens, patterns, state model and QA.
- **3:** Major motion has documented reduced-motion behavior that keeps its meaning.
- **4:** Accessibility is designed alongside the default across tokens, patterns, specs, QA and governance, and the maker can say what must remain when movement is reduced.
- **5:** An ecosystem strategy across visual, haptic, audio and input alternatives and new modalities, with the accessible path as the default.
Proof: default versus reduced state matrix; alternative-feedback matrix; motion risk checklist; accessibility QA suite.
False positive: "respects prefers-reduced-motion" in one sentence; duration set to zero everywhere; "accessibility-first" with no variant shown.

### D9. QA, validation and tooling (8, Org Leverage)
Merges FW1 C11, C15, C16; FW0 §12, §15, §16; PA 4.15; WB §24.6.
Look at: a QA matrix across states, devices, content, accessibility and performance; visual and behavioral regression; who owns validation; findings that flow back into patterns; prototypes tied to a question with discarded alternatives logged; tooling (scripts, panels, generators, validators, templates, AI workflows with QA gates) with named users, work removed and a maintenance owner.
- **3:** Checklists and coverage matrices for real edge cases; repeatable utilities that help peers.
- **4:** A systematic QA framework with owners; tooling that measurably raises throughput or consistency for several designers or engineers; prototypes that settle systemic questions.
- **5:** Automates the high-value validation, turns QA findings into system fixes, and builds shared infrastructure that changes how the organization explores, implements and maintains motion.
Proof: working tool plus a usage signal; workflow before and after; QA matrix; regression suite; prototype decision log.
False positive: tool maker (clever plugin, no users, no owner); "detail oriented"; saves the author a few clicks; automating a broken process; AI variation without quality control.
Authoring-app tooling (After Effects scripts and panels) counts as leverage when others use it and measured work disappears. For product roles, tooling that touches the token, linting or spec-export pipeline is stronger, and also supports D7.

### D10. Product reasoning and outcomes (8, Product Interaction)
Merges FW1 C20; FW0 §19; PA 4.12; FR 3.12 and §12; WB §3.
Look at: the user problem; evidence from research, usability or analytics; constraints and trade-offs; the metric class (behavioral, comprehension, perceptual, operational, anecdotal); causal language (correlation, contribution, causation); baseline, denominator and method; when not to prioritize motion.
- **3:** Decisions tie to a concrete user or product problem.
- **4:** System investment is framed in user, product, engineering, accessibility and organizational outcomes, with alternatives, trade-offs and the limits of the claim stated.
- **5:** Motion strategy shapes product strategy, risks surface before implementation, and the measurement model changes investment decisions.
Proof: hypothesis log; research plan; experiment matrix; outcome dashboard; decision memo.
False positive: "delight"; "users loved it"; a bare percentage; credit taken for a team or company outcome.

### D11. Governance and evolution (6, Org Leverage)
Merges FW1 C17, C21; FW0 §17; FR 3.9, 3.14, 3.15; PA 4.14; WB §26.
Look at: decision rights; a contribution path (proposal or RFC); review criteria; versioning; deprecation and migration; exception rules (when the system says no, when it allows a justified exception); changelog; debt register and roadmap; whether it outlived launch or its author; governance that enables rather than gatekeeps.
- **3:** Review criteria exist and significant decisions are documented.
- **4:** Scalable governance balancing consistency and team autonomy, with safe paths for change, exception and migration rules, and a roadmap that names systemic debt.
- **5:** A federated or platform-level operating model that evolves without turning bureaucratic, plans the next generation while retiring the old, and survives personnel change.
Proof: contribution workflow; RFC template; decision record; deprecation policy; migration guide; changelog; roadmap.
False positive: a document titled "governance" with no owner, review or versioning; "owned the design system"; every exception made permanent.

### D12. Adoption and enablement (8, Org Leverage)
Merges FW1 C18 and C19 enablement; FW0 §15; FR 3.10, 3.11, §11.1, §16; PA 4.14, 4.18; WB §26.3.
Look at: where the work sits on the adoption ladder (awareness, tryout, routine, default, embedded, self-governing); the definition, denominator and method behind any adoption number; the first adopter outside the home team; bypass and exception rates; enablement kits (workshops, critique rubric, onboarding, office hours, templates); what another designer did successfully without the author present.
- **3:** Usage and qualitative feedback are tracked; teammates reuse the work.
- **4:** Meaningful adoption and health metrics; several product teams adopt; documentation and training back it; other designers work independently; data sets priorities.
- **5:** The system is run as a product with telemetry, hypotheses and investment calls; adoption sustains itself through contributors and champions.
Proof: adoption scorecard with denominators; coverage and exception dashboard; enablement kit; migration counts; named adopters outside the home team.
False positive: "available to everyone"; "company-wide" for one flagship product; raw instance counts; a one-time guideline presentation; mentoring that left no independent capability.

### D13. Cross-functional influence and strategy (6, Org Leverage)
Merges FW1 C19; FR 3.5, 3.6, 3.13, §5, §6; PA 4.17, 4.18; HI Part V.
Look at: decisions changed outside design (engineering, product, research, brand, leadership); influence without authority; who disagreed and what they protected; a decision the candidate lost and what followed; the strategy chain (problem, evidence, principle, decision, trade-off, artifact, adoption, outcome, evolution); choosing high-leverage problems under ambiguity; an executive narrative; making invisible motion logic legible to non-designers.
- **3:** Communicates clearly with engineering and product; makes project-level trade-offs; influences adjacent disciplines on project decisions.
- **4:** Changes decisions, architecture, roadmap or implementation approach for teams that do not report to them; decision frameworks cut repeated debate; picks high-leverage problems without being assigned.
- **5:** A trusted neutral expert in the space between teams who changes direction, investment or system strategy and can explain rejected alternatives and second-order effects.
Proof: decision memo; decision record; roadmap change; stakeholder map; executive narrative; rollout plan; an account of a lost decision.
False positive: "led cross-functional"; "strategy" meaning a moodboard; stakeholder logos instead of changed decisions; a story with no conflict.

### D14. Expression, originality and emerging modalities (2, Craft)
Merges FW1 C22; FW0 §20 to §22A; PA 4.16, §13, §14; WB §8, §17, §25, §27.
Look at: brand turned into behavior ("playful" as controlled overshoot, asymmetric timing, brief celebratory states, plus where it may not appear); distinctive behavior that solves a problem rather than novelty; sound, haptics, material and spatial feedback coordinated rather than stacked; AI-assisted motion with a spec, evaluation criteria, rejected outputs and accessibility and performance review; streaming and probabilistic states; machine-readable motion (state schemas, tokens, component contracts). Optional lens from WB §22: utility, expressiveness, systemization, embodiment as four independent axes.
- **3:** Brand character and product semantics produce distinct behavior; patterns adapt to new surfaces.
- **4:** Reusable behavior models for multimodal or AI-forward interaction; a recognizable language coherent across contexts; AI workflows with guardrails and QA gates.
- **5:** The motion language carries across new paradigms with meaning intact; new patterns are adopted or recognized outside the author's team.
Proof: multimodal interaction model; streaming-state prototype; haptic and motion spec; AI workflow with QA gates; brand-to-behavior table.
False positive: AI demonstrator; spectacle or 3D offered as interaction proof; novelty without purpose.
In `creative-leadership` mode, brand-voice and studio-system evidence (a modular system whose consistency lives in behavior, not identical visuals) belongs here at higher weight.
