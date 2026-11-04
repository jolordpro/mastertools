---
id: pipeline-ai-generated-characters-need-decimate-merge-and-rigify
title: Generated 3D characters need Decimate and Merge by Distance before a Rigify rig, which can stay rough when it is only a guide
domain: pipeline
tags: [trellis, rigify, decimate, blender, ai asset, rig, mickmumpitz, deep-read]
applies_to: Blender, Trellis (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=7J7hi-Hxpac, src:yt-transcripts]
feeds: []
conflicts: none
---
Mickmumpitz [05:56-07:14]. Trellis models come out heavy, so lower the vertex count with Decimate, then in edit mode select all and Merge by Distance. Rigify (place a few bones, auto-build) is enough, with manual weight painting on broken areas, because the rig only guides a later AI render and need not be clean. The author kept the pipeline free but says a paid generator or hand modelling gives better quality. Generated heads can be made separately and attached to the body.

**Use it:** A rough-rig route for background characters when the final look comes from another process.
