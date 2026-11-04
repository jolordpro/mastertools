---
id: motion-unreal-cloners-effectors-realtime-54-55
title: Unreal 5.4/5.5 Motion Design: cloners and effectors replace multi-minute frame waits with a live viewport
domain: motion
tags: [unreal engine, motion design, cloners, effectors, real-time, 5.5, mograph, epic, deep-read]
applies_to: Unreal Engine 5.4, 5.5
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5P-sO_2aiwU, src:yt-transcripts]
feeds: [estimator, pipeline]
conflicts: none
---
Epic technical product manager Andy Blondin (name as captioned) presents Unreal's MoGraph-style set: cloner patterns include grid, honeycomb, cylinder and sphere; effectors add noise and procedural movement [06:43]. A demo cloned 10,000-triangle meshes with good viewport performance [07:13]. His claim: as an art director he used to wait 2 to 3 minutes per frame for such results [06:12].
New in 5.5 [08:15]: proximity effects that can feed colour to emissive, torus and disc effector shapes with inner and outer falloff, scale and squash on effector shapes, a push-apart effector for force-field looks [09:46], physics on cloned particles with particle-to-particle and mesh collisions [10:17], and a Twist property on grids and honeycomb for spirals [12:21].
Cloner features can feed materials: effector count, randomness, particle age and a particle colour function [28:58].

**Use it:** Reference for any real-time versus offline C4D MoGraph discussion: cloner/effector parity exists, so an Unreal option is feasible for stylised broadcast loops. Version-specific, recheck on new Unreal releases.
