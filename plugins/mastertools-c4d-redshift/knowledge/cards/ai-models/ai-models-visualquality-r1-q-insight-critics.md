---
id: ai-models-visualquality-r1-q-insight-critics
title: VisualQuality-R1 and Q-Insight are VLM quality critics that explain their score, but they are trained on camera photos
domain: ai-models
tags: [visualquality-r1, q-insight, vlm critic, image quality, qwen2.5-vl, grpo]
applies_to: 2025
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/pdf/2505.14460, https://neurips.cc/virtual/2025/poster/119363, src:research-verticals]
feeds: [critic QC voice]
conflicts: none
---
VisualQuality-R1 is Qwen2.5-VL-7B tuned with reinforcement learning to rank, writing reasoning then a 1-5 score. Q-Insight (NeurIPS 2025) uses GRPO on score regression plus degradation perception; repo location unconfirmed. Neither is tuned for CG lighting.

**Use it:** usable as a QC voice for artefacts, not for lighting taste.
