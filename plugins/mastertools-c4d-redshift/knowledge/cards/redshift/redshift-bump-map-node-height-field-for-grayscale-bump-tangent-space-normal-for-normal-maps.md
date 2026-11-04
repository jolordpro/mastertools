---
id: redshift-bump-map-node-height-field-for-grayscale-bump-tangent-space-normal-for-normal-maps
title: Redshift (C4D): both bump and normal maps go through a Bump Map node; keep Height Field for a greyscale bump and switch to Tangent-Space Normal for a normal map
domain: redshift
tags: [redshift, bump map node, normal map, tangent space, height field, height scale, maxon, deep-read]
applies_to: Redshift in Cinema 4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=08CqyBVkpeU, src:yt-transcripts]
feeds: [lookdev, CHECKS]
conflicts: none
---
Maxon Training Team [04:40-05:20]. A bump map is greyscale up/down information; a normal map is RGB that resembles XYZ axes [01:03]. Either needs an extra Bump Map node so Redshift reads it correctly: connect the texture to the node's input, then the node to the material's bump map input [04:42]. Grayscale bump: leave the input map type on Height Field. Normal map: change the input map type to Tangent Space Normal [05:10]. The Height Scale value sets how much surface detail shows [05:15]. Many materials have one or the other, some both.

**Use it:** Common first-material mistake to catch: normal map plugged straight into a bump input or left on Height Field.
