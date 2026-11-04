---
id: c4d-geometry-solver-relax-a-spline-with-matrix-tracer-and-push-apart-effector
title: Relax a C4D spline in a geometry solver - resample every 6 cm, Matrix on vertices, Push Apart (radius 3.5 cm), Tracer, resample again
domain: c4d
tags: [scene-nodes, geometry-solver, spline, push-apart, matrix, tracer, cinema-4d-2025, deep-read]
applies_to: Cinema 4D 2025
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Iy2FAJbbyrY, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Dominik Ruckli, 2025 [13:33-20:35]. There is no direct spline relax, so MoGraph does it.
- Helix (height 0) displaced slightly, resampled with step length 6 cm; stored via the solver [13:48-14:56].
- Instance of the stored spline goes into a Connect object (feeding the instance straight to the Matrix gave trouble), then Matrix with distribution Vertex, and a Tracer on the Matrix with Connect objects [15:27-16:28].
- Push Apart effector: radius 3.5 cm (3 cm does nothing at 6 cm spacing), 2 iterations; Tracer output is the new solved spline, resampled again at 6 cm [17:00-18:05].
- A random field on the Push Apart strength controls where relaxation happens; animate the field's speed [19:05-20:10]. More initial displacement was needed before it showed [18:35].

**Use it:** Same trick works for relaxing any generated line work.
