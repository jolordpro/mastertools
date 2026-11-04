---
id: pipeline-usd-isolate-time-dependency-cache-full-range
title: Cache the full frame range in USD so nodes are not time dependent; lighting scenes should have none
domain: pipeline
tags: [usd, time dependency, time samples, cache, houdini lops, lighting, luca scheller, deep-read]
applies_to: Houdini Solaris / OpenUSD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
In SOP-style work you try to remove time dependency to stay fast; in USD you can write time samples so the whole range is available and the node is not time dependent [36:53-37:24]. Use the cook-full-range option on nodes, or a cache node where missing [37:24-38:56]. Heavy geometry import is cached for the shutter range around the current frame so motion blur has deformation data [37:56-38:26]. Final rule: lighting scenes should have no time dependency, so exporting a single frame still carries all animation [50:54]. Culling for a whole range in one node took about 2 seconds for 100 frames of 10,000 instances in his demo [39:27].

**Use it:** Aim to get a time-independent scene before the render step; that makes single-frame test renders cheap.
