---
id: pipeline-render-time-predictors
title: Render-time prediction exists only as a Blender add-on (two reduced test renders), a DNEG 2019 poster and papers; Greyscalegorilla's calculator multiplies a typed frame time
domain: pipeline
tags: [render time estimate, predictor, dneg, blender estimator, calculator, ml]
applies_to: 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://superhivemarket.com/products/render-time-estimator, https://www.dneg.com/wp-content/uploads/2022/11/2019-4.pdf, https://greyscalegorilla.notion.site/Render-Calculator-Script-1519d0a6a6c080d4944de6d657626998, src:research-agency-pipelines, src:research-verticals, https://www.youtube.com/watch?v=H3KurpOBE24]
feeds: [estimator design (M1)]
conflicts: none
---
DNEG treats render time as regression on geometry, looks, lighting and user-setting features from past renders. No C4D or Redshift predictor was found, and no YouTube video covers ML time prediction.

**Use it:** the render ledger is the same data grown over time; start with scene-card features plus draft timing.
Transcript support: The Blender add-on is about 6 dollars and reports elapsed, ETA, average, shortest and longest frame; better on animation than stills. (https://www.youtube.com/watch?v=H3KurpOBE24 [00:34-04:42])
