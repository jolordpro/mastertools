---
id: lighting-tune-bounce-counts-by-viewing-each-indirect-pass
title: Tune bounces per ray type by watching the indirect passes: he settled on diffuse 5, glossy 4, transmission 6, transparent 5, max 12
domain: lighting
tags: [spencer magnusson, blender, cycles, noise, light paths, bounces, diffuse, glossy, transmission, indirect pass, interior, deep-read]
applies_to: Blender Cycles 5.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts, https://www.youtube.com/watch?v=EKb5G_Efunw]
feeds: [redshift, advisor]
conflicts: none
---
Magnusson [25:39-30:30], interior test: set all bounces to zero and open each indirect render pass. Diffuse 5 (no visible gain over 6); glossy 4 (3 or 4 is a good baseline, 1-2 feels too dark); transmission 6 (each glass pane costs a bounce); transparent 5; total 12. Principled shaders emit diffuse and glossy together, so set them one by one.
Fewer bounces cut fireflies but too few darken interiors. Clamping is a last resort when shader changes do not help [24:25]. This agrees with the Redshift advice to treat noise as samples and missing detail as depth.

**Use it:** the advisor can show the method (view indirect passes, raise until no visible change), not his numbers, which are scene specific.
