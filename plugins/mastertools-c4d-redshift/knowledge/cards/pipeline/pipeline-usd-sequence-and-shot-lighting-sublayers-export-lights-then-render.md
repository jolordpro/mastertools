---
id: pipeline-usd-sequence-and-shot-lighting-sublayers-export-lights-then-render
title: Lighting in layers: sequence lights apply to every shot, shot lights are added per shot, then lights are exported and the container is rendered
domain: pipeline
tags: [lighting, usd, solaris, sequence lighting, shot lighting, deadline, batch, render, deep-read]
applies_to: Houdini Solaris, Prism states, Deadline
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
A sequence-lighting preset places sequence lights once (applied to all shots) in one column and shot lights in per-shot columns [21:41] [22:11]. Each export writes a sublayer, sequence and shot, referenced into the lighting department layer [22:42] [23:43] [24:45].
He prefers exporting lights and rendering the shot container instead of rendering from Houdini: it removes dependence on Houdini for rendering and lets other departments, such as effects, see their work under the real lights [23:12]. A state manager runs all exports then submits one Deadline job per shot [23:43] [24:14].

**Use it:** Pattern for a C4D render platform: one global light layer per sequence plus per-shot overrides, exported separately from the render step.
