# Failure modes

Name the pattern, state the cause, and prescribe what an expert does. Naming a failure mode is a shortcut to the diagnosis, not a substitute for it: always point to the evidence in the piece.

## Contents
1. Craft and aesthetic failures
2. Interaction and product failures
3. Brand and system failures
4. Accessibility and honesty failures
5. Process failures (prototype and handoff)
6. Reviewer failures (how critique goes wrong)

## 1. Craft and aesthetic

| Failure | Looks like | Cause | Expert move |
|---|---|---|---|
| Curve fetishism | Hours on curve choice, no semantic reason | Easing treated as an aesthetic palette | Define curve families by meaning (arrival, departure, in-place change) |
| Smoothness fetish | Everything smooth, not necessarily understandable | Aesthetic criterion replaces semantic analysis | Identify the information purpose; remove motion that does not help |
| Physics theater | Springs everywhere because they feel modern | Physics used as novelty | Classify behaviors by meaning; use springs where state or input dynamics justify them |
| Spring everywhere | Every state bounces; frequent actions pay for the personality | Physics as default personality | Reserve overshoot for moments that earn it; tighten for routine |
| Choreography inflation | Every element has its own entrance | Sequence mistaken for quality | Define focal hierarchy and concurrency budgets |
| Stagger tax | Lists and dashboards reveal serially every time | Choreography mistaken for hierarchy | Group, adapt, or suppress after first exposure; stagger only when it carries meaning |
| Preset worship / motion monoculture | One easing and duration everywhere; same rhythm for every event | Parameters mistaken for system rules; over-constrained system | Separate invariants from variables; semantic classes with contextual scaling |
| Cinematic workflow | Long sequences delay basic actions | Showmanship over repetition cost | Shorten, make interruptible, or remove |
| Template ossification | Toolkit produces repetitive work | Consistency over creative range | Controlled variants and escape hatches |
| Dead keyframes | Moves with no hold, no beat, no stillness; no rest state | Continuous motion mistaken for energy | Add holds and rest; stillness is what makes motion legible |
| Broken solidity | Objects hover above the surface they should rest on, pass through a solid, or appear from inside it; debris sprays from nowhere | Contact and collision never modeled; each object keyed alone | Treat every solid as solid: rest objects on surfaces with a contact cue (shadow, settle), give solids collision, and scatter debris from where the break happens with varied direction and timing. Check it frame by frame at the contact frames |
| Harsh camera or light | Camera starts or stops abruptly, whips where it should sweep; light pops on or jumps in intensity | Camera and lights keyed like UI elements, with short linear or default eases | Long, gradual ease in and out on camera and light; let the camera sweep in an arc; fade light changes the way a studio dims, never a step |
| Dead gap at the cut | One beat ends, a frame or more of nothing, then the next starts; motion direction resets at every cut | Each piece built alone, never played after the clip before it | Review the transition in context with the outgoing clip; carry direction and speed across the cut, overlap the beats so there is no dead air |
| Repeated or split words | A key phrase repeats across shots; a sentence spreads over several shots and stops reading as a sentence | Copy laid over the edit without checking read order | One phrase per shot, no repeats; if a line will not fit a shot, move it onto the shot or cut the shot shorter. Read the edit aloud with the cuts |

## 2. Interaction and product

| Failure | Looks like | Cause | Expert move |
|---|---|---|---|
| Teleportation | Objects jump between states with no usable correspondence | Transitions designed as screenshots | Preserve a meaningful anchor or make the change explicit |
| Scripted-animation trap / prototype illusion | Works in the demo, fails under interruption or real data | Timeline treated as behavior model | Prototype states and edge cases, not playback |
| Stale animation | Finishes an old state; contradicts current feedback | No interruption policy; request-driven visuals | State machine; retarget; ignore out-of-order responses |
| Motion as sole feedback | Important state carried only by movement | Accessibility and redundancy omitted | Add persistent visual or semantic cues, alternative channels |
| Scale-blind motion | Same duration for 8 px and 900 px | Token applied without judgment | Scale duration with distance and size; use ranges or classes |
| Moving target | Menu slides into pointer path; button scales away at click; list reflows under aim | Motion changes the motor task unexamined | Keep hit geometry stable; stage the movement away from the aim |
| Layout motion tax | Whole screen shifts, user loses their row or reading position | Layout animated where content update would do | Update layout instantly or preserve the anchor |
| Bright shimmer skeleton | Loading skeleton brighter than the UI around it, with a fast light-wipe sweep | The library default shimmer, copied | Keep skeletons darker than the surface, low contrast, slow and spread out; the content arriving is the event, not the placeholder |

## 3. Brand and system

| Failure | Looks like | Cause | Expert move |
|---|---|---|---|
| Brand cosplay | Product uses the campaign animation literally | Expression not translated into utility | Make context dialects; translate the verb, not the spectacle |
| AI genericity | Polished but interchangeable | Optimizes plausibility over specificity | Encode grammar, constraints and evaluation; review for the distinctiveness test |
| Perceptual debt | Looks correct in the static spec, confuses in use | QA ignores real-time attention and interruption | Test complete workflows and interruption states |
| System theater | Token library exists; teams do not adopt it | Governance detached from workflow and tooling | Integrate into components, code, reviews, education |
| Exception sprawl | Every team has a special case | No taxonomy or divergence governance | Require an explicit reason, document it, track a divergence budget |
| Semantic inconsistency | Same meaning, different motion; or different meaning, same motion | Consistency pursued as identical parameters | Equivalent actions share motion; different meanings differ |
| Expressive leak | Flagship behavior on a high-frequency control | No expressiveness budget | Tier by frequency; reserve high expression for rare moments |

## 4. Accessibility and honesty

| Failure | Looks like | Cause | Expert move |
|---|---|---|---|
| Accessibility afterthought | Reduced motion just disables animation | Meaning encoded in movement with no alternate | Redesign the semantic signal: fade, highlight, focus move, immediate state |
| Peripheral motion | Something loops beside the thing being read | Only the focal transition audited | Audit what moves in the periphery during reading or tasks |
| Flash and pattern risk | Rapid luminance flashes, strobing, high-contrast patterns | Impact effects without a safety check | Reduce flash rate and area; test with the relevant analyzer; see context-dialects.md |
| False progress | Animation implies advancement that is not real | Perceived performance optimized without truth | Align progress representation with actual state |
| Early success | Checkmark before the system has committed | Visuals decoupled from state | Acknowledge intent, then outcome; show pending honestly |
| State loop that lies | "Thinking" loop implies certainty or progress that does not exist | Looping motion used as reassurance | Indeterminate where unknown; state vocabulary for AI states |
| Rollback spectacle | Failure is theatrical or teleports the object | Error motion designed to attract, not to help recovery | Return along a readable path; localize emphasis; actionable recovery |

## 5. Process: prototype and handoff

| Failure | Looks like | Expert move |
|---|---|---|
| Spec of numbers without semantics | Many timing values, no taxonomy, no meaning | Name behaviors by meaning; include trigger, states, interrupt policy, reduced branch, acceptance criteria |
| Handoff as a clip | Video delivered where runtime state is required | Prototype in the runtime or deliver a state-aware asset (Rive, state machine) |
| Fidelity drift | Build differs from prototype and nobody can say how | Compare onset, peak, settle, end state frame by frame; decide spec gap vs. constraint vs. detail to remove |
| Design-tool truth only | Looks right in AE or Figma, stutters in production | Test on target hardware and content; know which properties are cheap |

## 6. Reviewer failures

- **Adjective feedback** ("make it pop"). Climb the ladder: variable, perception, system.
- **Solution first.** Proposing fixes before agreeing on the problem; run diagnosis before prescription.
- **Polish before meaning.** Tuning ease influences on motion that should not exist.
- **Taste as truth.** Present preference as defect. Label taste.
- **Ideal-path review.** Judging only the uninterrupted, placeholder-content playback.
- **Number worship.** Quoting millisecond values without semantic context or distance, size and frequency.
- **Critic's inflation.** Always asking for more motion, more dynamics. Often the right note is less.
- **Pretending to have watched.** Describing look and feel from a spec or a still. State your evidence ceiling.
- **Over-generalizing a system's rules.** Treating one platform's curves or durations as laws; each system optimizes for its own goals and the overlap is the durable part.
- **Praise-free notes.** Without a preserve clause the maker may revise away the best part.
