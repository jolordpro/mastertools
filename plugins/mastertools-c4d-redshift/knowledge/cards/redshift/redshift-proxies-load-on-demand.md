---
id: redshift-proxies-load-on-demand
title: Redshift proxies load on demand and one proxy plus instances beats separate copies
domain: redshift
tags: [proxy, instances, memory, on demand, bounding box, scene weight]
applies_to: Redshift 2027 help
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Proxies.html, https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Intro+to+Proxies.html, src:research-production-pipelines, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=MuVzbVhMUvI]
feeds: [CHECKS memory]
conflicts: none
---
A proxy loads only when a ray hits its bounding box. Many copies of the same mesh cost memory and speed that one proxy with instances does not.

**Use it:** preflight counts identical meshes that are neither proxies nor instances and suggests converting.
Transcript support: Use instances and proxies over many objects. (https://www.youtube.com/watch?v=L4riSkE7FwA [07:32])
Transcript support: Practical proof: 1250 proxy instances in a cloner stayed interactive in 2017. (https://www.youtube.com/watch?v=MuVzbVhMUvI [09:19-12:32])
