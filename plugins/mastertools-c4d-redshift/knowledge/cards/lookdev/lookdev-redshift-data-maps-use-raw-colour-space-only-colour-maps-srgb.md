---
id: lookdev-redshift-data-maps-use-raw-colour-space-only-colour-maps-srgb
title: Redshift texture nodes: colour maps use sRGB, but metallic, bump, normal and displacement maps need Raw or a seam/wrong look appears
domain: lookdev
tags: [color space, raw, srgb, texture node, normal map, displacement, roughness, deep-read]
applies_to: Redshift in Cinema 4D (2025)
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=HlQhMbjrM6M, src:yt-transcripts]
feeds: [lookdev, CHECKS]
conflicts: none
---
School of Motion bonus tip [10:32-11:35]: a visible seam on an object came from wrong colour space on texture nodes. Diffuse and other pure-colour maps: sRGB. Metallic, bump, normal, displacement (data): Raw. 'Auto' did not fix it for him. Matches ledger §8.

**Use it:** Texture check: list nodes whose data maps are not Raw.
