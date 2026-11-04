---
id: lighting-restir-light-count-barely-affects-realtime-cost
title: With ReSTIR-based real-time path tracing, light count barely changes frame time up to about 1000 lights
domain: lighting
tags: [richard cowgill, nvidia, unreal fest, restir, path tracing, light count, nvrtx, deep-read]
applies_to: Unreal Engine 5, NvRTX branch
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=zD9kS1nOuyU, src:yt-transcripts, https://www.youtube.com/watch?v=u6xhzA40Af0]
feeds: []
conflicts: none
---
Richard Cowgill (Nvidia RTX Unreal evangelist) explains that ReSTIR stores light samples in a screen-space reservoir built from neighbouring pixels and previous frames (often 2 to 8), so every light counts about equally and lights are not denoised one by one [04:15-06:50].
Charts: frame rate stays almost flat from 0 to 100 lights, and he says stays high out to 1,000 lights with some falloff, whereas traditional ray-traced area lights collapse past about 250 lights and stop working at 400-500 [12:10-13:43].
Target is 60 FPS with very sparse sampling, about one sample per pixel, millions rather than billions of rays [03:11, 24:56].
Practical effect: light a scene by placing as many lights as wanted instead of baking or budgeting [09:59].

**Use it:** context that real-time and offline have opposite light-count behaviour: in Redshift each light still adds cost.
