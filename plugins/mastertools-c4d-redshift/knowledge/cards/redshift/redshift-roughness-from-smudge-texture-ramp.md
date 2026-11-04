---
id: redshift-roughness-from-smudge-texture-ramp
title: Use a smudge texture for roughness, then a ramp to keep fingerprints subtle
domain: redshift
tags: [roughness, fingerprint, smudge, ramp, imperfection, product, realism]
applies_to: Redshift 2026
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, src:yt-transcripts, https://www.youtube.com/watch?v=yFCUHeTf0mQ, https://www.youtube.com/watch?v=RpiCCLHjlWQ, https://www.youtube.com/watch?v=0Zg4lpwZGe0]
feeds: [elevate, lookdev]
conflicts: none
---
Plug a fingerprint texture into roughness: black is shiny, white is rough [1:05:00-1:05:32]. A client may find full smudges dirty, so a ramp remaps contrast to a few slight details [1:06:05-1:06:37]. Triplanar at 200 cm fit a bottle for a hand-size feel.
The trainer calls that kind of small detail what separates product work from the rest [1:39:16].

**Use it:** elevate suggests subtle roughness variation on glossy hero objects, kept low contrast through a ramp.
Transcript support: Maxon trainer: black 0 and white 1 roughness map via triplanar and ramp; lowering the ramp white node to 75 or 50 percent caps roughness (https://www.youtube.com/watch?v=RpiCCLHjlWQ [1:27:54-1:34:44])
Transcript support: Say drives reflection roughness from a grunge texture through a ramp (white = full blur); warns that tiled scratches look penny-sized and tiling is a CG tell (https://www.youtube.com/watch?v=0Zg4lpwZGe0 [36:39])
