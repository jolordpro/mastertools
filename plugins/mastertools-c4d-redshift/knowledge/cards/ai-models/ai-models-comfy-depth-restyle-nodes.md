---
id: ai-models-comfy-depth-restyle-nodes
title: ComfyUI depth-guided relight: image to depth map, Instruct Pix2Pix conditioning, Flux model and LoRA, KSampler
domain: ai-models
tags: [comfyui, depth map, relight, flux, pix2pix, lora, ksampler]
applies_to: ComfyUI Cloud, Flux
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=zT6Z_WAaIeQ, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Nodes: load image, scale to total pixels (Lanczos), image to depth map, Instruct Pix2Pix conditioning with the text, dual CLIP, Flux guidance, LoRA, diffusion model, KSampler, VAE decode, save [00:31-04:51].
Lowering KSampler steps gives faster variations [05:23]. The video does not name the depth model or a timing.

**Use it:** treat as a node outline for a depth-guided restyle; there is no timing, so do not use it for estimates.
