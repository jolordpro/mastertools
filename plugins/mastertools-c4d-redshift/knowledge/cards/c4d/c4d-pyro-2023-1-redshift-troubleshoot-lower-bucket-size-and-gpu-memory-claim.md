---
id: c4d-pyro-2023-1-redshift-troubleshoot-lower-bucket-size-and-gpu-memory-claim
title: Claim - Pyro renders that show nothing may need smaller Redshift bucket size and GPU memory use near 60-80 percent (C4D 2023.1)
domain: c4d
tags: [pyro, redshift, bucket-size, gpu-memory, ledger-check, troubleshooting, deep-read]
applies_to: Cinema 4D 2023.1 Pyro with Redshift (2022)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=TLlITrj5A_4, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Effectatron's claim only [16:34-17:05]. If a heavy Pyro scene will not render or shows nothing, in the Redshift tag, Advanced, System: lower the bucket size and lower the GPU memory setting to roughly 80 or 60 (his words, unit not stated). If that does not help, the voxel count is probably too high. For animation he also turns the random noise pattern off in Advanced and uses a medium preset [23:49]. He keeps the denoiser on what the caption renders as Optics (likely Optix), faster than Altus single or dual, which he names as the quality options [23:18].

Treat as unverified; the redshift ledger outranks it. Ledger check (Oct 31): OptiX is NVIDIA only, so not on a Mac; Altus single/dual run in bucket mode only (§3). Turning the random pattern off for denoised animation agrees with §3. Redshift reserves 90% of free GPU memory by default (§9), so 60-80 is a lower cap, not a fix the ledger confirms.

**Use it:** Only a last-resort checklist line after voxel size and caching; do not apply as a default.
