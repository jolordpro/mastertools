---
id: redshift-deep-exr-requirements
title: Redshift deep output needs Multi-Part EXR, a Main AOV on Direct Output and Deep Output switched on
domain: redshift
tags: [deep exr, multi-part exr, direct output, deep output, comp, aov, deep, exr, redshift, multi-part, objectid, z threshold]
applies_to: Redshift 2026-2027
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/en-us/Content/html/EXR+Topics.html, src:research-vfx-pipelines, https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=pKfKsUYpk4w]
feeds: [comp-fix planner]
conflicts: none
---
Seen only as a search summary because the Maxon page is over 600,000 characters. Re-read it before building deep output into a workflow.
Merged from `comp-deep-exr-redshift`: Merge modes: Z, ObjectID, MeshID. Raising the Z threshold from 0.01 to 0.1 cut one pixel from 218 to 37 samples. Overlapping deep elements can artefact. Search summary only; the Maxon page was too large to read fully.

**Use it:** do not offer deep output as a comp option until those three settings can be verified in a scene.
Transcript support: multipart EXR plus Direct Output is how per-AOV compression is set (https://www.youtube.com/watch?v=IcLiz8e8ffc [52:17])
