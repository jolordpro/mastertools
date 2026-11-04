---
id: ai-models-gaussian-splat-capture-sharp-frames-and-parallax
title: Gaussian splat capture: sharp in-focus frames and multi-view parallax matter most; any still camera works
domain: ai-models
tags: [gaussian splatting, capture, sharp frames, parallax, smartphone, 360 camera, nerf, reconstruction, deep-read]
applies_to: 2026 splat pipelines
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KZqv3Z5rRg8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Michael Rubloff (radiancefields.com): any camera that makes stills can feed splatting, including phones, mirrorless, film, thermal and 360 cameras, and SLAM scanners with several cameras and lidar [11:06] [11:37]. Two things matter most: sharp, in-focus frames and multi-view parallax [12:09]. Blur in the input is reconstructed as if it belonged to the scene, so cull soft frames [14:14] [14:44]. An MIT-licensed tool called sharp-frames picks the sharpest images from video [15:16]. Phones are good because of deep depth of field [12:41].
He built a free capture app that fires the 0.5x and 1x lenses together with manual shutter and ISO to get sharper data; it is pipeline-agnostic [13:11] [13:43].

**Use it:** Capture checklist for a splat or photogrammetry job: lock shutter fast enough to avoid blur, cull soft frames, move the camera for parallax.
