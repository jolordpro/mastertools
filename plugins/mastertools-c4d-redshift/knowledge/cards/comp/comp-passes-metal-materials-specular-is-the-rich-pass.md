---
id: comp-passes-metal-materials-specular-is-the-rich-pass
title: Which pass is richest depends on the material: for metals the specular passes carry the colour, for dielectrics the diffuse ones do
domain: comp
tags: [aov, specular, diffuse, conductive, metal, pass selection, nuke, sarkamari, deep-read]
applies_to: Arnold AOVs, Nuke 12.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts]
feeds: []
conflicts: none
---
With mostly conductive materials, direct and indirect diffuse hold little colour [08:02-08:33]. Dielectric objects make diffuse the rich pass; here specular was [08:33]. Build in this order: diffuse (direct + indirect, Plus), specular (direct + indirect, Plus), merge both with Plus, then SSS, then the matte [08:02-13:17].

**Use it:** Choose which passes to rely on after looking at the materials; useful hint for a pass-priority tooltip.
