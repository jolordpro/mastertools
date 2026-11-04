---
id: lighting-rim-light-height-burnt-edges-versus-readable-edge
title: A rim light set too low burns the edge into the background; raise it until the edge shows as a thin highlight and the whole shape reads
domain: lighting
tags: [rim light, edge highlight, burnt, product lighting, separation, renderram, deep-read]
applies_to: any 3D (2022)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=xFGEdIs5OSM, src:yt-transcripts]
feeds: []
conflicts: none
---
RenderRam [05:23-07:22]. With the back light low, the top edges of the crate handles were burning to near the background value and merging with it. Raising the light gave a clean edge highlight with no burn, and the complete outline of the crate became visible; the downside was a dark side that was fixed by moving and enlarging the light. Combined with all lights, a too-big rim highlight was reduced with the light's size [08:22].

**Use it:** Check for rim light that burns: edge pixels should differ from the background; raise or shrink the rim until they do.
