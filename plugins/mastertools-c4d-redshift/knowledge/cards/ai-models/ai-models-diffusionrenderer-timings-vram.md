---
id: ai-models-diffusionrenderer-timings-vram
title: NVIDIA DiffusionRenderer: 512x512, 24 frames takes 9.7 s inverse and 20.3 s forward on an A100 80 GB; a 4090 needs over 22 GB
domain: ai-models
tags: [diffusionrenderer, nvidia, relighting, inverse rendering, g-buffer, a100, 4090]
applies_to: released June 2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/nv-tlabs/diffusion-renderer, src:research-verticals]
feeds: [research track phase 3]
conflicts: none
---
Inverse renderer (frames to G-buffers) plus forward renderer (G-buffers plus light to frames). NVIDIA only in practice; the target light format is not described on the repo page. Licence is NVIDIA-source plus Stability community on the base model.

**Use it:** test its relight against our light-group re-mix, scored with FLIP.
