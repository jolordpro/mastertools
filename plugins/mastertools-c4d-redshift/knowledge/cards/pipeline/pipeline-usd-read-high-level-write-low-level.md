---
id: pipeline-usd-read-high-level-write-low-level
title: Read with USD's high-level API, but write, copy and move data with the low-level Sdf API for speed
domain: pipeline
tags: [usd, sdf api, high level api, pcp, houdini lops, luca scheller, rise, deep-read]
applies_to: OpenUSD, Houdini Solaris (SIGGRAPH 2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
Luca Scheller (Rise) says the high-level API gives convenient getters and setters and reads the composed result of all layers, working at stage level [06:29]. The low-level Sdf API works on individual layers and is the route for creating, copying, moving and anything performance critical [06:59]. In Houdini the habit is to query another stage with the high API and write with the Sdf API [07:00]. Use Sdf path objects, not strings, because paths also encode attributes and variants [08:03-08:36].

**Use it:** When scripting a USD export or a checker, plan read-high, write-low from the start; use path objects.
