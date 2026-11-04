---
id: motion-rebellion-ocean-direction-masks-and-proximity-whitewater
title: Direction-aware drag masks and proximity masks keep waves off the beach and cut whitewater to the shoreline
domain: motion
tags: [rebellion vfx, evil genius 2, ocean, masks, whitewater, proximity, dot product, performance, deep-read]
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
Drag mask: dot product of velocity with the shore direction gives 0 when water recedes and 1 when it advances; multiply with a distance gradient so drag applies only near the shore, and mix with vorticity to damp turbulent zones. This kept waves off the beach where people sit [31:06-33:10].
Whitewater: a purpose-made leading-edge source for a clean line; then keep only particles within a set distance of rocks and beach (proximity mask) and reduce them with each iteration; the same trick placed foam around distant islands [33:10-35:17].
Result: four times fewer particles still looked right at distance and played nearly in real time [35:17]. A proximity-to-ground mask also drives transparency near shore and darker opaque blue further out [36:18-37:22].

**Use it:** shows how to limit effect cost by distance masks; numbers are Houdini-specific.
