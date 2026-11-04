---
id: redshift-hex-tiling-hides-repeats
title: Hex tiling in UV Context Projection breaks up visible texture repeats on large organic surfaces
domain: redshift
tags: [hex tiling, tiling, repetition, uv context projection, ground, landscape, texture]
applies_to: Redshift 2026 (hex tiling shipped one release before 2026.8)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4]
feeds: [redshift, coach]
conflicts: none
---
Set the node's tiling mode to Hex: hexagonal cells with noise and blending, so a texture tiled 8x on a 4000x4000 plane stops repeating [09:23, 15:53]. Controls: tile blend, blend curve (falloff), blend noise and noise scale, plus offset and rotation [10:25].
Use on organic or large-scale maps (road, ground, landscape). Not for geometric patterns, it scrambles them [10:58].
Plug it straight into the output to hit every texture, or into individual nodes when one layer should not hex-tile (for example two stacked displacements) [16:23-17:57]. Many older library materials still use the legacy triplanar node.

**Use it:** when a large surface shows obvious tiling, the coach points to Hex mode; the scene check could flag an 8x-style tile count on a big plane with a non-hex mapping.
Transcript support: Same stream, second upload: adds that the test grid exaggerates hexes, and tile blend/blend curve/blend noise/noise scale are the controls; legacy library materials still use old triplanar and may be updated by the capsule team (trainer cannot promise). (https://www.youtube.com/watch?v=74lleTzTfC4 [05:46-17:50])
