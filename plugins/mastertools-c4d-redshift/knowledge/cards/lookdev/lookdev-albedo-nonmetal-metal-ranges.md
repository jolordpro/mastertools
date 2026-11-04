---
id: lookdev-albedo-nonmetal-metal-ranges
title: Albedo guide values: non-metal sRGB 50-243 (linear about 0.032-0.896), metal reflectance sRGB 186-255 (linear about 0.49-1.0)
domain: lookdev
tags: [lookdev, albedo, pbr, material, validator, metal, range, unity]
applies_to: any PBR workflow
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://docs.unity3d.com/2020.1/Documentation/Manual/MaterialValidator.html, https://www.marmoset.co/posts/physically-based-rendering-and-you-can-too/, src:research-production-pipelines, https://www.youtube.com/watch?v=r2PXd6l7kBg, https://www.youtube.com/watch?v=nlbJwMoj1Dg, https://www.youtube.com/watch?v=6lioyniEl_E]
feeds: [PLAN 0A texture stats]
conflicts: none
---
Unity's validator thresholds, applied in linear space only; linear values are computed from sRGB.
Community lore for non-metals: about 30 tolerant, 50 strict, up to about 240.
These are guidelines; a black logo plate can be correct on purpose.

**Use it:** flag out-of-band maps only where the map feeds a colour slot, and show the number before suggesting a change.
