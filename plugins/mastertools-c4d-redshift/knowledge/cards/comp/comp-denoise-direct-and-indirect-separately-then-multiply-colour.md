---
id: comp-denoise-direct-and-indirect-separately-then-multiply-colour
title: Multi-pass denoise: denoise direct and indirect light separately, add them, then multiply by colour; it restores texture detail the beauty denoise smudges
domain: comp
tags: [spencer magnusson, blender, cycles, noise, multi pass denoise, direct, indirect, color pass, compositor, detail, deep-read]
applies_to: Blender compositor
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts, https://www.youtube.com/watch?v=NlDrXkb37lg, https://www.youtube.com/watch?v=dLZEmfqob7k]
feeds: [comp, redshift]
conflicts: none
---
Magnusson [35:43-39:57]: render diffuse, glossy, transmission, emission and environment passes plus denoising data. In comp: denoise direct light, denoise indirect light, add, multiply by the colour pass (the manual's pass diagram gives the recipe). On the test, normal and albedo denoise was still smudgy; the multi-pass version kept much more detail, though not perfect.
Cost: about six images denoised instead of one (two passes each for three light types). He suggests lowering the threshold, upscaling or raising samples to improve further. Temporal denoise exists in Optix, After Effects, and DaVinci Studio [36:14].

**Use it:** for Redshift, test the same recipe on a texture-heavy hero shot before relying on the beauty denoise.
