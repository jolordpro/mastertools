---
id: comp-diffuse-filter-times-raw-lighting
title: Rebuild diffuse as Filter multiplied over (Diffuse Lighting Raw + GI Raw + SSS Raw), with the multiply layer on top
domain: comp
tags: [diffuse filter, raw, gi, sss, aov, after effects, multiply]
applies_to: Redshift AOVs, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=5hQKHD8fSs8]
feeds: [comp-fix planner, AOV package]
conflicts: none
---
Filter is the flat surface colour with no light or shadow; Raw is illumination only [32:05-33:42]. Put Filter on Multiply on top, and Add the raw passes under it [32:37, 34:14]. The order of the adds can change; the multiply has to act on their sum [35:16]. Name every precomp; the Redshift docs AOV page has a combine chart [30:32].

**Use it:** Write this order into the comp-fix planner and verify the rebuild against the beauty pass.
Transcript support: Raw channels go on Multiply, not Add; splitting filter and raw lighting gives more control than combined Diffuse Lighting (https://www.youtube.com/watch?v=5hQKHD8fSs8 [07:17-08:18])
