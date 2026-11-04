---
id: redshift-toon-grain-and-brush-edge-from-maxon-noise-on-exposure-and-bump-casey-gu
title: Casey Gu toon look: contour noise as displaced turbulence, tone-map colour edges broken with bump noise (undulating turbulence, Y scale 100), grain by noise into exposure
domain: redshift
tags: [redshift toon, tone map, bump, maxon noise, grain, brushstroke, contour, casey gu, deep-read]
applies_to: C4D + Redshift toon shader (2024 upload, Casey Gu)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=LWavn-Io1_o, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Scene: long lens flattens the frame for a 2D feel, an infinite light from the top left, UV-mapped model [00:03]. Contour noise controls thickness by greyscale (black zero, white keeps it); raise contrast to break the line, enlarge scale to calm it, use displaced turbulence for more detail, and a smaller duplicate on the external line [01:05-02:44].
Reflection off. Break hard tone-map colour steps with a bump map from noise at scale 0.01, type undulating turbulence, Y scale 100 for horizontal strokes, more contrast [02:44-04:18].
Grain: Maxon Noise into base tone map exposure, scale 0.05, raise low-level clip so whites stay, turbulence variant for edge grain [04:18-05:26].

**Use it:** tool-chain: cel look via three noise nodes. Values are for his model size, tune per scene.
