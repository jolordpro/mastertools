---
id: pipeline-frame-offset-and-link-over-append-solo-tips
title: Start every shot at a high frame (101), link instead of appending, and keep push logs and synced backups even when working alone
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, start frame, library override, link, append, solo artist, backup, syncthing, deep-read]
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
Winchester [41:51-42:22, 54:29-56:02]: starting at the same high frame gives room for sim caches and lets shots be added without renumbering, unlike old sequential frames. The studio dropped nested library overrides (override of an override) after a project lost them a lot of sleep [08:42-09:46]; they use plain overrides and an empty copying a bone's transform for FX [53:53].
A solo artist should keep separate files, a push log, link rather than append, and use Syncthing as a backup that keeps up to five versions.

**Use it:** for C4D, ask solo users the same: reference external assets, log what changed, back up automatically.
