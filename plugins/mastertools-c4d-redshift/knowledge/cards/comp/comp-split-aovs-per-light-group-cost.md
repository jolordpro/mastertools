---
id: comp-split-aovs-per-light-group-cost
title: Splitting every material AOV by light group roughly doubled file size and tripled layers and channels
domain: comp
tags: [light groups, aov split, file size, exr, channels, nuke]
applies_to: Blender 2025 test scene, generalises
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, src:yt-transcripts]
feeds: [comp, estimator, CHECKS]
conflicts: none
---
HD frame: 112 MB to 222 MB; 23 layers/67 channels to 58 layers/180 channels [09:21-10:55]. Also longer renders, slower Nuke reads, big layer lists in shuffle/copy, and clone or expression-link edits across copies [10:23-16:32]. Nuke channel limit he recalled as 1024 (may have changed) [10:55].

**Use it:** estimator: AOV count x light groups multiplies EXR size and render write time. Advise against the brute split.
