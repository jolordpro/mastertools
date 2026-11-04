# Lexicon and diagnosis

Use this when turning an adjective into a mechanism, or choosing precise words for a note. Terms are a working vocabulary, not a standard.

## Contents
1. Compound variables: what a motion is made of
2. Critique vocabulary by category
3. Vague complaint to mechanical cause to fix
4. Velocity profiles and what they read as
5. Duration is not speed; delay is not duration; the hold
6. The critique-language ladder
7. Anatomy checklist for "what should I be looking at?"
8. Judder, strobing and sub-pixel flicker

## 1. Compound variables

Any motion decomposes into interacting variables. Change one on purpose while holding the rest, or change several knowingly.

| Dimension | Variables | Question |
|---|---|---|
| Time | duration, delay, holds, cadence, repetition | How long does the viewer need to understand this? |
| Velocity | speed profile, peak, acceleration, deceleration | How should speed change over the journey? |
| Curve | easing, spring response, damping | How does it enter and leave a state? |
| Space | direction, distance, trajectory, depth, scale | Where does it appear to be going? |
| Hierarchy | primary, secondary, ambient | What should the eye follow first? |
| Physicality | mass, inertia, friction, elasticity, collision | What does it feel like it weighs? |
| Structure | sequence, loop, nesting, reset | Is this an event or a state? |
| Semantics | cause, state, progress, relationship | What does the motion communicate? |
| Perception | attention, grouping, continuity, peripheral load | How will a person parse it? |
| Expression | brand intensity, surprise, exaggeration | How much creative capital does this moment spend? |

Semantic test: if the motion were removed, what information disappears? If "nothing", it is expressive, not informational. That is allowed, but it must then justify itself by emotional value, brand value and frequency, not by "clarity".

## 2. Critique vocabulary by category

| Category | Terms | Diagnoses |
|---|---|---|
| Temporal | rushed, languid, abrupt, over-held, under-held, flat cadence, syncopated, premature resolve, delayed, cadence-flat | Timing and rhythm |
| Kinematic | weightless, inert, rubbery, floaty, mechanical, under-damped, over-damped, brittle, viscous, snappy, sluggish | Physical credibility and character |
| Spatial | unclear origin, weak destination, competing trajectories, weak continuity, excessive parallax, poor focal transfer, discontinuous | Space, hierarchy, relationships |
| Choreographic | simultaneous clutter, weak lead, no handoff, unresolved secondary motion, no anticipation, late handoff, serialized, over-layered | Sequence and event relationships |
| Narrative | no setup, weak payoff, no crescendo, premature closure, missing connective beat, unresolved beat | Story arc and pacing |
| Graphic | muddy, over-revealed, over-masked, mask leaks, morph feels arbitrary, scale jump, typographically unstable, type loses legibility | Form legibility in motion |
| Brand | generic, unowned, diluted, over-expressive, under-expressive, wrong register, off-language, inconsistent physicality | Distinctiveness and tonal fit |
| Product | decorative, ambiguous, latency-masking, state-confusing, attention-stealing, false affordance, unclear cause | Utility and meaning |
| Accessibility | vestibular burden, flashing, attention capture, excessive recurrence, motion-only meaning, poor fallback | Comfort and comprehension |
| Engineering | fragile, hard-coded, unbounded, over-coupled, non-interruptible, non-portable, expensive | Shippability and maintenance |

## 3. Vague complaint to mechanical cause to fix

Treat the causes as ranked hypotheses; confirm with the test column before prescribing.

| Complaint | Likely mechanical causes | Fix direction | Test |
|---|---|---|---|
| Feels slow | Peak velocity occurs late (first 40% of travel spent accelerating); ease-in on an entrance; long ease-out tail so the state is not actionable until late; over-long hold before or after; delay standing in for choreography; stagger extends task | Raise early acceleration, keep endpoint and duration; trim the tail not the front; shorten hold; cut or group stagger | Play at 2x; mark when the new state becomes readable/actionable versus when motion ends |
| Feels rushed / abrupt | Missing hold (state never registers); no anticipation for a large change; duration too short for travel distance or read time | Add a hold of a few frames at the landed state; add brief proportional anticipation; scale duration to distance and reading | Ask: is it total duration or an absent hold? They are different problems |
| Floaty | Under-damped spring; long low-velocity settle; exit and entrance on symmetric soft curves; no deceleration cue of mass | Raise damping or stiffness; cut the tail where velocity is barely visible; switch to a firmer ease-out | Scrub the last 25%: is it doing information work or only wasting time? |
| Bouncy / rubbery | Overshoot not justified by object semantics; settle period visible; same spring on routine and celebratory events | Reduce overshoot amplitude; critically damped response; move emphasis into the confirmation | Does the object have a reason to be elastic? |
| Mechanical / inert | Linear or symmetric easing on discrete movement; every property on the same curve; no secondary motion | Asymmetric ease matching arrival or departure; offset secondary elements; vary property timing | Reverse playback: if it looks identical, it has no physical model |
| Busy / chaotic | Many equally salient onsets; no lead event; background motion competing; stagger on everything; crossing trajectories | Establish one primary action; stagger supporting events behind it; freeze or remove secondary regions; separate x and y movement | Freeze at 20/50/80% and count changing regions; mute and ask what you notice first |
| Cheap / not premium | Default easing and one duration everywhere; linear fades; no hold; uniform stagger as the only choreography; overshoot used as polish; weak resolution; low-contrast hierarchy of timing | Define two or three timing roles, make one moment unmistakably the hero, add stillness around it, resolve decisively | Reduce to the single most important move and refine only that |
| Generic | Behavior carries no ownable idea; logo, color and type do all the identity work | Identify the signature behavior and make it explicit (physics, cadence, reveal logic, temporal texture) | Strip logo, color and type; is it still recognizably this brand? |
| Disconnected | Origin or destination unclear; unrelated layers; child lags parent on a separate curve; dismissal direction does not mirror arrival | Preserve an intelligible origin/destination, share a profile across related elements, or use a deliberate fade | Which source object maps to which destination object? |
| Flashy | Expression exceeds communicative need; amplitude, duration or concurrency too high for the moment's frequency | Reduce amplitude, duration or concurrency; reserve strong expression for milestones | What tier of the expressiveness budget is this moment? |
| Jittery / stuttery | Dropped frames; a fractional speed on fine detail; a critical speed for the frame rate; a repeating pattern aliasing; mixed frame rates; keyframe off-by-one; interpolation type switching; expression-driven noise at the wrong rate | Fix source; lock frame rate; a whole-pixel speed; slow the move or add motion blur (section 8) | Frame-advance through it; compare comp rate to delivery rate; `scripts/move_speed.py` |
| Laggy / unresponsive | Visible response arrives late relative to action; waiting for backend before acknowledging; delay before onset | Acknowledge intent immediately, then show outcome; remove onset delay | Measure input to first visible change |
| Confusing | Hard cut with no correspondence; too many simultaneous mappings; motion makes the transition harder to follow | Preserve one anchor; reduce simultaneous mappings; make the state change explicit | Can the viewer say what changed and what stayed? |
| Annoying after a while | Frequent action carries expressive motion; stagger replays on every visit; no cancellation | Shorten, make interruptible, suppress after first exposure | Repeat it 20 to 50 times |
| Hard to read (type) | Read time shorter than text needs; movement during the read window; stretch or warp harming letterforms; character-level motion on long copy | Hold the landed state for the reading time; move less during read; block or line level for longer text | Read it aloud at speaking pace; does the animation outlast the reading? |

## 4. Velocity profiles and what they read as

Inspect the velocity graph, not just position.

| Profile | Tends to read as | Good for | Risk |
|---|---|---|---|
| Near-linear | constant, mechanical, procedural | loaders, continuous indicators, deliberately engineered motion | Inert for discrete movement |
| Fast-in / slow-out (ease-out) | decisive arrival, controlled landing | entrances, focus acquisition, reveals | Abrupt if distance is small |
| Slow-in / fast-out (ease-in) | departure, release, escape | permanent exits, dismissal, handoff | Sluggish start if used on entrances |
| Symmetric ease-in-out with mid peak | energetic, cinematic | hero or expressive transitions | High attention cost; the default look nobody chose |
| Underdamped spring | lively, elastic | spatial emphasis, expressive direct manipulation | Playful or unstable |
| Near-critically-damped spring | physical but restrained | product interaction where continuity matters | Generic without semantic framing |

Semantic rule behind the curves: an object arriving needs a clear landing; an object leaving permanently can accelerate away because it is no longer relevant; an object leaving temporarily but still recoverable is conceptually nearby and should not behave like a permanent exit. Name the intent ("departure rather than arrival at an unseen resting point") before the curve.

Vocabulary for features on a curve: early peak, late peak, long tail, abrupt stop, velocity discontinuity, underdamped oscillation, excessive dwell near the midpoint.

## 5. Distinctions that fix most notes

- **Duration is not speed.** Duration is the envelope; the velocity profile is the character inside it. A 250 ms move that accelerates fast and settles slowly differs from a 250 ms linear move and from a 250 ms spring.
- **Duration versus distance.** The same 200 ms for 8 px and 900 px are not equivalent. Check scale, not just the token.
- **Delay is not duration.** Response delay (belongs to responsiveness), choreography offset (belongs to hierarchy), and motion duration (mechanics of one transformation) are separate. Delay is often used to patch a choreography problem that is really a velocity or hierarchy problem.
- **The hold is a communicative unit.** A hold is a perception budget: time to register a state, read a message, recognize the endpoint, or anticipate what is next. If a moment feels rushed, ask whether the problem is total duration or a missing hold.
- **Anticipation** should be brief and proportional in UI; it can be expressive in brand storytelling where nobody is waiting on a state change.
- **Overshoot, follow-through, settle** are a family describing what surrounds the main event. Judge them as a group.
- **Relative perception.** Motion is judged against neighbors. 200 ms feels instant beside a 500 ms page transition and sluggish beside a 70 ms press. Review in context, not in isolation.

## 6. The critique-language ladder

Aim one rung above where the conversation currently is.

| Rung | Sounds like | Limit |
|---|---|---|
| Adjective | smooth, slow, bouncy, premium, awkward | No mechanism, no action |
| Mechanics | long tail, late peak, ambiguous correspondence, excessive stagger | Correct, but silent on why it matters |
| Perception and behavior | state reconstruction cost, common-fate grouping, agency, repeated-workflow cost, read time | Local to the piece |
| System implication | missing semantic category, ownership gap, adoption barrier, token needed | The level that changes how a team works |

Example climbing one piece of feedback: "slow" -> "the panel reaches its destination early, but the last 25% is a low-velocity tail" -> "the layout is not actionable until that tail ends, which delays the next click on every open" -> "our panel and sheet tokens share that tail, so every overlay inherits it; I would split settle time from travel time in the token."

## 7. Anatomy checklist (what to look at)

- **Temporal**: duration, acceleration, deceleration, hold, delay, stagger, cadence, repetition, interruption, resolution.
- **Spatial**: origin, destination, direction, distance, trajectory, scale, depth, camera, parallax, framing.
- **Kinematic**: velocity, momentum, inertia, friction, damping, stiffness, overshoot, elasticity, collision, weight.
- **Graphic**: mask/reveal, morph, crop, opacity, typography at block/line/word/character, color transition, shape deformation.
- **Narrative** (films, opens, stings): setup, anticipation, primary event, consequence, hold, resolution; match cuts, visual rhyme, crescendo.
- **Semantic**: cause, effect, hierarchy, continuity, state, progress, focus, completion, uncertainty, relationship.

Morphology shortcut: name the relationship between old and new states (appear, disappear, reposition, expand/collapse, transform, merge/split, reorder, reveal/conceal, assemble/disassemble, environmental response) before judging mechanics. If the maker cannot name it, the motion was probably art-directed from appearance rather than meaning.

## 8. Judder, strobing and sub-pixel flicker

Movement that will not play smoothly is often the speed, not the playback. Check playback first: if the player reports dropped frames, it is a data-rate or hardware problem. If a render in a standard delivery codec at a standard data rate still judders, the speed is the cause. For a file, extract the frames (the frame-extraction step in SKILL.md) and look for repeated frames before blaming the move.

| Cause | What you see | Test | Fix |
|---|---|---|---|
| Fractional speed on fine detail | Rendered with sub-pixel positioning (the normal case): thin lines, hairline rules and small serifs pulse in brightness as they straddle pixel rows. Snapped to whole pixels (Draft quality, rounded positions): the move steps unevenly instead. Credit rolls and crawls suffer most | `move_speed.py`: the sub-pixel phase cycle (the pulse) and the snapped steps, e.g. `1 2 1` (the stutter), repeating at the same rate | A speed that is a whole number of pixels per frame (1.33 px/frame pulses or stutters; 1 or 2 does neither). Rounding positions alone swaps the pulse for the stutter |
| Critical speed for the frame rate (judder) | A detailed image or pan steps across the frame instead of gliding | Seven-second rule: the key element takes at least 7 s to cross the frame | Slow the move, add motion blur, reduce fine detail, or raise the frame rate |
| Repeating pattern aliasing (wagon wheel) | Stripes, grids, halftone or an LED texture crawl, freeze or run backwards | `move_speed.py ... pattern_px`: the apparent speed | Keep the per-frame move well under half the pattern period, or blur or soften the pattern |
| Frame rate | The same move judders far more at 24p than at 29.97, and less again at 59.94 | Compare the comp rate with the delivery rate | Ask whether the project needs 24p; higher rates reduce judder |

Numbers and limits:
- **Two symptoms, one cause.** At 1.333 px/frame a one-pixel stroke sits at phase 0, 1/3, 2/3 of a pixel and repeats every 3 frames. Sub-pixel rendering spreads it over two rows at those phases, so its peak brightness cycles (100%, 67%, 67%): that is the flicker. Snapping the same move gives steps of 1, 2, 1: that is the stutter. Name which one the viewer sees; the fix is the same.
- **Seven-second rule.** RED states it as no faster than a full image width every seven seconds, for 24 fps with a 180-degree shutter, and calls it a starting point, not a cutoff. At 1920 px and 24 fps that is about 11 px per frame. A short fast move past camera, or a swish pan buried in blur, does not need to meet it; a move the eye tracks also tolerates more.
- **Shutter angle.** A wider shutter (more motion blur) reads smoother but smeared; a narrower one reads crisper but choppier. In AE, motion blur is the cheapest fix that keeps the timing.
- **Interlaced delivery.** Interlacing widens the range of smooth motion but makes thin horizontal detail in vertical moves flicker more. Test on the delivery format, not only the progressive comp.
- **Rescue for a finished 24p render.** Interpret the render at a higher rate (30, 36 or 48 fps) and re-render that comp: every frame is kept, the piece gets shorter, and the judder usually goes. Only when the timing change is acceptable.

Sources: Rick Gerard, "Avoiding Judder in Motion Graphics" (Adobe community, reposted 2021); RED, "Camera panning speed" (red 101). The aliasing behaviour is sampling arithmetic, which `move_speed.py` computes.
