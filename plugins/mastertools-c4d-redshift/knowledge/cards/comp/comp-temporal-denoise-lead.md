---
id: comp-temporal-denoise-lead
title: Ginzburg neural denoiser is the best open lead for flicker-free sequence denoising, but it is early and self-reported
domain: comp
tags: [comp, denoise, temporal, flicker, ginzburg, oidn, optix]
applies_to: research code (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://github.com/ginzburg-dev/ginzburg-neural-denoiser, src:research-verticals, https://www.youtube.com/watch?v=w3HGJ2KuGfo, src:yt-transcripts, https://www.youtube.com/watch?v=eGAjsSNtX6E]
feeds: []
conflicts: none
---
One 36-frame shot: temporal PSNR 43.78 against OptiX 43.75 and OIDN 42.33; flicker 0.045% against 0.060% and 0.054%.
On single frames OIDN wins (41.74 dB against 40.02). MIT licence, NVIDIA RTX 40 build, flagship weights private, 9 commits.
No mature open temporal AOV denoiser with weights was found.

**Use it:** copy the metric set (temporal PSNR, flicker) for our own tests rather than adopting the tool.
Transcript support: Spatial denoisers (OIDN, OptiX) leave temporal flicker; a motion-vector-reprojected average of three frames reduces it. (https://www.youtube.com/watch?v=w3HGJ2KuGfo [01:03])
