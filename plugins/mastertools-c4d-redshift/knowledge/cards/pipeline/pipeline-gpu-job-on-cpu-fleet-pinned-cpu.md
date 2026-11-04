---
id: pipeline-gpu-job-on-cpu-fleet-pinned-cpu
title: A render job making no progress with 100% CPU use may be a GPU-optimised job on a CPU-only fleet
domain: pipeline
tags: [deadline cloud, fleet, gpu, cpu, no progress, pinned cpu, blender, troubleshooting]
applies_to: AWS Deadline Cloud (Apr 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=zz10CeybNeQ, src:yt-transcripts]
feeds: [preflight, why-did-it-fail]
conflicts: none
---
[01:38] The Assistant, after a 10-step workflow covering job config, step dependencies and CloudWatch task and worker logs, reported the fleet only had CPU instances while the job suited GPU; CPU pinned at 100% was the sign. Moving to GPU instances and resubmitting fixed it.

**Use it:** preflight: compare renderer and fleet type before submit.
