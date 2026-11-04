---
id: ai-models-ai-render-control-passes-outline-depth
title: AI video rendering from a 3D layout uses an outline pass for freedom and a depth pass for fidelity; export both and test
domain: ai-models
tags: [ai render, controlnet, outline pass, depth pass, workbench, freestyle, wan, comfyui, ltx, blender, mickmumpitz, deep-read]
applies_to: Open-source ComfyUI workflow, 2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0WkixvqnPXw, src:yt-transcripts, https://www.youtube.com/watch?v=7J7hi-Hxpac]
feeds: [ai-models plan]
conflicts: none
---
[02:46] Outline preserves composition and leaves detail free; depth follows geometry more strictly; the two can be blended.
[03:08] Outline pass: toon outlines in white on black. Depth: normalised, inverted, contrast boosted [04:10]. Control net strength: as low as possible [06:15].
[01:34] The model is a merge of Skyreels reference-to-video and VACE.
Merged from `ai-models-ltx-render-from-3d-depth-plus-outline-passes`: Mickmumpitz [03:06-03:37, 07:46-09:49]. Two control videos are made from the 3D scene. Depth: black and white, white near. Blender's depth output arrives inverted and unnormalised, so add Normalize then Invert Color, and optionally an RGB Curves node to separate the foreground. Outline: render with the Workbench engine with Outline and Cavity on, straight to a black-and-white video (no image sequence), and let ComfyUI extract the lines later with Canny. Outlines give structure, depth gives 3D form; use one or both for maximum precision. The Canny node copes with any render, not only clay.

**Use it:** if the platform offers AI previews, output outline and depth passes.
