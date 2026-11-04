---
id: ai-models-motion-vector-frame-extrapolation
title: G-buffer and motion-vector frame extrapolation (ExtraSS, GFFE, PatchEX) targets real-time games; no code seen
domain: ai-models
tags: [extrass, gffe, patchex, frame extrapolation, motion vectors, g-buffer]
applies_to: 2024-2025
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://poiw.github.io/ExtraSS, https://ar5iv.labs.arxiv.org/html/2407.17501, src:research-verticals]
feeds: [interpolation rung]
conflicts: none
---
PatchEX claims gains over ExtraNet and ExtraSS in PSNR and speed (own claim). FSR 3.1.5 and older are open on GitHub; FSR 4 source was posted by accident under MIT and pulled. These need game-engine inputs.

**Use it:** low fit for offline frames; OIDN plus an upscaler is closer.
