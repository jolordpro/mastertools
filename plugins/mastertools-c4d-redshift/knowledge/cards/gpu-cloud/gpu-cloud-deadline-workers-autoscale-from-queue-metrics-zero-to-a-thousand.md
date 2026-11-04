---
id: gpu-cloud-deadline-workers-autoscale-from-queue-metrics-zero-to-a-thousand
title: Deadline workers can autoscale from queue metrics in containers: about 20 seconds to start, zero to 1,000 in a minute (CoreWeave, 2021 and 2022)
domain: gpu-cloud
tags: [deadline, autoscale, keda, prometheus, kubernetes, render workers, coreweave, spire, deep-read]
applies_to: Deadline on Kubernetes (CoreWeave managed), 2021-2022
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=me25mlhgERI, https://www.youtube.com/watch?v=aJTLc7qQ1G0, src:yt-transcripts]
feeds: []
conflicts: none
---
2021 talk: Deadline runs natively in containers on bare metal; Prometheus metrics scale the render pods by what software the queue needs; a render pod starts in about 20 seconds and the speaker says a thousand GPUs can turn a two-day local render into five minutes [07:27-07:57, CW].
2022 talk (Spire Animation): the managed Deadline offering uses KEDA (captioned 'keita') to autoscale workers; submit a job, metrics are pulled, workers appear; zero to 1,000 workers within a minute [22:01-23:04, SP]. Unreal's Movie Render Queue was the job type Spire planned to run this way [23:04, SP].
Both are the vendor describing its own managed service.

**Use it:** when judging any farm, ask what triggers scale-up (queue depth), what the floor is (zero) and the start time per worker; those three numbers decide whether a Sunday-night surge is feasible.
