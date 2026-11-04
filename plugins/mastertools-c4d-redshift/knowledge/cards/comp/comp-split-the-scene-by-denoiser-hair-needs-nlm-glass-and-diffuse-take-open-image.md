---
id: comp-split-the-scene-by-denoiser-hair-needs-nlm-glass-and-diffuse-take-open-image
title: One denoiser does not suit every object: at 32 samples OpenImage denoise smeared hair but handled glass, so the hair was rendered with NLM and the rest with OpenImage, then layered
domain: comp
tags: [denoise, openimage, nlm, hair, holdout, alpha over, render layers, ibn xr, deep-read]
applies_to: Blender Cycles
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XjzUeI31QVE, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
IBN XR Studio test (Cycles, 32 samples, adaptive) [2:14-3:03]: the glass sphere was denoised properly by OpenImage; the diffuse cube looked about the same in both; the hairy sphere was right only with NLM. OpenImage drops fine detail on very detailed objects, and its detail capture grows with resolution. Method [3:53-13:24]: put objects in two collections, make two linked scene copies, hold out the other collection in each, turn on transparent film, then render both through one empty root scene whose compositor stacks them with Alpha Over (transparent layer over the opaque one). The OpenImage scene ran at about 8 samples (16 or 32 optional) with its denoiser run in the compositor, the NLM scene kept 32. For stills, a render border around the hair object avoids rendering empty alpha [13:54]. Holding out the background in the OpenImage scene changed fine detail slightly at the hair edge, so use hold out in both scenes for animation [15:10-16:44].

**Use it:** The coach can suggest per-object denoise passes when fur or hair loses detail; in Redshift, check denoise on a hair or fur layer separately, then comp.
