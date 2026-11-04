---
id: pipeline-kramer-real-time-preview-must-match-the-final-render-so-nothing-restarts
title: "Kramer: a real-time preview is only worth it if it matches the final ray-traced render, so you never rebuild after the mood is right"
domain: pipeline
tags: [polish, andrew-kramer, real time, preview, game engine, ray tracing, eevee, octane, final render, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gNh9r-VbSVg, src:yt-transcripts, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
Kramer wants to iterate camera, mood and layout in real time and then hit render with the result almost identical, only more accurate, so the pipeline is never a dead end where you restart in a final renderer [1:01:54-1:03:58]. He says game-engine limits (shadows through refractive surfaces, caustics, screen-space occlusion) cannot be fully cheated even with deferred rendering, and interactive ray tracing still needs time to clean noise [1:02:24, 1:05:30]. The Blender host cites Eevee-to-Cycles with shared shaders as that idea [1:04:29]. Talk from 2018.

**Use it:** Keep the draft look and the final look on the same shader set; do not let a viewport-only cheat become the approved look.
