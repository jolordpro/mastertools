---
id: pipeline-blender-master-file-linked-asset-workflow-dated-wips
title: Blender linked-asset workflow: a never-renamed master file per asset and shot, dated work-in-progress files overwrite it, relative paths throughout
domain: pipeline
tags: [blender, linked assets, master file, versioning, layout, relative paths, animation pipeline, pierrick picaut, deep-read]
applies_to: Blender (2026)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=JckDEblB7gc, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Pierrick Picaut [01:41-08:33]: layout comes first with primitives and a bouncing ball; scale and camera must be near final because animators and environment artists both work from the same layout, so they share camera motion and framing [01:53-02:48]. Each asset has a master file whose name and master collection name never change, since linked files look for exactly that [03:20-03:50]. Updates are made in a copy named by date plus a version number, never on the master; when ready, save over the master and every linked file updates on reload; if the version is buggy, overwrite the master with the previous one [04:21-05:23]. Use relative paths so Dropbox or any server gives the same paths to everyone [03:50]. A shot has a master animation file with collections for layout environment, camera, characters and final environment; animators and environment artists each overwrite their own master and link the other's, so each previews in the other's evolving work [05:27-06:57]. Technical staff manage the file linking so artists just open, work and save [07:29].

**Use it:** The "overwrite the master, keep dated copies, roll back by overwriting again" pattern is a cheap publish system for small teams.
