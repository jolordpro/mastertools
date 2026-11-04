---
id: lookdev-rise-texture-lod-fixes-slow-streaming
title: Slow renders often come from texture streaming off the network, so set a low texture LOD for lighting and often for finals
domain: lookdev
tags: [rise, texture lod, mipmap, streaming, materialx, karma, render time, 4k udim, deep-read]
applies_to: Karma, MaterialX; principle any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Rise's experience: slow renders are often not about geometry count or shader count but texture streaming from the network [40:03]. A scene with about 1.5 million USD prims stayed interactive using the lowest texture level (level 5 of several) [40:33].
They store LOD paths on the image shader prim and apply the level through an inherits class, which avoids de-instancing assets and extra variants. Level can follow the camera distance [40:33-41:04].
Lighting is always set up at very low quality, and finals rarely need the top level: 4K UDIM tiles are pointless for a far camera [41:04].

**Use it:** Check: for far or small shots, flag full-res textures. Matches the Redshift texture cache advice.
