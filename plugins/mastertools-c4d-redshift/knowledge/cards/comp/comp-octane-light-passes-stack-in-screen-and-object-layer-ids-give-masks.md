---
id: comp-octane-light-passes-stack-in-screen-and-object-layer-ids-give-masks
title: Octane (C4D): turn on a light pass per light and an object layer ID per object, save EXR, and the lights stack in Screen mode in post while each ID gives a ready mask
domain: comp
tags: [octane, render passes, light passes, layer id, masks, exr, screen mode, photoshop, deep-read]
applies_to: Octane for Cinema 4D
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=8zCqKpeF5Uc, src:yt-transcripts]
feeds: [comp, coach]
conflicts: none
---
3seater [08:27-12:42]. Enable render passes in the Octane render settings and pick Beauty passes (emitter, diffuse, reflection, refraction, shadow) plus a lighting pass for each light [08:59-09:31]. Stacking all the light passes in Screen mode in Photoshop recreates the full 3D lighting, and any single light can be raised or lowered in post [09:31-10:03]. Z depth and AO sit under info passes [10:03]. Object layer IDs set in the Octane object tag (his butterflies were ID 5) render as layer masks, so no hand masking is needed [10:35-11:07]. Save as EXR for the best quality; the free exr.io plugin opens the passes in Photoshop [11:38-12:09]. In Photoshop, Ctrl-click a mask channel to load it as a selection.

**Use it:** Use as the Octane version of the AOV plan: one light group per light plus ID masks, linear EXR out. Redshift users get the same result from light-group AOVs and ID/Cryptomatte.
