---
id: pipeline-render-small-then-ml-upscale-glass-animation
title: Render glass animations at half size (a quarter of the pixels) and ML-upscale to 4K with chaiNNer and an ESRGAN model
domain: pipeline
tags: [upscale, esrgan, chainner, low resolution render, glass, render time, polyfjord, deep-read]
applies_to: Blender, chaiNNer, PyTorch (2022)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Jwl48psPrxU, src:yt-transcripts]
feeds: []
conflicts: none
---
Hard organic glass shapes responded well to AI upscaling, so rendering at 50 percent resolution (under 3 seconds a frame) then upscaling to 4K cut render time a lot [22:42-23:43, 28:21-28:52]. chaiNNer's image-file iterator loads a folder of PNGs, upscales, and saves; PyTorch with CUDA is installed from within the app [25:16-26:18]. A pre-trained .pth model is required; he chose a Real-ESRGAN df2k jpeg model from the cupscale package over those on the wiki he disliked [26:49-27:51]. Bake the physics cache before rendering an animation [21:40]. Only tested on a few shots.

**Use it:** A low-confidence option for draft-to-final speedups; compare carefully against a native render, since ML upscaling can invent detail.
