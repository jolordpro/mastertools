---
id: redshift-scratches-shader-outputs
title: The procedural scratches shader has several outputs, bump plugs in directly, and its steps control was broken on Mac in 2026.8
domain: redshift
tags: [scratches, procedural, shader, bump, mask, material blender, bug, 2026.8]
applies_to: Redshift 2026.8 (Mac M3 in the demo)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4]
feeds: [redshift]
conflicts: none
---
New node [56:46]: outputs include scratch colour, a mask, roughness, anisotropy and bump; bump strength lives on the node so no bump node is needed, negative strength flips the relief [1:00:27-1:00:58]. Inputs can be driven by ramps or noise (ctrl/cmd-click) [59:24].
Scratch length, density, width, curve, seed. The mask output can drive a material blender to show another material in the scratches [1:03:34]. Steps (orientation) could not be changed on Mac in this build; fix promised for the next release [1:02:01].

**Use it:** when a metal look needs wear, the coach suggests this node and its mask; recheck the steps bug against the current release before relying on directional scratches.
Transcript support: Second upload; adds scratch canvas size = length 100 reference, mask 0-1 masks scratches out, material layer/blender with the mask output. (https://www.youtube.com/watch?v=74lleTzTfC4 [56:46-1:04:38])
