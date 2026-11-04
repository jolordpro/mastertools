---
id: ai-models-motion-blur-in-start-frame-and-post
title: Put some motion blur in the start frame so the clip starts moving, and add blur, lens effects and shake in post
domain: ai-models
tags: [motion blur, start frame, post, camera shake, lens effects, ai video]
applies_to: Seedance 2.0 workflow
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=LcrSp_hzYvA, src:yt-transcripts]
feeds: [video preview]
conflicts: none
---
A sharp start frame can make the clip start static then jump into motion [05:43]. The model often gives less motion blur than wanted, so add subtle blur, lens effects and shake after [14:14]. Directing ground blur toward the car helped on the hardest shot [18:14].

**Use it:** Add a post step for motion blur to AI-video previews; do not judge speed from the raw output.
