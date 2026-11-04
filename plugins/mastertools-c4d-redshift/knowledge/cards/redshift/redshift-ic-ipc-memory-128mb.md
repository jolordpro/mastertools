---
id: redshift-ic-ipc-memory-128mb
title: Irradiance cache and point-cloud working memory defaults to 128 MB; raise to 256 or 512 only if a render errors
domain: redshift
tags: [irradiance cache, irradiance point cloud, memory, 128 mb, brute force]
applies_to: Redshift 2027 help
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Memory.html, src:research-production-pipelines]
feeds: [CHECKS memory]
conflicts: none
---
Raise the working memory in steps only after an error. If it still fails, the scene has too much micro-detail for the cache; try Brute Force GI.

**Use it:** treat a cache memory error as a GI-method question first, not a hardware one.
