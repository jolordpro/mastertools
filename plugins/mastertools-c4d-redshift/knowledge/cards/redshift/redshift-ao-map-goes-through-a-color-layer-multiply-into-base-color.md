---
id: redshift-ao-map-goes-through-a-color-layer-multiply-into-base-color
title: Redshift (C4D): the standard material has no AO input, so mix the AO map into the colour with a Color Layer node set to Multiply
domain: redshift
tags: [redshift, ambient occlusion, ao map, color layer, multiply, base color, texture, maxon, deep-read]
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
Maxon Training Team [05:47-06:18]. Redshift's standard material has no dedicated AO input. Put the colour map in the Color Layer base colour and the AO map in layer 1; blend with a Photoshop-style blend mode, where Multiply works best; then connect the Color Layer to the material's base colour [06:18]. Displacement in the same tip needs an RS object tag, Geometry Override, with tessellation and displacement enabled, enough subdivisions, and then maximum displacement and scale to set the look [05:20-05:47].

**Use it:** Supports the existing Color Layer and tessellation cards; the AO route is a baked-texture AO, unlike the AO render pass.
