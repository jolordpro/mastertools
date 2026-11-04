---
id: pipeline-vast-data-size-tiers-for-studios-100-render-servers-1000-and-3000
title: A storage vendor's sizing tiers for VFX studios, small ~100 render servers and 80-150 TB, medium ~1,000 servers and 250-750 TB, large ~3,000 servers and over 1 PB
domain: pipeline
tags: [vast-data, storage, studio-size, render-farm, joe-cup-of-joe, howard-marks, pipeline, deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=lCr3vIKUpwo, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Host Joe (A Cup Of Joe VFX) sets three example studios for his storage series, in his words and not Vast's [24:25-25:57]: small, 50 to 100 people, a couple of projects, about 100 render servers, 80 to 150 TB; medium, roughly 250 to 500 people, 2 to 4 projects, about 1,000 render servers and 50,000 cores, 250 to 750 TB (often under a petabyte excluding tape); large, 500 to 1,000 artists, 5+ projects, about 3,000 render servers and 200,000+ cores, usually over a petabyte. Studios drift upward through tiers, so storage should be planned for the next two or three years to avoid a forklift migration mid-growth. Vast's Howard Marks adds that his entry point is one 600 TB usable building block and that a studio staying under about 200 TB for three years is probably not a fit [26:27-27:29] (vendor's view). Recorded 2022.

**Use it:** use these tiers as ballpark checks on farm-to-storage ratios (from the tiers: about 0.8-1.5 TB per render server for small, 0.25-0.75 for medium; our arithmetic); not Redshift-specific.
