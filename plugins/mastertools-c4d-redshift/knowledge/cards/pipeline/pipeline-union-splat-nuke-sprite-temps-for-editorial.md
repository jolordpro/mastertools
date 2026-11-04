---
id: pipeline-union-splat-nuke-sprite-temps-for-editorial
title: Union cuts the 40 camera views into sprites and lays them out in Nuke USD so crowd temps reach editorial before splat processing
domain: pipeline
tags: [nuke, usd, sprites, temps, crowd layout, editorial, workflow, deep-read]
applies_to: Nuke USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Ybln1zAQDVc, src:yt-transcripts]
feeds: [handoff]
conflicts: none
---
After capture, chosen camera angles (no motion blur, well lit) come back with a roto pass to remove the background [25:54]. Compositors place the sprites in work-in-progress CG environments in Nuke's USD workflow [26:26]. Temps go to editorial fast, and the supervisor and director choose crowd behaviour per section with the same elements they will finally get. Layout metadata is then exported to ClearAngle for processing [26:56].

**Use it:** model for a temp-first handoff: approve placement with cheap stand-ins, then send metadata for the final pass.
