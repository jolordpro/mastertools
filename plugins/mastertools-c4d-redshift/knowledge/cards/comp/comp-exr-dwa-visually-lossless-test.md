---
id: comp-exr-dwa-visually-lossless-test
title: DWAA/DWAB EXR compression is lossy but a trainer sees no problem in comp; test it with a Difference blend and crushed Levels
domain: comp
tags: [exr, dwaa, dwab, compression, difference, levels, file size]
applies_to: OpenEXR via Redshift, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
DWAA is lossy yet showed no comp problems in the trainer's work; DWAB gives smaller files. Deep compositing, which After Effects cannot do, or very high resolution might show a difference [17:07-18:08].
Test for your own scene: render one frame with two compressions, put one over the other in Difference mode, add a Levels adjustment layer to crush it, and see if the eye can find any change [18:40-20:16].
If the difference only shows after crushing, it is theoretical, not real.

**Use it:** a delivery or draft step can offer a compression A/B with a measured difference image before choosing the farm output format.
