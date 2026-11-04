---
id: pipeline-farm-etiquette-optimise-for-shared-resources
title: Rendering on a shared farm forces optimisation: jobs must play nicely with others running at the same time
domain: pipeline
tags: [render wrangler, render farm, optimization, shared resources, cache, cloud, a cup of joe, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=eb0QFXD3AaA, src:yt-transcripts]
feeds: []
conflicts: none
---
A guest wrangler: anyone who wants to render seriously must at some point be involved in the farm, which has issues a local render does not show: renders behind a cache, cloud costs [18:38].
On a farm a job must play nice with other jobs running simultaneously, giving a better appreciation of optimisation and resource use [19:09].
This knowledge, seeing the whole pipeline from client intake to delivery, is why wranglers get promoted quickly into lead roles at big studios [03:05].

**Use it:** Teach users to size jobs for a shared farm: memory, frame time, and priority, not just whether it renders on their own machine.
