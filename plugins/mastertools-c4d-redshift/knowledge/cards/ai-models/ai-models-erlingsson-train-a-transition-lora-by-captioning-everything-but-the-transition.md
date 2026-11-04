---
id: ai-models-erlingsson-train-a-transition-lora-by-captioning-everything-but-the-transition
title: "Ingi Erlingsson trained a transition LoRA by captioning everything in each clip except the transition, so the model learns the gap"
domain: ai-models
tags: [ingi-erlingsson, golden-wolf, lora, transitions, training, comfyui, systems, polish, deep-read]
applies_to: open-source video models (2024-25)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XnaT-aJQZM0, src:yt-transcripts, src:polish-roster]
feeds: [coach]
conflicts: none
---
For him transitions are the storytelling in motion graphics, so he trained a model to do them [47:17-48:19]. Image-only or video-only training does not teach it; with older models you cannot tell it a transition exists, so you describe the two scenes and leave the transition undescribed, hoping the model attributes the gap to the LoRA [48:19-49:20]. It took the best part of a year to work well; the result is an 8-15 second seamless morph clip, about 65 frames per short clip [49:20-50:21]. Method details are his account; unverified.

**Use it:** Concept only: caption the invariant content and leave the target effect unlabelled so a fine-tune binds to it.
