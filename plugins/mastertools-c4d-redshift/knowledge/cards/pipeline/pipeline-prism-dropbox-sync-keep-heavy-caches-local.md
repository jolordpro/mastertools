---
id: pipeline-prism-dropbox-sync-keep-heavy-caches-local
title: Prism teams shared a project through Dropbox, and let heavy caches, renders and playblasts stay local rather than sync
domain: pipeline
tags: [pipeline, dropbox, sync, cloud, caches, remote, prism, storage, deep-read]
applies_to: Prism 1.3 and 2.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
Asked about cloud use, the developer says two people worked remotely by sharing a project folder on Dropbox, each running Prism locally [43:25] [43:57]. Prism lets you decide per output type whether exports, caches, renderings or playblasts go to the local folder or the synced cloud folder, since FX caches can be several gigabytes [43:57] [44:29].
Prism 1.3 lacked user management and permissions for big studios; 2.0 was to address it; the core stays open source with commercial plugins for advanced users [45:31] [46:32] [47:04].

**Use it:** Relevant to Dropbox-based projects: sync source files and finals, exclude caches and sims. Compare pipeline-prism-c4d-plugin.
