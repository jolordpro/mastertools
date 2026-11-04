---
id: pipeline-usd-playblast-from-the-container-for-unified-look
title: Make playblasts from the published container, not the authoring app, to prove the export and unify the look
domain: pipeline
tags: [playblast, review, usd, export check, consistency, prism, deep-read]
applies_to: Prism USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Rather than playblast from Maya, he exports the objects first and then makes a standalone playblast of the shot container [18:34]. Reason: it shows the export worked and nothing broke, and all playblasts look the same no matter whether they start from Maya, Houdini or the standalone [18:34] [19:05].
Prism also lets a team set a turntable preset on an asset in its standalone browser: lights, ground plane and camera in one click, with a higher-quality renderer choice [14:29] [14:59].

**Use it:** Validation habit: the thing reviewed must be the thing published. Add a publish-then-preview step before sending to review.
