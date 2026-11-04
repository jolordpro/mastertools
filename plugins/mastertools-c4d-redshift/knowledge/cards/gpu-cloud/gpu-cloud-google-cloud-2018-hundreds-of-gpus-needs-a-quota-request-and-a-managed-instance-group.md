---
id: gpu-cloud-google-cloud-2018-hundreds-of-gpus-needs-a-quota-request-and-a-managed-instance-group
title: Google Cloud 2018: a new account has a small GPU quota; running 100 or 1,000 GPUs means filing a quota request and using a managed instance group of one template
domain: gpu-cloud
tags: [google-cloud, quota, instance-group, gpu, scale, deep-read]
applies_to: Google Compute Engine, webinar uploaded 2018-07
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=heDHOWmVMbU, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Steps from the Q&A: have an account, then request quota for the maximum number of GPUs you want, submitted online with an answer back soon; with a managed instance group built from one instance template you set the group size to your target [39:36-40:06].
Demo: set size to 1 to test the template, then edit to 1,000 and save; the cluster appears in minutes, GPU drivers and CUDA preinstalled [10:13-11:46].
GPUs are passed straight through to the VM, so he claims bare-metal performance [20:13-20:44].

**Use it:** ask for cloud GPU quota before the project starts, because approval lag, not the price, can be what holds a deadline up.
