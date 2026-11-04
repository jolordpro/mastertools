---
id: ai-models-firefly-half-buffer-detection
title: Firefly detection from two half-buffer renders (DreamWorks) flags outliers by variance but keeps real highlights that appear in both halves
domain: ai-models
tags: [firefly, half buffer, dreamworks, outlier, esd, median of means, noise]
applies_to: 2021 methods
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://research.dreamworks.com/?p=760, https://diglib.eg.org/handle/10.2312/sr20211296, src:research-verticals, src:research-render-farms]
feeds: [QC fireflies]
conflicts: none
---
Jeffery's method uses a Generalized ESD outlier test; Buisine et al. (EGSR 2021) use an adaptive median of means with a Gini test. Needs two independent-seed draft renders. No learned firefly detector was found.

**Use it:** build the check with simple maths on two-seed drafts.
