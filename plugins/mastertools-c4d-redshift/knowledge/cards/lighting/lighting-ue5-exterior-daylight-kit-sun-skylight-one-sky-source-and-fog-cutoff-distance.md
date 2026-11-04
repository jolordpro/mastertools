---
id: lighting-ue5-exterior-daylight-kit-sun-skylight-one-sky-source-and-fog-cutoff-distance
title: Unreal exterior daylight needs a sun, a skylight and a sky source; keep one skylight, recapture after changing the HDRI, and cap fog with its cutoff distance
domain: lighting
tags: [unreal engine 5, exterior lighting, directional light, skylight, sky atmosphere, hdri backdrop, exponential height fog, josh toonen, deep-read]
applies_to: Unreal Engine 5 (2023); Lumen/real-time
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=dT4Vl3PGe08, src:yt-transcripts]
feeds: []
conflicts: none
---
Josh Toonen [02:35-05:42]: a directional light with Atmosphere Sun Light enabled, a sky light as fill and bounce, and a sky: Sky Atmosphere (plus volumetric clouds), or an HDRI on an unlit emissive material applied to the engine's inverse-normals sphere, or the HDRI Backdrop actor.
Keep only one sky light: use the HDRI Backdrop's own, or add yours. With a custom HDRI sphere, toggle real-time capture on then off to recalculate the sky light and reflections [03:36-04:39].
Exponential height fog separates foreground from distant dark buildings; match its inscattering colour to the background (eyedropper from the sky), and raise fog cutoff distance (his test: 1000 cm cut it off) so fog affects buildings but not the sky dome [04:39-05:42, 08:50-09:21].

**Use it:** a first-check list for real-time lighting scenes. Engine-specific; the principle (fog tinted to the sky separates depth layers) transfers to C4D/Redshift atmosphere.
