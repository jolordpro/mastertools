---
id: pipeline-push-pull-buttons-own-the-cleanup-and-publish-log
title: Push and pull buttons that do the file work let a pipeline inject cleanup, a publish log and filters by assigned shot
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, push, pull, publish log, cleanup, automation, tracker filter, deep-read]
applies_to: Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Winchester [13:55-18:36, 36:35-38:08]: the push/pull operators only open a file and save it elsewhere, yet they became central. Users cannot misplace or misname files; the tool filters shots by tracker assignment (a 250-shot list reduces to the artist's own) and can limit to shots not yet pulled.
Every push runs a long cleanup list, writes a log (JSON), and offers a publish note. A bulk cleanup strips unused characters from layout files built in big chunks (one character wanted, nine in the file) using tracker asset tags [29:51].
Advice: create buttons for simple tasks, and store info in JSON so other tools can read it [37:38].

**Use it:** design file moves as tool buttons, with an automatic cleanup and log step, instead of artist-run manual saves.
