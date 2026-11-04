---
id: depth-space
title: Depth and space
type: facet
aliases: [depth, space, depth cues, monocular cues, occlusion, overlap, atmospheric perspective, aerial perspective, linear perspective, vanishing point, foreground midground background, planes, deep space, flat space, limited space, ambiguous space, deep focus, staging in depth, Cutting and Vishton]
tags: [facet, depth, cutting-vishton, block, bordwell, evidence-strong]
related: [framing-cropping, value-contrast, color, camera-lens-movement, visual-structure, line-direction, photo-craft]
evidence: strong for the cues themselves; practice for stylistic use.
updated: 2026-10-20
---

# Depth and space

## Quick answer
- Occlusion is the strongest ordinal depth cue at every distance. `[E-strong]`
- Stack cues (overlap, size change, aerial perspective, focus falloff, converging lines) for deep space; strip them for flat, graphic space. `[Practice]`
- Choose the space type on purpose; mixing them unintentionally reads as confused. `[Practice]`

## Definition
- Depth cues per Cutting & Vishton 1995: occlusion, relative size, relative density, height in visual field, aerial perspective, motion perspective (parallax), binocular disparity, convergence, accommodation.
- Block's four space types `[Unverified]`
  - Deep: emphasizes the third dimension.
  - Flat: emphasizes the picture plane.
  - Limited: deep cues used sparingly or only in parts.
  - Ambiguous: viewers can't read size or distance.

## Evidence
- Cutting & Vishton 1995 `[E-strong]`
  - Effectiveness measured as an ordinal depth-contrast threshold; 10% depth contrast as the practical threshold.
  - Three zones: personal (about 2 m), action (about 2 to 30 m), vista (beyond 30 m).
  - Occlusion strongest at all distances; binocular disparity strongest within a few meters; aerial perspective matters most at vista distance.
- Shading and texture gradients also support shape and depth. `[E-strong]` `[Unverified: relative cue weights]`

## Techniques
- `[Practice]` Three planes: foreground element, subject in midground, background context.
- `[Practice]` Foreground framing (branches, doorways, shoulders) for depth and intimacy.
- `[Practice]` Diagonal recession instead of planes parallel to the frame.
- `[Practice]` Lighter, lower-contrast, cooler background (aerial perspective).
- `[Practice]` Shallow focus isolates; deep focus lets the viewer choose (Welles and Toland, *Citizen Kane*). `[Unverified]`
- `[Practice]` Staging in depth: actors placed along the lens axis to show relationships without cutting (Bordwell). `[Unverified]`
- `[Practice]` Wide lenses exaggerate depth; long lenses compress it (see `camera-lens-movement`).
- `[Practice]` Flat space for graphic power (Anderson's planar tableaux, poster design).

## By medium
- Photography: aperture and focal length control depth rendering.
- Film and camera moves: parallax from a moving camera is a strong depth cue; dolly and crane moves reveal space.
- Broadcast and motion graphics: parallax layers and depth of field add dimension; keep text on a flat readable plane.
- Design: overlap and drop shadows create shallow depth; keep it consistent.

## How to measure
- Monocular depth estimation (Depth Anything V2) → histogram of depth → count of distinct planes.
- Occlusion detection from segmentation overlaps.
- Contrast and saturation vs estimated depth (aerial perspective present?).
- Blur map vs depth (focus falloff).
- Vanishing point detection from line segments.

## Failure modes
- Subject merges with background of the same depth, value and focus.
- Background more contrasty and saturated than the subject.
- Mixed depth cues that contradict (scale says far, sharpness says near).
- Everything on one plane when depth is wanted.

## Critique questions
- How many planes, and which one holds the subject?
- Which depth cues are working, and do any contradict?
- Is the space type (deep, flat, limited, ambiguous) intended?

## Terms
- occlusion, relative size, relative density, height in field, aerial perspective, motion parallax, disparity, vanishing point, foreground framing, planes, deep focus, shallow focus, staging in depth, compression

## Sources
- Cutting & Vishton 1995; Block, *The Visual Story*; Bordwell & Thompson, *Film Art*; Mercado, *The Filmmaker's Eye*; Ward, *Picture Composition*.
