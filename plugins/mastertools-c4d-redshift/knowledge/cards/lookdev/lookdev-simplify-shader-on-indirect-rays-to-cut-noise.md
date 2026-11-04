---
id: lookdev-simplify-shader-on-indirect-rays-to-cut-noise
title: Swap noisy shader parts for simpler ones on indirect rays (glossy after bounce one, glass past depth three, emission for volumes) to get consistent samples
domain: lookdev
tags: [spencer magnusson, blender, cycles, noise, light path, ray depth, glossy, glass, volume, fireflies, deep-read]
applies_to: Blender Cycles 5.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts]
feeds: [redshift, advisor]
conflicts: none
---
Magnusson [03:14-12:10]: a Light Path node tells a shader which ray it is. Metal: after one bounce, mix in a diffuse, so reflections-of-reflections stop sparkling but first reflections stay. Glass: principled glass while ray depth is under 3, diffuse transmission after (depth 1 looks frosted); a camera or transmission ray uses max of 0/1 as a switch. Volume: real volume for camera rays, emission-style volume for others; far cleaner though not noise-free.
Also: fade subsurface by camera distance through a map-range on camera depth [01:35]. Randomness itself is fine; pull it back only where it forces far more samples than wanted [02:43].

**Use it:** in Redshift, look for the equivalent ray-switch/ray-type shader option before raising samples (not verified here; check the redshift ledger).
