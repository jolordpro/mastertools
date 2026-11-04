---
id: ai-models-qwen-image-edit-hosted-price-nunchaku
title: Qwen-Image-Edit costs about $0.021 per image on fal; Nunchaku 4-bit FP4 is about 3x faster than BF16 on a 5090
domain: ai-models
tags: [qwen-image-edit, nunchaku, fp4, fal, price, flux kontext, 5090, image edit]
applies_to: 2026
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://fal.ai/learn/tools/flux-vs-qwen-image, https://github.com/nunchaku-ai/nunchaku, https://docs.bfl.ai/quick_start/pricing.md, src:research-gaps-deep]
feeds: [PLAN 1.6 mockups]
conflicts: none
---
Edit 2511 about $0.03 per megapixel. FLUX.2 Klein hosted costs about $0.014-0.016 per image. No seconds-per-image on a 5090 was found for Qwen or Kontext. FluxRT reports about 0.2 s end to end at 512x512 on a 5090 (github thinhlpg/fluxrt). A 5090 warm all month at $0.69 is about $500.

**Use it:** self-hosting only wins if the GPU stays busy.
