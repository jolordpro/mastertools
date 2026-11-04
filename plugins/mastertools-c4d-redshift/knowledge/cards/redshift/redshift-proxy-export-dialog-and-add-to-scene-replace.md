---
id: redshift-proxy-export-dialog-and-add-to-scene-replace
title: Redshift proxy export: compress data, world origin, and Add Proxy to Scene swaps the mesh for its proxy in one step
domain: redshift
tags: [proxy, export, redshift proxy, compress, sequence, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
File > Export > Redshift Proxy asks for selected objects or the whole scene, whether to include lights, and whether to compress data (he turns it on for a smaller file) [02:07-02:37]. Proxy origin stayed at World because the mech sat at world zero [02:37].
Add Proxy to Scene exports, loads the proxy and removes the original in one go, leaving a black bounding box in the viewport [03:10-04:11].
Animation: Current Frame for a still mesh, All Frames for point-cache or MoGraph motion, which writes a proxy sequence [03:10-03:40].
Chad calls it the Redshift version of an Arnold .ass file.

**Use it:** pipeline step: bake heavy or repeated assets to proxies before layout; the farm needs the proxy files at the same path.
