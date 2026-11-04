---
id: c4d-dynamics-follow-position-and-rotation-blend-keyframes-with-simulation
title: Rigid Body tag Follow Position and Follow Rotation above zero let a moving cloner steer a simulation, giving controllable avalanches and clumping
domain: c4d
tags: [rigid body, follow position, follow rotation, force object, cloner, avalanche, volume builder, cache, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Trainer (Nosman) [1:09:49-1:15:00]. In the Rigid Body tag's Force tab, Follow Position and Follow Rotation default to 0, so moving the cloner changes nothing once dynamics run. With values like 5/5, or even 1/1, the sim respects the cloner's animation (keyframes, inheritance, noise) while still colliding. Rocks and sticks on a cloner moving across a floor give a controllable avalanche [1:12:31-1:13:34].
A Force object set to attract with a radius clumps clones, good for organic cell or surface-tension looks [1:13:34].
Before Volume Builder: set instances on, then bake with a Cache object; live dynamics do not work under it [1:14:05].
Companion fix [42:13-43:15]: objects tunnelling through the floor? In Project Settings, Dynamics, Expert tab raise Steps per Frame and Maximum Solver Iterations per Step to 10-15 or higher depending on speed, but send a simplified scene if that fails.

**Use it:** Choreographed physical reveals in broadcast graphics; keep the sim controllable, then cache before meshing or farm.
