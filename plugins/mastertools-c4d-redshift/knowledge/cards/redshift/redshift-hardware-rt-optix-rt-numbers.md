---
id: redshift-hardware-rt-optix-rt-numbers
title: Hardware ray tracing helps RTX cards a lot and does nothing on others; one test saved about 10 s of 45 s
domain: redshift
tags: [hardware ray tracing, optix rt, rtx, speed]
applies_to: Redshift 3.x, RTX cards
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=G43QVR1TqXg, https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
CG Shortcuts: tick hardware ray tracing if you have an RTX card, big speed boost, no effect without one [03:10, RT; 09:23, RF]. Daily Course: Optix RT for spotted GPUs under System > experimental, 2000-series and up; about 10 s less on a 45 s frame [08:58-09:45, DC]. Brute force also gains from it [09:54, RF].

Ledger agrees: §9 "Irradiance Cache and Irradiance Point Cloud do not benefit from hardware ray tracing the way brute-force tracing does".

**Use it:** scene check: report whether hardware ray tracing is on for the render device.
