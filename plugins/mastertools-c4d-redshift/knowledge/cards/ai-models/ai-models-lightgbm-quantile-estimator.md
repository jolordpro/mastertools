---
id: ai-models-lightgbm-quantile-estimator
title: LightGBM with quantile loss on scene card + settings + machine gives a render-time range instead of one guess
domain: ai-models
tags: [lightgbm, quantile, render time, estimator, regression, ledger, m1]
applies_to: proposal
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [src:research-verticals]
feeds: [estimator M1]
conflicts: none
---
Our own proposal, not sourced: gradient trees, MIT licence (unverified). The baseline to beat is Greyscalegorilla's Render Calculator, which only multiplies a typed per-frame time.

**Use it:** each render adds a row; score estimate against actual.
