---
id: ai-models-ic-light-background-match-and-animated-path
title: IC-Light can match a subject to a background, and a spline path moves the light for an animated pass
domain: ai-models
tags: [ic-light, background match, animated light, spline, comfyui]
applies_to: ComfyUI IC-Light nodes, May 2024
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=yJRBn0QS368, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Matting removes the background, a grown mask sets the light spread; a smaller spread (512 tried) blends more [04:52-06:54]. Animated version: a spline decides the light's path, 8 frames with a context window about 360 to slow it [10:44-12:36].

**Use it:** possible AI previs for lighting direction; not frame-accurate.
