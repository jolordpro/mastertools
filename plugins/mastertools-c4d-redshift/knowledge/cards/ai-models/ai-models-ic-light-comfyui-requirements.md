---
id: ai-models-ic-light-comfyui-requirements
title: IC-Light in ComfyUI runs on SD 1.5 with an SDXL-size canvas, needs the FC variant, and is hard to set up
domain: ai-models
tags: [ic-light, comfyui, sd1.5, res adapter, fc model, fbc, relight, ollama]
applies_to: ComfyUI, IC-Light (layered diffusion variants), 2024
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=sMMYSmDHAY8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
The workflow takes an SDXL-resolution canvas through an SD 1.5 checkpoint with ResAdapter to avoid hallucination [E 01:15, 23:35-24:13]. It uses the FC IC-Light model (not FBC) because the background comes from an empty latent plus a reference, not a direct background input [26:36-27:08]. About 16 custom nodes plus a local Ollama vision model to write product and background prompts [03:29, 17:52-21:22].
Grey placeholder background; product masked with a background-removal network, two variants because each fails on different cases [09:13-10:53]. Do not feed the product-resized image into the canvas size, or it crops [11:23].

**Use it:** a heavy route; the platform only needs to know it exists and what it requires if a product relight pass is wanted.
