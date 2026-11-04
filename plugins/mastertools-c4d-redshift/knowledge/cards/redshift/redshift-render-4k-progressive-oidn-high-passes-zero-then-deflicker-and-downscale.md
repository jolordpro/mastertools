---
id: redshift-render-4k-progressive-oidn-high-passes-zero-then-deflicker-and-downscale
title: Lukas Thorup: 4K progressive 32 passes with OIDN High and the progressive slider at 0 took about 13 s a frame; the flicker was fixed in Resolve Fusion and the 4K delivered at 1080
domain: redshift
tags: [lukas thorup, progressive, oidn, deflicker, resolve, fusion, 4k downscale, animation flicker, ledger-check, deep-read]
applies_to: C4D + Redshift (2025 upload) and DaVinci Resolve Fusion
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=x_xdQrCJsCM, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Ledger-check: ledger says final delivery goes through bucket, and flicker is worse than a longer render; this is the speaker's shortcut. Bucket off, final rendering set to progressive with 32 passes: 7 s but noisy; OIDN on at High: 16 s, edge hair detail softened; progressive slider at 0 so denoise runs only after all samples: 13 s [06:58-08:32]. Fur size doubled to survive denoising [09:04].
Denoising flickers between frames. He rendered 4K, then in Resolve made a 1080 by 1920 timeline: downscaling hides detail loss and flicker. HD render took 8 s but looked flat and flickered; 4K took 13 s [09:35-11:40].
Fix: Fusion DeFlicker node, mode fluorescent light, detail-restored slider about 0.08 or 0 if flicker remains [12:05-13:44].

**Use it:** an option when Altus or bucket is too slow; always check a moving range for flicker first (ledger §4 on bucket for delivery, §6 on testing a moving range).
Ledger (Oct 31 master) agrees on the parts: OIDN High is the final-quality setting (§3, [V]); denoise overhead 0 means one denoise at the end (§3, [V]).
