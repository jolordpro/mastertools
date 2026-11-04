---
id: ai-models-erlingsson-train-motion-not-style-for-video-and-teach-a-trigger-word-through-captions
title: "Erlingsson: do not train video LoRAs for style, pair a strong image model with a video model, and train for movement; his transition LoRA took six months"
domain: ai-models
tags: [ingi erlingsson, video lora, transition lora, caption trigger, wan, image model, first frame, polish, ingi-erlingsson, deep-read]
applies_to: Wan 2.2
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ktSEt_8T9MA, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
He would not advise training a video LoRA for a style today, unless the model struggles with it: put a brilliant image model (he cites GPT 2.5 for images) in front of a capable video model (Wan) because the video keeps the detail of its input [55:55-56:57].
What he trains for is movement: about a year and a half of transition models [56:27]. The video model takes one video at a time, so the transition has to be taught through captions: simple scene description, very detailed description of what happens in between, or detail everything else so the trigger word means everything not named [57:28-57:59]. It took about six months to get it working [58:31]. He also notes Wan 2.2 had the best pixel quality but weak prompt adherence [19:05].

**Use it:** Fix the look in the first frame with the best image model, and spend training effort on motion behaviour.
