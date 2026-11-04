---
id: pipeline-arnold-procedural-archive-gives-lighting-td-a-finished-asset
title: A procedural archive holds geometry, shader and displacement, so the asset artist hands the lighting TD a finished asset
domain: pipeline
tags: [manuel-casasola-merkle, procedural, archive, proxy, cloner, handoff, arnold, instances, deep-read, polish]
applies_to: Arnold C4DtoA (2015); same idea as Redshift proxies
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sxNf7Ei5Ezc, src:yt-transcripts, src:polish-roster]
feeds: [coach, CHECKS]
conflicts: none
---
Speaker: Manuel Casasola Merkle. An Arnold procedural is a full scene exported to disk (his example is a birch tree in a cloner). It carries the model, shader and displacement, so the asset artist finishes the asset and gives it to the lighting TD to pick up. It is not limited to Cinema 4D: assets from Houdini, Maya or XSI render the same [47:59-49:32].
Changing the cloner count updates at once because nothing is re-exported; he moved the camera among 1,000 heavily displaced, textured trees while rendering, and calls it faster and more flexible than render instances [49:01-50:03].
Also notes: particles are exported as positions only with geometry built at render time (200,000 coloured particles reacted as fast as the viewport) [41:24-43:50]; VDB volumes load from disk so rendering starts at once [44:21-45:23]; the HDRI sky needs the image resolution entered for importance sampling [39:50-40:53].

**Use it:** Handoff rule: lock the asset with its shader inside a proxy or archive, test it in a cloner at high count, then hand it to lighting.
