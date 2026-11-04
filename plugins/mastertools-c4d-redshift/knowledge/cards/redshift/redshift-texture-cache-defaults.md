---
id: redshift-texture-cache-defaults
title: Max CPU texture cache defaults to 4 GB; raise to 8 GB or more for texture-heavy scenes
domain: redshift
tags: [texture cache, cpu cache, gpu cache, textures, memory, feedback]
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
If the Feedback display shows textures uploaded climbing into hundreds of MB or GB, raise the GPU texture cache cap (256 MB first) and then the percentage. Ray reserved memory defaults to 0 (automatic).
The page contradicts itself on some texture cache percent and cap defaults, so check in the app.

**Use it:** read the texture upload figure from a draft log before changing cache sizes.
