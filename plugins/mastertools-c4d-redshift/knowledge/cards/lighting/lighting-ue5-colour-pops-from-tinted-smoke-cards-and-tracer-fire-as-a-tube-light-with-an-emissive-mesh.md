---
id: lighting-ue5-colour-pops-from-tinted-smoke-cards-and-tracer-fire-as-a-tube-light-with-an-emissive-mesh
title: Cheap colour and motion in a real-time night scene: tint smoke cards instead of lighting, and fake tracers with an extended-length light plus an emissive cylinder
domain: lighting
tags: [smoke cards, colour pops, tracer fire, source length, emissive, lumen, volumetric fog, unreal engine, josh toonen, deep-read]
applies_to: Unreal Engine 5 (2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=dT4Vl3PGe08, src:yt-transcripts]
feeds: []
conflicts: none
---
Rim light far away plus a wider, darker secondary light gave the tank some front shape [13:00-13:28]. Reds, blues, greens and yellows from storefronts stop the frame being monochrome; he got them by tinting planes with animated smoke instead of casting coloured light, and the same pops separate soldiers, tanks, ground and background layers; volumetric fog could do the same [13:28-14:30].
Tracer fire is a point light whose source length is extended into a tube, with a cylinder carrying an emissive texture attached; animate them together and they reflect off tanks and light the smoke [14:30-15:01]. He says Lumen alone does not give the same result as pairing light and mesh [15:01].

**Use it:** a pattern for Redshift too: a visible emissive object plus a matching light reads better than either alone.
