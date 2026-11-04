---
id: lookdev-vray-c4d-cosmos-import-convert-to-node-material-and-blend-node-with-texture-mask
title: V-Ray for C4D: import a Chaos Cosmos material, convert selected classic materials to nodes with the Convert Materials tool, and combine two with a Blend node driven by a texture
domain: lookdev
tags: [v-ray, chaos cosmos, convert materials, blend node, node editor, triplanar, cinema 4d, deep-read]
applies_to: V-Ray for Cinema 4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=i6zQmQD_auA, src:yt-transcripts]
feeds: [lookdev, pipeline]
conflicts: none
---
Chaos V-Ray tutorial [07:23-11:46]. Cosmos browser: filter by category (fabric), search, press the green import button; the drop-down shows import options including triplanar mapping, for models without UVs [07:23-08:25]. Imported materials arrive as classic materials; the V-Ray menu, Tools, Convert Materials converts all or only the selected ones, and can delete the original and assign the new one to the mesh [08:25-09:28]. Combining two: a Blend node, with one material as base and the other in the coat slot; an opacity slider would weaken the coat evenly everywhere, so plug a texture into the blend amount instead [10:05-11:46]. Also: pick objects straight from the frame buffer with a right-click [01:15].

**Use it:** Pattern worth copying: control a blend with a texture mask, not a global slider.
