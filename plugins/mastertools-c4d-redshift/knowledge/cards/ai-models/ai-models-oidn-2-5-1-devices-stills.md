---
id: ai-models-oidn-2-5-1-devices-stills
title: Intel OIDN 2.5.1 runs on Apple Metal GPUs, NVIDIA Turing to Blackwell and CPUs, takes albedo and normal, but is not temporally stable
domain: ai-models
tags: [oidn, open image denoise, denoiser, metal, apple silicon, albedo, normal, flicker]
applies_to: OIDN 2.5.1
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/RenderKit/oidn, src:research-verticals]
feeds: [PLAN 5b, denoise rung]
conflicts: none
---
Apache. Use `cleanAux` and prefilter aux images for the best frames. Built for stills.

**Use it:** fine for draft denoise on the Mac; do not trust it for flicker-free sequences.
