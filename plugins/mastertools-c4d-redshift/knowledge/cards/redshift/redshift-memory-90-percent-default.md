---
id: redshift-memory-90-percent-default
title: Redshift uses 90 percent of free GPU memory by default; lower it to 70-80 if other GPU apps run
domain: redshift
tags: [memory, gpu memory, 90 percent, automatic memory management, instability]
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
Automatic memory management is on by default and should stay on. 90% of free GPU memory is the default; going above it risks instability. Memory is released after 10 seconds without render activity.
The same page is inconsistent on some defaults, so check values in the app.

**Use it:** if a Mac or desktop shares its GPU with other apps, suggest 70-80% instead of raising the cap.
