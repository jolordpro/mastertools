---
id: redshift-gpu-only-devices-no-hybrid
title: Render on GPUs only: untick the CPU, keep hybrid off, and check every card is enabled
domain: redshift
tags: [devices, gpu, hybrid, cpu, preferences]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uKRqHwVr0F4, https://www.youtube.com/watch?v=u5eoWCQvegI, src:yt-transcripts]
feeds: [CHECKS, coach, redshift]
conflicts: none
---
Preferences: select the GPUs, not the CPU, and avoid hybrid since sharing with CPU slows things [12:34, RF]. iRender: confirm Redshift sees all four 5090s; a card left disabled is paid for and unused; watch GPU load before walking away [01:11-01:38, OR].

**Use it:** preflight: read device list and flag unused GPUs or CPU/hybrid.
