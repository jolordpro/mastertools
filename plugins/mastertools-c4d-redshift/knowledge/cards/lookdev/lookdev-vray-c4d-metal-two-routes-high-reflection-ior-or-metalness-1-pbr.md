---
id: lookdev-vray-c4d-metal-two-routes-high-reflection-ior-or-metalness-1-pbr
title: V-Ray for C4D metal has two valid routes: black diffuse with white reflection and a high IOR (5 looked polished, 18 better), or the PBR route with metalness 1 and colour in diffuse
domain: lookdev
tags: [v-ray, chaos, metal, metalness, ior, glossiness, roughness, copper, cinema 4d, deep-read]
applies_to: V-Ray for Cinema 4D (node material)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=i6zQmQD_auA, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Chaos V-Ray tutorial [03:08-06:19]. Route 1, traditional: diffuse black, reflections pure white, then raise the IOR-style value: metals need far higher values than other materials, and he moves from 5 (quite polished) to 18 (better); the reflection colour can tint the metal. Glossiness 1 is polished and lower is rougher [03:31-04:02]. The speaker says "I value"; captions may have misheard IOR, so check in the UI. Bump plugs into the bump channel with the amount tuned to the texture [04:37]. Route 2, PBR: set the material to the roughness model, metalness 1, colour in diffuse (his copper), shininess from roughness [05:08-05:38]. Chaos publishes a metalness page with a table of values for gold, silver, iron and others [06:19]. Both routes are called correct.

**Use it:** Reference for a V-Ray scene audit. Do not use V-Ray IOR numbers in Redshift; see the Redshift per-metal edge-tint card.
