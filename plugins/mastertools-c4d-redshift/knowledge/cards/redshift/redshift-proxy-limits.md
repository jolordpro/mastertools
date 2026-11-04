---
id: redshift-proxy-limits
title: Proxies cannot deform, animated proxies are heavy per-frame caches, and adaptive tessellation does not work with instancing
domain: redshift
tags: [proxy, animated proxy, adaptive tessellation, instancing, alembic, limits]
applies_to: Redshift 2027 help
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Proxies.html, src:research-production-pipelines]
feeds: [CHECKS memory]
conflicts: none
---
Only the whole proxy can move, rotate or scale. Animated proxies are per-frame caches and can be big. Cache sims to Alembic or VDB and reference the cache is community advice; Maxon has no VDB versus Alembic comparison.

**Use it:** flag animated proxies and large Alembics that exceed the shot's frame range.
