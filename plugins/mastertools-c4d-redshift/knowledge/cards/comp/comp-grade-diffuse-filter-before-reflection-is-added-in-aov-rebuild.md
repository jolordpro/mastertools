---
id: comp-grade-diffuse-filter-before-reflection-is-added-in-aov-rebuild
title: Rebuild the beauty from AOVs when a colour note must not touch the reflection: grade the diffuse filter, then add specular and reflection on top
domain: comp
tags: [chad-ashley, aov rebuild, diffuse filter, reflection, fusion, nuke, after effects, deep-read]
applies_to: Redshift 2.x AOVs, any compositor (Fusion shown)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ARykOD6lG3c, src:yt-transcripts]
feeds: [comp, coach]
conflicts: none
---
Redshift's manual gives the beauty as diffuse filter multiplied on diffuse lighting and GI raw, plus subsurface, specular, reflections and refractions; Chad built that in Fusion and it matches the beauty [02:39-05:18]. He says it works in any comp, even Photoshop, and he rarely uses it himself [04:47-05:18, 55:02-55:37].
Why do it: a sticker colour or brightness matte applied to the diffuse filter only, before reflection is added, does not blow out or tint the reflection sitting over the sticker [52:27-54:00]. A tint on the specular pass alone tints the reflection without touching diffuse [54:30-55:02]. A late-comp grade with the same matte would burn the reflection too.
Check the rebuild equals the beauty before grading.
Transfer: car-paint or glossy helmet graphics where the colour change must keep the studio reflection.

**Use it:** Add the 'does the rebuild match beauty' test, then apply colour notes at diffuse. Supports comp-aovs-sum-to-beauty.
