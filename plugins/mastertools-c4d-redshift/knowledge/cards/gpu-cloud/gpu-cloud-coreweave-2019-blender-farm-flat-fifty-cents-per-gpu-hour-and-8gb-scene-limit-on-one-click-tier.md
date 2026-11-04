---
id: gpu-cloud-coreweave-2019-blender-farm-flat-fifty-cents-per-gpu-hour-and-8gb-scene-limit-on-one-click-tier
title: CoreWeave's 2019 Blender farm (BCON): 0.50 dollars per GPU-hour, one-click tier capped at 8 GB scenes, concierge tier 16 GB
domain: gpu-cloud
tags: [coreweave, blender, cloud-render, pricing, vram-limit, p104, marco, deep-read]
applies_to: CoreWeave Kubic and Concierge, Blender Conference talk uploaded 2019-10
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=sh8UhQ1zofg, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Marco (founder, Blender-focused cloud platform) gives the 2019 terms: one-click add-on tier with up to 80 GPUs per project, scene limit 8 GB of memory in use; Concierge web tier up to 16 GB and up to 500 GPUs at once, with larger-memory cards being added [02:43-03:14, 27:18-29:23].
Both cost 0.50 dollars per GPU-hour (Concierge had been 0.60); the GPU is a P104, a mining-origin card close to a GTX 1080, with a Titan V option [19:36-20:39, 29:59].
Billing only while rendering. Example: 250 frames of a light scene about 8 dollars [20:07-20:39]. Free credits at sign-up: 5 dollars, about 10 GPU-hours [37:51].
He says the limit is memory in use when the file is open, not file size on disk [27:18-27:49].

**Use it:** a VRAM ceiling per farm tier is the first thing to check before sending a heavy Redshift scene; ask for the farm's VRAM per card.
