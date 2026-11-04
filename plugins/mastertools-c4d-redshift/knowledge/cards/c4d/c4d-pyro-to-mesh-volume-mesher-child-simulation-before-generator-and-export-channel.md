---
id: c4d-pyro-to-mesh-volume-mesher-child-simulation-before-generator-and-export-channel
title: C4D 2023 Pyro to polygon mesh - make the Pyro object a child of a Volume Mesher, enable the channel to export, and set simulation before generator
domain: c4d
tags: [pyro, volume-mesher, cinema-4d-2023, mesh, simulation, generator, deep-read]
applies_to: Cinema 4D 2023 Pyro (2022)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=2yaRgwWYoDg, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
PixelAffair, uploaded 2022-11-19.
- Pyro voxels are already a volume, so a Volume Mesher with the Pyro object as its child is enough [10:07-10:40]. Nothing appears at first because the sim lives on the GPU and is not really in the scene [10:40-11:11].
- On the Pyro object, object tab, switch on the channel to bring into the scene: temperature for fire, density (smoke) for smoke. Then lower the mesher voxel range until the mesh shows [11:11-11:44].
- It still fails on playback until Project Settings (Ctrl+D), simulation, has "simulation before generator" ticked, so the sim runs first and the mesher after [12:14, 13:51]. He repeats this as an always-on step.
- Mesh smoothness depends on voxel size; blocky voxels give poor results, so use a smaller Pyro voxel size [20:33].

**Use it:** Meshing fire or smoke gives real polygons for ordinary materials, but needs a sim-first order and a visible channel.
