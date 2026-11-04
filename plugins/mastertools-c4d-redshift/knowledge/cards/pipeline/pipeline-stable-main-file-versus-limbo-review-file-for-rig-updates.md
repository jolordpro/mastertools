---
id: pipeline-stable-main-file-versus-limbo-review-file-for-rig-updates
title: Static main files break every shot if a rig update is bad, so DillonGoo adds a review 'limbo' file and only updates the stable one after checks
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, rig update, static file, stable version, review file, trade-off, deep-read]
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
A questioner [46:03-47:07] argued that a single static asset file risks every shot if a rigger pushes a broken update, and that stable/testing versions let old shots keep rendering. Winchester: their jobs run two to four months so changes seldom break; they back up before big changes [47:40].
Dylan Goo [47:40-48:41]: a new character review step pushes updates to a limbo file first, and the stable static file changes only once it works.

**Use it:** a hybrid works: one stable name for linking, plus a test copy that gets promoted after checks.
