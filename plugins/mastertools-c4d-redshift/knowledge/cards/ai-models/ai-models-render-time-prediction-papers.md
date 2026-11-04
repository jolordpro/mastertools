---
id: ai-models-render-time-prediction-papers
title: Render-time prediction research: DNEG poster (regression on geometry, looks, lighting, settings) and ENTIRE (volume rendering time)
domain: ai-models
tags: [render time prediction, dneg, entire, regression, estimator, features]
applies_to: 2019, arXiv 2501.12119
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.dneg.com/wp-content/uploads/2022/11/2019-4.pdf, https://arxiv.org/abs/2501.12119, src:research-verticals, src:research-agency-pipelines, https://www.youtube.com/watch?v=-Ks7SSgeHGg]
feeds: [estimator features]
conflicts: none
---
DNEG (SIGGRAPH Asia 2019 poster) groups features as geometry, looks, lighting and user settings, trained on past production renders; accuracy not seen. ENTIRE predicts volume rendering time from structure, resolution and camera. A 2016 Blender paper and a Blender time-estimator add-on exist.
No open Redshift render-time predictor was found.

**Use it:** use DNEG's feature groups for the scene card.
Transcript support: Entropic/NIM plan to train predictive bidding on historical bids, farm actuals and per-shot cost (https://www.youtube.com/watch?v=-Ks7SSgeHGg [21:52])
