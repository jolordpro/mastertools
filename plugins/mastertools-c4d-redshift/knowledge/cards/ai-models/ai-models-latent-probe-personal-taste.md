---
id: ai-models-latent-probe-personal-taste
title: A per-user linear probe on frozen VLM features (0.611) beat LoRA with 100 shots (0.578) for personal aesthetic taste
domain: ai-models
tags: [personalization, taste, linear probe, vlm, qwen3-vl, piaa, latent]
applies_to: ACL 2026 Findings, arXiv 2604.11374
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/pdf/2604.11374, https://github.com/ynklab/vlm-latent-piaa, src:research-verticals]
feeds: [taste critic]
conflicts: none
---
Qwen3-VL 4B on the PARA set, as summarised by a secondary source. Ten-shot prompting did much worse. No fine-tuning needed and retraining takes seconds after each pick. Task Vector Customization (arXiv 2407.07176) has code "coming soon".

