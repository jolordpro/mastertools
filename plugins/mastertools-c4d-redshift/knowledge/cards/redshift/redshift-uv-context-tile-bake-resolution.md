---
id: redshift-uv-context-tile-bake-resolution
title: Tiling through UV Context Projection gives the bake resolution per tile, not once for the whole grid
domain: redshift
tags: [uv context projection, tiling, displacement, bake resolution, detail]
applies_to: Redshift 2026.2
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZAom6DvSi3s, src:yt-transcripts, https://www.youtube.com/watch?v=Xh8A767yA1U]
feeds: [redshift, coach]
conflicts: none
---
512x512 bake: tiling 4x4 with the texture remap stretches 512 over all tiles. Tiling 4x4 with UV Context Projection on the displacement uses 512 per tile, so far more detail without raising resolution [52:13-53:17]. Plug it into the Displacement node's UV context input.

**Use it:** coach: for tiled displacement use UV Context Projection, not texture remap.
Transcript support: Demo at 512 bake resolution: tiling by remap uses 512 for the whole 4x4 grid; tiling by UV Context uses 512 per tile. (https://www.youtube.com/watch?v=Xh8A767yA1U [50:09-53:49])
