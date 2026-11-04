---
id: comp-three-grade-nodes-match-black-white-gamma
title: Match an element to a plate with three grades: black and white points, then lift and gain, then gamma; the reversible stack gets about 70-78% there
domain: comp
tags: [courtney price, nuke, foundry, grade, colour matching, black point, white point, concatenate, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=yl28HkA-qyo, src:yt-transcripts, https://www.youtube.com/watch?v=fxfuhl8Q7ys]
feeds: [composition, coach]
conflicts: none
---
Courtney Price's start for any element (CG, stock, still) [28:13-31:17]:
1. Grade node one: sample and set black and white points.
2. Grade node two: lift and gain mapped to the black and white values of the destination plate.
3. Grade node three: gamma only (to suit the baked gamma curve), and optionally RGB tonality.
Because grade nodes concatenate, adding the reverse of each returns the original image with no loss [30:16]. Only after that does she use colour-correct nodes with shadow/mid/highlight splits, which are not reversible. She says the three grades take her about 70-78% of the way, then she adds atmosphere (haze, fog, wet, highlight pings), a wash of light for light direction, and shadows [31:17].
In Q&A [1:04:38] she says black/white point equals lift/gain; she keeps them as two operations so lift/gain stay tied to the sampled plate while the points can be re-adjusted.

**Use it:** A repeatable first pass for matching CG renders to footage, and a rule to keep grades reversible until the last step.
