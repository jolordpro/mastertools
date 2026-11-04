---
id: comp-selective-denoise-walls-vs-rest-with-cryptomatte-mix
title: Denoise by material: blend denoised and noisy images with a cryptomatte matte so walls get more denoise than furniture
domain: comp
tags: [denoise, cryptomatte, compositor, mix node, interior, walls, noisy image, deep-read]
applies_to: Blender compositor (principle transfers)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dLZEmfqob7k, src:yt-transcripts, https://www.youtube.com/watch?v=aplU2CXwXLY]
feeds: [coach]
conflicts: none
---
Plain denoise-everything hits detail you want to keep, and walls need more than sofa or rug [05:22]. Setup: enable Cryptomatte Material in view layer passes, render with denoise on, and keep the noisy image as well [05:52]. Mix denoised and noisy images with one mix node per target (one for the walls, one for the rest) and judge the factor by eye, he gives no magic number [06:23]. A Cryptomatte node picks the wall material; its matte output (white on walls) drives the final mix factor [07:25]. Repeat for any problem material [07:56].

**Use it:** with a noisy plus denoised pair and a cryptomatte AOV, the same mask-weighted blend works in Nuke or AE; keep the noisy beauty in the multilayer EXR.
Transcript support: Cryptomatte selections give per-object alpha in Nuke across an animation (https://www.youtube.com/watch?v=aplU2CXwXLY [11:11-12:44])
