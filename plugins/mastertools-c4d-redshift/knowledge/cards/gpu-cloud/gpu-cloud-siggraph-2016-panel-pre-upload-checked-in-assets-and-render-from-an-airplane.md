---
id: gpu-cloud-siggraph-2016-panel-pre-upload-checked-in-assets-and-render-from-an-airplane
title: Kevin Bailey: mark important assets in the tracker so they upload as soon as they are checked in, then a Star Trek Beyond render submitted from a plane returned in about 10 minutes
domain: gpu-cloud
tags: [pre upload, asset sync, shotgun, conductor, atomic fiction, star trek beyond, data transfer, siggraph 2016, deep-read]
applies_to: cloud rendering with a tracker, 2016
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
Gerald Chu's answer to the transfer bottleneck is not to move data at all: put workstations, rendering and sharing inside the same vendor so there is nothing to ship [57:28]. Bailey adds the interim method: know which data matters, mark it in the production tracker (Atomic Fiction used Shotgun) and push it to the cloud when it is checked in, before an artist submits [58:31]. Proof: he submitted a Star Trek Beyond render from a flight from Montreal and had frames back in about 10 minutes [59:01].

**Use it:** the platform's 'pre-upload' idea matches this: sync textures, caches and HDRIs as soon as the scene saves, so submit sends only the scene file. See gpu-cloud-zync-2016-upload-only-job-syncs-assets-ahead-so-the-render-submit-sends-one-scene-file.
