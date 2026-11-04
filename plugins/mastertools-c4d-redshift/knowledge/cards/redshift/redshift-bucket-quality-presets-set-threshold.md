---
id: redshift-bucket-quality-presets-set-threshold
title: Basic-mode Bucket Quality presets just switch the adaptive error threshold; typing your own value flips it to Custom
domain: redshift
tags: [bucket quality, threshold, adaptive error, presets, basic mode, automatic sampling]
applies_to: Redshift 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=j6cD3MhcsXM, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
Higher quality presets lower the threshold and cut noise at a time cost [00:08-00:32]. Basic mode uses Automatic Sampling by default. Example times were on an M3 Max 128 GB with bucket size 512 and are not in the captions [01:04].

Ledger agrees: §2 "Basic quality presets map to threshold".

**Use it:** The advisor can name the preset and the threshold it maps to, with times from a scene test.
