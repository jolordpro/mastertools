---
id: comp-recolour-diffuse-filter-limits
title: Hue/Saturation on the diffuse filter recolours without relighting; a Cryptomatte matte targets one object, but big colour changes look fake
domain: comp
tags: [diffuse filter, recolour, cryptomatte, variant, bounce light, hue saturation]
applies_to: Redshift AOVs, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [variant engine, comp-fix planner]
conflicts: none
---
Changing the filter hue/sat recolours everything while lighting and contrast stay put [43:32]. For one object, pick its colours in the Cryptomatte effect, output as RGBA, precomp, and use it as the matte for the adjustment [1:16:26-1:18:31]. Emission can be recoloured the same way [1:19:33]. Limit: a red wall would not bounce red light, so it reads fake; chair-sized changes are fine [1:19:01].

**Use it:** Mark a variant comp-only when the object is small and bounce is minor; larger colour changes need a re-render.
