---
id: comp-assemble-passes-add-compare-beauty
title: Assemble passes with everything on Add, then expect a close but not exact match to the beauty when reflection is split
domain: comp
tags: [assemble, add, beauty compare, reflection total, refraction, aov rebuild]
applies_to: Redshift AOVs, After Effects
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [sum-to-beauty check]
conflicts: none
---
Diffuse total, specular, emission, translucency total, reflection total and volume lighting all sit on Add [36:17-40:57]. The split reflection/refraction rebuild looked wrong; he suspects a bug and fixed transparency with an Exposure cut on the reflection filter [41:28]. With that, the result was very close, not identical, to the beauty [42:00]. Keep a second comp viewer locked on the final to compare while editing inside precomps [42:31].

**Use it:** The sum-to-beauty check should allow a tolerance when reflection or refraction raw/filter pairs are used; report the error rather than failing.
