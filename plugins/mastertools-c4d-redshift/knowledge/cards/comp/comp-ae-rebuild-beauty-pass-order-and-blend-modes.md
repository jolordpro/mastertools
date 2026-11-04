---
id: comp-ae-rebuild-beauty-pass-order-and-blend-modes
title: Rebuild a beauty in After Effects from the bottom: GI, then lighting, then reflection, specular and self-illumination on Add, AO on Multiply, Z-depth as reference only
domain: comp
tags: [after effects, passes, beauty rebuild, blend modes, add, multiply, gi, ao, z-depth, cgstirk, deep-read]
applies_to: After Effects, V-Ray passes (2019)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=AxviuFLniB8, src:yt-transcripts]
feeds: []
conflicts: none
---
CGStirk [03:36-04:37]. Delete the master beauty if you rebuild from passes. Stack bottom to top: GI, lighting (direct), then reflection, specular, self-illumination. Those last four are additive, so their order does not matter; set them to Add. AO goes on Multiply. The Z-depth layer sits on top and is used only as a matte or reference, never as a visible layer. The Z-depth value direction does not matter (here near is dark), because it can be inverted in AE.

**Use it:** Reference for the comp step: lay out the passes in this order and blend modes, and use the order to explain what each pass contributes.
