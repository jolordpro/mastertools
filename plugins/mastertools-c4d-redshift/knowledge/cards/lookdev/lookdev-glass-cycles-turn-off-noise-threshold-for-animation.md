---
id: lookdev-glass-cycles-turn-off-noise-threshold-for-animation
title: For glass animations in Cycles, turn the noise threshold off: it stops light bouncing inside the glass, invisible in stills but noisy in video
domain: lookdev
tags: [glass, cycles, noise threshold, adaptive sampling, animation, refraction, polyfjord, deep-read]
applies_to: Blender 3.3 Cycles (not Redshift)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Jwl48psPrxU, src:yt-transcripts]
feeds: []
conflicts: none
---
Polyfjord shows that with exposure raised to 4, the noise threshold version loses the internal bounces and shows noise [04:08]. It is hard to see in a still but visible in an animation, so he disables it for glass sequences [04:08-04:39]. Test render used 256 max samples, 5 s per frame [02:37]. This is a Cycles setting; Redshift values must be checked against the redshift ledger.

**Use it:** Treat as a hint to test adaptive-sampling thresholds on glass animations, not as a Redshift rule.
