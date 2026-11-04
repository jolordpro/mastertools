---
id: redshift-cutoff-thresholds-and-trace-depth
title: Optimization cut-off thresholds saved about 2 s of 8.6 s; lowering trace depth darkens the image
domain: redshift
tags: [optimizations, cutoff, trace depth, reflection depth, refraction, render time]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uKRqHwVr0F4, https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, src:yt-transcripts, https://www.youtube.com/watch?v=s5ElfI1q8uU]
feeds: [coach, redshift]
conflicts: none
---
Raising the cutoff thresholds in Optimizations ended rays sooner: 8.6 s to 6.3 s with a slight noise increase in shadows [10:26-10:56, RF]. Lowering trace depth also speeds up but tends to darken, so leave defaults unless needed [09:14, RF].
Daily Course: no refraction or transparency in the scene, so lower those depths; 45 s to about 30 s, with some reflections lost [16:26-17:31, DC].

**Use it:** advisor: only suggest lower depths when the scene lacks the effect; show before/after.
Transcript support: 10x default cutoff thresholds, up to 30 percent saved, grain left for denoise (low confidence) (https://www.youtube.com/watch?v=s5ElfI1q8uU [02:38-03:10])
