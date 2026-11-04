---
id: lookdev-brand-colour-under-tone-mapper
title: Brand colours can shift under a tone mapper; measure the colour difference of the brand hex after the view transform
domain: lookdev
tags: [lookdev, brand colour, tone mapping, aces, agx, pbr neutral, delta e, hue shift]
applies_to: any
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://khronos.org/news/press/khronos-pbr-neutral-tone-mapper-released-for-true-to-life-color-rendering-of-3d-products, https://www.youtube.com/watch?v=VlMB73cvROg, src:research-production-pipelines, src:research-youtube, https://www.youtube.com/watch?v=nlbJwMoj1Dg]
feeds: [PLAN 5b brand-colour fidelity]
conflicts: none
---
Khronos PBR Neutral was built to keep a product's base colour, hue and saturation; AgX and ACES-class mappers roll off highlights better but shift hue.
Users report trouble matching brand colours under ACES; no source compared ACES 2.0 hue behaviour.
A hex must read the same in Photoshop, After Effects and C4D, which means checking linear versus display values.

