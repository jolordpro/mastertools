---
id: redshift-opacity-map-to-geometry-opacity-emission-map-to-emission-colour-plus-weight
title: Redshift (C4D): an opacity map connects to the Geometry opacity input, an emission map to Emission colour with Weight raised; remap values with a Ramp or Color Correct node
domain: redshift
tags: [redshift, opacity map, emission map, ramp, color correct, remap, maxon, deep-read]
applies_to: Redshift in Cinema 4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=08CqyBVkpeU, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Maxon Training Team [06:18-07:18]. Opacity map: Geometry, Opacity input. Emissive map: base properties, Emission colour; right-click to add the input, then raise the weight (it starts at zero) [06:18-06:48]. To change the look without a new texture: adjust scale, offset or rotation on all texture nodes together, add a Color Correct node between Color Layer and material for hue and saturation, or a Ramp between a texture and the material to remap the black and white values with the knots [06:48-07:18].

**Use it:** Short wiring map for material builds; the coach can quote where each map type goes.
