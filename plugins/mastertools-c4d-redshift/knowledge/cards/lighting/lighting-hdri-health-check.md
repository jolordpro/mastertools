---
id: lighting-hdri-health-check
title: HDRI health check idea: float and linear file, sun peak versus median, exposure normalised when swapping HDRIs
domain: lighting
tags: [lighting, hdri, check, preflight, oiio, exposure]
applies_to: any
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [src:research-production-pipelines, https://www.youtube.com/watch?v=gjgAZ0x29ag]
feeds: [PLAN 0A HDRI check]
conflicts: none
---
A clipped or 8-bit file shows a flat top at 1.0.
Compare peak pixel to median to tell if a sun is present; normalise exposure so a swap does not change brightness; weigh resolution against how much of the frame shows reflections.
Proposal from the research, to build with OpenImageIO.

