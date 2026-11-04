---
id: ai-models-qwen-image-edit-relight-lora-warning
title: ComfyUI ships a Qwen-Image-Edit relight workflow with a community LoRA, and a guide warns such LoRAs can learn colour grading instead of lighting
domain: ai-models
tags: [qwen-image-edit, relight lora, comfyui, masked edit, cryptomatte, apache]
applies_to: Qwen-Image-Edit 2509 / 2511
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://huggingface.co/Comfy-Org/Qwen-Image-Edit, https://www.runcomfy.com/trainer/ai-toolkit/qwen-edit-2511-relighting-lora, src:research-verticals]
feeds: [mockup design]
conflicts: none
---
Apache licence. Training our own LoRA on synthetic light pairs is the suggested fix.

**Use it:** quick masked mockup with a Cryptomatte mask; verify it changed light, not grade.
