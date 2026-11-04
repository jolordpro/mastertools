---
id: lighting-ue5-night-exterior-hide-one-huge-light-above-frame-and-let-a-low-roughness-ground-reflect-it
title: Night exterior trick: hide one very large, very bright light above the frame, keep the ground roughness below 0.2, and design a few big shapes
domain: lighting
tags: [night lighting, wet ground, reflection, roughness, girl with the dragon tattoo, unreal engine, big shapes, levels, josh toonen, deep-read]
applies_to: Unreal Engine 5 (2023)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=dT4Vl3PGe08, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
Seen repeatedly in film night exteriors: no visible lamp in shot, but a large light at the top of frame reflects on the concrete [09:38-10:23]. Make sure the ground material roughness is below 0.2, or use wetness decals [10:23].
In his study of a Dragon Tattoo still, the off-screen light is the key, silhouettes the car and character, and adds volumetrics from the top; he blasted a spotlight to about 1000 intensity then walked it back, and raised its distance to even the falloff [10:54-11:57].
Prefer a few lights that make big, clear shapes over micro-detail; hard shadows mean the source is small, so keep the shadows crisp here [12:27-12:58].
Put lighting and effects on separate levels to toggle against unchanged geometry [10:23-10:54]. Volumetric light needs exponential height fog with volumetric fog on [12:27].

**Use it:** for a Redshift night frame, put one large rectangle light above camera and check a wet-floor reflection before adding fills.
