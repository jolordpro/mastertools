---
id: ai-models-flux2-klein-speed
title: FLUX.2 Klein 4B edits an image in about 1.2 s on an RTX 5090, 30-85 s on a Mac
domain: ai-models
tags: [flux, klein, image edit, mockup, speed, apple silicon, comfyui]
applies_to: FLUX.2 Klein 4B, 2026
status: V2
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://blog.comfy.org/p/flux2-klein-4b-fast-local-image-editing, https://lilting.ch/en/articles/flux2-klein-apple-silicon]
feeds: [PLAN 1.6 mockups]
conflicts: none
---
About 1.2 s per edit on an RTX 5090; 30-85 s on Apple Silicon. Self-hosted cost about $0.0002-0.0006 per image vs about $0.015 on APIs (researcher's maths).

**Use it:** 1-5 s mockups need one warm cloud GPU per session, not the Mac.
