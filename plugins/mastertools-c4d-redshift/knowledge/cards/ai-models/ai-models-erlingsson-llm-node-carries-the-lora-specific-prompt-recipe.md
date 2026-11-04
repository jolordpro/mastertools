---
id: ai-models-erlingsson-llm-node-carries-the-lora-specific-prompt-recipe
title: "Erlingsson: the workflow's LLM node holds a standing instruction matched to the LoRA, for example a transition recipe, instead of hand-written prompts"
domain: ai-models
tags: [ingi erlingsson, comfyui, prompting, llm node, transition lora, prompt template, images in, polish, ingi-erlingsson, deep-read]
applies_to: ComfyUI
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=4xS4LOn3CTE, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
His workflows contain LLM nodes with a preset prompt that already matches what the LoRA wants. For a transition LoRA the instruction is roughly: write a transition between image A and image B, find a commonality in shape, colour or person, describe how that thing changes into the other, and include these trigger terms [06:36-07:07].
He feeds sets of images, for example seven reference images, and lets the LLM write the text, rather than writing prompts by hand [05:33].

**Use it:** Store a per-model prompt recipe in the workflow so every run starts from the wording that model responds to.
