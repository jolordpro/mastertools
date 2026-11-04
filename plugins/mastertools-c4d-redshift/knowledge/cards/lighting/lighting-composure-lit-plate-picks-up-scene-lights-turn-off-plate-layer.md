---
id: lighting-composure-lit-plate-picks-up-scene-lights-turn-off-plate-layer
title: Composure plate meshes can take scene light if the plate layer is disabled, then set specular 0, roughness 1 and a multiply colour
domain: lighting
tags: [[unreal, composure, plate-lighting, specular, roughness, sequencer], deep-read]
applies_to: Unreal Engine 5.7 Composure
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=zlZCKT-5pLU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
To let UE lights hit the projected plate, disable the Plate layer in the composite actor so the composite mesh material is rendered with the environment [22:56]. The material then looks glossy; set specular 0 (default 1) and roughness 1 [23:29-24:06]. Brightness mismatch is fixed by multiplying the composite texture RGB by a grey constant exposed as a parameter ("multiply color"), which can be animated in Sequencer through a static mesh component material slot [24:06-26:21]. The view only updates when scrubbing in Simulate mode or toggling the layer [26:29]. A cylinder stand-in only gives crude light; a human-shaped proxy should light better [23:29]. Animated flicker lights matched the set's practical flicker, and a big rectangle light flickers both plate and background [26:52-27:25]. If the set lighting had a moving light, match it with an animated light in the engine [02:50].

**Use it:** Test the plate against its CG lighting by rotating one light and watching the plate react.
