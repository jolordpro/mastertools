# Scorecard, axes and calibration

## Contents
1. The 12-dimension scorecard
2. How to score
3. Four independent axes
4. Calibration ladder: the same element at four levels
5. Worked calibration: a lower third
6. Alternative rubric lenses

## 1. The 12-dimension scorecard

Scores are 1 to 5 and diagnostic, not a verdict. Every score of 3 or below gets a revision hypothesis (what I would change and what I expect it to improve). A scorecard without hypotheses is a grade; with them it is a plan.

| Dimension | What a 5 means | 1 looks like | Evidence to look for |
|---|---|---|---|
| Intent | Clear communicative job, stated or inferable | Cannot say what it is for | Can the maker or viewer state the job in one sentence? |
| Brand ownership | Behavior feels proprietary, not generic | Logo, color, type do all the work | Strip-it test; recurring verbs, cadence, physicality |
| Hierarchy | Directs attention correctly | Everything equally salient | Muted playback; 20/50/80% freeze count |
| Timing | Pacing matches communicative importance | One tempo everywhere; late peak; wrong holds | Velocity graph; read time; 2x playback |
| Physics | Weight, acceleration, overshoot and settle feel intentional | Weightless, floaty or rubbery by accident | Reverse playback; settle tail; spring parameters |
| Choreography | Elements cooperate rather than compete | Clutter, no lead, no handoff | Attention route; overlap; common fate claims |
| Restraint | No unnecessary movement or decoration | Moves because it can | "What was deliberately not animated?" |
| Context fit | Belongs to the right dialect and frequency tier | Flagship behavior on routine events, or reverse | Expressiveness-budget tier vs. actual frequency |
| Accessibility | Reduced motion preserves meaning; flash, vestibular and cognitive load considered | Meaning only in motion; flashing; no fallback | Reduced-motion branch; peripheral motion; photosensitivity check |
| Implementation | The behavior can be built and maintained reliably | Prototype illusion; fragile; expensive | Property choices, frame rate, interruption, real content |
| System fit | Reinforces reusable language and patterns | One-off that conflicts with neighbors | Naming, tokens, reuse, exceptions documented |
| Memorability | Important moments have enough signature character | Interchangeable with any template | Is there one moment someone would describe later? |

Mark a dimension "not assessable" when you lack the evidence (for example Implementation from a video alone, or Physics from a still). Do not guess a number. Report scores as "x of y assessed" if several are missing.

## 2. How to score

- Score against the stated intent and context dialect, not against an abstract ideal. A 4 on Restraint for a news package differs from a 4 for a design-system toggle.
- Frequency matters. Context fit and Restraint are judged against how often the motion occurs.
- Do not average into a single headline number unless asked. Averages hide a 1 in Accessibility or Intent, which can veto an otherwise strong piece. State vetoes explicitly (photosensitivity risk, motion that lies about system state).
- Be consistent and show the evidence for each score in a clause. If two reviewers would argue about a score, the evidence clause should show why.
- The "5" bar is rare; most strong shippable work is a 3 to 4 on most rows. Use 5 where the work would change how the team thinks.

## 3. Four independent axes

Score separately; do not collapse into one rank.

| Axis | Low | High |
|---|---|---|
| Utility | Merely decorates | Materially improves orientation, feedback, efficiency, comprehension (lower uncertainty, not just faster) |
| Expressiveness | Neutral and quiet | Distinctive personality, emotion, rhythm, surprise coupled to context |
| Systemization | One-off | Reusable primitives, semantic patterns, tokens, governance, adoption |
| Embodiment | Screen-only | Input, haptics, sound, material and spatial behavior agree |

A broadcast open may be low on Utility and Systemization by design and very high on Expressiveness. Say that; do not penalize it for the wrong axis. A system toggle should be the opposite.

Frequency-weighted expressiveness budget (use to check Context fit):

| Tier | Frequency | Expression | Examples |
|---|---|---|---|
| Utility | very high | low | hover, focus, press |
| System | high | low to moderate | navigation, panel, common state change |
| Signature | medium | moderate | brand-coded reveal, recurring behavior |
| Milestone | low | high | completion, first use, major transformation |
| Flagship | rare | very high | launch, campaign, show open, major narrative moment |

Failure pattern: flagship behavior leaking into utility tier.

## 4. Calibration ladder

For `calibrate` mode, take one element and describe it at four levels so the bar becomes visible.

| Level | Character | What changes |
|---|---|---|
| 1 Decorative | Motion exists to look animated | Default ease, one duration, fade or slide-in; no stated job |
| 2 Competent | Clear intent, decent execution | Intent clear, sensible easing by role, feedback and continuity considered; edge cases absent |
| 3 Strong | Meaningful hierarchy, timing, continuity | Temporal hierarchy, input coupling or read-time logic, interruption/responsive content handled, reduced motion with preserved meaning, real-content tested |
| 4 Benchmark | Changes how others work | Reusable pattern or template with semantic names and tokens, implementation guidance, QA criteria, governance, adoption; or for brand work, a signature behavior others can reproduce |

For each level write: intent, timing with values, physics, choreography, robustness, accessibility, system thinking, and "what a reviewer would say". Make the differences between adjacent levels concrete (a number, a state, a rule), not adjectival. End with the one change that moves it up one level.

Scoring anchors for whole case studies: 1 decorative; 2 competent; 3 strong; 4 exceptional (sophisticated behavior, reuse, strong accessibility and performance, fidelity); 5 benchmark (changes how the product or organization thinks, with evidence of adoption).

## 5. Worked calibration: a lower third (broadcast)

- **Level 1**: Name bar slides in from left over 20 frames, linear ends; text fades with it; sits; reverses out. Same timing on every use. No stated read time.
- **Level 2**: Ease-out in, ease-in out, bar leads text by 3 frames, 2-second hold, safe-area correct, legible at distance. Works for the one name length it was built for.
- **Level 3**: Hold length derives from character count (words per second reading rate plus a fixed floor); entrance asymmetric (decisive in, quieter out); handles long names and two-line titles without reflow jumps; secondary line arrives after the name has landed; behaves if the operator triggers out early; flat-color fallback for the reduced-motion/clean-feed version; no flashing elements; tested on live-data strings.
- **Level 4**: Packaged as a rig: duration and hold exposed as controls tied to text length, expression-safe, named layers, documented timing roles (arrive, read, depart), a family of variants (name, topic, breaking) that share one physical language, QA checklist, and a clear signature behavior (for example a distinctive mask-reveal tied to the brand shape) so it remains recognizable with the logo removed.

Same exercise for a product toggle: L1 snap with a spinner; L2 150 ms ease and a color change; L3 retargetable on rapid retap, persistent state not dependent on a flourish, optimistic with truthful pending/failure, reduced-motion preserved through color and label; L4 a semantic "selection.change" token with reduced branch, tests, adoption guidance.

## 6. Alternative rubric lenses

Use only when the user asks for a different framing.

- **100-point forensic rubric** (for portfolio or senior-level evidence): Meaning 10; Timing/velocity 10; Spatial continuity 10; Choreography 8; Interaction coupling 10; Interruption/state 10; Feedback/causality 8; Cognition/perception 8; Accessibility 8; System/governance 8; Implementation/performance 5; Influence/teaching 5. Competent evidence is local and adequate; Staff evidence defines semantic categories, models state and retargeting, redesigns reduced motion, defines tokens and adoption.
- **Portfolio weighting**: Motion craft 25; Interaction logic 20; Product reasoning 15; Systems thinking 15; Implementation fluency 10; Accessibility 5; Cross-functional influence 10.
- **Evidence hierarchy**: a hero animation proves local craft; an interactive prototype proves behavioral thinking; a spec proves rigor when it encodes semantics and variants; a shipped component proves implementation collaboration; a pattern adopted by several teams proves system thinking; documented standards with measurable adoption prove organizational influence. A strong portfolio shows the problem first, an iteration where something was removed, an edge-case prototype, what became a rule versus what stayed bespoke, how engineering shipped it, and the accessibility branch.
- **Red flags that look impressive but score lower**: long choreographed intros on ordinary interactions; dramatic easing on high-frequency controls; 3D or WebGL offered as proof of interaction sophistication; only ideal-path demos; no cancellation, reversal or async example; no reduced-motion discussion; specs with many timings and no semantic taxonomy; AE clips where runtime state is required; system claims without adoption evidence; "delight" or "magic" language with no user impact.
