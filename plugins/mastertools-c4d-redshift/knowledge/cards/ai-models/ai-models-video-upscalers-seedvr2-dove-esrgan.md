---
id: ai-models-video-upscalers-seedvr2-dove-esrgan
title: Video upscalers: SeedVR2 (Apache, heavy), DOVE (about 15 s for 33 frames at 720p on an A100), Real-ESRGAN (BSD, fast CNN that can flicker)
domain: ai-models
tags: [upscaler, seedvr2, dove, real-esrgan, video super resolution, flicker, topaz]
applies_to: 2025-2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/html/2506.05301v2, https://en.papernotes.org/NeurIPS2025/image_generation/dove_efficient_one-step_diffusion_model_for_real-world_video_super-resolution/, https://arxiv.org/pdf/2605.25940.pdf, src:research-verticals, src:research-youtube]
feeds: [upscale rung]
conflicts: none
---
SeedVR2 is ICLR 2026. DOVE's comparison (about 173 s for STAR) is a secondary summary. A 2026 study (arXiv 2605.25940) releases human scores for SCST, DOVE, SeedVR2, Lanczos and two paid tools. Diffusion upscalers invent detail.
No Topaz test on CG renders with numbers was found.

**Use it:** score every upscale with FLIP against a full render of the hero frame.
