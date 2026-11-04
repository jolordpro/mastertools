---
id: lighting-cycles-speed-ladder-samples-then-noise-threshold-bounces-light-tree-and-subdivision
title: One Cycles frame fell from 25 hours to 39 seconds by cutting samples, raising the noise threshold, dropping bounces to 4 to 5, fixing the light tree threshold and removing subdivision
domain: lighting
tags: [cycles, render time, noise threshold, light bounces, light tree, subdivision, samples, persistent data, deep-read]
applies_to: Blender Cycles
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=fvBDaMy2oPY, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Rasheed's Edit [0:04-3:44], one test scene: default settings took 25 hours; samples to the 100 to 300 range gave 43 minutes; noise threshold 0.2 to 0.5 (lower for dimmer scenes) gave 14 minutes (note: that is far looser than Blender's usual default; check the caption); max bounces from 12 to 4 or 5 gave 6 minutes; light tree unticked with a manual threshold of 0.01 gave 3 min 42 s; subdivision level to 0 gave 39 seconds. Bonus: set denoise and compositing to GPU, and enable persistent data to cut the total animation time (not the first-frame time) [3:14]. The step sizes belong to this scene; the order shows what to try, and the cost of each change on quality is not shown.

**Use it:** In the render-time coach, the ladder from "biggest unforced waste" to "scene geometry" is a template: samples, noise threshold, bounces, light sampling, then geometry.
