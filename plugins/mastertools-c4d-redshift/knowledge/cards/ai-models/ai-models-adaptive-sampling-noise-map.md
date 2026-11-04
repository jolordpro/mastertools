---
id: ai-models-adaptive-sampling-noise-map
title: Learned adaptive sampling: a net predicts a per-pixel sample map from a 1 spp pass, and 4 spp adaptive matched 6 spp uniform
domain: ai-models
tags: [adaptive sampling, deep adaptive sampling, noise map, denoise, kuznetsov, spp]
applies_to: 2018, 2026 follow-up
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://cseweb.ucsd.edu/~viscomp/projects/dasr/, https://arxiv.org/html/2602.08642v1, src:research-verticals]
feeds: [estimator]
conflicts: none
---
Kuznetsov 2018; a 2026 paper (arXiv 2602.08642) goes below 1 spp with code promised on acceptance. A cheap noise map from a low draft shows where samples go and should predict final cost better than scene counts alone.

**Use it:** candidate feature for the estimator.
