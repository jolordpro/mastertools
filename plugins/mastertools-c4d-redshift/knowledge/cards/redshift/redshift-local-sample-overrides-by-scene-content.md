---
id: redshift-local-sample-overrides-by-scene-content
title: Turn on local sample overrides only for ray types the scene contains, starting at 512
domain: redshift
tags: [local samples, reflection, refraction, brute force rays, overrides, light samples, ssS, ao]
applies_to: Redshift GPU (any DCC)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, https://www.youtube.com/watch?v=ZsqM8QHZ0pQ, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Overrides (reflection, refraction, AO, lights, volume, SSS) replace the global sample count or scale it [23:16-23:47]. Enable only what the scene has; an interior with a floor and a glass window needed reflection and refraction at 512 [24:18].
The GI brute-force rays are a separate local control; the interior needed 512 then 1024 [25:20, 53:45]. Noise in glass or on a floor means raise those, not trace depth [27:56, 41:41].
Per-light samples are only needed when real lights do the lighting; a scene lit by GI alone needs none [59:29-1:00:01]. Greyscalegorilla 2019 gives the same idea: raise light and GI samples first, last the global ones [H 06:13-09:23].

**Use it:** the advisor maps visible noise location to the matching override (floor/mirror to reflection, window to refraction, dark corners to GI rays).
