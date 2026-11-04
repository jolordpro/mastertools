---
id: redshift-scene-cost-checklist
title: Scene-side render costs to remove before touching settings, plus the expensive features list
domain: redshift
tags: [scene optimisation, cache simulations, tessellation, instancing, proxies, textures, displacement, expensive features]
applies_to: Redshift GPU, C4D
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=TEM9BU-Fp0E]
feeds: [shakedown, coach, CHECKS]
conflicts: none
---
Bake sims to cache [07:01]. Use Redshift tessellation instead of high subdivision [07:01]. Instances and proxies over many objects [07:32]. Drop unneeded 8K textures [07:32]. Delete unused materials, including leftover copies from iteration [08:02]. Use Redshift displacement in the material and tag instead of geometry [08:33].
Expensive to render: motion blur, depth of field, volumetrics, caustics, transmission/refraction, SSS [08:33].

**Use it:** scene checks: unbaked sims, high subdivision with no tessellation, oversized textures, unused materials, many unique copies where instances would do.
Transcript support: Another source for baking sims to cache before render/hand-off (https://www.youtube.com/watch?v=TEM9BU-Fp0E [02:05-03:39])
