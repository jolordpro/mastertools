---
id: redshift-single-multichannel-exr-half-zip16-with-aov-preset-and-tokens
title: Chad Ashley's output setup: Multi image only, one half-float zip EXR with every AOV embedded, alpha on, saved as a render preset with tokens
domain: redshift
tags: [chad-ashley, exr, multichannel, half float, zip, aov preset, tokens, deep-read]
applies_to: Redshift 2.x for C4D (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ARykOD6lG3c, src:yt-transcripts]
feeds: [comp, estimator, pipeline]
conflicts: none
---
Output: leave Regular Image off, turn Multi Image on, and make an EXR preset: zip compression, 16 scan lines per block, half float (16 bit per channel), multichannel; tick alpha, which he finds oddly placed and often forgets [12:33-13:04]. All AOVs ride in one EXR; separate files per pass are possible but he prefers one clean file [14:07].
The AOV list, including custom AOVs, is saved inside a render preset so a standard set is not rebuilt each job; add an output path built with tokens [26:01-27:03]. Catch: a preset that names a custom AOV fed from a shader fails if that shader is not in the new scene, so keep generic AOVs in the preset or start from a scene that already holds the helper shaders [48:13-49:17].
Depth should be saved unfiltered; see the depth and DOF card.

**Use it:** A delivery check can look for Multi image on, half float, alpha on and a token path. Supports redshift-multipart-exr-per-aov-compression.
