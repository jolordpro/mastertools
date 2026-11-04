---
id: pipeline-impostor-lod-options-billboard-multiplane-sprite-sheet-packed
title: Shader-based LOD options for distant objects: front billboard, multiplane billboard, octahedral sprite-sheet impostor with stepping, and a packed impostor card
domain: pipeline
tags: [impostor, lod, billboard, sprite sheet, octahedral, distant objects, blender, thomas murphy, deep-read]
applies_to: Blender, real-time and offline (2026)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ofTjypijLEU, src:yt-transcripts]
feeds: []
conflicts: none
---
Thomas Murphy [00:00-02:38]. Instead of reducing polygons, bake a shader proxy to a plane. Options: (1) front-facing billboard, a plane tracked to camera with a static image: breaks for objects with a back or depth. (2) Multiplane billboard: more angles, but intersections look messy and costs many faces; works for pine trees. (3) Octahedral sprite-sheet impostor (the Instant Imposters add-on): ortho renders from many angles on a convex mesh, with albedo, normal and emit sheets; a visible stepping between angles, softened by view interpolation noise. (4) His packed impostor card: one plane, no stepping, up to 60 unique items packed into three textures (normal, diffuse, roughness); every impostor shares one material, so a single draw call. Best on cuboid shapes, also works on trees; a depth-slice 'ultra' mode adds parallax for other shapes.

**Use it:** For heavy background scenes, offer the impostor ladder before decimation: how far is the object from camera and does it need a back view?
