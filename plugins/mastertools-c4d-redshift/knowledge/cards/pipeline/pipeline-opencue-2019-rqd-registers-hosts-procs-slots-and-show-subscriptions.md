---
id: pipeline-opencue-2019-rqd-registers-hosts-procs-slots-and-show-subscriptions
title: OpenCue (2019): render nodes run RQD that registers with the Cuebot, hosts are split into 'procs' work slots, and shows subscribe to allocations of hosts for fair share
domain: pipeline
tags: [opencue, cuebot, rqd, procs, allocation, subscription, fair share, bin packing, host report, siggraph 2019, deep-read]
applies_to: OpenCue 2019
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
The RQD daemon on each render node phones home to the Cuebot server and is then registered; on the same network nothing else is needed [20:01]. The host report lists cores, RAM, local and scratch storage and GPUs, sent about every 30 seconds with a faster fallback cycle (speaker unsure of the exact numbers) [32:44-33:45]. The Cuebot can break a host into slots (procs, a work slot, not a processor) and bin-packs jobs into them [35:47-36:22]. For fair share, hosts sit in allocations (buckets) and shows subscribe to several; one flat pool shared by priority, or reserved pools for quick jobs, are both configurable [36:56-37:29]. The scheduling loop runs constantly; thousands of tasks scheduled within a few seconds, with 6,000 tasks in about 20 seconds [34:15-34:46].

**Use it:** the same words (host, slot, allocation, subscription) appear in any shared farm; useful when reading farm docs and when sizing how many frames a node takes at once.
