---
id: pipeline-union-splat-crowd-render-cost-and-camera-distance
title: Splat crowds render as instances of instances: a 2K GPU frame in about 20 minutes, and they hold up at three-quarter screen height
domain: pipeline
tags: [gaussian splat, render time, instancing, crowd, camera distance, karma xpu, deep-read]
applies_to: Karma XPU
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Ybln1zAQDVc, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Splat characters are instances of one primitive shape, and a crowd is instances of those, so memory stays low [15:33]. Rendered on Karma XPU (CPU plus GPU machines); the speaker estimates a 2K frame in perhaps 20 minutes on a GPU machine, said loosely [16:05]. Tested close to camera: characters at about three-quarters of screen height, camera roughly a couple of metres away, still convincing and unoccluded [16:46]. Traditional crowds were buried behind plates or extras; Union argues that is no longer needed [18:08].

**Use it:** rough budget line for instanced-crowd renders; treat the 20-minute figure as a spoken estimate, not a benchmark.
