---
id: lookdev-unreal-path-tracer-glass-needs-enough-bounces
title: Glass breaks down at low bounce counts: 1 bounce looks wrong, 2-3 improve, 10 looks as it should; use only as many bounces as the scene needs
domain: lookdev
tags: [william faucher, unreal, path tracer, glass, max bounces, caustics, thin translucent, frosted, deep-read]
applies_to: Unreal 4.27 path tracer
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=X5zVhc5ahl0, src:yt-transcripts]
feeds: [[redshift, lookdev]]
conflicts: none
---
Faucher [10:34-11:05, 16:26-16:56]: indirect light climbs from 1 to 3 to 10 bounces with diminishing returns after that, so use only what is needed; but glass and other translucent materials look wrong at 1, better at 2 and 3, and correct at 10. Glass setup: flat base colour, roughness, opacity, IOR 1.5, translucent blend; frosted glass is just higher roughness [14:23-14:53]. Thin translucent is for plastic wrap or bubbles and gives coloured shadows; he says not to use it for coloured glass because it reads as plastic [15:24-15:56]. Also: path tracer needs an emissive-light setting to let emissive materials cast light, and unsupported features then include hair, decals, volumetric fog and multi-GPU [20:52-21:51].

**Use it:** Advisor: if glass reads dark or flat, raise ray depth for refraction before touching materials. Reminder that Redshift trace depth values must come from the redshift ledger.
