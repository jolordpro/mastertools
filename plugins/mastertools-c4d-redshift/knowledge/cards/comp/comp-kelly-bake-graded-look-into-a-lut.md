---
id: comp-kelly-bake-graded-look-into-a-lut
title: "Cullen Kelly: anything graded upstream or downstream of a LUT can be baked into a new LUT, but editing the original recipe is cleaner"
domain: comp
tags: [cullen-kelly, lut, baking, look, hue, contrast, polish, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp]
conflicts: none
---
A LUT is a list of numbers describing what was done to an image, so adjustments around a LUT, including hue changes, can be combined into one new LUT. There are best practices to follow [50:02-51:03]. It is not ideal for changing a LUT's behaviour because you are fixing something you could have neutralised if you had the original recipe [51:35]. He covers separating contrast from colour in a LUT in his 'visual math' series on Mixing Light [48:28-49:00].

**Use it:** Bake a delivery look into one LUT only after the grade is signed off, and keep the node recipe.
