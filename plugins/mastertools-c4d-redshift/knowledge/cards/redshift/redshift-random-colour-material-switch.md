---
id: redshift-random-colour-material-switch
title: Random Color Switch and Random Material Switch nodes distribute colours or materials with weights, seed and HSV jitter, even across separately named objects
domain: redshift
tags: [random color switch, random material switch, weight, seed, tint jitter, variation]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts]
feeds: [variant engine, lookdev sheet]
conflicts: none
---
Add inputs, set weight per colour (mostly pink, few blue and yellow) and a seed [38:40-39:44]; Color Jitter varies hue, saturation and value [39:44-40:14]. Material switch sits between materials and output [41:50]. Works on separate objects by object name, so it does not need MoGraph [43:57]. Newer nodes, about one to two months old in Feb 2025 [37:36].

**Use it:** Offer to replace per-object material copies; seed changes the distribution.
