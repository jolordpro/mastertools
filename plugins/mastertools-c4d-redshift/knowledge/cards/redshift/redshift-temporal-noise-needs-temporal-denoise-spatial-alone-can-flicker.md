---
id: redshift-temporal-noise-needs-temporal-denoise-spatial-alone-can-flicker
title: A frame that denoises cleanly can still flicker or shimmer in animation, because spatial denoising works in X/Y only; temporal noise needs a pass across frames
domain: redshift
tags: [temporal denoising, spatial denoiser, flicker, shimmer, animation noise, optix, samples, blender cycles, deep-read]
applies_to: Blender 3.5 Cycles (principle general)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jyGQIKOPwGA, src:yt-transcripts]
feeds: [redshift, shakedown, coach]
conflicts: none
---
All render noise comes from random sampling; spatial denoisers smooth neighbouring pixels and keep detail, but a perfect still can flicker over a sequence, and spatial denoising can make it worse [00:00][00:32]. Temporal noise comes from differences between consecutive frames; temporal denoisers work on the time axis, together with spatial ones [00:32][01:04]. Blender's OptiX temporal option is hidden in developer extras (as of 3.5) and was built for games with 1-2 samples per pixel [01:04][01:40]. Free extra samples: merging three 1024-sample frames gives roughly the noise of one 3072-sample frame, and also smooths inter-frame flicker [02:16][02:47]. Doubling samples gives diminishing returns [02:16]. Render a multi-layer EXR with the needed passes so either path stays open [09:23].

**Use it:** diagnostic: when a denoised sequence shimmers, treat it as temporal noise and test frame merging or a temporal denoiser. Check Redshift ledger for its own denoiser behaviour.
