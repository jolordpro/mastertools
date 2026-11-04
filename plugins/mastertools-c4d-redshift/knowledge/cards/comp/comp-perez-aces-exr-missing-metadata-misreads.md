---
id: comp-perez-aces-exr-missing-metadata-misreads
title: An ACES file with no ACES metadata opens as plain scene-linear and looks wrong until its input is set to ACES2065-1
domain: comp
tags: [victor perez, foundry, fmx, aces, failure, exr, metadata, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Perez made a file on purpose without the ACES metadata. Nuke read it as scene linear and the picture looked wrong [44:54-45:56]. The fix is one pick: set the read's input transform to ACES2065-1.
The reverse also holds: a CG render written as ACEScg opened correctly with no change at all, because Nuke already treats linear as ACEScg [45:56-46:26].

**Use it:** First thing to check when a received EXR looks off: is the colour-space tag and metadata flag there? Ask the sender which space it is before grading.
