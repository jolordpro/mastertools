---
id: broadcast-capacity-masks-on-channels-work-in-3d-too
title: Masks are non-destructive, channel-based and work in 3D: a plane mask on a channel clips anything assigned to that channel
domain: broadcast
tags: [masks, channels, reveal, 3d mask, cloners, wipe, motion design, deep-read]
applies_to: Unreal Engine 5.6 / 5.7 motion design
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts]
feeds: []
conflicts: none
---
A mask is an actor in space; anything on the same channel is clipped by it [26:58]. Toggling a mask off lets elements break out, which is how text reveals from behind a box [32:45]. Most scenes use around five channels and none go without [33:16]. Masks also clip 3D cloners, so a sidebar can hold a live 3D scene; in 5.6.1 clone masking needed a geometry-mask-reader blueprint component (fixed in 5.7) [43:07-44:11]. A ball wipe was a mask following the camera, with a second mask wiping it off, all on one channel [44:44-45:14].

**Use it:** Think of reveals as channel masks. For C4D/AE, consider live 3D inside 2D shapes instead of pre-rendering and keying.
