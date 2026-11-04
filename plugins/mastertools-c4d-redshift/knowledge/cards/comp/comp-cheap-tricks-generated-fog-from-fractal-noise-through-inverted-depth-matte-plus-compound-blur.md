---
id: comp-cheap-tricks-generated-fog-from-fractal-noise-through-inverted-depth-matte-plus-compound-blur
title: Fog without a fog pass: Fractal Noise solid matted by inverted depth, with a depth-masked Compound Blur and a Supercomp haze
domain: comp
tags: [fog, atmosphere, fractal noise, set matte, compound blur, supercomp, haze, depth, deep-read]
applies_to: After Effects, Red Giant Supercomp
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Fog recipe [19:45-24:20]: a solid with Fractal Noise at the scale of the comp, evolution on a time expression and transform keys if the fog should move; use the depth pass as an inverted luma matte, and Levels or Brightness and Contrast on the depth layer to change how thick it reads. Add a Compound Blur on an adjustment layer with the depth as blur layer and Invert Mask ticked, so far areas also diffuse the footage (the host prefers the Universe version since it repeats edges). In Supercomp instead use Set Matte (inverted luma, 'effects and masks' ticked), then Blur Behind, Haze (blends the background colour into the fog), diffusion and volume fog for rays; one click presets such as Dense Mist or Light Smoke exist [21:15-23:48]. The same set-up works with stock fog or smoke footage; colour-correct the footage below and it propagates, which also gives an underwater look.
Transfers: a rendered Z-depth AOV works the same way.

**Use it:** Prefer when no volumetric fog was rendered; match fog tint to the plate with the depth.
