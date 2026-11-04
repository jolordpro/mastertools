---
id: lighting-light-size-sets-shadow-softness-and-eye-light-shape
title: The bigger the light, the softer the shadow; light size also sets the catchlight shape in the eyes and the amount of free fill
domain: lighting
tags: [light size, soft shadow, rectangle light, source radius, source length, catchlight, josh toonen, unreal, deep-read]
applies_to: Unreal Engine 5 (2023), principle applies anywhere
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=jAz4Lb93gwY, src:yt-transcripts, https://www.youtube.com/watch?v=RCCaQmwxNB4, https://www.youtube.com/watch?v=dT4Vl3PGe08]
feeds: []
conflicts: none
---
Josh Toonen [06:29-11:17]. Two portrait fundamentals: direction and size. A point light and a spotlight of the same position, intensity (6) and temperature (3500 K) look nearly the same; the spot just spills less. A rectangle light at the same place gives a softer shadow, smoother falloff and extra fill, due only to its size. Source width/height of 1 matches a point light; larger gives soft shadows around the nose. Source radius of 50 to 100 on a point or spot light gives a similar soft look. Source length turns a point into a tube: it changes reflections and diffuse spread but not the shadow shape (check with a chrome ball). The rectangle's square shows up in the eye reflection and scales with the light [12:20-12:52]. On set this is done with diffusion, grids of 8x8 diffusion for sun, and bounce off cloth, mimicked by dim, very large rectangle lights rather than relying on GI bounce [08:13-09:14]. Barn door angle 0 narrows the beam to cut spill in dark interiors [09:45].

**Use it:** Coach rule: to soften a shadow, enlarge or move back the source before adding fill. The catchlight shape is a free check of source shape.
Transcript support: Volkov uses a bigger, dimmer eye-light so the catchlight is always there when the eyes move (https://www.youtube.com/watch?v=RCCaQmwxNB4 [07:15])
Transcript support: Toonen again: sun small is crisp, overcast is a giant softbox; widen source angle (his example 100) to match overcast (https://www.youtube.com/watch?v=dT4Vl3PGe08 [07:19])
