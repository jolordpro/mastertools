---
id: comp-yann-do-not-bend-shader-aovs-in-comp
title: If you must bend spec, diffuse or bump passes in comp to get the look, the lookdev was wrong; comp is for the last 5%
domain: comp
tags: [[yann dupont, comp, aov, lookdev, shader components, last 5 percent, lighting artist], deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=gjgAZ0x29ag, src:yt-transcripts]
feeds: [comp, shakedown]
conflicts: none
---
Yann Dupont: lighters mostly play with light intensity, not shader components. Artists who render spec, diffuse, bump and normal passes and rebalance them in comp are covering a lookdev problem that should have been fixed at the source; hand comp only the last 5% [42:44-43:14].

**Use it:** supports the "simple pass workflow" stance; flag heavy per-pass rebalancing as a sign to go back to materials.
