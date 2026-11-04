---
id: redshift-material-layers-base-first-then-roughness-map-bump-blend-and-scratches
title: Maxon trainer's wear-layer order: base metal first, then roughness map, bump, a blended wear layer, and scratches that also dent via a bump blender
domain: redshift
tags: [maxon, redshift standard material, layering, roughness, material blender, bump blender, triplanar, ramp, deep-read]
applies_to: Redshift 3.5 Standard Material in Cinema 4D R26 (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [lookdev, elevate]
conflicts: none
---
Think like a car getting older: clean paint first, then scratches and dirt [1:17:19-1:18:23]. Finish the base properties before adding layers, since changing them later changes every layer [1:19:59-1:20:29].
Steps: Metalness to 1 and a base colour; reflection colour a slightly lighter copy of the base [1:18:54-1:21:00]. Roughness from a greyscale map: black is 0, white is 1; run it triplanar first (same image on each axis, image X) to fix projection, then a Ramp to pull blacks up and drop the white node to 75 or 50 percent to cap roughness [1:22:36-1:34:44]. Bump node for surface roughness. Roughness also fakes bump [1:39:21].
Wear: Material Blender, layer 1 a duplicate with darker colour, blend colour is a triplanar map through a ramp; white shows the layer, so invert if reversed [1:40:22-1:45:30]. Layer 2 a dark under-layer for scratches (scale 2 by 2 for fine marks) [1:46:34-1:50:41]. Bump Blender with weight between 0 and 1 makes scratches dents, not just colour [1:51:12-1:53:18].
Advice: keep values subtle on a real render; she exaggerated for the stream [1:50:11-1:50:41]. Brightness of base colour affects reflectivity in the metalness workflow (Darren) [1:42:28].

**Use it:** The coach can give this as the standard order for a worn hero material.
