---
id: ai-models-ic-light-save-generated-prompt-text
title: When a local LLM writes the prompt, save the text to a file: it comes out different after restarting ComfyUI
domain: ai-models
tags: [[ic light, comfyui, ollama, llava, prompt reproducibility, product relight, prompt file, concatenate prompts], deep-read]
applies_to: ComfyUI IC-Light workflow with Ollama
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sMMYSmDHAY8, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
The tutorial author (channel ControlAltAI) uses a local vision model to write one detailed description of the background reference ("extreme detail, atmosphere, mood, tone, lighting, as for a product advertisement") and another of the product ("as a product photographer") [18:22-20:06]. The two texts are joined product first, then background, so the sampler reads it as one product ad [21:22].
The model is generative, so closing and reopening ComfyUI can give a different description. If a generation is liked, save the final positive prompt to a text file and reuse it through a "custom conditioning" input [21:55-22:31]. Labelling mistakes in the description did not matter in his tests [20:50].

**Use it:** any AI step whose input is machine-written needs the exact text logged with the output, or the shot cannot be reproduced.
