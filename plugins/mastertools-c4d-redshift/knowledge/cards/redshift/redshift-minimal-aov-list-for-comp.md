---
id: redshift-minimal-aov-list-for-comp
title: Minimal comp AOV set: Diffuse, GI, Emission, Reflection, Refraction, Specular, Subsurface, Beauty; add volume only if volumes exist
domain: redshift
tags: [aov package, minimal, diffuse lighting, gi, emission, specular, subsurface, volume lighting]
applies_to: Redshift 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=IcLiz8e8ffc, https://www.youtube.com/watch?v=TonSU8Ljm5c, https://www.youtube.com/watch?v=5hQKHD8fSs8]
feeds: [AOV package builder]
conflicts: none
---
The base package [10:44-11:46]. Volume fog, emission and tint passes are only for scenes with fog [15:25]. The raw plus filter set for advanced rebuild: diffuse filter and lighting raw, GI raw, reflection and refraction filter and raw, SSS raw, translucency filter and lighting raw and GI raw [12:48-14:23]. Shadow only works with the raw and filter diffuse set [15:00]. Z-depth only if needed.
Merged from `comp-essential-aov-list-simple-rebuild`: Trainer's essential set [10:52-13:28]: diffuse lighting at the bottom, then GI, emission (for glowing meshes and the background), reflection, specular lighting, refraction (glass), SSS (wax, plants, fabric). Reflection means objects reflected in each other; specular lighting means the light sources themselves, including a dome HDRI [11:23]. Label, filter and raw passes are skipped for simple work; volume was switched off in the scene. If AOVs are not enabled in the Redshift render settings, none appear [10:21].

**Use it:** Use as the default package list and the advanced list, and drop passes the scene has no use for.
Transcript support: Not directly: AO into Overall Tint is a material shortcut, see new card. (https://www.youtube.com/watch?v=TonSU8Ljm5c [1:04:55-1:07:42])
Transcript support: Beauty kept only as a reference; Diffuse Lighting, Reflection, Specular, Refraction, GI, Shadows as a starter set (https://www.youtube.com/watch?v=5hQKHD8fSs8 [02:39-05:13])
