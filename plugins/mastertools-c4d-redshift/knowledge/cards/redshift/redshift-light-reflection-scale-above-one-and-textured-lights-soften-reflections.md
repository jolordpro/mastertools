---
id: redshift-light-reflection-scale-above-one-and-textured-lights-soften-reflections
title: Light reflection scale can go above 1; lowering it softens a light's reflection on metal, and a textured light shapes the highlight
domain: redshift
tags: [light, reflection scale, gobo, metal, highlight, product, lionel, maxon, dustin-falcoma, deep-read]
applies_to: Redshift 3.x in C4D R26 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [lighting, redshift]
conflicts: none
---
To keep a strong key but soften its reflection in a shiny part, lower the light's reflection scale; it is not capped at 1 (he tried 3 for a very strong reflection) and he only discovered that about a year and a half earlier [34:59-35:29].
Putting a gobo or spot-pattern texture on the key shapes and softens the reflected highlight; the fill got a very soft texture, which cuts intensity so he raised it [35:45-36:32].
Host Dustin Falcoma: a gradient plugged into the light does the same job for product lighting [37:33-38:04]. For a stray highlight, exclude the light from reflection for one object [11:06-11:36].

**Use it:** lighting: reflection scale is the first move when a key light's reflection is the problem, not the light's power.
