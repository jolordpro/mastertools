---
id: motion-principles
title: Composition in motion (timing, easing, staging, choreography)
type: domain
aliases: [motion design principles, animation principles, Disney 12 principles, easing, ease in ease out, slow in slow out, timing, spacing, staging, anticipation, follow through, overlapping action, arcs, secondary action, choreography, stagger, transitions, kinetic typography]
tags: [motion, animation, broadcast, practice]
related: [broadcast-standards, visual-structure, continuity-attention, gestalt, attention-saliency, line-direction, rhythm-pattern, reframing]
evidence: practice for animation principles; strong evidence that motion onset captures gaze and common fate groups.
updated: 2026-10-20
---

# Composition in motion

## Quick answer
- Motion is the strongest attention magnet in a frame, so animate only what must be seen now. `[E-strong]`
- Elements moving together read as a group (common fate). Use it to group or separate. `[E-strong]`
- Composition in motion is a sequence of compositions: every resting frame should hold up as a still. `[Practice]`

## Evidence anchors
- Motion onset and flicker capture gaze and synchronize viewers (Mital et al. 2011; Smith & Mital 2013). `[E-strong]`
- Common fate is a core Gestalt grouping cue (Wagemans et al. 2012a). `[E-strong]`

## Disney's 12 principles (Thomas & Johnston 1981) `[Practice]`
- Squash and stretch: mass and flexibility.
- Anticipation: prepare the viewer for the action.
- Staging: present one idea clearly at a time.
- Straight ahead and pose to pose: two working methods.
- Follow-through and overlapping action: parts settle at different times.
- Slow in and slow out: easing.
- Arcs: natural motion follows curves.
- Secondary action: supports, never competes with, the main action.
- Timing: number of frames sets weight and mood.
- Exaggeration: push for clarity.
- Solid drawing: volume and weight.
- Appeal: charisma and clarity of design.

## Graphics-specific practice `[Practice]`
- Choreography: a planned order of entrances that mirrors the reading hierarchy.
- Stagger: offset starts so elements read in order; keep offsets consistent in a package.
- Easing: no linear moves for objects that have mass; strong ease-out for arrivals reads confident.
- Directional logic: elements enter from where they "come from" and exit where they "go."
- Hold the resting state long enough to read (see `broadcast-standards`).
- Transitions should carry the eye from the outgoing focal point to the incoming one (eye trace).
- Reduce motion in secondary elements while primary information is read.
- UI motion durations commonly run about 100 to 500 ms. `[Practice] [Unverified; check platform guidelines]`

## Composition checks for motion
- Freeze-frame test: pause at every hold and every midpoint. Does each frame compose?
- First and last frame: both must be strong; they are the thumbnails and the cut points.
- Path design: motion paths are lines (see `line-direction`); arcs and diagonals feel alive, flat linear slides feel mechanical.
- Rhythm: align beats to music; vary intervals to avoid monotony (see `rhythm-pattern`).

## By medium
- Broadcast packages: system-wide motion language (verbs, durations, easing family) so every asset feels related.
- Title sequences and opens: Block-style intensity curve (see `visual-structure`).
- Social: first 1 to 2 seconds must state the idea; motion hooks early. `[Practice]`

## How to measure
- Optical flow per region over time → where motion is when text must be read.
- Keyframe data (After Effects export or Lottie JSON) → easing curves, durations, stagger offsets.
- Freeze-frame sampling → run still-image metrics on holds.

## Failure modes
- Everything moves at once; nothing reads.
- Linear interpolation on heavy objects.
- Secondary loops (shimmers, particle drift) competing with text.
- Holds too short to read.

## Critique questions
- What should the eye see at each beat, and is that the only thing moving?
- Does every hold work as a still composition?
- Do motion directions agree with the story and the reading direction?

## Terms
- timing, spacing, easing, ease in, ease out, overshoot, anticipation, follow-through, overlap, arcs, staging, stagger, choreography, hold, eye trace, motion language

## Sources
- Thomas & Johnston 1981; Mital et al. 2011; Smith & Mital 2013; Wagemans et al. 2012a. For detailed motion critique use the motion-critique and motion-system-architect skills.
