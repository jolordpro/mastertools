---
id: pipeline-spring-sample-merging-progressive-farm-render
title: Sample merging: render a small chunk of samples first, check the shot, then add more samples with an offset and merge on the farm
domain: pipeline
tags: [render farm, sample merging, flamenco, progressive, noise, denoise, preview, cycles, deep-read]
applies_to: Blender Cycles + Flamenco
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
A farm job renders a chunk of samples (he gives ten as an example) to see whether the shot is fine, for instance no pink missing textures [33:51]. Later jobs render more samples with a seed offset and the farm merges them; Flamenco supports this [33:51]. Denoising is done afterwards in post on merged frames, with an operator that denoises and overwrites individual frames [34:14] [34:22].
Benefit: a quick first version, then more quality as time allows.

**Use it:** Idea for a render platform: first pass cheap, verify, top up with extra samples under a new seed, then denoise last. Check whether Redshift supports a comparable accumulate-and-merge workflow before promising it.
