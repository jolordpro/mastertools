---
id: redshift-gernge-production-preset-threshold-0007-overrides-2048-brute-force-gi-1024
title: One artist's near-all-scenes Redshift preset: automatic sampling off, threshold 0.007, overrides pre-set to 2048 and used selectively, brute-force GI at 1024
domain: redshift
tags: [redshift preset, threshold, sampling overrides, brute force gi, irradiance point cloud, render settings, deep-read]
applies_to: Redshift in Cinema 4D (2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=s5ElfI1q8uU, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Gernge [00:32-02:38]. Automatic sampling unchecked so threshold, min and max appear. Threshold 0.007 is close to production; he suggests testing/drafts much higher. Sampling overrides (reflection, refraction, volume etc.) pre-filled with 2048 and only the relevant ones ticked per scene: volume for fog or VDB, refraction for glass, reflection for speculars. Warning: doubling an override does not clean that effect unless Max Samples is also raised; they are a balance [01:36-02:07]. GI: primary and secondary both brute force, 1024 samples; Irradiance Point Cloud may help interiors. Bucket size: larger is faster but uses more memory; reduce on low-VRAM cards [03:10-03:41]. Save with right-click Save Preset and load from the same menu. Legacy material processing and texture projections kept because he finds the newer ones buggy.

**Use it:** Compare with the ledger bands (broadcast final 0.003-0.007). The 2048 overrides are one person's practice, not a vendor default.
