---
id: pipeline-splat-versus-photogrammetry-baked-lighting-and-glass
title: A splat keeps the lighting and reflections it was captured with; photogrammetry is shot flat so materials can be added later
domain: pipeline
tags: [gaussian splat, photogrammetry, baked lighting, cross-polarised, glass, fbfx, chris, deep-read]
applies_to: Gaussian splat vs photogrammetry
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=H4LW2fMtSN8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Chris of FBFX's capture department (the guest; Adam Savage is host) says photogrammetry is shot with cross-polarised, highlight-free light so materials go on later; a splat bakes the lighting in, so you can light the subject for the final scene and keep the real reflections without shaders [08:29-09:33]. Splats also handle glass, which photogrammetry loses, though glitchy [10:04]. Splats look good from video but lack the clean mesh for post sculpting; the team still does heavy artist clean-up on photogrammetry hair and skin [03:49-04:21].
Processing: capture is quick, processing takes roughly two to three hours, and running training longer (2 vs 10 hours of steps) keeps refining the result [03:19, 07:57]. A 3-million-splat asset runs in a browser where a 3-million-polygon asset would not [02:48].

**Use it:** a splat is a lighting-locked reference, not a relightable asset (unlike the creator in QW8ec3qquHA who plans relighting in Octane); do not promise relighting from a splat.
