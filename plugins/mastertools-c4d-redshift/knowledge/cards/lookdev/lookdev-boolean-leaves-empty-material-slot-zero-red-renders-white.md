---
id: lookdev-boolean-leaves-empty-material-slot-zero-red-renders-white
title: After Boolean operations an empty material slot at index 0 made a red shell render white; check slot assignments when a material seems ignored
domain: lookdev
tags: [material slot, boolean, empty slot, material index, debug, blender, poké ball, deep-read]
applies_to: Blender (principle general)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=TojQChim9mM, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Codex's red top half rendered white; after several iterations it found Booleans had left an empty material slot at index 0 and every face pointed at it, so the red material never applied; fix was rebuilding the slot assignments [07:13][07:44]. Also: specular highlights blowing out hot on glossy bodies was fixed by lowering light and gloss [04:09][04:39]; chrome borders kept catching too much light and washing the centre until the key was moved and roughness changed [06:12].

**Use it:** debug order for "wrong material": check slot or selection assignment before touching shader values.
