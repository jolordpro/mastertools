---
id: redshift-volume-object-vdb-sequence-and-matching-scatter-absorption-0-01
title: Redshift Volume object plays VDB sequences; defaults of 1 for scatter and absorption look dense and dark, and about 0.01 each, kept equal, gave a soft cloud
domain: redshift
tags: [vdb, volume object, vdb sequence, scatter coefficient, absorption coefficient, volume trace depth, cloud, renderbaron, deep-read]
applies_to: C4D + Redshift (2023 upload, renderbaron)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_5a-cWSjB7U, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Redshift menu > Redshift Volume links a VDB file or sequence by path; points preview with max points and a prune threshold, and Detect Frames reads the animation with a start offset [00:16-01:15]. Scale it in object mode, not with the model tools [01:15].
A volume material (create > materials > volume) holds a Redshift Volume node in the output volume slot [01:26-01:57]. Scatter acts like diffuse, absorption like transmission; both start at 1, which is dense and dark [02:15-02:47].
Cloud test: drop absorption to about 0.01 and scatter to about 0.01; he says the two should be roughly equal [02:47-03:17]. Lower shadow density on the Advanced tab. Volume trace depth (render settings > globals > trace depth) adds bounce but heavily raises time; 1 is usually enough [03:17-03:50].

**Use it:** cloud starter: both coefficients near 0.01, trace depth 1, then tune. Flag volume trace depth above 1 as a render-time risk.
