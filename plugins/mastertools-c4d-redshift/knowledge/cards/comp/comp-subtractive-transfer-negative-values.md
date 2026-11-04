---
id: comp-subtractive-transfer-negative-values
title: Carrying a comp change as a minus-and-plus difference goes negative when both rebuilds darken
domain: comp
tags: [difference map, subtract, negative values, light groups, nuke]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, src:yt-transcripts]
feeds: [comp, coach]
conflicts: none
---
Method: change map = rebuild A minus beauty; add it to rebuild B. Works if you only brighten or darken slightly. Darken both (kill lights, then lower specular) and the same energy is removed twice: negative values, odd colours; one channel hits zero first, so it can hide [26:06-31:44].

**Use it:** comp checker: look for negative pixel values after transfer.
