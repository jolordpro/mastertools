---
id: lighting-ue5-turn-off-auto-exposure-to-see-real-light-values
title: Unreal's auto-exposure hides wrong light values, so lock exposure with fixed EV before judging light
domain: lighting
tags: [sean gobi, gameloft, unreal fest, ue5, exposure, eye adaptation, ev, post process, deep-read]
applies_to: Unreal Engine 5
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nlbJwMoj1Dg, src:yt-transcripts, https://www.youtube.com/watch?v=dT4Vl3PGe08]
feeds: [lighting]
conflicts: none
---
Failure he opens with: a scene lit by a sun at 10 lux or at 100,000 lux looks the same because the engine adapts exposure to always look fine, so the numbers are never tested [02:38-03:41].
Fix: show the eye-adaptation visualiser; in a post-process volume turn exposure compensation off and set min and max EV (14 for a noon sun) so lights and camera behave like a real camera [10:55-12:29].
He stresses a camera, not an eye, is being simulated, since eyes have more dynamic range, and monitors have less [03:41-04:14].

**Use it:** the same discipline applies in Redshift: set camera exposure and light units deliberately instead of fixing by eye.
Transcript support: night-exterior study keeps lights crisp and expects blown highlights; exposure is a separate decision (https://www.youtube.com/watch?v=dT4Vl3PGe08 [10:23])
