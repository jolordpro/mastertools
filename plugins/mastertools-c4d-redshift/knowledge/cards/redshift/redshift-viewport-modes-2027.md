---
id: redshift-viewport-modes-2027
title: C4D 2027's viewport offers Live plus Production Progressive and Bucket IPR; Bucket previews AOVs and SSS
domain: redshift
tags: [viewport, ipr, bucket, progressive, live, aov, sss, preview]
applies_to: C4D 2027 / Redshift 2027
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Redshift_Viewport_Rendering.html.md, src:research-gaps-deep, https://www.youtube.com/watch?v=G43QVR1TqXg]
feeds: [PLAN 1.3 draft render]
conflicts: none
---
Besides Live, the 2027 viewport can run Production-based Progressive and Bucket IPR. Bucket is the mode that previews AOVs and SSS, which Live cannot.
Progressive mode's pass behaviour is in the ledger (section 4).

**Use it:** when a human needs an AOV or SSS preview, point at Bucket IPR; the machine draft stays a low-res Production render.
