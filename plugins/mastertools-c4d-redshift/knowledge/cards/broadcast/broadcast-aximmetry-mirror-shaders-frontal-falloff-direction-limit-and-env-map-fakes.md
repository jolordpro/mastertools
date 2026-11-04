---
id: broadcast-aximmetry-mirror-shaders-frontal-falloff-direction-limit-and-env-map-fakes
title: Aximmetry reflections: use the mirror shader on flat floors with a frontal falloff, limit it by direction, and fake curved surfaces with cube maps
domain: broadcast
tags: [aximmetry, mirror shader, environment map, frontal min, mirror direction, gpu budget, fake reflection, 2018, deep-read]
applies_to: Aximmetry shaders (mirror vs 'rough' environment-map types), 2018 tutorial
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=leqVJhmy_zQ, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Narrator unnamed:
- Terminology trap: in shader names, 'mirror' means planar reflection from a real-time render; 'rough' means environment-map reflection [03:40].
- Setting a frontal minimum value to zero makes reflection strength depend on view angle, closer to real; trim the reflection colour for intensity, one case ended at 0.82 [05:44-06:47].
- A higher floor needs its own mirror plane and render, else misalignment shows; a shared plane is a cheat for small areas only [06:47-07:19]. Side faces show wrong reflections; split the object or set Mirror Direction (0,1,0 is up, fourth value is strictness, default 0, he used 1.5) [07:50-08:53].
- Each extra mirror costs GPU; with a third floor he checks spare GPU first and otherwise reuses an image or skips it [09:42-09:57].
- Curved or odd surfaces: no real-time ray tracing, so use a cube-map shader with a faint stock environment map, reduce reflection and specular colours, and rotate the map if it looks harsh [10:28-12:33].

**Use it:** Budget mirror renders per floor plane and keep fakes faint; cheaper than adding more real reflection renders.
