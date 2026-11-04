---
id: ai-models-synthetic-data-infinigen-blenderproc-kubric
title: Synthetic pair generators: Infinigen (BSD), BlenderProc and Kubric produce varied Blender scenes, but not Redshift truth
domain: ai-models
tags: [infinigen, blenderproc, kubric, synthetic data, blender, lighting pairs, calibration]
applies_to: 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/princeton-vl/infinigen/wiki, https://arxiv.org/abs/2406.11824, https://arxiv.org/pdf/2203.03570, src:research-verticals]
feeds: [PLAN 4.3, PLAN 1.7]
conflicts: none
---
Infinigen Indoors makes rooms with free ground truth. Kubric (Google) scales over thousands of machines; neither it nor BlenderProc has a built-in lighting-pair feature, so one is scripted. Kubric licence Apache, BlenderProc GPL (both unverified).

**Use it:** use for volume, keep a small Redshift calibration set of our own.
