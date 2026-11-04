---
id: comp-blender-dojo-denoiser-tradeoffs-and-sample-floor
title: Blender Dojo's test: NLM trades noise for smudge artifacts, OIDN trades noise for blur, OIDN with normal and albedo inputs beat NLM at 1000 samples while using 200
domain: comp
tags: [blender dojo, denoise, nlm, openimagedenoise, oidn, albedo, normal, samples, artifacts, deep-read]
applies_to: Blender Cycles 2.9x, GTX 1060 (2021)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RQJwR6povJo, src:yt-transcripts]
feeds: [[redshift, comp]]
conflicts: none
---
Blender Dojo (hobbyist, 2021, low confidence; his own test on a GTX 1060). 20 samples is far too noisy and the noise shows most in out-of-focus background [01:35-03:39]. NLM leaves thumb-print smudges, shaking leaf edges and loss of small text, even at 1000 samples [04:10-06:12]. OIDN has no artifacts but blurs at 20 samples; start from 200 and it keeps more sharpness because the denoiser has less to solve (sticker-peeling analogy) [06:26-08:16]. With denoising normal and albedo plugged into the denoise node, 20 samples already beat both others at 1000, and 200 samples added detail; 1000 vs 200 differed only by slight detail, so 200 saves about 10-15 minutes per frame [09:18-12:55]. Using the node with only the noisy image creates a disconnect, like denoising in Photoshop after export [09:49]. Shadows can lose texture (turn muddy) when denoised from a noisy start [08:16].

**Use it:** Rule for the platform: feed the denoiser its guide AOVs and give it a decent sample floor; do not treat the denoiser as a fix for a noisy draft. Redshift values must come from the redshift ledger.
