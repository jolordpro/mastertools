---
id: gpu-cloud-siggraph-2016-panel-two-ways-to-use-cloud-service-black-box-or-network-extension
title: Panel: cloud is used either as a service with an API (Conductor, Zync) or as a virtual extension of the studio network; big studios keep on-prem and use raw cloud parts
domain: gpu-cloud
tags: [managed service, network extension, zync, conductor, azure, google cloud, pipeline, siggraph 2016, deep-read]
applies_to: cloud rendering architectures, 2016
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Bailey describes two models: a service (you hand over data, an API runs the computation, you get results back) and the cloud as an extension of your network, which works only with plenty of bandwidth and does not translate to the service model [19:59-20:29]. Many pipelines assume centralised live data, which suits the second model [20:29]. Prives says smaller studios with simple pipelines suit a managed service, while large studios with ingrained pipelines use the cloud's core compute, storage and network, and he expects big studios to keep on-prem and extend into cloud for years [43:24-44:25]. Bailey's tip, passed on from Shotgun: build for what people are used to first, then show them the new way [42:21].

**Use it:** for a render platform aimed at freelancers and small studios, the service model (submit, render, download) is the fit; keep hooks so a bigger studio can use the pieces.
