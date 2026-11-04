---
id: comp-prebake-textures-to-acescg-exr-when-the-renderer-lacks-input-transform
title: When a renderer's texture node cannot set an input transform, pre-convert sRGB textures to ACEScg EXR and read those with no linearize
domain: comp
tags: [aces, acescg, renderman, maya, texture conversion, davinci resolve, nuke, ocio, meshmen, deep-read]
applies_to: RenderMan for Maya (2020), OCIO
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=3_dlZVNlrIc, src:yt-transcripts]
feeds: [redshift, post-composite]
conflicts: none
---
Meshmen's Peter Augustine on RenderMan for Maya in 2020: the texture read node only offered "linearize", which goes sRGB to linear sRGB, not to ACEScg, so albedo colour came out with a visibly different hue [08:28-10:38]. Fix: convert each sRGB colour texture with a colour-space transform from utility sRGB texture to ACEScg in Nuke or Resolve's free Fusion page, write EXR, and read that file raw [11:25-19:09]. In Resolve set the project to ACES with the output device transform temporarily at ACEScg before export, otherwise an sRGB view transform is burned in [18:03]. The converted albedo is slightly darker than the source and that is correct [10:05]. Texture maps made in a painter should be exported as ACEScg directly, with data maps (roughness, bump, displacement) left as data [28:54-30:26]. Non-colour data was not converted.

**Use it:** Same trap exists in any renderer whose file node lacks an input transform; check by comparing a colour chart through both paths.
