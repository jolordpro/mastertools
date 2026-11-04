---
id: comp-woodin-render-position-world-object-camera-through-a-data-material-and-a-view-layer-override
title: Position world, position object and position camera passes come from three AOV outputs in a "data" material applied by a view layer override
domain: comp
tags: [mitchell-woodin, blender, aov, position pass, material override, view layer, nuke, deep-read]
applies_to: Blender (Cycles)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tB5-Oe7pTUs, src:yt-transcripts]
feeds: [[post-composite]]
conflicts: none
---
Method: make a material named data with three shader AOV outputs; feed Geometry Position to the world one, and Texture Coordinate Object and Camera outputs to the other two; name them (pw and so on) and add matching shader AOVs in the pass settings [05:23][05:53][06:25][06:56]. Editing the material changes every layer, so instead apply it with the data layer's Material Override, which covers every object (the viewport looks blank except in rendered view) [07:28][07:58]. Make sure the override is on the data layer, not the beauty [08:32]. Test with one frame first [08:32][09:29]. Results: position world is relative to the scene origin; position object has similar colours per object (red front, blue back left); position camera looks 2D and hard to read [10:00][10:45][11:15]. Data layer renders black on the beauty, which is correct [10:00].

**Use it:** the same idea on Redshift: a utility material override per render layer for position/depth AOVs, then use them in comp for fog, relight or masks.
