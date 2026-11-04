---
id: gpu-cloud-redshift-headless-on-marketplaces-unproven
title: No source shows Redshift running headless on Vast, RunPod or Salad
domain: gpu-cloud
tags: [redshift, headless, docker, vast, runpod, salad, spike, linux]
applies_to: 2026-10
status: U
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [src:research-gaps-deep]
feeds: [PLAN 0A spike, PLAN 5b]
conflicts: none
---
Docker-based hosts fit Linux: Vast (Docker and KVM VMs), RunPod (Docker, network volumes), Salad (containers only, free image pulls), TensorDock (Windows VMs shown in two case studies).
Nobody documents a Redshift licence, Linux driver and redshiftCmdLine frame on these. Absence of evidence only.
The researcher ranks the one-day spike (licence, driver, redshiftCmdLine, one frame) as the thing Phase 2 hangs on.

**Use it:** run the spike before any plan relies on marketplace GPUs for Redshift.
