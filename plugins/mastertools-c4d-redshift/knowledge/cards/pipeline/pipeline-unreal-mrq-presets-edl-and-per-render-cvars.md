---
id: pipeline-unreal-mrq-presets-edl-and-per-render-cvars
title: Unreal's render queue saves presets to a chosen folder, adds per-render console variables, and exports EDL/XML from the shots track
domain: pipeline
tags: [unreal, movie render queue, preset, console variables, edl, 16-bit exr, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25-4.26
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
New in 4.25 queue: 16-bit EXR output, a hint when alpha needs a setting [1:16:29-1:17:00]. Presets default to a Cinematics movie pipeline folder but the location can be set outside the project [1:17:31]. Console variables can be added to the render only (for example turn ray tracing on just for the render) [2:06:06]. Right-click the shots track to export EDL or XML, cut elsewhere, and re-import so shots reorder [2:07:08-2:07:38]. Command-line and Python rendering existed but needed know-how [2:05:03]. Console variable list: Help menu generates an HTML file [2:00:22].

**Use it:** Check the Unreal version before relying on these, and wire render presets into the farm.
