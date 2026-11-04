# Perception science for critique

These are the perceptual reasons behind the notes. Use them to explain why, not to claim timing laws. The corpus is explicit that exact thresholds are heuristics, and that several organizing models here (perception stack, expressiveness budget) are synthesis built from research plus platform guidance, not published standards or something a company formally uses.

## Contents
1. Motion as information and as cost
2. Attention capture and the attention budget
3. Common fate: motion makes claims about membership
4. Continuity, correspondence, change blindness
5. Event segmentation: starts, boundaries, stable landings
6. Agency, latency and perceived responsiveness
7. Motor effects: Fitts, steering, moving targets
8. Waiting, loading and truthfulness
9. The perception stack
10. Attention choreography
11. Cautions

## 1. Motion as information and as cost

Motion encodes sequence, causality, continuity, attention and state in time. It improves things when it makes information easier to perceive than an instant change would. It is poor when it adds time cost, attention cost, or sensory burden without a commensurate gain. The useful benchmark is semantic information per unit of attentional cost, not maximum "clarity through movement".

The chain: state change -> perceptual signal -> interpretation -> action. A note should say where in that chain the motion helps or breaks.

## 2. Attention capture and the attention budget

Motion onset can capture attention even when the viewer is looking elsewhere, so motion works like an alert channel more than like decoration. The more motion on screen, the less discriminable any one movement. Choreography behaves like typography: it sets emphasis, grouping, rhythm and reading order.

Critique use:
- Map the attention route: intended first fixation, second region, stable landing. Compare with what the motion alone would draw the eye to (mute, ignore static styling).
- Ask what moves in the periphery while the viewer reads or acts. Reviewers who audit only the focal transition miss the most disruptive behavior.
- One distinctive motion among stable neighbors is highly legible; crossing trajectories, similar velocities and simultaneous onsets make objects easy to confuse.
- Density audit: freeze at 20%, 50%, 80% and count simultaneously changing regions. Five unrelated regions demanding tracking is high density: legitimate for a hero moment, a liability for routine tasks.

## 3. Common fate

Elements that move together are grouped. Shared motion is therefore a claim about membership. If an image, title and button translate as one object, the motion says they are one transformation. If the image moves while the title fades from elsewhere, the motion says two objects, whatever the static layout says. The reverse failure: unrelated elements that accidentally share a curve and vector get read as related. Treat accidental synchronization as a semantic defect when it implies the wrong grouping. Motion can also separate things that look alike statically.

## 4. Continuity, correspondence, change blindness

When a screen changes, viewers must work out what is new, what persisted, what moved, what was replaced. A good transition externalizes some of that reasoning. Animated viewpoint and graph transitions help when the transformation preserves correspondence the viewer benefits from tracking, and can hurt when many things change at once with weak mappings.

- Object constancy: can they track what stayed the same? State reconstruction: can they infer what changed? Strong transitions support both.
- Continuity has several kinds: object, spatial, semantic, causal, temporal, hierarchical, interaction. Name which one the piece is protecting. A shared-element transition is one means, not the goal; a diagonal sweep may look polished and preserve nothing.
- Change blindness: simultaneous multi-property changes, changes outside attention, and hard cuts with no correspondence get missed. Motion can mark a change that matters. If everything moves, nothing is distinctive.
- Ask: which source object maps to which destination? Is that mapping obvious? Too many simultaneous mappings? Is the viewer forced to track something unimportant?
- Chart transitions that reorder unpredictably can be less informative than a clean replacement if correspondence cannot be tracked.

## 5. Event segmentation

People segment activity into events using movement cues and goal structure. The start of an animation sets an event boundary, the trajectory reveals the transformation, the end establishes the new stable context. Several regions updating with unrelated timing blur the boundaries. A product that continuously morphs and reorders loses the distinction between action and consequence. Good motion creates continuity where correspondence matters and clear boundaries where the task needs a new context. The final resting state matters most: it is what the viewer acts on or reads.

## 6. Agency, latency, perceived responsiveness

Sense of agency depends on temporal and spatial correspondence between action and effect. A system can be fast at the backend and still feel unresponsive if the visible consequence is disconnected from the action. Immediate acknowledgement can establish agency while work continues. Response thresholds of roughly 0.1 s, 1 s, 10 s are useful heuristics for thinking about perceived rather than measured latency, not laws.

Latency path stages worth separating: input capture, immediate acknowledgement, computation or network, reconciliation, visual transition, final confirmation. Immediate feedback says "I heard you"; intermediate says "working"; terminal says "done or failed". Motion collapses these accidentally: a checkmark that arrives before the system has committed is a lie.

Trust is congruence: pressing Save should not animate an unrelated region; a dragged card should respond under the pointer, not via a delayed proxy.

## 7. Motor effects

Motion changes the motor task. A menu that slides into the pointer path creates a steering problem; a button that scales away as the user clicks changes target width at the worst moment; a growing hit area helps acquisition; a table that reflows while the user aims makes them lose the row. Duration, travel and settle should be judged against what the user is trying to hit.

## 8. Waiting, loading, truthfulness

Loading animation has three jobs: represent state, occupy attention selectively, avoid making the wait feel longer. Studies find continuous motion can shorten subjective waiting versus a static symbol, with effects depending on speed and involvement; moderate speeds did best in the studied incidental waits. Treat that as a hypothesis to test, not "always animate loading".

Semantics differ: indeterminate says activity, not duration; determinate says measurable progress; a skeleton says structure and reserves geometry; shimmer adds activity but not progress. A progress-like animation over work with no meaningful progress is a false promise; an inert indicator can make working software look broken. Skeletons lose their value if the final content shifts dimensions or position.

## 9. The perception stack

Detection -> grouping -> tracking -> interpretation -> response. A design model, not a claim about the brain.

| Stage | Question | Failure |
|---|---|---|
| Detection | Is the change salient enough to notice? | Important change missed |
| Grouping | Which elements belong together? | Unintended relationships inferred |
| Tracking | Can the viewer follow the object or state? | Continuity lost |
| Interpretation | What does it mean? | Ambiguous or misleading state signal |
| Response | What should happen next? | Motion does not support agency |

## 10. Attention choreography

Acquire -> emphasize -> transfer -> release -> recover.

| Operation | Controls | Diagnostic |
|---|---|---|
| Acquire | arrival, contrast, onset, scale change | What makes this the next thing worth looking at? |
| Emphasize | velocity, amplitude, duration, uniqueness | Is emphasis proportionate to importance? |
| Transfer | spatial bridge, shared motion, sequencing | How does the eye know where to go next? |
| Release | settle, fade, stillness, removal | When is the attention demand over? |
| Recover | interrupt, cancel, re-entry, restoration | What if the user acts before it ends? |

Temporal hierarchy: the first change gets more attention than the third; the element that settles last becomes the implied conclusion; a short sharp cue can dominate a long subtle movement. Variation creates texture; emphasis creates meaning. A sequence with two or three clear timing roles can be clearer than one with different timings everywhere.

Exits: in many contexts the outgoing element should leave quickly and quietly while the incoming state earns attention. Giving the exit as much drama as the entrance is a common beginner error.

## 11. Cautions

- Perceptual findings support the reason a note works; they do not hand you millisecond prescriptions. Say "heuristic" when you give a number.
- Platform durations (for example 83/167/250 ms in one system, 70 to 700 ms scales in another, 50 to 150 ms for interactions and 150 to 400 ms for larger transitions in a third) differ and converge only on the idea that frequency, size and importance should set duration.
- Much of the evidence is from product and visualization research. For broadcast and film, rely on editorial and viewing-context reasoning (see context-dialects.md) and be honest where there is no direct evidence.
- Several organizing frameworks in the corpus are labeled synthesis. Present them as useful models, not as how any named company operates.
