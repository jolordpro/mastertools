---
id: gpu-cloud-siggraph-2016-panel-file-paths-as-database-cost-85-percent-of-one-storage-budget
title: Phil Peterson: in some multi-petabyte studios 85% of storage infrastructure cost went to looking up paths rather than reading and writing data
domain: gpu-cloud
tags: [phil peterson, shotgun, object storage, file paths, nfs, storage cost, metadata, siggraph 2016, deep-read]
applies_to: VFX storage, 2016
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
The panel wants software to refer to assets by something other than a disk path so cloud object storage can be first class [51:43-52:45]. Peterson, a Shotgun architect, says Shotgun stores its media in an object store, and that in past consulting he saw studios with multi-petabyte storage where about 85% of the infrastructure cost went to path lookups instead of data reads and writes [53:15]. He frames it as a generalisation, not every studio, and says it does not scale [53:46]. Kevin Bailey adds that most DCCs cannot yet say what they depend on, a gap for any service that must know which files a scene needs [21:02].

**Use it:** a scene check that lists every external file path (textures, caches, HDRIs) is the cloud-ready version of this problem; absolute and unlisted paths are the failure to catch.
