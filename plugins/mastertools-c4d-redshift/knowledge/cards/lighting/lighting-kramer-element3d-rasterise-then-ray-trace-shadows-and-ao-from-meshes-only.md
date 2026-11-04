---
id: lighting-kramer-element3d-rasterise-then-ray-trace-shadows-and-ao-from-meshes-only
title: "Kramer on Element 3D: shadows and ambient occlusion alone lift a rasterised image from pretty good to really good, and need meshes but no textures"
domain: lighting
tags: [polish, andrew-kramer, ambient occlusion, shadows, rasterisation, ray tracing, element 3d, cost, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=gNh9r-VbSVg, src:yt-transcripts, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
The plugin renders with fast OpenGL rasterisation, then adds ray-traced shadows and ray-traced ambient occlusion. Ray tracing normally means loading every texture because bounces pick up colour, but shadows and occlusion only need the meshes, so they chose those two and skipped colour-bounce GI [1:07:02-1:07:34]. That made the cost far lower than re-tracing the whole frame while still giving a big jump in realism.

**Use it:** For quick drafts, get grounding from shadows and occlusion first and leave colour-bounce GI for finals.
