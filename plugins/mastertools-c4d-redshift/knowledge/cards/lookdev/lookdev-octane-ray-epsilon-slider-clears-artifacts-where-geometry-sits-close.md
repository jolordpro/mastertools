---
id: lookdev-octane-ray-epsilon-slider-clears-artifacts-where-geometry-sits-close
title: Octane (C4D): the Ray Epsilon slider in the render settings clears speckle artifacts where geometry nearly touches, such as eyes and hair; lower it until they go
domain: lookdev
tags: [octane, ray epsilon, artifacts, eyes, hair, close geometry, deep-read]
applies_to: Octane for Cinema 4D (version not stated)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=8zCqKpeF5Uc, src:yt-transcripts]
feeds: [CHECKS, lookdev]
conflicts: none
---
3seater (beginner channel). Artifacts showed on a character's hair and eyes, where surfaces sit very close together [04:52-05:52]. The Octane settings slider Ray Epsilon was dragged down and the specks disappeared. The speaker does not know exactly what it does (he says it relates to geometry and light rays interfering) and gives no fixed value: move it, watch the artifacts, expect it to end on the low side.

**Use it:** Octane-only. When a closeup shows speckle at touching surfaces, try lowering Ray Epsilon before adding samples. Do not carry the idea over to Redshift without checking its own settings.
