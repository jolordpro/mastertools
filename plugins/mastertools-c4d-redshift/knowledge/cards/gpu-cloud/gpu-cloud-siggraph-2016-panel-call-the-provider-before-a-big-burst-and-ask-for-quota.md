---
id: gpu-cloud-siggraph-2016-panel-call-the-provider-before-a-big-burst-and-ask-for-quota
title: Panel: tell the cloud provider before bursting to 10,000+ cores; surprise spin-ups fail, and preemptible quotas are the easier route to very large counts
domain: gpu-cloud
tags: [burst, quota, cores, google cloud, microsoft azure, brennan chapman, moonbot, gerald chu, siggraph 2016, deep-read]
applies_to: AWS, Azure, Google Cloud in 2016
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Gerald Chu (Microsoft) says a provider will happily give 10,000 cores tomorrow if you call first, but not if you spin up without warning; he said not all customers can get 200,000 cores in one US region on a day's notice, and providers forecast but cannot cover everyone [31:25-35:04]. Brennan Chapman (Moonbot) says that three days before a deadline they asked Google for 10,000 cores and got a yes [33:29]. A Google compute engineer in the audience said preemptible quotas let people reach tens of thousands of cores because they cannot take capacity from others [38:42].
Scale reported that year: Atomic Fiction's earlier peak of 12,000 cores on The Walk, and over 40,000 cores for one customer by 2016 [14:40]. Bailey adds that many customers bursting at offset times will smooth the peaks over time [35:04].

**Use it:** note that cloud GPU capacity is not guaranteed: the platform needs a fallback provider and a quota check before a booked big render. Prices and quotas from 2016 are context only.
