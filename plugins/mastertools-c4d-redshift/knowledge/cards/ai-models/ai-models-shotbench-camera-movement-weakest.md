---
id: ai-models-shotbench-camera-movement-weakest
title: ShotBench: 3,572 expert questions from 200+ films; camera movement was the weakest dimension for most VLMs
domain: ai-models
tags: [shotbench, shotqa, shotvl, camera movement, vlm, cinematography, dataset]
applies_to: arXiv 2506.21356
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://arxiv.org/html/2506.21356v2, src:research-production-pipelines]
feeds: [computed shot labels]
conflicts: none
---
Eight dimensions (shot size, framing, camera angle, lens, composition, lighting and movement among them); 16 movement types such as push in, pull out, arc, dolly zoom. ShotQA is about 70k pairs from 243 films. Best model, ShotVL 3B, 65.1%. Code and data were promised, repo not named.

**Use it:** read camera moves exactly from keyframes and use these label words.
