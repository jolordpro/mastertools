---
id: redshift-fast-4k-sampling-recipe-threshold-0-008-min-8-max-16-then-raise-by-pass-lukas-thorup-2025
title: Lukas Thorup 2025: from a 31 s bucket benchmark, automatic sampling off, threshold 0.008, min 8 max 16 and raised reflection, light and SSS samples gave 9-12 s
domain: redshift
tags: [lukas thorup, sampling, threshold, min samples, max samples, reflection samples, bucket size, ledger-check, 4k, deep-read]
applies_to: C4D + Redshift (2025 upload), RTX 3090 workstation
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=x_xdQrCJsCM, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Ledger-check: one creator's numbers on a shoe with fur, SSS sole and leather, not ledger values. Benchmark: all default, bucket, 1080: 31 s [02:11]. Then advanced mode, automatic sampling off, threshold 0.008, min 8, max 16, reflection samples 64, multi SSS 64 then 256, light samples 228: noisier but 9 s [03:15-04:19].
Raising max to 32 and min to 16, reflection 228, SSS 512, unified up to 32 and 64: about 12 s, similar time, with denoise easy to apply [04:19-05:55]. A bigger bucket helps on his 3090 but depends on VRAM [04:51].
Switching the same settings to 4K (2160 wide) took 43 s and revealed leather and fur detail missing at 1080 [06:12-06:58].

Ledger (Oct 31 master): threshold 0.008 sits in the general-production band (§2, [T]); min 8 meets the [V] 8-16 floor for DOF or motion blur; max 16 is below every [T] max bracket (32+), which fits the noisier result.

**Use it:** ledger remains the reference; use this as a shape of test (benchmark, then raise per-effect samples) and log results on the 640 draft.
