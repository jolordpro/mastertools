---
id: c4d-take-token-output-paths
title: Without a $take token in output paths, takes overwrite each other
domain: c4d
tags: [takes, output path, $take, overwrite, aov path, farm]
applies_to: C4D with Redshift
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://irendering.net/cinema-4d-redshift-takes-render-farm/, src:research-agency-pipelines, src:research-gaps-deep, https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts, https://www.youtube.com/watch?v=ZAom6DvSi3s]
feeds: [take-aware preflight]
conflicts: none
---
Vendor guidance (iRender, 2026-10-19). Redshift Direct AOV paths hard-coded to one folder overwrite each other too.

**Use it:** warn when more than one take renders to a path without a take token.
Transcript support: 2027 adds Take Parent and Take Hierarchy tokens so variants get distinct names (https://www.youtube.com/watch?v=FmaKhqSITFQ [1:05:19])
Transcript support: Save path can use the take name. (https://www.youtube.com/watch?v=ZAom6DvSi3s [30:47])
