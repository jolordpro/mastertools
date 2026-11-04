---
id: comp-translucency-reflection-same-pattern
title: Translucency and reflection rebuild the same way (Filter times Raw), but plain reflection and refraction passes are enough 90-95% of the time
domain: comp
tags: [translucency, reflection filter, refraction, raw, aov, over-splitting]
applies_to: Redshift AOVs, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [AOV package, advisor]
conflicts: none
---
Translucency total is Trans Tint (filter) times Trans Lighting Raw plus GI Raw, added on top [37:18-38:20]. Reflection total is Reflection Filter times Reflection Raw [39:54]. He says he rarely needs raw and filter for reflection or refraction [13:51, 38:20], and only splits what he needs to change [38:52].

**Use it:** Default the AOV package to plain reflection and refraction; split only on request.
