---
id: lookdev-nineb-denoiser-removes-detail-when-input-too-noisy-and-skips-split-aovs
title: The OptiX denoiser strips real detail if the input is too noisy and only cleans the beauty, so split light AOVs stay noisy unless added
domain: lookdev
tags: [nine between, houdini, solaris, usd, denoiser, optix, aov, noise, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, redshift, comp]
conflicts: none
---
With the Nvidia OptiX denoiser on, a very noisy frame loses detail because it treats it as noise; as samples rise it does a better job and detail returns [2:31:59-2:32:30]. It runs on the beauty (C) only, so per-light split passes stayed noisy until added to the denoise list [2:33:02-2:34:36]. Karma XPU is a much faster GPU path, but needs MaterialX shaders [2:37:41-2:38:43].
He notes denoise runs when rendering to disk as well as in the viewport [2:32:30].

**Use it:** A denoise check: tell artists to denoise at a sample count that keeps detail, and denoise split passes too if they will be re-summed in comp.
