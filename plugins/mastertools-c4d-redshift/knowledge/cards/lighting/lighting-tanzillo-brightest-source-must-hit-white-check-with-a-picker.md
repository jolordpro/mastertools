---
id: lighting-tanzillo-brightest-source-must-hit-white-check-with-a-picker
title: The brightest emitter in the frame must reach white, check it with a picker, and let glowing parts light their neighbours
domain: lighting
tags: [mike-tanzillo, critique, glow, emission, colour picker, vignette, comp, bleed, deep-read, lighting-critique]
applies_to: Arnold, Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=sjiuEeAp-JE, https://www.youtube.com/watch?v=55eY1-LlY3k, https://www.youtube.com/watch?v=sCDCs5At8uY, src:yt-transcripts]
feeds: [elevate, shakedown]
conflicts: none
---
Mike Tanzillo sCDCs5At8uY [07:31-08:32]: he samples the image with a picker, since nothing in frame can be brighter than a light source or eye white, so those must be white. One was a notch off, probably because a vignette sat on top, so keep the vignette off the brightest areas.
55eY1-LlY3k [06:20-07:22] a glove said to glow should throw its colour onto the body; making bright read as glowing is lighting plus comp. sjiuEeAp-JE [35:17-35:47] a back light box needs more glow and edge bleed in comp. sjiuEeAp-JE [37:21] x-ray panels could be brighter so light seems to pass through.

**Use it:** Add a max-value check on emitters and a glow-spill check on neighbours before bloom is judged.
