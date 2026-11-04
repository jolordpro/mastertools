---
id: comp-passes-add-stack-duplicate-to-boost
title: Rebuild the beauty from passes with Add layers, then duplicate a pass layer (reflection, post effects) to boost it or drop its opacity to cut it
domain: comp
tags: [Zak, i_go_by_zak, multipass, AOV, add, After Effects, deep-read]
applies_to: Redshift multipass in After Effects
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts]
feeds: [comp-fix planner]
conflicts: none
---
Zak builds the image from diffuse, GI, reflection, refraction, subsurface, specular, lighting and caustics, all Add, plus a post-effects layer [39:27-40:02].
He then keeps control per layer: duplicate the reflection layer for more reflections, or lower a layer, and the same for post effects [41:37-42:08].
The ACEScg to sRGB transform and the gamma fix sit on top of the whole stack [41:05].

**Use it:** Comp: give clients a per-pass dial (reflection, post) by keeping passes as separate Add layers.
