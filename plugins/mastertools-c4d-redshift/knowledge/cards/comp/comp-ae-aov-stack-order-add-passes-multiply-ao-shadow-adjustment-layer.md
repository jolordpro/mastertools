---
id: comp-ae-aov-stack-order-add-passes-multiply-ao-shadow-adjustment-layer
title: Stack AOVs in After Effects as Add layers, multiply AO under an opacity matched to the plate, and darken shadows with a matted adjustment layer
domain: comp
tags: [after effects, aov, diffuse direct indirect, specular, ambient occlusion, shadow matte, adjustment layer, cryptomatte, deep-read]
applies_to: After Effects, Arnold AOVs (method applies to Redshift AOVs)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kHkUtx8dS1o, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Project set up [00:42-01:35]: sRGB (IEC61966-2.1) working space with 32-bit depth and Linearize Working Space (his words: explained in another video), and the EXR footage interpreted as linear light. Matte: a cryptomatte extractor effect picks the chair into a chair-matte layer, used as a Luma track matte to drop its shadow (alpha matte would keep it) [02:08-02:39]. Beauty from passes [03:09-04:12]: base layer, then diffuse direct, diffuse indirect, specular direct, specular indirect, each an extractor layer with blend mode Add. AO on top with Multiply, no track matte; lower the opacity until its darkest value is near the plate (he read 0.0037 against 0.0029 in the info panel) [04:43-05:47]. Shadows: extract the shadow mask, make it a track matte for an exposure adjustment layer above the background, Luma preferred since it protects edges [05:47-06:49].

**Use it:** the AE comp recipe in the coach; use the Info panel readings of the darkest area to set AO and grade strength, not by eye alone.
