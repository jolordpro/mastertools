---
id: comp-merged-aov-one-exr-per-frame-shuffle-out-and-plus-rebuild
title: Merged AOVs write one EXR per frame; in Nuke shuffle each layer out and rebuild the beauty with plus merges (direct+indirect, diffuse+specular)
domain: comp
tags: [sarkamari, reza, nuke, arnold, merged aov, shuffle, exr layers, direct, indirect, diffuse, specular, sss, rebuild, deep-read]
applies_to: Maya Arnold to Nuke 12.3
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=xwD_UPqbmCU, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Reza [01:04-12:06]: pick the driver, tick merged AOVs, render: each frame is one EXR with every pass inside. In Nuke, look at the layers from the viewer; subtle ones need gain or gamma up. Use the new Shuffle (Nuke 12.3), one per layer, postage stamps on, a backdrop per group, and label each.
Rebuild: diffuse direct + diffuse indirect (merge plus), specular direct + indirect the same, then diffuse + specular, then add subsurface. Alpha via copy node (K). He finds merged AOVs faster to comp than separate files [09:10].

**Use it:** keep layer names consistent with the render's AOV list; the plus-rebuild must match the beauty.
