---
id: motion-unreal-media-textures-realtime-video-layers
title: Unreal media textures play ProRes video live inside materials, limited by disk speed
domain: motion
tags: [unreal engine, media texture, prores, video playback, sequencer, real-time, title sequence, deep-read]
applies_to: Unreal Engine 5.5
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5P-sO_2aiwU, src:yt-transcripts]
feeds: [estimator, pipeline]
conflicts: none
---
The Material Designer now accepts media textures: four stock clips played fully in real time in Sequencer, wiped with a black-and-white mask, with an alpha channel supported [15:42] [15:57]. No caching or render wait; drag in a new asset and it plays [16:28].
The clips were Apple ProRes, a mix of 4K and 1080; how well it plays depends on the machine's disk speed and requirements [16:28]. He frames it as a way to mix video playback with 3D, for titles and concert-style visuals [17:01] [19:35].
Stack: footage, tint, glow, texture overlay all inherit down the layers [18:35].

**Use it:** Check disk throughput before promising real-time 4K ProRes layering; draft with 1080 clips first.
