---
id: gpu-cloud-google-cloud-2018-preemptible-gpus-24-hour-cap-cpu-80-off-gpu-50-off
title: Google Cloud GPUs in 2018: preemptible VMs ran at most 24 hours and cost 80 percent less for CPU/memory and 50 percent less for the GPU
domain: gpu-cloud
tags: [google-cloud, preemptible, gpu, gce, checkpoint, cost, deep-read]
applies_to: Google Compute Engine, K80/P100/V100, webinar uploaded 2018-07
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=heDHOWmVMbU, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
The Google presenter says preemptible VMs are spare capacity: they last up to 24 hours and can be taken back, in exchange for CPU and memory about 80 percent off and GPUs about 50 percent off [26:28-27:30].
His advice: build the work to checkpoint so a replacement VM resumes where the last stopped [27:30-28:02].
On the demo screen switching one setting dropped the monthly price by about a thousand dollars [25:58-26:28].
One managed group needs identical VM shapes; mix dedicated and preemptible by using two groups, or an unmanaged group, or two node pools in Kubernetes [38:03-39:04]. 2018 figures, now historical.

**Use it:** for Redshift frame renders, frame-level retry is the checkpoint; the same trade (cheap, revocable, resubmit) applies to today's spot or preemptible GPUs.
