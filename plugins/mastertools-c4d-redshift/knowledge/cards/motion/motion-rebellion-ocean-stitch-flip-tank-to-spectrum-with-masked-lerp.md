---
id: motion-rebellion-ocean-stitch-flip-tank-to-spectrum-with-masked-lerp
title: Hide the seam between a FLIP tank and the open-ocean spectrum by flattening the border and lerping with a mask
domain: motion
tags: [rebellion vfx, evil genius 2, ocean, flip, seam, ocean spectrum, houdini, deep-read]
applies_to: Houdini
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: []
conflicts: none
---
Clip bottom and side borders of the meshed sim (keep the front where it hits the shore), mask a midsection, flatten under that mask, evaluate the ocean spectrum over the whole mesh and lerp between old and new meshes with the same mask; add noise to hide the seam [38:56-41:33].
Keep edge grids aligned between the two meshes; the process is procedural so a calmer or more violent ocean updates automatically [41:33-42:03].

**Use it:** a seam-hiding method for tiled simulations.
