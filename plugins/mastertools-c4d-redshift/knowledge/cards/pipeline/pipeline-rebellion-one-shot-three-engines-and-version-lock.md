---
id: pipeline-rebellion-one-shot-three-engines-and-version-lock
title: One trailer shot went from offline Houdini renders to Unreal to game-engine footage; the team stayed on Houdini 18.0 all project
domain: pipeline
tags: [rebellion vfx, evil genius 2, redshift, unreal, houdini, version lock, hybrid, deep-read]
applies_to: Houdini 18.0, Redshift alpha, Unreal
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
The island opening was half offline (Houdini/Redshift Hydra plugin, which was still alpha-to-beta), half real-time Unreal, then footage from the studio's own game engine [20:49-21:50]. GPU rendering suited the show because assets had few textures, so memory risk was low [20:49].
Unreal as an offline renderer with layers and AOVs was still clunky [21:50].
They locked on Houdini 18.0 for the whole project and missed 18.5 features; support answers kept being 'try 18.5' [22:22-22:52].

**Use it:** version-lock policy for a job; budget a deliberate upgrade point between projects.
