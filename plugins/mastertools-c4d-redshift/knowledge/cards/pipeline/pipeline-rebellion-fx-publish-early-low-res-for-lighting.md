---
id: pipeline-rebellion-fx-publish-early-low-res-for-lighting
title: FX publishes a low-res mesh early so lighting can test shaders and look, then checks naming before the final publish
domain: pipeline
tags: [rebellion vfx, evil genius 2, fx, publish, usd, naming convention, ocean, deep-read]
applies_to: Houdini, USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Alexander (FX TD, Rebellion; surname unclear in captions) works in loops: load the latest published assets, make sops setups, bring back into the USD context to test with the latest lighting rigs, then fine-tune the sim [23:53-25:25].
He quickly meshed a low-res version of the water and imported it to check how it looked in the context of the shader and lighting, and to catch render breakage, then published so lighting had an FX asset early [37:54-38:24].
Before final publish he checks attributes and naming convention; republishing updates downstream departments automatically [25:25].

**Use it:** staged publishing - rough first for context checks, final after naming QC.
