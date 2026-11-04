---
id: ai-models-mickmumpitz-playblast-to-render-settings-and-camera-slide
title: Local AI render from a clay playblast: 24 fps only, set clip lengths, 8 steps with speed LoRA vs 20 for max quality; a blank white backdrop makes the camera slide
domain: ai-models
tags: [mickmumpitz, comfyui, playblast, clay render, 24 fps, lora, steps, camera sliding, lip sync, deep-read]
applies_to: ComfyUI, open video model named "Minimax H3" in captions (name unsure), 2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Q2oVBVQNQ_U, src:yt-transcripts]
feeds: [[coach]]
conflicts: none
---
Mickmumpitz (single creator, low; model name garbled in captions). Input is a gray matcap playblast (Blender Workbench matcap, optional cavity or outlines; an outline pass is flat black with white outlines) [03:07-04:09]. The workflow resizes it and trims the clip to one of the lengths the model accepts, so plan shot length while animating; frame rate must be 24 fps because the model was trained at 24 [04:09-04:39]. Speed group optional: with the speed LoRA he still uses 8 steps (4 degrades quality) and a cache node that costs a little quality; bypass both and set 20 steps for maximum quality [02:35-03:07]. The prompt must name each reference and its role (e.g. the playblast is an untextured clay render defining layout, staging, animation); he has an LLM draft it [04:39-05:10]. Failures: a white backdrop gives the model too little camera information so characters slide; add a floor grid or detail [06:45]; more reference images slow the run, so merge them into one composite reference with an image-edit model [07:15-08:20]; a low-poly sphere marking an explosion made the explosion look like a sphere, and an outline pass gave more freedom [11:25]; extreme camera moves still break, and audio of the same length as the clip drives lip sync [11:58-12:59]. Old model capped at 81 frames, the new one avoids stitching [13:10].

**Use it:** If a previs/playblast ever goes to an AI look-test: 24 fps, grid floor, name the references in the prompt, expect camera slide on blank backdrops. Treat as fast-decaying.
