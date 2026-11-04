---
id: ai-models-flux-styleframe-from-render-depth-and-references
title: A locked style frame comes from a layout render plus its depth map and up to four reference images, usually after about three tries
domain: ai-models
tags: [ai render, flux, style frame, reference images, seed, comfyui, mickmumpitz, deep-read]
applies_to: FLUX 2 Klein 9B in ComfyUI (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=7J7hi-Hxpac, src:yt-transcripts]
feeds: []
conflicts: none
---
Mickmumpitz [09:49-12:25]. Prompt alone changes the look from shot to shot, so lock the look with a reference-driven image first. Pick a frame where all characters are in view, render it and its depth map, load both, then add references (the workflow takes up to four; more can be packed onto one image and addressed in the prompt). Describe in detail which object goes in which region. Expect about three tries and test several seeds; one frame was enough for a shot with two characters. Setup of any ComfyUI workflow: drag in the JSON, install missing custom nodes in Manager, restart, download the listed models into the shown folders.

**Use it:** Matches the pipeline step 'style frame before shots'; the lock-the-look frame then becomes a guide frame in the video render.
