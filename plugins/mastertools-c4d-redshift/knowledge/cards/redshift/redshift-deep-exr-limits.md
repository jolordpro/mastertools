---
id: redshift-deep-exr-limits
title: Redshift deep output carries only beauty, depth and object ID, and raising the Z merge threshold from 0.01 to 0.1 cut one pixel's samples from 218 to 37
domain: redshift
tags: [deep exr, deep output, merge threshold, z, object id, file size]
applies_to: Redshift 2026-2027
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/en-us/Content/html/EXR+Topics.html, src:research-vfx-pipelines]
feeds: [comp-fix planner]
conflicts: none
---
Other AOVs are disabled in deep mode. Merge modes are Z, ObjectID and MeshID. Overlapping deep elements can show artifacts. The 218 to 37 figure is one example pixel in the docs, via a search summary.

**Use it:** expect deep to answer layer-redo questions, not general AOV needs.
