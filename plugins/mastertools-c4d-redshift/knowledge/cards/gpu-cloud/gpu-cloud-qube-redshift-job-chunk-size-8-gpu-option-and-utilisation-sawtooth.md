---
id: gpu-cloud-qube-redshift-job-chunk-size-8-gpu-option-and-utilisation-sawtooth
title: Qube Redshift job: 320 frames in chunks of 8 on 40 nodes; expert mode sets which GPUs Redshift uses, and GPU load dips at each frame change
domain: gpu-cloud
tags: [qube, chunk size, redshift, gpu selection, job submit, expert mode, gpu utilization, azure, deep-read]
applies_to: Qube 7 + Redshift (2018 upload, PipelineFX)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=p50NXgsMGiw, src:yt-transcripts]
feeds: [estimator, pipeline]
conflicts: none
---
Resubmit a single-frame job as a 320-frame sequence, chunk size 8 so each worker takes eight frames before asking the supervisor for more [04:20]. The worker count field is raised (the caption reads 42) to tell the supervisor how many workers join [04:20].
Expert mode shows Redshift options: by default it uses all GPUs on the box, or set a specific GPU such as GPU 0 [04:51]. Sanity check: watch GPU utilisation on a node; usage drops at the end of each frame and rises again, so eight dips per chunk appears [07:27-08:00]. Frames complete out of order [08:00].
The run on 40 nodes finished with no time reported in the video [08:31-09:08].

**Use it:** chunk size trades supervisor chatter against load balance; ask for per-frame time before choosing it.
