---
id: redshift-texture-cache-vendor-budgets
title: A vendor suggests a 4-6 GB texture cache on 24 GB cards and 8-12 GB on 32 GB cards
domain: redshift
tags: [texture budget, texture cache, 24 gb, 32 gb, vram, irender]
applies_to: Redshift on 24-32 GB GPUs
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://irendering.net/redshift-render-farm-guide-2026-setting-texture-budgets-rstexbin-caching-and-eliminating-out-of-core-latency/, src:research-production-pipelines]
feeds: [CHECKS memory]
conflicts: none
---
iRender (a render farm, not Maxon) gives these budgets in a 2026 guide; seen only as a search summary. Treat as a starting point to test on a draft.

**Use it:** do not quote as Maxon guidance; use it only to seed a test.
