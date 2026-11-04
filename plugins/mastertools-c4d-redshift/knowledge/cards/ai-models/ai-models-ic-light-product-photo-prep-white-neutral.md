---
id: ai-models-ic-light-product-photo-prep-white-neutral
title: Product photo prep for AI relight: plain white surfaces, no extra lighting, neutral glass reflections, and test two background-removal models
domain: ai-models
tags: [[ic light, product photo, background removal, segmentation, glass, white background, birefnet, ultra mask], deep-read]
applies_to: ComfyUI IC-Light workflow
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sMMYSmDHAY8, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
The author shoots the source product on a phone, point and shoot, on white backgrounds and surfaces with no extra lights, because white minimises coloured reflections in glass [12:00-12:39]. A hard case (clear glass with a neutral reflection) was used to test segmentation: the second, finer-tuned background-removal node removed the whites better with default values, while the first node was fine for most images [12:39-13:17]. He starts on the default node and switches only when needed [12:00].
The cut-out is placed on a flat grey background, scaled and positioned by percentage (50% is centred, 20% moves left) and rotated, and the whole composed image goes to the latent so the new background is generated with the product's perspective [14:30-16:09].

**Use it:** judge a matte on the hardest object (glass), not the easy one.
