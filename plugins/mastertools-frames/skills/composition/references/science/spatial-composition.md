---
id: spatial-composition
title: Subject placement, center bias, inward bias, representational fit
type: science
aliases: [subject placement, where to put the subject, lead room, look room, nose room, walking room, headroom, center bias, inward bias, short siding]
tags: [palmer, placement, direction, evidence-strong]
related: [balance, framing-cropping, geometry-proportion, myths-evidence, culture-direction, shot-grammar, line-direction]
evidence: strong. Center and inward biases replicated across methods, media and frame shapes.
updated: 2026-10-20
---

# Spatial composition

## Quick answer
- A lone front-facing subject is preferred at or near center. `[E-strong]`
- A subject facing or moving sideways is preferred off-center, with more space in front than behind. `[E-strong]`
- Vertical position should fit the object's meaning and ecology (lamps high, bowls low, "sinking" low). `[E-strong]`
- Departures from these defaults read as intentional tension. Use them on purpose.

## Definition
- **Placement**: where the subject's center sits in the frame (x, y as % of width, height).
- **Direction**: which way the subject faces, looks or moves.
- **Inward bias**: preference for the subject's facing vector to point into the frame.
- **Representational fit**: the frame position matches what the image means.

## Mechanism
- SAYS (Palmer et al. 2008): center bias may relate to the strong foveation of the retina. Inward bias is object-dependent and knowledge-based.
- `[Infer]` Viewers anticipate the next action. Space ahead gives the action somewhere to go; space behind reads as past or as being chased.

## Evidence
- Palmer, Gardner & Wickens 2008 `[E-strong]`
  - Three methods agreed: forced choice, adjustment, free photo-taking.
  - Front-facing objects: preference peaks at center, falls symmetrically.
  - Side-facing objects: off-center, facing in. Same for people, cars, chairs, teapots.
- Sammartino & Palmer 2012 `[E-strong]`
  - Vertical center bias plus ecological position.
  - A title that changes meaning changes preferred position.
- Inward bias outside the lab `[E-strong]`
  - Stock photography (Gardner et al. 2008).
  - Profile portraits: on average about 62% of free space sits in front of the sitter's head (Miton et al. 2020).
  - Animal artworks across centuries: more space in front of the head ("anterior bias"; Bertamini, Bennett & Bode 2011).
  - Film frames (Bode et al. 2016).
- Forman et al. 2021 `[E-strong]`
  - Across frame widths, viewers kept a roughly constant ratio of space in front vs behind the face.
  - The frame's borders drive the inward bias more than its center.
- Rule of thirds as a quality predictor is weak. See `myths-evidence`.

## Techniques
- `[Practice]` Lead room: space in the direction of gaze or motion.
- `[Practice]` Short-siding: subject faces the near edge to create unease, confinement or an ending.
- `[Practice]` Centered frontal symmetry for authority, confrontation, formality (Kubrick, Anderson).
- `[Practice]` Headroom shrinks as shots tighten; extreme close-ups crop the top of the head.
- `[Practice]` Low placement for weight, defeat, smallness; high placement for lightness, aspiration, threat from above.

## By medium
- Photography: centered square portraits are valid; thirds placement helps mainly for directional subjects.
- Design: a single hero object centered reads fastest. Off-center hero needs a counterweight (type, logo).
- Film: dialogue singles give look room toward the other speaker; reverse shots mirror it.
- Broadcast: talent framing leaves look room toward the interviewer; graphics must not sit in the look room.
- Motion: an element entering should have room ahead in its direction of travel.

## How to measure
- Subject mask (segmentation) → centroid x, y normalized 0 to 1.
- Facing vector from face or pose landmarks, or motion vector from optical flow.
- Inward score: +1 if the facing vector points toward frame center, −1 if toward the nearer edge.
- Front-to-back space ratio: free space ahead / free space behind along the facing axis.
- `[Infer]` Flag: outward-facing subject within 15% of an edge, with no stated intent.
- `[Infer]` Do not penalize a centered frontal subject.

## Failure modes
- Pushing a camera-facing subject onto a thirds line for no reason.
- Cutting lead room on a moving subject.
- Graphics or text placed in the subject's look room.
- Head touching or crowding the top edge in a medium shot.

## Critique questions
- Which way does the subject face, and is there room ahead?
- If the subject faces out, does the story want tension?
- Does the vertical position match what the subject means?
- Is the subject centered? If so, is the frame frontal and symmetric enough to justify it?

## Terms
- lead room, look room, nose room, walking room, headroom, short side, long side, center bias, inward bias, anterior bias, representational fit

## Sources
- Palmer et al. 2008; Sammartino & Palmer 2012; Gardner et al. 2008; Bertamini et al. 2011; Miton et al. 2020; Bode et al. 2016; Forman et al. 2021. Full citations in `sources`.
