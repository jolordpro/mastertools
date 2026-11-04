---
id: redshift-manual-sampling-start-values
title: Manual sampling start point from the Maxon trainer: min 16, max 128 to 512, threshold from 0.1 down to 0.01
domain: redshift
tags: [unified sampling, min samples, max samples, threshold, manual sampling, bucket quality, starting point]
applies_to: Redshift GPU (any DCC)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=LcxjkHFS-2k, https://www.youtube.com/watch?v=x_xdQrCJsCM]
feeds: [redshift, estimator, coach]
conflicts: none
---
Turn Automatic Sampling off to get the controls [15:53]. Min 16 covers most cases with the new standard material; start max at 128 [21:09]. Presets are shorthand for the threshold: 0.1 matches Low, 0.01 matches Medium [22:12, 28:58].
These samples drive primary rays only (anti-aliasing, depth of field, motion blur). With heavy DOF or blur, raise max to 512 or 1024 [22:42]. Lower threshold = more aggressive, so a bigger max wants a smaller threshold [28:26].
Use powers of two; the speaker says rays are fired in bundles of 32 (explanation unverified).

Ledger agrees: §2 "Basic quality presets map to threshold: Low 0.100 / Medium 0.010".

**Use it:** the estimator and the advisor use these as the baseline when proposing sample changes; the coach reads Low/Medium presets as 0.1/0.01 thresholds.
Transcript support: older method (2017): min 1 max 1 to locate noise source, then min 8 max 16; not the same start values (https://www.youtube.com/watch?v=LcxjkHFS-2k [24:23-31:42])
Transcript support: one creator's manual test: threshold 0.008, min 8 max 16 then 16/32; a 3090 test, low confidence. (https://www.youtube.com/watch?v=x_xdQrCJsCM [03:15-05:55])
