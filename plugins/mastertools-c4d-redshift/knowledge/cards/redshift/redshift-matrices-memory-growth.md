---
id: redshift-matrices-memory-growth
title: Per-object matrices for instancing and motion blur live in GPU memory and grow with object count and blur steps
domain: redshift
tags: [matrices, instancing, motion blur, memory, cloner, gpu memory]
applies_to: Redshift 2027 help
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Feedback+Display.html, src:research-production-pipelines, https://www.youtube.com/watch?v=cE-Bbdspu_8]
feeds: [CHECKS memory]
conflicts: none
---
Matrices cover instancing, motion blur and texture transforms. They become large with huge object counts or many blur steps.

**Use it:** when matrices show large in the log, look at instance count times blur steps.
