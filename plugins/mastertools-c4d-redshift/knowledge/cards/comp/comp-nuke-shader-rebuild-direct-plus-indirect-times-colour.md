---
id: comp-nuke-shader-rebuild-direct-plus-indirect-times-colour
title: Rebuild a render from passes per lobe as (direct + indirect) times colour, then add lobes and emission
domain: comp
tags: [alex, levelup plus vfx, nuke, multipass, beauty rebuild, diffuse, glossy, transmission, emission, aov, deep-read]
applies_to: Nuke; passes from Blender Cycles
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts, https://www.youtube.com/watch?v=b0hbVd9aZkA]
feeds: [comp]
conflicts: none
---
Per lobe: shuffle out colour, direct and indirect; add direct to indirect, multiply by colour [07:44-08:45]. Do this for diffuse, glossy (reflections; his rule: B input always points up) and transmission, then add the lobes together [09:16-10:52].
Emission is added on top with no maths; the environment/HDRI light pass is a separate shuffle, only needed if the world lights the scene (here it was occluded) [11:23-12:26].
Why: once rebuilt, each lobe can be graded alone, then glow goes on the lights [12:57]. Contact-sheet the layers first to see what the EXR holds [06:42].

**Use it:** matches the rule that light groups must sum to the beauty; use it as the verification step before grading a pass-built comp.
