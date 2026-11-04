---
id: motion-unreal-mrq-temporal-vs-spatial-samples
title: In Unreal's Movie Render Queue, temporal samples drive motion blur and spatial samples drive anti-aliasing, and they multiply
domain: motion
tags: [unreal, movie render queue, motion blur, anti-aliasing, samples, shutter angle, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25-4.26
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Epic's Patrick Wongbo [1:20:05-1:23:42]: temporal sample count sets the motion blur (samples spread either side of the frame, shaped by the camera shutter angle); spatial sample count is the anti-aliasing (camera jitters). The two multiply: 8 x 8 = 64 sub-samples per frame. The tool warns when the product is under what normal engine TAA uses (8), and when it is above 8 he turns engine TAA off, since stacking both makes the frame look soft. His default is 8 and 8 with TAA forced to none; he says there is little art to it. With ray tracing he turns the denoiser off and pushes samples very high for final frames [1:19:04]. The next version was to add path-tracer output and per-shot render toggles [1:14:25].

**Use it:** Treat motion-blur samples and AA samples as two separate dials whose product is the real cost; start at 8/8 and drop engine TAA when rendering with the queue.
