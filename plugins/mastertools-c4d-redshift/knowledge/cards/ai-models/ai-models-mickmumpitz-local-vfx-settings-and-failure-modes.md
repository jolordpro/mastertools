---
id: ai-models-mickmumpitz-local-vfx-settings-and-failure-modes
title: Local AI VFX limits: 720p max, 121 frames (about 5 s), about 10 min per clip on a 4090; Sage Attention halves time; shots fail on literal masks and open frames
domain: ai-models
tags: [mickmumpitz, comfyui, wan vace, gguf, sage attention, 121 frames, 720p, qwen image edit, deep-read]
applies_to: ComfyUI, Wan VACE merge, RTX 4090 (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=_n0ir5V5tX4, src:yt-transcripts]
feeds: [[coach]]
conflicts: none
---
Numbers [09:23-14:02]: use the FP8 model if the GPU allows, else a GGUF compressed model that fits VRAM (slightly worse quality); 720p is the maximum input; basic workflow makes up to 121 frames, roughly 5 seconds, longer needs looping with per-segment prompts; a 4090 took about 10 minutes for a first test (OBS open); Sage Attention installs halve generation time with no visible loss; live preview set to latent-to-RGB lets you judge a run from the first step; RTX Super Resolution upscales to 4K afterwards. Image-edit start-frame tip: turn the 4-step Lightning LoRA off and use 31 steps, CFG 3 when the result looks cartoony [08:20]. Failure modes [15:36-18:08]: a ball-shaped mask gives a literal fireball (add hand-made Canny outlines and loosen the reference); a black mask moving over footage gives a floaty crocodile that vanishes when the mask stops; a fully dark ending lets the model invent a new camera move, so blend Canny outlines at the edges to hold the original composition; each driving-video variation was about "80% good" with something odd. Prompt tip: have an LLM rewrite the prompt to describe effects only, not camera moves, since camera comes from the track [10:56].

**Use it:** Budget for AI look-tests: one clip is short (5 s), 720p and about 10 min, so it is a tool for boards and shape tests, not delivery. Specs decay fast.
