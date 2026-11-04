---
id: pipeline-prism-usd-asset-variant-sets-from-scratch
title: Build a USD asset with one root, a geometry prim and a materials prim, then variant sets per shot
domain: pipeline
tags: [prism, usd, variant sets, asset, materialx, polyhaven, deep-read]
applies_to: Prism 2 (private beta mid-2023), QuiltiX early dev
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GE6Af6hjYfI, src:yt-transcripts]
feeds: []
conflicts: none
---
Richard Frangenberg (Prism founder) demo [08:24-10:29]: root prim with one child for geometry and one for materials; variant sets such as geometry (elephant, horse) and material (wood, stone), each with one selected. Drag geometry from the library into the variant, drag MaterialX files onto prims to assign, add an HDRI, then swap renderer (Arnold in demo). The saved asset opens in Houdini or Maya and lets a shot override the variant.
Prism also integrates Poly Haven and AMD's MaterialX library, letting artists download them in several resolutions and formats from inside the DCC [07:21-08:24].

**Use it:** For a shot-specific look change, set a variant rather than copy the asset.
