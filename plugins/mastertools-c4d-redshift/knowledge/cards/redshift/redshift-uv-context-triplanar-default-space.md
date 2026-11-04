---
id: redshift-uv-context-triplanar-default-space
title: UV Context triplanar can default to Reference Object space and appear not to project; switch to Object or World
domain: redshift
tags: [triplanar, uv context, projection space, bug, default]
applies_to: Redshift 2026.x
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
On air, triplanar did nothing until the projection space was changed from Reference Object to Object (World should also work, but resize) [1:17:07-1:19:11]. Neither host was sure whether the default changed.

**Use it:** coach troubleshooting step when a triplanar looks missing.
