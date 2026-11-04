---
id: lookdev-metalness-and-f0-rules
title: Metalness maps should be 0 or 1; metals carry colour in reflectance; insulator F0 is 0.04 linear (0.22 sRGB)
domain: lookdev
tags: [lookdev, metalness, f0, reflectance, pbr, roughness, validator]
applies_to: any PBR workflow
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.marmoset.co/posts/physically-based-rendering-and-you-can-too/, https://experienceleague.adobe.com/en/docs/substance-3d-sampler/using/filters/tools/pbr-validate, src:research-production-pipelines, https://www.youtube.com/watch?v=-lpj38Cql4c]
feeds: []
conflicts: none
---
Grey metalness is for transitions only; metals have black diffuse.
Adobe's validator flags bad combinations rather than roughness alone; its named example is dark colour with roughness 0 and metallic 1. Adobe's default thresholds are not printed.
No published numeric roughness limits exist; roughness 0 with anything dark or metal is suspect.

**Use it:** check combinations, not single values, and word the finding as suspect rather than wrong.
