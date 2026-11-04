---
id: redshift-ipr-oidn-with-progressive-passes-128-keeps-gpus-from-running-flat-out
title: School of Motion (2025): use the OIDN denoiser in IPR and cap progressive passes at 128 so GPUs stop constantly rendering
domain: redshift
tags: [ipr, oidn, progressive passes, denoiser, redshift 2025.1.2, preview speed, deep-read]
applies_to: Redshift 2025.1.2+ in C4D (2025)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=HlQhMbjrM6M, src:yt-transcripts, https://www.youtube.com/watch?v=x_xdQrCJsCM]
feeds: [redshift]
conflicts: none
---
School of Motion [07:40-08:25]: since Redshift 2025.1.2 the OIDN denoiser gives a quick smooth IPR; set progressive passes to 128 so the GPUs aren't constantly working and loud. Redshift Live (2026.4) replaced RT; see ledger §3-4 for OIDN quality modes and the progressive-pass behaviour.

**Use it:** Use as preview setting; final renders still go through Bucket.
Transcript support: Lukas Thorup: OIDN High with the progressive slider at 0 denoises only after all samples (16 s to 13 s on his test); ledger-check. (https://www.youtube.com/watch?v=x_xdQrCJsCM [07:28-08:32])
