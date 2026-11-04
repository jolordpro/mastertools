---
id: redshift-ic-settings-numbers
title: Irradiance Cache working numbers: 500-1000 rays typical, 2000-4000 for architectural interiors
domain: redshift
tags: [irradiance cache, gi, rays, min rate, max rate, min detail, 4k, draft]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Global+Illumination+-+Advanced.html.md, https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/The+Irradiance+Cache+GI+Engine.html.md, src:research-agency-pipelines]
feeds: [advisor]
conflicts: none
---
Rays 500-1000 usually; 2000-4000 for architectural interiors. If splotchy, try adaptive error 0.005 or 0.001.
Draft: Max Rate -1, Min Detail 4-8. Final: Max Rate 0, Min Detail 0. Min Rate -4 or -5 for 4K.
Brute Force avoids all of this and stays flicker-free; the ledger covers when to prefer it (section 6).

**Use it:** only quote these when the user has chosen an Irradiance Cache primary; default animated glossy shots to Brute Force.
