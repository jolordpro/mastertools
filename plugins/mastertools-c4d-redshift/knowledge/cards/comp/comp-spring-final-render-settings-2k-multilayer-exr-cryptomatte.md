---
id: comp-spring-final-render-settings-2k-multilayer-exr-cryptomatte
title: Spring final render: 2K multilayer EXR 32-bit, 2000+ samples, noisy shots 4000 to 6000, smoke bounces limited to 2 or 3, Cryptomatte on
domain: comp
tags: [render settings, multilayer exr, cryptomatte, samples, motion blur, denoise, cycles, blender studio, deep-read]
applies_to: Blender Cycles (2019)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Everything rendered at 2K to multilayer EXR 32-bit [32:18]. Samples: 2000 plus, 4000 or 6000 on very noisy shots; smoke shots limited bounces to 2 or 3 [32:18] [32:49]. Motion blur was costly but needed for the animation [32:49]. Cryptomatte was "really, really" important [32:49]. Denoising passes were saved inside the multilayer EXR alongside the noisy image [33:21].
These are Cycles numbers from 2019, not Redshift values.

**Use it:** As a reference for a high-end offline stills pipeline: save noisy and denoised data together, keep ID mattes, and trim bounces for volumes.
