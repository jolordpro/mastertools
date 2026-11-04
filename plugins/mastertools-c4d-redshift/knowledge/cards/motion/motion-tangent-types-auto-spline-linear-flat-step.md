---
id: motion-tangent-types-auto-spline-linear-flat-step
title: What each tangent type does to a move, and when stepped blocking is used
domain: motion
tags: [tangent, interpolation, auto, spline, linear, flat, stepped, blocking, overshoot, break tangents, deep-read]
applies_to: Maya, applies to C4D/AE/Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RQ31vjgJM2c, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Key positions stay the same; the tangent decides timing and spacing between them [05:08]. Auto stays smooth and never goes above or below the keys; spline continues the incoming curve and can overshoot beyond a key [07:12-07:42]; linear gives straight mechanical point-to-point moves [06:10]; flat handles on every key give jittery insect-like motion for organic moves [08:14]; step holds a pose then jumps, used while blocking before tuning timing [06:42-07:12].
Break tangents splits left and right handles so an in-slope and an out-slope can differ (needed at a bounce contact) [17:32-18:03].
Workflow tips: copy a working key and paste it elsewhere [18:34]; to move many objects' curves together, filter and select all same-channel curves [04:07].

**Use it:** when a camera or logo move looks robotic, check for linear or flat tangents; check mid-blocking files stay in stepped.
