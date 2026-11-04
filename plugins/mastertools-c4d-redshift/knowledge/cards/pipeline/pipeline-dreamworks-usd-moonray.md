---
id: pipeline-dreamworks-usd-moonray
title: DreamWorks runs OpenUSD as its pipeline backbone; MoonRay has a Hydra delegate and distributed layer (Arras); ACES was used on The Wild Robot
domain: pipeline
tags: [dreamworks, moonray, arras, openusd, hydra, aces, wild robot]
applies_to: 2025-2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.aswf.io/news/moonray-dreamworks-animations-open-source-production-renderer-joins-the-academy-software-foundation/, https://theasc.com/news/academy-software-foundation-aces-siggraph-2025, https://www.youtube.com/watch?v=fQUnq6drevw, src:research-production-pipelines, src:research-youtube, https://www.youtube.com/watch?v=GcPlNw9kFVk, https://www.youtube.com/watch?v=XfMp13jOSxE]
feeds: []
conflicts: none
---
The 2026 keynote splits the renderer into three parts: renderer, shader library and distribution. ACES 2.0 shipped in spring 2025 and ACES became an ASWF project. The Wild Robot's painterly look came from stylisation in the renderer.

**Use it:** studio pattern is open standards (USD, OCIO, EXR) as the shared base.
