---
id: ai-models-long-prompts-lose-details
title: Piling details onto an image prompt drops them: corner placement, light type and lens went wrong as the caption grew
domain: ai-models
tags: [[prompting, captions, detail, basse, nano-banana], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Basse's test with one image model: a short caption for a tabby cat gave what was asked. After more clauses were added, the climbing tree was not in the corner, the "afternoon sun" came out overcast, and the lens look was off [1:06:54-1:08:28].
Training captions are written by a vision-language model that sees the picture only; it missed the record player and radio in a Roma frame and invented a pendant lamp glow, so prompts built from such captions miss intent, story and exact light [1:09:30-1:11:03]. A recreation with the technical caption still lost the black-and-white vibe and added pillars outside 2.39:1 [1:11:35-1:12:05].
He says captioning also uses several VLMs per image at Stability to vary phrasing [1:02:44].

**Use it:** Keep prompts short and check each stated detail (placement, light direction, lens) against the result; list the misses instead of re-rolling blindly.
