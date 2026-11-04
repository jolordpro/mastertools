---
id: redshift-houdini-volume-needs-light-volume-contribution-scale-and-samples
title: Redshift fog or VDB volumes render as black blocks until lights have Volume Contribution Scale above 0 and enough volume samples
domain: redshift
tags: [volumes, fog, vdb, volume contribution scale, light volume samples, houdini, redshift, deep-read]
applies_to: Redshift for Houdini 2.5.24 (Maxon Redshift channel); concept applies to C4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kwFwyzjXsdM, src:yt-transcripts, https://www.youtube.com/watch?v=vnHKQmvKYH8]
feeds: [redshift, CHECKS]
conflicts: none
---
Maxon's Houdini tutorial [13:18-15:49]: a fog volume showed as dark blocks because the lights' Volume Contribution Scale was 0; set to 1 on both area lights and the noise turned pink. It stayed grainy until each light's volume samples went to 128. He says it is a mistake he often makes. Also in the volume material: set the volume geometry type to VDB/Houdini primitive in the object settings. In C4D the same two controls live on the light (volume contribution) and in the sampling overrides (volume samples).

**Use it:** Volume checklist item: light volume contribution above zero and volume samples raised, before touching Unified Sampling.
Transcript support: C4D side: light Volume tab contribution scale defaults to 0 and a Redshift Environment object is required; typical values 0.01 to 0.1. (https://www.youtube.com/watch?v=vnHKQmvKYH8 [01:39])
