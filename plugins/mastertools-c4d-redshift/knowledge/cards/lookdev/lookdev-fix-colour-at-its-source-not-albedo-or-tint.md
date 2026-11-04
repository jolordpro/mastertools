---
id: lookdev-fix-colour-at-its-source-not-albedo-or-tint
title: To hit a "more saturated" note, choose the right stage (shading, texture, light or grade); pushing albedo or tint breaks lighting
domain: lookdev
tags: [[nora shramek, albedo, saturation, tint, art direction, final pixel, hsv, lighting artist], deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=r2PXd6l7kBg, src:yt-transcripts]
feeds: [redshift, lookdev, elevate]
conflicts: none
---
Nora Shramek: when art direction says "more saturated", others often raise albedo saturation and then red blows up in lit result [35:18-35:48]. The better question is which stage gets the final pixel colour best: shading, texture, lights or colour grade [36:18]. Host Amit adds (opinion): don't use a tint control to fix value; fix the texture, and work in HSV so brighter changes only one value [36:50-37:51]. Lighting also ends up as unofficial art director since everything is lit and the lighter sees the whole game [10:48, 34:47].

**Use it:** when a client says "pop the colour", diagnose lighting or grade before touching diffuse colour; keep albedo in plausible ranges (see lookdev-albedo-nonmetal-metal-ranges).
