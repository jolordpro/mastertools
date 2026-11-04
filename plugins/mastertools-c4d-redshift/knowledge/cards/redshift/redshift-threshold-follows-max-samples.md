---
id: redshift-threshold-follows-max-samples
title: When raising Max Samples, re-derive the threshold in the same step
domain: redshift
tags: [threshold, max samples, unified sampling, tuning, elly wade]
applies_to: Redshift 2024+
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:research-youtube, https://www.youtube.com/watch?v=j6cD3MhcsXM, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
The Maxon stream chapter "adjusting threshold based on high max" (28:29) points at changing the two together. Chapter title only, no numbers heard.
The ledger holds the actual threshold bands (section 2).

**Use it:** the advisor changes max and threshold as one move and quotes the ledger bands.
Transcript support: Bucket Quality presets only change the adaptive error threshold; Custom appears when a value is typed. (https://www.youtube.com/watch?v=j6cD3MhcsXM [00:32])
