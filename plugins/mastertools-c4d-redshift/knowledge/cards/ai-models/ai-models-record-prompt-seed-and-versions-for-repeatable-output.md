---
id: ai-models-record-prompt-seed-and-versions-for-repeatable-output
title: To repeat a generated image, log the prompt, seed, model, sampler, steps and library versions together
domain: ai-models
tags: [[seed, prompt, reproducibility, comfyui, diffusion], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Hanno Basse (ex-CTO Stability, Digital Domain) says always save the prompt and the seed with every generated image [39:26]. The seed fixes the first noise tensor; after that the run is deterministic. Same output only if the model version, sampler settings, step count and even PyTorch and CUDA versions match [39:58].
He calls it fragile in practice: GPU precision and non-deterministic GPU ops can still change results [41:31]. Test it by generating twice in ComfyUI with one seed.

**Use it:** Any AI-generated plate or boards handed into a job get a sidecar note with prompt, seed, model version, sampler and steps; a mismatch of any one means the look cannot be re-made.
