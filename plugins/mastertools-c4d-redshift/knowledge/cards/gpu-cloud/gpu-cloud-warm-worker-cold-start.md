---
id: gpu-cloud-warm-worker-cold-start
title: A 1-5 s mockup needs a warm GPU worker: Modal snapshots cut ComfyUI start to under 3 s, RunPod's sub-200 ms is for warm workers only
domain: gpu-cloud
tags: [cold start, warm worker, modal, runpod, flashboot, comfyui, snapshot, mockup]
applies_to: 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://modal.com/blog/comfyui-mem-snapshots, https://www.runpod.io/blog/serverless-gpu-cold-starts-flashboot, src:research-gaps-deep]
feeds: [PLAN 1.6 mockups]
conflicts: none
---
Modal CPU memory snapshots cut ComfyUI starts from 10-15 s to under 3 s, but checkpoint loading still happens on the first workflow run; GPU snapshots are experimental and sub-second claims are marketing.
RunPod FlashBoot claims sub-200 ms on active endpoints; warm workers can be evicted under load and then a full cold start returns. Replicate boot times are not published.
Cold start is 3 s at best and about 40 s at worst for 8 GB of weights (researcher's reading).

**Use it:** keep one warm GPU per active session and release it when idle.
