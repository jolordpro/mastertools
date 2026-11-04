---
id: lighting-light-size-and-scale-set-softness-and-caustics-in-unbiased-render
title: In a physically based renderer a light's real size, distance and the scene scale decide softness and caustics
domain: lighting
tags: [light size, scale, caustics, soft shadow, glass volume, real world production lights, deep-read]
applies_to: Octane (path tracer); principle applies to Redshift
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=TuKDhZU7ySE, src:yt-transcripts, https://www.youtube.com/watch?v=0Zg4lpwZGe0]
feeds: [redshift, elevate]
conflicts: none
---
Octane demo (Andrei, a cinematographer-minded CG artist): a light almost the size of the car gave very soft shadows at any distance; shrinking it to about 20 cm, then a 15 by 10 cm panel, gave harder shadows [04:40-06:11]. His advice: look up real production lights and use their real dimensions [06:11]. Small sources or the sun produce strong caustics; a big source gives almost none; combine a small light for caustics with a big far one for soft shadows [06:43-09:19]. Glass must be modelled as a solid with volume (he nested a slightly smaller duplicate), not a single plane/shell, for correct results [07:13].

**Use it:** the scene check could flag wildly large or tiny area lights against the object's scale; in Redshift, check light size, scale and glass thickness the same way (our inference; the Redshift ledger governs values).
Transcript support: sharper shadows read as larger objects; soft shadow light made the same logo look smaller (https://www.youtube.com/watch?v=0Zg4lpwZGe0 [26:39])
