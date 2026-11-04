---
id: redshift-matcap-node-cel-shading-step-ramp-fresnel-outline-and-ao-layers
title: Redshift MatCap node (2023, pre-Toon): ramp set to step turns a matcap into cel shading, with a Fresnel outline and AO multiplied in a Color Layer
domain: redshift
tags: [redshift matcap, cel shading, npr, ramp, fresnel, ambient occlusion, color layer, c4d, eyedesyn, deep-read]
applies_to: Cinema 4D + Redshift matcap node, mid-2023 (before the Toon material)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=rE_15TwtY5A, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
EJ (eyedesyn, July 2023). Matcap texture (a lit sphere image) goes into the MatCap node, whose output plugs straight into the material output surface; no Redshift material node is needed [02:07-03:41]. It ignores scene lights (dome, sun and sky do nothing), so shading stays camera-fixed; the texture's rotation moves the apparent light [03:41-04:43, 07:21-07:52].
Cel look: feed the matcap into a Ramp, select all knots and set interpolation to step; remap the colours [05:16-06:49]. Blend or linear interpolation gives a softer toon falloff [08:23-09:27].
Outline: Fresnel with facing and perpendicular colours swapped (white facing, black edge), turn off use IOR, lower the curve number to widen, raise it to thin the line; clamp it through a ramp [09:57-11:30]. Combine with Color Layer: cel ramp as base, Fresnel on layer one, blend mode Multiply [11:30-12:34]. Shadow in concavities: AO node with spread at 0 plugged to layer two, Multiply [15:21-16:41].
Per-material variants (green, red, white, black) copy this node tree with different ramp colours [13:05-15:09].

**Use it:** if Toon material is unavailable (older Redshift) or a camera-fixed fake light is wanted, use this graph; for exposure and light-driven toon use the Toon material card instead.
