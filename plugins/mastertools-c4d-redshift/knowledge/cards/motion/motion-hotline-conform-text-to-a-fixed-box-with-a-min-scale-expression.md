---
id: motion-hotline-conform-text-to-a-fixed-box-with-a-min-scale-expression
title: Make text scale itself to a fixed container - scale = 100 times the smaller of target width / text width and target height / text height
domain: motion
tags: [after-effects, expression, text, scale-to-fit, evan-abrams, kyle-hamrick, deep-read]
applies_to: After Effects
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=bnFRXVbi0ZA, src:yt-transcripts]
feeds: [motion-critique, coach]
conflicts: none
---
[47:16-54:05] Evan's method: lock the text anchor point to the middle, add sliders for target width and height (example 500 by 500), read the layer's sourceRectAtTime width and height, and set scale to 100,100 multiplied by a ratio chosen with an if: target width over W if that ratio is smaller, otherwise target height over H. Kyle's free preset does the same with Math.min of the two ratios. Reason: copy, names or languages change late and the text must always sit in its box or circle; use text animators to stay procedural.

**Use it:** a template rule for lower thirds and score bugs: no hand-scaled text.
