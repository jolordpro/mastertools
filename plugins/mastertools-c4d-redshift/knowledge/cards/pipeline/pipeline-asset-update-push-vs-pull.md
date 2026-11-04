---
id: pipeline-asset-update-push-vs-pull
title: Two ways asset updates reach shots: push (auto-update on publish) or pull (each shot repoints by hand)
domain: pipeline
tags: [pipeline, asset update, push, pull, hero version, publish, linked library, blender, approval, deep-read]
applies_to: any (study of Blender studios)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AiRjt7nWcZc, src:yt-transcripts]
feeds: [shakedown, estimator, CHECKS]
conflicts: none
---
A French research team (Remy Soyer and Swan Martinez, Paris 8 / Inrev, with Cube Creative, Autour de Minuit and Normal Animation) found two propagation patterns across three studios [26:02].
Push: the asset artist publishes to a single "hero" version; layout and animation scenes link to it, so a new publish reaches every shot automatically [26:35] [27:06]. Fast, almost no pipeline code, but it can change shots that were already approved [27:37] [34:00].
Pull: shots link to versioned asset files, so each shot must be repointed to a new version; this respects the validation chain but needs custom tools or tedious manual work [30:17] [30:51] [34:30].
Tradeoff in one line: push buys iteration speed, pull buys control over approved shots.

**Use it:** Pick per department: use push while a shot is still in layout, freeze to pull once a shot is approved. Add a pipeline check that warns when a linked asset version differs from the approved one.
