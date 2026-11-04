---
id: redshift-vram-out-of-core-limits
title: Out-of-core slows a render, and irradiance caches and volumes cannot go out-of-core and can error
domain: redshift
tags: [vram, out of core, memory, irradiance cache, volumes, gpu memory log]
applies_to: Redshift 2026-2027
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://support.maxon.net/hc/en-us/articles/22085399180060-Managing-VRAM-issues-with-Redshift, src:research-agency-pipelines, src:research-gaps-deep, https://help.maxon.net/r3d/cinema/en-us/Content/html/System+-+Advanced.html]
feeds: [CHECKS memory]
conflicts: none
---
The Redshift log has a GPU memory section: if the amount requested exceeds what is available, the task ran out-of-core. Caches and volumes must fit in VRAM or the render errors.
Cut memory with proxies, smaller textures and less displacement. The Maxon page itself returned 403, so this rests on a search snippet.

**Use it:** read the memory section of the draft log and flag out-of-core before a farm run.
Maxon check (2026-10-31): Maxon docs: volumes are not handled by the out-of-core system; baked displacement textures cannot go out of core. Irradiance caches are not named. Out-of-core use shows in the log's GPU Memory figures and the Render View feedback display. (https://help.maxon.net/r3d/cinema/en-us/Content/html/System+-+Advanced.html)
