---
id: gpu-cloud-siggraph-2016-panel-big-file-transfer-parallel-tcp-threads-beat-pricey-udp-tools
title: Panel: Aspera-style UDP transfer is costly and open-source UDP was fragile for Conductor, so it splits uploads over about 16 parallel TCP threads
domain: gpu-cloud
tags: [aspera, udp, tcp, file transfer, upload, kevin bailey, conductor, siggraph 2016, deep-read]
applies_to: upload to cloud storage, 2016
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Bailey says Atomic Fiction keeps an expensive Aspera server for client and subcontractor transfers; open-source UDP options were tried for Conductor and caused problems, so uploads spawn about 16 parallel threads (his example number) to fill the pipe regardless of distance [55:55-56:56]. He says the commercial tools need to come down in price to be used daily [56:26]. An audience member from a render-farm company asked when TCP/HTTP becomes obsolete for this [54:50].

**Use it:** if the platform handles multi-GB uploads, parallel chunked HTTP uploads are the baseline to meet; UDP products are optional extras.
