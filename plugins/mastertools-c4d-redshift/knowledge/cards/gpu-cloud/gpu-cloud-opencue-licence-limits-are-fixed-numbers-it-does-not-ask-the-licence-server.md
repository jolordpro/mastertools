---
id: gpu-cloud-opencue-licence-limits-are-fixed-numbers-it-does-not-ask-the-licence-server
title: OpenCue has no licence or node-config management; its limits feature caps concurrent use against a fixed number, not the live licence server count
domain: gpu-cloud
tags: [opencue, licences, limits, render-farm, brian-cipriano, deep-read]
applies_to: OpenCue 0.4.55, ASWF Open Source Day 2020
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fnbRcTeKirw, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Brian Cipriano (project chair): OpenCue does not manage app or renderer licences, nor render-node configuration; asset storage also has to be supplied by the user [36:57-37:36].
What exists is a limits feature added about a year before: name a limit, give a number, and attach it to layers so the farm never consumes more than that. The number is static, it does not read the licence server [42:16-42:46].
Users asked for documentation on priorities and per-layer node limits; he says the user guides are thin [44:23-44:56].

**Use it:** when designing a Redshift cloud queue, a licence-count cap is a hand-set limit; keep it in sync with the licences actually bought.
