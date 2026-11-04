---
id: pipeline-versioned-files-versus-shared-big-files-folder-split
title: Blender Studio splits project folders: version-controlled blends, a shared folder for big files (playblasts, renders, Blender builds), and a local folder
domain: pipeline
tags: [nick alberelli, blender studio, kitsu, editorial, folder structure, svn, syncthing, version control, blender version, deep-read]
applies_to: Blender Studio pipeline (2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jiXB5X1S1AI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Alberelli [04:24-08:55]: the project tool creates three top-level folders. SVN holds blend files and the master edit; shared holds big items that need no version control (playblasts, rendered frames, Blender binaries) and syncs via Syncthing, Dropbox or a network share; local holds the user's Blender copy and add-ons.
Blender is launched only through a run script that copies the project's Blender build and add-ons into local, so everyone has the same version; preferences are per project [06:50-07:53].
Syncing big playblasts is the hardest part; they self-host Syncthing and have not needed folder permissions [37:11].

**Use it:** same split suits C4D jobs: scenes in versioned storage, caches and renders in shared storage, and a pinned app version per project.
