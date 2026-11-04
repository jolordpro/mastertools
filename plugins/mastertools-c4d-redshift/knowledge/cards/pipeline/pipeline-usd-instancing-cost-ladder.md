---
id: pipeline-usd-instancing-cost-ladder
title: Point instancing is the most efficient USD instancing, then instanceable references, then plain references
domain: pipeline
tags: [usd, instancing, point instancer, instanceable reference, vram, lawn, scott keating, deep-read]
applies_to: USD, Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TLJPDt4YpYM, src:yt-transcripts]
feeds: [estimator, pipeline plan]
conflicts: none
---
Keating [47:23-48:30]: a point instancer (true instancing) renders insane amounts of geometry. Instanceable references are still good but more limited. Plain references nearly duplicate the geometry. Flexibility rises as efficiency falls. For something like a lawn he would use the point instancer.
Rise reached the same limit with multi-props: still some overhead, and point instances are faster [RISE talk jpbMbafS9FY 1:02:10].

**Use it:** Redshift/C4D: for scatter (fans, grass, confetti) use true instances before cloning geometry.
