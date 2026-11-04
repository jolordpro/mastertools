---
id: comp-blender-denoiser-ranking-per-pass-temporal-and-topaz
title: Denoiser choice: Open Image Denoise for stills with albedo and normal, per-pass denoise only for long renders, temporal denoise for animation, Topaz Video best overall in one test
domain: comp
tags: [denoise, open image denoise, optix, temporal denoise, per pass, topaz video, boiling, film grain, robin squares, deep-read]
applies_to: Blender 4.x / 5, RTX 4080 (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=yAbuPpbbATA, src:yt-transcripts, https://www.youtube.com/watch?v=XjzUeI31QVE]
feeds: []
conflicts: none
---
Robin Squares one-clip test [00:00-13:41]. Boiling is the bad-denoise artifact. DaVinci Resolve noise reduction is built for sensor noise and was surprisingly bad on render noise. OptiX and Open Image are about equal; Open Image slightly better, best for stills, and it takes albedo and normal inputs to keep detail. Static noise (animated-seed button off) gave slightly better results on flat areas. Per-pass denoising then recombine beats denoising the finished frame, but 12 passes at full HD cost about 4 minutes of denoise on an RTX 4080 that could have gone into more samples: worth it for complex scenes (about 20 min a frame), not simple ones. Blender's hidden temporal denoise (developer extras, command 'denoise animation', must run in the file that rendered) is better than the above but needs the finished image, no passes. Topaz Video AI (about $300 now) won overall on hair and skin but was bad on glass fireflies and defocus. Order suggested: vector blend, then temporal, then Topaz for long renders. Never skip clean-up optimising: render as clean as you can, denoise to noise-free, add film grain last, since render noise is not film grain [13:03].

**Use it:** Advisor line: the denoiser is a finisher; choose by deliverable (still, animation with passes, animation without) and add grain after denoise.
