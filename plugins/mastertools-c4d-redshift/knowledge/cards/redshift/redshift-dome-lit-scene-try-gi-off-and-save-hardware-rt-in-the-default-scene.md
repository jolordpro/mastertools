---
id: redshift-dome-lit-scene-try-gi-off-and-save-hardware-rt-in-the-default-scene
title: Maxon trainer Darren: when the dome gives most of the light, render without GI for a slightly shorter time; set hardware RT in the default scene
domain: redshift
tags: [maxon, darren, global illumination, dome light, hardware ray tracing, default scene, ledger-check, deep-read]
applies_to: Redshift 3.5 in Cinema 4D R26 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Darren: if most light comes from a dome, try rendering with GI off; the look changes little and the render is a bit shorter [2:14:14-2:14:48]. No timing given.
Hardware ray tracing: switch it on, then Window, Customization, Save As Default Scene so each new file starts with it [2:09:01-2:10:02]. Ellie's Mac showed no such option at the time [2:08:28-2:09:32]; the ledger/HWRT cards cover Apple support.
Check by A/B snapshot; GI also lights shadows from other objects, so a dome-only test is not proof for scenes with bounce.

**Use it:** Offer GI-off as a test, never a rule; always compare with a snapshot.
