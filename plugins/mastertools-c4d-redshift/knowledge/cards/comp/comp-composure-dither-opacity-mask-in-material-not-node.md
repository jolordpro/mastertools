---
id: comp-composure-dither-opacity-mask-in-material-not-node
title: In Unreal Composure the smooth-edge fix is the material's Dither Opacity Mask switch, not a Dither Temporal AA node
domain: comp
tags: [[unreal, composure, dither, masked-material, edges, anti-aliasing], deep-read]
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
Dean Yurke (30+ years film compositing, own channel) found that a Dither Temporal AA node fed to both opacities gave newsprint cross-hatch edges that stayed hard at render time [20:18-21:22]. His fix: duplicate the engine's M_CompositeMesh lit-mask material into your own folder (alt-click the instance to find it), then in Material Attributes details switch on "Dither Opacity Mask" and apply [19:47-21:53]. It randomises edge points across temporal samples, so more samples blend smoother [21:53]. He had lived with the problem for two years.

**Use it:** Masked UE plates edges: use the built-in dither switch and render with enough temporal samples.
