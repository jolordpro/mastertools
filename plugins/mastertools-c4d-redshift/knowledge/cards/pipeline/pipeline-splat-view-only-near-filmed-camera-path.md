---
id: pipeline-splat-view-only-near-filmed-camera-path
title: Splats only hold up from views close to where the footage was shot, so plan the capture around the final camera move
domain: pipeline
tags: [gaussian splatting, camera path, novel view, capture planning, floaters, deep-read]
applies_to: Gaussian splats
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ERuRMOVO58Q, src:yt-transcripts]
feeds: [challenger]
conflicts: none
---
At roughly 2,000 steps the scene is already representative, but there is ugliness when viewed from different angles; splats are meant to be viewed from near the filming positions [04:41]. He warns against viewing from far off to one side. Reflections and transmission work because they are splats that fade in and out with view direction [05:12]. Cleaning floaters: do many training steps first, because deleting during training makes them regrow [06:46].

**Use it:** before committing to a splat as a background or set, confirm the final camera sits inside the captured path.
