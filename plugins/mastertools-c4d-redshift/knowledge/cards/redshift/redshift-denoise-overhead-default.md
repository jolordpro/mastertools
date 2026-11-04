---
id: redshift-denoise-overhead-default
title: Denoise overhead defaults to 10 percent in bucket mode and 100 percent in progressive; 0 denoises once at the end
domain: redshift
tags: [denoise overhead, bucket, progressive, denoise, large frames]
applies_to: Redshift 2026-2027
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Denoising.html.md, src:research-agency-pipelines, https://www.youtube.com/watch?v=G43QVR1TqXg, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
The overhead setting controls how much of the render budget goes to denoising passes. Zero runs a single denoise at the end, which suits very large frames.
Defaults are 10% for bucket and 100% for progressive.

**Use it:** for a big hero still, suggest 0 and check the result at 100% zoom.
Transcript support: Overhead 0 halved a 12 s render to 6 s; RF [05:46] says the same. (https://www.youtube.com/watch?v=G43QVR1TqXg [05:42])
