---
id: gpu-cloud-provider-reliability-notes
title: Marketplace GPU reliability: Vast has a 0-1 host score, Salad warns of interruptions, RunPod Secure quotes 99.5-99.95%
domain: gpu-cloud
tags: [reliability, vast, salad, runpod, uptime, interruptible, retry]
applies_to: 2026-10
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://docs.salad.com/container-engine/explanation/core-concepts/service-performance, https://www.spheron.network/blog/runpod-vs-vastai-2026/, src:research-gaps-deep]
feeds: [PLAN 5b]
conflicts: none
---
Vast: each host has a reliability score 0 to 1; one guide says filter above 0.95; no uptime guarantee. A rival's blog says unverified Vast hosts cost 20-40% more after restarts (weak).
RunPod Secure: sources quote 99.5-99.95% uptime; Community works like Vast. Salad says over 90% of consumer nodes are stable but cannot promise 100%; its data-center tier is the reliable one.
A Redshift frame of 3-9 min is restartable, so a retry is enough.

**Use it:** design the dispatcher to retry a lost frame instead of paying for a reliable tier.
