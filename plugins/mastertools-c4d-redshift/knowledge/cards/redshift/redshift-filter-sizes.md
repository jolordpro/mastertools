---
id: redshift-filter-sizes
title: Redshift's default Gauss filter works at size 2-3; Mitchell needs 3-5, and a sharper filter needs a larger size
domain: redshift
tags: [filter, gauss, mitchell, antialiasing, sharpness, fireflies]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Sampling+-+Advanced.html.md, src:research-agency-pipelines, src:research-youtube, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=le17-h6tUD0, https://www.youtube.com/watch?v=aheTC8N2xQg]
feeds: [advisor]
conflicts: none
---
Gauss is the default, size 2-3. Mitchell is typically 3-5. Sharper filters need a larger size to avoid ringing.
A Maxon stream also lists "fixing fireflies, filter size" as a chapter, so filter size is a known firefly lever (chapter title only).
The ledger lists filter behaviour and the Gaussian-for-animation guidance as an open hole (section 11).

**Use it:** start from Gauss 2-3 for animation and test Mitchell on stills only.
Transcript support: Reducing filter size is offered as a firefly fix. (https://www.youtube.com/watch?v=L4riSkE7FwA [1:03:38])
Transcript support: Lanczos with filter size 6 used for a crunchier, sharper look (https://www.youtube.com/watch?v=le17-h6tUD0 [34:17])
Transcript support: Chad recalls a Lanczos size-4 look being replaced by Gauss when denoise is on; unverified. (https://www.youtube.com/watch?v=aheTC8N2xQg [1:11:54])
