---
id: ai-models-video-critic-judges-prefer-low-motion
title: VLM video judges can be reward-hacked: they prefer low-motion clips
domain: ai-models
tags: [vlm judge, video critique, reward hacking, worldjen, gt-svj, low motion]
applies_to: 2025-2026 papers
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/pdf/2511.22974v1, https://arxiv.org/pdf/2605.03475, https://arxiv.org/abs/2602.05202, src:research-frontier-ai]
feeds: [motion critique]
conflicts: none
---
WorldJen scores generated video on lighting, scene consistency, object permanence and smoothness with a VLM judge (1-5 plus reason), closest to a critique format. GT-SVJ (CVPR 2026) turns a video generator into a judge. No benchmark was found that tests critique of motion, lighting and continuity together.

**Use it:** never accept a critic's motion verdict without measured numbers.
