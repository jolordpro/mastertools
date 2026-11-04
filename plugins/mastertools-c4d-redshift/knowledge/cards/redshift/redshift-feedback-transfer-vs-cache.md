---
id: redshift-feedback-transfer-vs-cache
title: In the Feedback display, trouble starts when geometry or texture 'transferred' is far larger than the cache size
domain: redshift
tags: [feedback display, out of core, geometry, textures, transferred, cache size, memory categories]
applies_to: Redshift 2027 help
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Feedback+Display.html, src:research-production-pipelines]
feeds: [render ledger, CHECKS memory]
conflicts: none
---
The display reports memory by category: free, overhead, geometry, textures, matrices, sprites, rays, photons, IC points, IPC points, SSS points. Geometry and textures each show transferred and cache size. The page's example of trouble is 100 GB transferred against a 4 GB cache.

**Use it:** log these figures from every draft and final into the render ledger and flag a large transferred/cache gap.
