---
id: lighting-hide-lights-from-camera-and-use-a-falloff-gradient-for-reflections
title: Use gradient-falloff area lights so reflections are not flat white rectangles, and hide lights from the camera
domain: lighting
tags: [reflections, falloff, gradient, area light, camera visibility, softbox, three-point, car lighting, deep-read]
applies_to: Octane; principle for any renderer
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=TuKDhZU7ySE, src:yt-transcripts, https://www.youtube.com/watch?v=HtDz9bOJT_E, https://www.youtube.com/watch?v=dT4Vl3PGe08]
feeds: [elevate]
conflicts: none
---
A plain area light reflects as a hard white rectangle, 'evenly lit surfaces do not exist'; give each light a gradient/falloff or texture for soft gradations in reflections [03:06-04:40]. Because lights can sit anywhere CG allows, disable camera visibility on them (his 'best cheat in humankind history') [09:19]. Car example: big key softbox at the wheel (falloff on), weaker fill, an overhead strip for the roof line, a wall light for the background, a back/hair light that also leaves a stripe on the floor [13:33-16:46]. Base light came from a night-scene HDRI [02:04].

**Use it:** hero reflective products: shape reflections with large gradient lights rather than a single flat panel; our inference for Redshift is a rect light with a ramp texture.
Transcript support: film night trick: hidden large light at the top of frame reflecting in a ground with roughness below 0.2 (https://www.youtube.com/watch?v=dT4Vl3PGe08 [09:53])
