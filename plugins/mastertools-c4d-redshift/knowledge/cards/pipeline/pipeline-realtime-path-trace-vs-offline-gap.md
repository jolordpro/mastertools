---
id: pipeline-realtime-path-trace-vs-offline-gap
title: A real-time path-traced still at 6 FPS on a 4090 with 50% DLSS came close to offline, but specular detail and shadow sharpness lagged
domain: pipeline
tags: [richard cowgill, nvidia, unreal fest, path tracing, offline, denoiser, dlss, ray reconstruction, deep-read]
applies_to: Unreal Engine 5, NvRTX branch
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=zD9kS1nOuyU, src:yt-transcripts]
feeds: []
conflicts: none
---
Comparison [24:44-26:31]: offline path-traced frame at full resolution versus real-time at 6 FPS, 6 samples per pixel on an RTX 4090 and 50% DLSS upscaling; very close overall.
He names two weaknesses himself: less detail in a specular highlight and slightly soft direct shadows, which he blames on the denoiser (fixable by better training) rather than on ReSTIR [26:00-26:31].
Ray reconstruction (part of DLSS 3.7) is called the best denoiser for path tracing: sharper detail and reflections [32:17-32:50].

**Use it:** when comparing engine stills to Redshift, check specular highlights and shadow edges first.
