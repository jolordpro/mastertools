---
id: comp-nuke-ground-shadow-by-masking-a-colour-correct-with-the-shadow-alpha
title: Instead of merging a shadow render over the plate, mask a ColorCorrect on the plate with the shadow alpha and lower gain plus contrast
domain: comp
tags: [alfie-vaughan, nuke, shadow, mask, colorcorrect, contact shadow, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=fxfuhl8Q7ys, src:yt-transcripts]
feeds: [composition]
conflicts: none
---
The shadow render is black until you press A, because the shadow lives in the alpha [01:34]. He does not Merge it; he adds a ColorCorrect on the plate and connects its mask input to the shadow render, then turns down gain, and also contrast, as a fake way to remove the specular highlights from the surrounding world [05:43-06:14]. He leaves it rough and fine-tunes after the car is on top. The shadow must be redistorted first or it lands off to the side [02:05].

**Use it:** Shadow-grade method for grounded CG. Compare comp-shadow-matte-invert-multiply-and-clone-the-transform.
