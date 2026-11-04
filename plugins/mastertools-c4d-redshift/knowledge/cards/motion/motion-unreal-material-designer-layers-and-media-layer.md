---
id: motion-unreal-material-designer-layers-and-media-layer
title: Material Designer builds PBR or layered effects in real time; a media layer plays video, Protron makes ProRes scrub
domain: motion
tags: [unreal, material designer, media layer, protron, prores, 60 fps, deep-read]
applies_to: Unreal Engine 5.5-5.6 Motion Design
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QWT8IAUfWSk, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker is David Grownick, Epic senior product specialist and ex Fox Sports real-time graphics, so vendor view. 5.5 added PBR support: drop in maps and channels fill (roughness, emissive) [10:54-11:24]; layer-based like a compositing app, so users find it familiar [11:55]; shader effects such as pixelate, colour shift, glow and noise stack cheaply, no profiling needed [12:26-13:59]. Broadcast needs a constant 60 fps (59.94) with no way around it, offline renders can be heavier [13:59].
5.6 media layer: a video clip layered in the material, foreground and background stackable [36:18-37:21]. The Protron media option makes ProRes accurately scrubbable [37:21-37:52].

**Use it:** Treat layered materials as cheap comp; check ProRes plates play scrubbed.
