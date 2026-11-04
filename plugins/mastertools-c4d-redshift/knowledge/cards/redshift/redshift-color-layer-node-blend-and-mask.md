---
id: redshift-color-layer-node-blend-and-mask
title: The Color Layer node stacks a base and seven layers with blend modes and masks; masks must be grayscale 0-1
domain: redshift
tags: [color layer, blend modes, mask, vertex color, ramp, grayscale, texture blending]
applies_to: Redshift 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, src:yt-transcripts, https://www.youtube.com/watch?v=-lpj38Cql4c, https://www.youtube.com/watch?v=08CqyBVkpeU]
feeds: [redshift, coach]
conflicts: none
---
Color Layer works like layer blending in Photoshop or After Effects on texture inputs, not materials [1:29:41]. Average gives a full mix of two textures; a noise or other grayscale map can be the mask [1:30:44].
A mask is numerical 0-1, so colour data such as ZBrush poly paint needs a ramp to turn it grayscale first [1:33:51].

**Use it:** the coach recommends Color Layer when a texture must combine with a logo or existing map; flag colour fed directly into mask inputs.
Transcript support: Color Layer with the colour map as base and the AO map as layer 1 on Multiply. (https://www.youtube.com/watch?v=08CqyBVkpeU [05:47-06:18])
