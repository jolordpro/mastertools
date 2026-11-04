---
id: comp-usd-no-cryptomatte-so-make-an-emission-mask
title: If the renderer lacks Cryptomatte, import the USD shot into Nuke and render an emission-only material as a mask
domain: comp
tags: [comp, nuke, mask, cryptomatte, usd, emission, 3delight, deep-read]
applies_to: Nuke, USD, 3Delight
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
For a colour correction on the dinosaur, the USD renderer did not support Cryptomatte yet [30:56]. Fix: import the shot container into Nuke as 3D nodes, assign the dinosaur a material with emission 1 and all else 0, then shuffle the output to alpha for a clean mask [31:27] [31:58].

**Use it:** Use when ID passes are missing: a flat emission material on one object gives a working matte quickly.
