---
id: redshift-sample-mode-heat-map-then-raise-threshold-and-widen-min-max
title: Use the bucket sample map: 256 samples in bright areas means the threshold is too tight, so raise it and widen min to max
domain: redshift
tags: [sampling, sample mode, adaptive threshold, min max samples, dome light samples, ledger-check, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream); values are his starting points
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [redshift, coach, estimator]
conflicts: none
---
Order he followed on a proxy crowd [15:09-22:56]: IPR 64 samples; bucket mode; Brute Force plus irradiance point cloud with 3 bounces; raise dome light samples by doubling until a crop is clean (1024); GI rays 512 because 16 was far too low. Unified sampling 1 and 1 looked crunchy, so he set 256 max and 16 min as a starting point [17:13].
Sample mode shows where Redshift spends samples: it put 256 almost everywhere bright, so he raised the adaptive error threshold and widened the min to max gap, which sped the frame up a lot; with the higher max he could then lower the dome light samples [21:22-22:56].
Depth of field needs no sample setting; it rides on unified sampling [20:21].

**Use it:** advisor: if a bucket sample map is mostly the maximum, suggest raising the threshold before raising samples. Check values against the Redshift ledger, which outranks this.
