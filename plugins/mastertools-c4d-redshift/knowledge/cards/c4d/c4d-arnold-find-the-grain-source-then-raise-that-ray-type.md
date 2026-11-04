---
id: c4d-arnold-find-the-grain-source-then-raise-that-ray-type
title: Arnold-era method: read where the grain comes from, raise only that ray type, then cap bounces per ray type
domain: c4d
tags: [manuel-casasola-merkle, arnold, sampling, grain, noise, ray depth, ipr, render theory, aixsponza, deep-read, polish]
applies_to: Arnold C4DtoA (2015); principle only for Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sxNf7Ei5Ezc, src:yt-transcripts, src:polish-roster]
feeds: [coach, estimator]
conflicts: none
---
Speaker: Manuel Casasola Merkle (Aixsponza, Munich; Maxon booth talk, 2015, a vendor-friendly demo).
His method with a pure ray tracer: look at the noisy frame, work out which effect the grain comes from (global illumination, blurry reflections), raise rays only for that effect until the grain is acceptable [16:17-16:47]. If you want one control, the camera/AA slider trades speed for cleanliness [09:28-09:59].
Ray depth is a second axis: with diffuse depth 0 the diffuse effect vanishes, at 1 you get GI but no colour bleed from the blue table, at 2 the bleed appears. Glossy at 1 shows reflections but not a reflection inside a reflection. Fewer bounces render faster [17:18-18:53].
He argues an interactive preview (IPR) matters because good scenes come from many iterations, such as placing rectangular lights to shape reflections on a car hood [10:31-12:06].
Transfers: same logic as unified sampling plus per-ray bounce limits in Redshift; verify exact setting names in the redshift skill.

**Use it:** Coach rule for noise: name the noise source first (GI, reflection, refraction, volume), raise or fix only that, and lower the matching bounce limit when an effect is not needed.
