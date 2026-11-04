---
id: comp-back-to-beauty-recipe-add-direct-indirect-multiply-colour-then-sum-components
title: Back to beauty: per component add direct and indirect, multiply by colour, sum components, copy alpha from the beauty
domain: comp
tags: [back to beauty, fusion, blender, cycles, passes, channel booleans, multilayer exr, alpha, deep-read]
applies_to: Blender Cycles into Fusion
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=evwUXSqbysQ, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Robin Squares (Fusion user, not a pro comper by his own account). Split a multilayer EXR into nodes with the Reactor script 'Haas EXR Splitter Ultra' [03:00]. Per component (diffuse, glossy, transmission): add direct to indirect, then multiply by colour; then add the components together [04:33]. Ambient occlusion and shadow catcher are not part of the beauty, so leave them out; view-layer pass tabs show what is [04:03]. The rebuild should match the rendered RGBA exactly: toggle the two in the viewer to confirm [06:39]. Alpha is lost, so add a channel-booleans node taking RGB from the rebuild and alpha from the original, and swap inputs if it looks wrong [07:10]. Why: grade one component, such as gain on glossy, without re-rendering [08:15]. Rebuilt in linear needs a viewport LUT; add an OCIO colour-space node only when exporting to screen colour [19:16]. Render linear Rec.709 or the comp maths is wrong [22:23].

**Use it:** same sum-to-beauty check as the existing rebuild cards; his cheat sheet and 'channel merge' node confirm the order colour, direct, indirect.
