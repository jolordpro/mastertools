---
id: pipeline-virtual-production-genlock-and-render-at-camera-rate
title: A volume renders at camera frame rate with shutter-angle blur and is synced by genlock across nodes and camera
domain: pipeline
tags: [10 dots, virtual production, genlock, unreal engine, chaos arena, nodes, tearing, shutter angle, deep-read]
applies_to: Unreal 5, Chaos Arena
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aKRcGoc_osQ, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
The environment renders at the camera speed, not at game speeds, so scenes can be heavier, but motion blur matching frame rate and shutter angle must be rendered in the engine [15:23]. 10 Dots' volume uses four render nodes (RTX A6000-class GPUs, 64-core Threadrippers) plus a master node that also drives the ceiling, on a 40 Gb network [15:55].
Without sync, animation tears between nodes; genlock fixes it and also syncs the camera sensor to the screens [16:27]. Cameras need a genlock input (Alexa 35 used; hybrid cameras rarely have it) [18:35]. Unreal can look gamey, fine for stylised looks, and ray tracing is limited; Chaos Arena offers real-time ray tracing with assets from Maya, Houdini, Max, Blender and V-Ray [17:00-18:35].
Environments must be rebuilt for Unreal.

**Use it:** If a client wants LED-wall content, deliver real-time-ready assets; check frame rate and shutter.
