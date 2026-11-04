---
id: redshift-dof-tuning-order
title: Tune the rest of the scene with DOF and motion blur off, then switch them on and raise samples
domain: redshift
tags: [depth of field, dof, motion blur, workflow, samples, tuning order]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Sampling+-+Advanced.html.md, src:research-agency-pipelines, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=KnfiJy2ND2o]
feeds: [advisor]
conflicts: none
---
DOF and motion blur raise the sample demand, so settle GI, lighting and materials without them first.
The ledger already has the numbers: 8-16 min samples with DOF or blur, 256+ max for strong effects (section 2).

**Use it:** advise the order in the coach, and quote the ledger numbers for the final step.
Transcript support: Heavy DOF or motion blur needs max samples raised to 512-1024. (https://www.youtube.com/watch?v=L4riSkE7FwA [22:42])
Transcript support: Displacement, motion blur, DOF, caustics and refractions are the costly features. (https://www.youtube.com/watch?v=KnfiJy2ND2o [1:05:00])
