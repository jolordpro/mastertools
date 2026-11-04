---
id: redshift-m1-bucket-size-claims-by-chip-and-ram
title: Speaker's claim (2022): Redshift bucket size on Apple Silicon: 512 on M1 Max, 256 on M1 Pro, 128 on M2 with 16 GB+, 64 with 8 GB
domain: redshift
tags: [bucket size, m1 max, m1 pro, m2, apple silicon, unified memory, redshift 3.5.8, ledger-check, deep-read]
applies_to: Redshift 3.5.8, C4D R26, Apple Silicon (Sept 2022)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ZhFjwt978HA, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Adam Doing Tech [00:34-02:40]: M1 Max suggests 512, M1 Pro 256, M2 128 if RAM above 16 GB, 64 (or 128) with 8 GB; he leaves it at 512 on his machine. A warning appears if you stay at default 128 on a bigger chip. His Redshift IPR on a heavy still took 32 s to become stable; the project needs about 5 min as a final still. Progressive passes 128 vs 64 [03:10-04:45]: lower is faster feedback. Recorded on screen, so timings are rough. He also says the Redshift bundled with C4D is CPU-only; unverified and probably outdated, so ignore.

**Use it:** A starting point for Mac bucket tests only; see redshift-bucket-size-is-a-test.
