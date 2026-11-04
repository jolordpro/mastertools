---
id: redshift-secondary-gi-ipc-default
title: The secondary GI engine defaults to Irradiance Point Cloud, and volumes force Brute Force when a point-based engine is used
domain: redshift
tags: [secondary gi, irradiance point cloud, volumes, brute force, gi engine]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Global+Illumination+-+Advanced.html.md, src:research-agency-pipelines, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
Irradiance Point Cloud is the default secondary engine. Whenever a point-based engine is on, volumes are forced to Brute Force.
The ledger's GI rows cover the trade-offs between the engines (section 6).

**Use it:** expect volumes to cost more than the GI settings suggest when a point-based engine is selected.
Transcript support: IPC fires a point per 16-pixel screen radius and interpolates; flicker fix is retrace threshold 2-3. (https://www.youtube.com/watch?v=L4riSkE7FwA [33:11])
