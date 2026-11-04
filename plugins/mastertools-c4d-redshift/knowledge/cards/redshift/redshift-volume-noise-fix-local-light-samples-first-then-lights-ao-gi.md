---
id: redshift-volume-noise-fix-local-light-samples-first-then-lights-ao-gi
title: Volume noise: raise the volume samples on the light itself first (cheapest), then lights, AO and GI; brute force GI is the usual extra noise source
domain: redshift
tags: [volume noise, volume samples, light samples, sampling overrides, gi, brute force, volumetric, bold and break, deep-read]
applies_to: C4D + Redshift 2018 (Maxon) and 2021 (Bold&Break)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vnHKQmvKYH8, https://www.youtube.com/watch?v=A-stHqCya4s, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Maxon (2018): volume noise can be cut by raising unified samples, by sampling overrides per scene, or by the local volume samples on each light; the local route is the fastest and most efficient [02:10, 12:21-12:51]. Lights in the demo went from 16 to 64 volume samples [13:56].
Bold&Break (2021) gives the order of attack: volumes first, then lights (the two are tightly linked), ambient occlusion about 512, then GI [10:18-11:10]. With GI on he saw much of the remaining grain come from GI; brute force cleaned it [11:41]. Some grain stays in volumes, and he saw banding he blamed on the host effect [12:43].

**Use it:** for a grainy shaft, raise the light's own volume samples before the global Max; mark GI as the next suspect. Supports `redshift-sampling-claim-automatic-sampling-in-system-experimental-slower-and-bad-with-volumes`.
