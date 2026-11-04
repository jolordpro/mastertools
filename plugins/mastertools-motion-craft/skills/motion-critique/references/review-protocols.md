# Review protocols

## Contents
1. Forensic review sequence (ten dimensions)
2. Temporal QA playback protocol
3. Interruption lab
4. Realistic-conditions QA checklist
5. Brand motion QA
6. Motion distinctiveness test
7. Gesture and async probes
8. Team-critique script and mentoring

## 1. Forensic review sequence

Go from meaning to mechanics, not from polish to meaning: user goal, state change, causal trigger, the most important perceptual relationship, temporal mechanics, edge cases, accessibility, then system fit and implementation feasibility.

| # | Dimension | Ask |
|---|---|---|
| 1 | Semantic necessity | What does the motion communicate: orientation, feedback, state correspondence, hierarchy, causality, progress, relationship, personality, error recovery? "It felt empty" and "competitors do it" are weak answers |
| 2 | Temporal mechanics | Point to a specific moment in the curve and its perceptual consequence. Is the issue peak speed, late settling, unneeded anticipation, competing events, or a mismatch between meaning and temporal shape? |
| 3 | Spatial logic | Anchors, paths, identity, hierarchy, containment, correspondence. Do elements move as systems or independent layers? Path crossings, collisions, unexplained direction changes |
| 4 | Interaction coupling | Compare input and output continuously: response delay, positional gain, thresholds, release dynamics, reversal. Prototype it, do not storyboard it |
| 5 | Interruption | Interrupt near start, middle and end; reverse; trigger a second action; resize; navigate away. Reveals whether it is a state machine or a scripted sequence |
| 6 | Workflow cost | Repeat 20 to 50 times. What was delightful once may annoy; the bar for expressive motion rises with frequency |
| 7 | Accessibility | Reduced motion as a designed branch: do hierarchy, state, causality and focus survive? Cognitive load: must the user remember transient information? |
| 8 | Performance | Realistic hardware and content: frame drops, layout thrash, paint cost, decode spikes. Perfect in the motion app but stuttering in production is an incomplete design |
| 9 | Systemization | How is the decision reused? "Copy this exact animation" is local; semantic rules, exceptions, tokens and acceptance criteria are system craft |
| 10 | Explanation | Can the reviewer or maker connect mechanics to perception and goals? Example of a model rather than a preference: "The finger controls the panel one-to-one until the dismissal threshold; on release it inherits gesture velocity into a spring settle; reduced motion keeps the immediate state change and drops travel." |

For a short live critique, order the talking: user goal, state change, semantic purpose, focal hierarchy, timing, spatial continuity, interaction risk, accessibility, implementation. This exposes whether the reviewer reaches for aesthetic fixes before understanding the behavior. The same 11-step critique sequence works as a prompt list: what is the user supposed to understand or feel; where should attention move; what is the primary event; what supports it; does timing reinforce hierarchy; does physics match intended character; does it belong to the shared language; is anything moving merely because it can; what happens under interruption; what remains true under reduced motion; can another designer or engineer reproduce it.

## 2. Temporal QA playback protocol

Do not judge motion only in real time. Each playback condition answers a different question.

| Condition | Inspect |
|---|---|
| 0.25x | Anticipation, staging, overlap, continuity, hidden technical discontinuities |
| 0.5x | Curve shape, settle behavior, sequencing, whether secondary actions distract |
| 1x | The actual feel |
| 1.5x to 2x | Sluggishness, over-long holds, over-long tails |
| Frame advance | Key poses, interpolation, jumps, visual rhythm, collisions, holds |
| Reverse (where relevant) | Whether it relies on an accidental curve or a coherent physical model |
| Sound off, first exposure | Visual clarity and hierarchy on their own |
| Visuals minimized, sound on | Whether audio carries more of the perceived structure than intended |
| Secondary-region focus | Peripheral motion competing with the task |
| Reduced-motion mode | Whether meaning survives |
| Shortened / skipped / interrupted | Whether the intended hierarchy survives |

Freeze at 20/50/80% for density. In AE: toggle the speed graph, check ease influence symmetry, step by single frames through every hold and handoff, and compare comp frame rate with delivery frame rate.

When you cannot play the footage, convert each row into a "needs-capture" entry with the exact recording you want.

## 3. Interruption lab

For any interactive motion check at minimum: complete forward; complete reverse; interrupt mid-progress; new state arriving during motion. The fourth is most diagnostic of whether design and engineering share one state model.

Name the interruption policy: cancel-to-end, reverse, retarget, preserve-velocity, snap-to-state, or ignore-until-complete. It should match the interaction and be consistent across related components.

| Motion context | Desired behavior | Reason |
|---|---|---|
| Frequent microinteraction | Immediate cancel or replace | Never make users wait for feedback |
| Direct manipulation | Input dominates timeline | User is the temporal driver |
| Navigation | Cancel or retarget where safe | Prevents dead time, preserves agency |
| Critical confirmation | May require completion feedback; must not block unrelated input | Separates acknowledgement from locking |
| Expressive celebration | May complete independently if non-blocking | Expression need not block action |
| Loading / async | Visual state reflects real task state | Stopping the animation must not imply the task stopped or completed |

Fixed-duration keyframes break when the target changes mid-flight; a spring or retargeting interpolation preserves velocity. A prototype that shows only the ideal path is a prototype illusion. The reviewer's question: draw the state machine before choosing curves.

## 4. Realistic-conditions QA checklist

- Real content, not placeholder copy; long, short, localized, enlarged text.
- Smallest and largest viewport or output format; safe areas.
- Slow and fast interaction, repetition, interruption, reversal.
- CPU and network stress; reduced-motion and other accessibility settings.
- Keyboard, touch, pointer and assistive input where relevant.
- Compare prototype and shipped build frame by frame for semantic fidelity (onset, peak, settle point, final state), not aesthetic resemblance. If they diverge, decide whether the cause is implementation constraint, a spec gap, or a detail that should be removed from the design rather than fought in code.
- Gates: input latency, frame stability, layout stability, interruptibility, semantic correctness without relying on motion alone, reduced-motion equivalence, resource cost, cross-platform differences that are deliberate.
- Regression: will changes elsewhere silently alter this behavior?

Acceptance criteria that survive platform differences: semantic fidelity, timing class, interaction coupling, endpoint correctness, accessibility branch, interruption behavior, acceptable performance variance. Frame-identical to the prototype is not the goal.

## 5. Brand motion QA

1. Can it be described with the approved motion vocabulary?
2. Does it have an identifiable brand trait without a logo?
3. Does it preserve the system's physical worldview?
4. Does intensity fit the context or dialect?
5. Does it make content clearer or merely more decorative?
6. Is there an intentional focal point?
7. Does it remain recognizable when translated to product constraints?
8. Does reduced motion preserve the communication intent?
9. Could a different designer reproduce it from the documentation?
10. Could it become a reusable pattern instead of a one-off?

If there is no documented vocabulary, skip questions 1 and 9 and say so rather than inventing a standard.

## 6. Motion distinctiveness test

Is the motion ownable, or is the brand carried by logo, color and type?

1. Strip logo, color and type wherever possible.
2. Mix the piece with competitor and generic polished work.
3. Ask for attribution and personality descriptors.
4. Look for repeated movement characteristics people can verbalize.
5. Decide whether recognition comes from motion behavior or residual visual cues.
6. Feed the result back into the vocabulary.

As a solo reviewer, run the thought version: describe what would remain if the logo, palette and typeface were gray boxes. Candidate carriers of ownership: trajectory, rhythm, physicality, transformation logic, camera behavior, typographic behavior, reveal structure, choreography, signature gesture, expressive range, temporal texture (reduced frame rate, held keyframes, stepped motion).

Generic versus potentially ownable:

| Generic | Potentially ownable |
|---|---|
| Standard ease-in/out | Brand cadence paired with a distinctive transition behavior |
| Generic fade | Identity-shaped mask or spatial reveal |
| Generic scale | Scale tied to a brand metaphor (growth, compression, emergence) |
| Generic spring | Signature stiffness and damping tied to behavioral semantics |
| Generic slide | Direction derived from identity geometry or narrative principle |
| Generic parallax | A branded spatial relationship or camera grammar |

This is a research method; as a single reviewer you can only offer a hypothesis, and should say so.

## 7. Gesture and async probes

Gesture: Can it be reversed halfway? What variable controls progress (time, distance, velocity)? Slow versus fast flick? Second gesture before settle? Release behavior and why? System interruption? Inspect the 0 to 100% continuum, not only the released endpoint. Look at touch slop, bounds, thresholds, hysteresis (entering a committed state at a different threshold than leaving it), gain changes that are not legible, resistance near boundaries.

Async truth (never imply backend state not confirmed):

| State | Useful behavior | Failure |
|---|---|---|
| Intent registered | Immediate local acknowledgement | Button looks frozen while waiting on server |
| Optimistic | Update as though succeeded, with persistent pending affordance | Implies success with no reconciliation if it fails |
| Pending | Subtle activity tied to the affected object | Global spinner blocking unrelated work |
| Success | Small localized confirmation | Large celebration for a routine action |
| Failure | Preserve context, make the failure legible, animate reversal when it explains | Object snaps back with no cause |
| Retry | Same path, clear reset | Unrelated animation obscuring whether the original is still running |
| Canceled | Return to stable state with clear result | Stale spinner or ambiguous half-state |

Rollback should preserve spatial continuity (return along a readable path) without humiliating the user with an error spectacle. Out-of-order responses should not animate a state that is no longer current.

## 8. Team-critique script and mentoring

Goal: leave the maker clearer and more capable, not just corrected. Keep it kind by being specific, causal and curious; keep it useful by naming mechanisms.

Before: maker states the intent in one or two sentences, what feedback they want, and what is locked. Agree the viewing protocol (sound off first, then on; 1x then 0.5x; once focusing on the periphery).

Run of show (about 25 to 40 minutes for a short piece):
1. **Watch** twice without talking.
2. **Observe, no solutions** (5 min): "What did you notice first, second, third? What did you think changed?" Capture on a shared board in plain language.
3. **Interpret** (5 min): "What does this communicate? How does that compare with the intent?" This surfaces mismatches early and cheaply.
4. **Diagnose** (10 min): translate reactions into mechanisms using the lexicon. "When you say it feels heavy, which part: the start, the landing, or the whole path?" Use the formula "doing X, needs Y, change Z".
5. **Propose** (10 min): each change is a testable hypothesis with an owner and a preserve clause. "Test A; it should keep B while improving C."
6. **Close**: keep list, test list, who captures what, when it returns.

Phrases that keep it constructive:
- "What I noticed was... which made me think..." (observation before judgment)
- "I think the intent is X; is that right?" (check before you correct)
- "Which of these is taste and which is mechanism?" (separate the two)
- "What would you try first, and what would you protect?" (return agency)
- "The strongest moment is..., so I would build the rest around it."

Redirects:
- "I don't like it" -> "What are you seeing that makes you feel that? Where in the timeline?"
- "Make it pop / more dynamic" -> "What should the eye land on, and what is competing with it?"
- Dominant voice -> collect written notes first, then go round the room.
- Solutions too early -> park them: "hold that; first let's agree what the problem is."
- Senior taste override -> ask them to state the mechanism or mark it as taste.

Mentoring layer: pick the one skill this piece is the best teaching case for and give a small exercise, not a lecture. Exercises from the corpus: curve decomposition (redraw the velocity profile of five admired motions); attention transfer (5-second piece with one deliberate focal handoff); physical translation (same shape as rigid, soft, magnetic, organic); brand compression (an identity reduced to three motion verbs); product translation (one expressive behavior turned into a utility one); interruption lab (a sequence that survives rapid reversal); the same-element-at-four-levels calibration (see scorecard.md). Show one iteration where something was removed or simplified; teach that removal is a skill.

Raising someone one rung on the language ladder: when they say an adjective, ask "which variable?"; when they name a mechanism, ask "what does the viewer experience?"; when they name an experience, ask "where else does this recur, and what would we change in the system?"

Self-audit prompts for the critic (use before giving notes): Can I describe the velocity profile without opening a graph editor? Can I explain why a stagger exists? Can I tell temporal problems from spatial ones? Can I tell when physics improves comprehension versus adds character? Can I explain this to a brand designer, an engineer, and an executive in different language? Can I design the reduced-motion version without deleting the meaning?
