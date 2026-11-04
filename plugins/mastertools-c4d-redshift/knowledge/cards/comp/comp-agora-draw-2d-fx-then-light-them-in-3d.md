---
id: comp-agora-draw-2d-fx-then-light-them-in-3d
title: Hand-drawn 2D effects were projected on a plane, then matched by 3D lights and post-process so they sit in the shot without a comp stage
domain: comp
tags: [2d fx, tracers, muzzle flash, screen space, fx lights, post process, bloom, agora studio, deep-read]
applies_to: Unreal Engine 5.6
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=hc6xf-3uDX8, src:yt-transcripts]
feeds: []
conflicts: none
---
The director's rough drawings fixed timing and placement of tracers, impacts and flashes [35:06]. A 2D artist drew them frame by frame in screen space on layers, then the CG supervisor added motion blur and chromatic aberration in Nuke [35:38]. The sequence is projected onto an image plane attached to the character [36:10]. To keep it from looking pasted on, lights are placed in 3D matching tempo, colour and intensity, giving reflections, area illumination and shadows [36:10-36:42], then post-process tweaks (motion blur, lens flares, glow) bleed it into the image [36:42-37:14].

**Use it:** A recipe for 2D flash/energy effects over 3D in C4D+AE: match with a real light that blinks the same way.
