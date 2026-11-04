---
id: redshift-cryptomatte-split-pass-low-quality-render-then-beauty-overwrites-the-rgb
title: Polygon Division 2024: render Cryptomatte alone in a second job at low samples (about 20 s), then render the beauty last so its RGB overwrites the rough one
domain: redshift
tags: [cryptomatte, render time, bucket size, vram, separate pass, older gpu, polygon division, 4k, deep-read]
applies_to: C4D + Redshift (2024 upload), GTX 1080 / RTX 2080 test machine
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=zFBuUVbGli8, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
On a 4K shock-absorber scene: base multipass beauty 1:15, with Cryptomatte added 7:46, so about 6:30 extra per frame [01:40-02:42]. Cryptomatte alone took 20 s; object plus material together added only 13 s [02:42].
Fix: duplicate the render setup, keep only the Cryptomatte AOVs (object and material), set samples to 1, reflections and refractions to near zero, turn GI off; the RGB is rough and ignored, and this pass took 25 s [03:14-04:46]. Render this first, then the beauty to the same folder so the beauty RGB overwrites the junk RGB [04:46-05:17].
Why: on his cards the Cryptomatte job would not render at bucket 512 (memory headroom), so it ran at 128, while the beauty alone runs at 512 [05:17-05:48]. He says recent versions moved Cryptomatte to the GPU, raising memory use [00:38]. Test machine cards: 1080 with 11 GB, 2080 with 10 GB, as stated (captions) [01:40].

**Use it:** cost estimator: model Cryptomatte as a separate cheap job; scene check flags Cryptomatte plus 512 bucket. Supports `redshift-bucket-size-is-a-test`.
