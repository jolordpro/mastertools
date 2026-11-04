---
id: lighting-ue5-tone-mapper-toe-and-local-exposure-before-grading
title: Treat the tone mapper like developing a negative - adjust toe and local shadow exposure first, then colour grade
domain: lighting
tags: [sean gobi, gameloft, unreal fest, tone mapper, toe, shoulder, local exposure, color grading, deep-read]
applies_to: Unreal Engine 5
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nlbJwMoj1Dg, src:yt-transcripts]
feeds: [lighting, elevate]
conflicts: none
---
Order: physical light, camera exposure, tone mapper, then grading, so you grade a good negative rather than grading an already graded image [14:06-17:47].
Moves in the demo: film toe from about 0.55 to 0.3 to flatten the curve and lift shadow contrast; raise local-exposure shadows rather than adding lights [14:37-16:12]; exposure range tuned to about 9 to 12 EV for an artistic look [15:08].
Takeaway list: physical lights, physical albedo, physical exposure, toe and shoulder for shadow and highlight detail, local exposure if needed [19:24-19:54].
Fog set earlier: exponential height fog with light-shaft occlusion and bloom on the sun, volumetric fog on, density low at noon with a far start distance [16:43-17:15].

**Use it:** same idea as grading before the view transform, since the order of operations keeps highlight roll-off.
