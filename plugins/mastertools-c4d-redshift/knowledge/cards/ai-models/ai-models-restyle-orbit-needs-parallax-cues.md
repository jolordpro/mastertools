---
id: ai-models-restyle-orbit-needs-parallax-cues
title: For orbit moves the restyle mistook the subject spinning for the camera; background props and own depth map helped
domain: ai-models
tags: [restyle, orbit, parallax, depth map, luma, kling]
applies_to: Luma Modify, Kling, early 2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=YB5Jp9_WN78, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
First orbit test spun the pigeon and not the camera; adding pillars and tiles to the 3D scene gave parallax and a solid result [05:40-06:10].
In the city test the AI's own depth and normals flickered; own depth from Unreal helped but was still unusable [07:12].

**Use it:** when an orbit is planned for AI restyle, the coach suggests adding background props for parallax.
