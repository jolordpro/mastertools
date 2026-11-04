---
id: comp-kelly-set-a-print-black-above-zero-so-nothing-clips
title: Kelly sets the black point slightly above zero (a print black) so shadows never clip and the image gets depth
domain: comp
tags: [cullen-kelly, davinci-resolve, look, black-point, clipping, deep-read, polish]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=RnSQq3OCNjY, src:yt-transcripts, src:polish-roster]
feeds: [comp, shakedown, polish coach]
conflicts: none
---
The default curve can run down to zero or below; setting the lowest control point slightly above zero acts as a soft container so shadows never spill below zero and clip [03:52-05:11]. Clipping pulls the viewer out of the image, consciously or not [05:11].
He says this also adds depth, and the black point can sit anywhere for a different texture [05:11-05:41].
The white point works the same way: in a colour-managed workflow the downstream transform already maps white, but he sometimes stalls whites below 100 to keep the signal inside its container [05:41-06:44].

**Use it:** Check the darkest pixels on the final delivery, not only on the grade, and pick a deliberate black level.
