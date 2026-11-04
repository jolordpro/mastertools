---
id: redshift-live-no-aovs
title: Redshift Live can't render AOVs, SSS, motion blur, volumes or light linking
domain: redshift
tags: [redshift live, ipr, draft, aov, preview]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/Redshift+Live.html, https://digitalproduction.com/2026/10/19/redshift-2027-memory-fur-live-rendering/, https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=FmaKhqSITFQ, https://www.youtube.com/watch?v=CXx75LxGxOw]
feeds: [PLAN 1.3 draft render, OPEN-STACK stage 3]
conflicts: none (ledger §5 checked 2026-10-30)
---
Redshift Live (formerly RT) is a viewport tool. It has no AOVs, SSS, motion blur, volumes or light linking.
The ledger dates refraction and transparent shadows in Live to 2026.8; press lists area-light spread and ray-traced DOF with 2027.0. Whether it now allows AOVs is unconfirmed: read the 2027 AOV notes or test in the 0A spike.

**Use it:** a draft that feeds the brain must be a low-res Production render, not Live.
Transcript support: Live still lacks refraction and portal lights (2026.8); DOF and post effects added. (https://www.youtube.com/watch?v=KoL7OAANlJ8 [1:05:07])
Transcript support: demo says not everything is transferred to Live yet; 15 s vs 5.5 min example (https://www.youtube.com/watch?v=FmaKhqSITFQ [52:08])
Transcript support: Progressive render view shows some AOVs wrong; use bucket rendering to check them. (https://www.youtube.com/watch?v=CXx75LxGxOw [20:13])
