---
id: redshift-fireflies-filter-size
title: Fireflies that will not clean up can be reduced by lowering the Unified Sampling filter size
domain: redshift
tags: [fireflies, filter size, max subsample intensity, clamp, unified sampling]
applies_to: Redshift GPU
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=kwFwyzjXsdM]
feeds: [redshift, coach]
conflicts: ledger
---
The trainer says shrinking the filter size resolves stubborn fireflies [31:36, 1:03:38]. She also links Max Subsample Intensity to clamping secondary and GI rays, but the transcript is muddled on which ray types.

Ledger disagrees: §7 says Max Subsample Intensity limits each individual sample; secondary and GI ray hot spots belong to Max Secondary Ray Intensity, so the card's link to secondary and GI rays is off. Trust the ledger until a test settles it.

**Use it:** advisor suggests smaller filter size and max-subsample clamp for fireflies after raising samples; verify the effect by Show Samples on the offending pixels.
Transcript support: clamping Max Subsample / Secondary Ray Intensity from 4 to 1 removed hot spots but darkened the image; ledger section 7 warns about DOF bokeh (https://www.youtube.com/watch?v=kwFwyzjXsdM [11:09-12:12])
