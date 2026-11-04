---
id: c4d-pyro-smoke-colour-to-mesh-via-vertex-color-tag-and-gradient-remap
title: C4D 2023 Pyro smoke colour can be carried onto the mesh with a Vertex Color tag, linear layer mode and a colour-mapping gradient
domain: c4d
tags: [pyro, vertex-color, volume-mesher, gradient, cinema-4d-2023, colour, deep-read]
applies_to: Cinema 4D 2023 Pyro with Volume Mesher (2022)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=2yaRgwWYoDg, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
PixelAffair, 2022 [13:51-22:08]. Smoke colour is keyframed on the Pyro tag (start red, at frame 20 key to green) so the sim carries a colour history [16:27-17:29].
- Mesher: add a Vertex Color tag to the Volume Mesher; on the Pyro object enable the Color output channel; drag the tag into the mesher's channel list [18:59-19:30].
- Set the layer mode to linear, enable remapping, then replace the colour with a gradient (presets are available) to recolour [19:30-22:08]. Same method works for temperature.
- His first result was only black and white and he put it down to a mesh that was not smooth enough or voxels too large; he did not fully resolve it [20:33-21:05]. Voxel size 3 to 4 on tag and object was used for the demo [17:59].

**Use it:** Treat as a lead for coloured smoke meshes; test before promising it.
