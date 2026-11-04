---
id: comp-cheap-tricks-ez-matte-depth-as-luma-matte-with-brightness-contrast-sliders-exposed
title: Use a depth pass as a luma matte, then expose its Brightness and Contrast in Essential Properties to slice depth without roto
domain: comp
tags: [depth matte, luma matte, essential properties, depth wish, after effects, title behind subject, deep-read]
applies_to: After Effects, Depth Wish free script
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Put footage and its depth pass in a new comp, set the depth as a luma matte, and add Brightness and Contrast (Legacy checked) to the depth layer: contrast sharpens the dividing line, brightness acts like a gradient-wipe reveal [05:51]. Expose both effects through Essential Properties and the pre-comp becomes a layer with two sliders, no need for both layers to be present; duplicate it for several depth slices [06:21-06:54]. The host's free Depth Wish script builds this 'EZ Matte' pre-comp from a footage and depth pair and also batches many pairs [06:54-07:25, 10:30].
Use for a trailer-style title behind a character: set the depth cutoff with the value slider and feather with softness, keyframing if the subject moves [07:40-08:56].

**Use it:** Fast fallback when a subject has no usable alpha: depth matte with exposed sliders and a keyframed cutoff.
