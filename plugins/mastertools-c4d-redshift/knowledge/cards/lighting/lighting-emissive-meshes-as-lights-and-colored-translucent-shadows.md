---
id: lighting-emissive-meshes-as-lights-and-colored-translucent-shadows
title: Real-time path tracing can light a scene from emissive meshes alone and cast coloured shadows through translucent surfaces
domain: lighting
tags: [richard cowgill, nvidia, unreal fest, emissive lighting, colored shadows, translucency, niagara lights, deep-read]
applies_to: Unreal Engine 5, NvRTX branch
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=zD9kS1nOuyU, src:yt-transcripts]
feeds: []
conflicts: none
---
Zero-light demo: no actor lights; glowing spheres alone give direct light, shadows, GI and reflections; every triangle becomes a light. He calls it still a bit experimental [21:28-23:41].
Coloured shadows from translucent surfaces (a stained-glass window) work without faking [26:31-27:03]. Particle (Niagara) lights can cast shadows and fog shadows [27:03-27:33].
Foliage with animated vertex offset path-traces too [20:25-21:31].

**Use it:** reference for what emissive-as-light looks like when properly sampled; Redshift already does this with its own sampling cost.
