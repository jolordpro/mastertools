---
id: ai-models-erlingsson-style-lora-start-from-a-need-lots-of-data-and-work-on-captions
title: "Erlingsson's style-LoRA rules: start from a need, be specific, have plenty of good data, and test captioning strategies, since there is no rulebook"
domain: ai-models
tags: [ingi erlingsson, lora training, captions, training data, style lora, gaussian splat look, failure, polish, ingi-erlingsson, deep-read]
applies_to: any
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ktSEt_8T9MA, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
He picks the style from a need, being very specific about what it is [51:09-52:52]. A LoRA for the Gaussian-splat 3D scan look 'came out spectacularly wrong', which he blames on too little training data [51:50].
Next: as much good data as possible, then the captioning strategy, a big deal for video [52:52]. Newer models were trained on essay-length captions, older ones on short ones [53:22]. He has trained with no captions, with essays on some images and two words on others, and sometimes trains several times [53:53].

**Use it:** Keep a training log (data count, caption style, steps) so a failed LoRA can be diagnosed.
