---
id: lookdev-bump-strength-high-distance-low-to-keep-normals-clean
title: Keep bump distance small (about 0.01) and strength high, since the normal pass feeds the denoiser
domain: lookdev
tags: [spencer magnusson, blender, cycles, noise, bump, normal pass, denoise, bump distance, filter width, deep-read]
applies_to: Blender Cycles 5.0
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
Magnusson [20:40-22:14]: a bump at distance 1 turned the normals dark; with distance 0.01 they came out bright. He could not find the unit in the manual, and a one-metre bump seemed wrong. Rule: max strength, turn the distance down. Also removed unneeded textures to save memory and reused shaders.

**Use it:** when a denoiser smudges texture, look at the normal AOV for dark or flat results.
