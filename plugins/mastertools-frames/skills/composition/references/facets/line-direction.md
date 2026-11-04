---
id: line-direction
title: Line, direction, movement and tension
type: facet
aliases: [line, leading lines, implied line, eye line, gaze direction, vectors, directional forces, diagonals, horizontals, verticals, curves, S-curve, C-curve, tension, visual movement, implied motion, dynamism, Arnheim perceptual forces, Kandinsky point line plane, Klee]
tags: [facet, line, direction, tension, arnheim, bang, practice, measurable]
related: [shape, attention-saliency, hierarchy-focal-point, culture-direction, continuity-attention, motion-principles, depth-space, spatial-composition]
evidence: strong for gaze and pointing cues guiding attention; practice for line emotions.
updated: 2026-10-20
---

# Line, direction and tension

## Quick answer
- Gaze, pointing gestures and motion are strong attention vectors; viewers follow them. `[E-strong]`
- Horizontals read calm, verticals poised or upright, diagonals active, curves graceful. `[Practice]`
- Make lines, gazes and motion converge on the focal point. Tension comes from instability: diagonals, crowded edges, off-balance mass, crops at joints. `[Practice]`

## Definition
- **Actual line**: edges, contours, roads, rails, architecture.
- **Implied line**: gaze, pointing, gesture, a row of points, motion paths.
- **Vector** (directional force): any element that points somewhere.
- **Tension**: felt instability that asks to resolve.

## Mechanism and evidence
- Gaze cueing: viewers reflexively shift attention toward where a depicted face looks. `[E-strong]` `[Unverified: effect size and timing]`
- Smith 2012: editors exploit off-screen sounds, conversational turns, motion, gaze cues and pointing gestures to steer attention. `[E-strong]`
- Arnheim: visual elements carry "directed tension" and perceptual forces. `[Practice] [Unverified]`
- VFCNet 2026: composition type can be read largely from saliency plus gradient-vector flow of edges, suggesting edge flow captures what humans call lines. `[E-mixed, recent]`

## Line emotions `[Practice]`
- Horizontal: rest, calm, stability, landscape.
- Vertical: strength, dignity, growth, aspiration.
- Diagonal: movement, energy, instability, conflict.
- Curves, S-curves: grace, flow, sensuality, meandering travel.
- Converging lines: depth, destination, focus.
- Broken or zigzag lines: agitation, danger.
- Rising left-to-right diagonal (in Western reading): ascent, progress. `[Infer]`

## Techniques
- `[Practice]` Leading lines that end at the subject, not out of the frame.
- `[Practice]` Gaze chains: one character looks at another, who looks at the object.
- `[Practice]` Dutch angle for unease or disorientation.
- `[Practice]` Counter-diagonal crossing for conflict.
- `[Practice]` Crop at joints (wrists, knees) only when you want tension; otherwise crop mid-limb.
- `[Practice]` Tangents (two edges touching) create unwanted tension; separate or overlap clearly.
- `[Practice]` Lines exiting at corners pull the eye out; block them with a stopper element.

## By medium
- Photography: roads, rails, shorelines; tilt changes the line's emotion.
- Design: alignment edges are implied lines; strong verticals and horizontals from grids.
- Film: screen direction is a line that persists across cuts; camera moves create lines over time.
- Broadcast and motion: graphic wipes and slides are directional vectors. Direction should agree with play, data and reading direction.

## How to measure
- Line segment detection (OpenCV LSD or Hough) → orientation histogram (horizontal, vertical, diagonal shares).
- Convergence: intersection density of extended lines; distance of convergence point to subject.
- Gaze vectors from face landmarks; pointing from pose; motion from optical flow.
- Check whether vectors terminate inside the subject mask.
- Horizon tilt in degrees (flag unintentional tilt under about 3°). `[Infer]`
- Tangent detection: near-touching edges of separate segments.

## Failure modes
- Strong line leading out of the frame or away from the subject.
- Slightly crooked horizon that reads as a mistake, not a choice.
- Gazes pointing at empty space with no payoff.
- Tangents and edge kisses.

## Critique questions
- Where do the lines and gazes lead?
- Is the tension intended and resolved where the story wants?
- Is the horizon level, or tilted enough to read as a choice?

## Terms
- leading lines, implied line, eyeline, vector, diagonal, S-curve, convergence, tangent, Dutch angle, tension, directed tension, screen direction

## Sources
- Arnheim 1954/1974; Bang 1991; Kandinsky 1926; Klee 1925; Smith 2012; VFCNet 2026; Freeman 2007.
