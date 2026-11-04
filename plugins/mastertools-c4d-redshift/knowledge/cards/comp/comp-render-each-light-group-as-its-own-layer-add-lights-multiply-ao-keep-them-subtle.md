---
id: comp-render-each-light-group-as-its-own-layer-add-lights-multiply-ao-keep-them-subtle
title: A night city was built by rendering diffuse, ambient, highlight, moon, window and AO layers separately, combining lights with Add and AO with Multiply, and keeping each light subtle
domain: comp
tags: [multipass, light groups, ambient occlusion, add, multiply, glow threshold, tootorials, deep-read]
applies_to: 3ds Max mental ray, After Effects
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=mchPC1LeMAE, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Tootorials (2011, 3ds Max, mental ray, comped in After Effects) [3:27-17:44]: render a diffuse pass first (lit plainly, harsh shadows), then each light set alone (street ambient, "highlights", moon, window lights with a falloff) and AO last. In AE: diffuse at the bottom, darkened for a night scene; ambient, highlights and windows set to Add and tinted (greens and warm tints); moon tinted slightly blue and blurred only slightly, because a heavier blur loses it; opacity lowered on all but diffuse so nothing is overbright [15:38]; AO set to Multiply and is the most important layer for corners and edges [16:09]. AO was a material override with a mental ray ambient occlusion shader; quality 80 samples (16 is low), plus spread and max distance, with other values left alone [12:30-13:01]. The same AO render is a clay render for model show-offs [13:32]. Glow: lower the threshold and more of the scene glows; higher and only whites do [17:11]. Mistake owned: window layer rendered with lights plus material, so tinting was entangled; he masked around it. A depth pass as a Luma matte for blur was skipped as confusing [19:17].

**Use it:** Same recipe for light-group passes in Redshift: sum check, Add for lights, Multiply for AO, then trim each light layer's opacity before grading.
