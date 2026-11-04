---
id: lighting-octane-baking-camera-group-id-bakes-light-into-square-texture
title: Octane lighting bake: baking camera, matching group ID on object tags, square 1024 texture, saved at 16-bit
domain: lighting
tags: [octane, baking, bake lighting, texture, group id, real time, game engine, deep-read]
applies_to: Octane for C4D (2019 lesson)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7tTLH8wqMYQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Octane Universe: set a square resolution (1024x1024), add an Octane camera with type Baking and a baking group ID (he used 10) [01:13]. Each object to bake gets an Octane object tag with the same ID under object layer; only objects sharing one texture space belong together (head and eyes were separate) [02:16]. The live viewer then shows lit surfaces unwrapped; changing the light temperature proved the light is baked [04:29]. Save as a 16-bit image (or EXR) from the viewer, apply to a new material, set the editor display to colour only [07:07]. Render passes such as diffuse direct and indirect can be added and saved, even multi-channel EXR [05:43]. Baked light does not update if lights move: use it only for static objects [08:13].

**Use it:** a pattern for static set pieces in real-time or lighter renders; not a Redshift step.
