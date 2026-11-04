---
id: pipeline-loud-colour-coded-viewport-messages-not-popups
title: DillonGoo shows pipeline errors as large colour-coded overlays in the 3D view because popup alerts get ignored
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, pipeline messages, draw handler, alerts, colour code, warning, deep-read]
applies_to: Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Winchester [18:36-21:18]: Python popups vanish when the mouse moves, so a custom overlay is drawn in the viewport, big and 'flashy' on purpose. Green: pushed fine, or fine to work but pull first. Red: file is behind the log by N pushes, not in the log, or maybe still syncing. Yellow: someone else pulled this file, so talk first. Blue: sync tool seems off. Purple: character review states.

**Use it:** make a scene-check result impossible to dismiss for blockers, and use a short fixed colour set for severities.
