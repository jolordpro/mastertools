---
id: comp-rebuild-beauty-from-direct-indirect-colour-passes-in-nuke
title: Rebuild the beauty in Nuke per component: (direct plus indirect) times colour for diffuse, glossy and transmission, then add emission and multiply shadow or AO
domain: comp
tags: [[nuke, passes, cycles, multilayer-exr, shuffle, rebuild-beauty, shadow-catcher, whisper], deep-read]
applies_to: Nuke with Blender Cycles passes (any renderer's equivalents)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=1GJPnzsA910, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
CG Kalvi tutorial (whisper transcript, heavy accent and several garbled stretches, so treat details as approximate): save all passes in one multilayer EXR; Shuffle each layer out [02:39-03:56]. For diffuse: merge direct plus indirect, then multiply by the diffuse colour pass; repeat for glossy and for transmission; then add emission, and bring shadows and ambient occlusion in with multiply [04:37-08:54]. A shadow-catcher render has no alpha, so shuffle the combined pass's alpha in before merging over a background [10:06-10:43]. Rebuilt this way, single components (gloss, transmission, emission) can be adjusted without re-rendering [11:56]. Pass names vary per renderer; the method does not [02:39].

**Use it:** Pass-rebuild check: rebuilt result must equal the beauty before any grading is done on a component.
