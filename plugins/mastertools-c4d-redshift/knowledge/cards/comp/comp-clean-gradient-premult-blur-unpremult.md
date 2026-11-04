---
id: comp-clean-gradient-premult-blur-unpremult
title: A clean gradient fill: mask the area, premultiply, blur, unpremultiply, then reveal with rotopaint
domain: comp
tags: [courtney price, nuke, foundry, premult, unpremult, gradient, clean plate, ludwig hailer, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=yl28HkA-qyo, src:yt-transcripts, https://www.youtube.com/watch?v=sTCeHUto1IM]
feeds: []
conflicts: none
---
Courtney Price learned this from Ludwig Hailer and says it replaced her older pixel-filler technique [44:22-44:54]. Mask the area to fill, premultiply so only colour values remain, blur to push the colour outward, unpremultiply to extend RGB to the edge of the blurred alpha. The blur amount sets how smooth the gradient is. Use rotopaint to reveal the clean background.

**Use it:** A fast way to build a smooth background fill behind removed marks or graphics.
Transcript support: Tanzillo reveals a graded copy through Roto Paint (second input becomes bg1) to paint warmth into a mouth; same reveal move (https://www.youtube.com/watch?v=sTCeHUto1IM [17:55])
