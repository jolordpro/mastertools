---
id: comp-oidn-inputs
title: OIDN 2.5.1 takes beauty plus optional albedo and normal; prefilter the aux inputs, and it is not temporally stable
domain: comp
tags: [comp, denoise, oidn, intel, albedo, normal, metal, apple silicon]
applies_to: OIDN 2.5.1
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/RenderKit/oidn, src:research-verticals, https://www.youtube.com/watch?v=RQJwR6povJo]
feeds: [PLAN Phase 1 denoise rung]
conflicts: none
---
Runs on CPU including Apple Silicon, Apple Metal GPUs (M1+), NVIDIA Turing to Blackwell, Intel Xe and AMD RDNA 2-4. Apache licence.
Use cleanAux with prefiltered aux for the best frames.
Built for stills: a sequence can flicker.

**Use it:** denoise single frames and hero stills with OIDN; test sequences for flicker before trusting it.
