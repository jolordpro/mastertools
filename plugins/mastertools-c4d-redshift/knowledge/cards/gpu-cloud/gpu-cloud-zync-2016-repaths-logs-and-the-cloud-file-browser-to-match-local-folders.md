---
id: gpu-cloud-zync-2016-repaths-logs-and-the-cloud-file-browser-to-match-local-folders
title: Zync (2016): cloud job logs and the cloud file browser show your local folder structure, so nobody reads cloud paths
domain: gpu-cloud
tags: [zync, repath, job log, file browser, paths, cloud storage, cinema 4d, ibc 2016, deep-read]
applies_to: Zync for Cinema 4D preview, 2016
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aAjOM-JqnHI, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
The VMs run on Google Cloud, but job logs are repathed so every file they reference appears as on the artist's machine [28:02-28:33]. The project file browser lists the cloud bucket with the same structure as the desktop, 'no confusing file paths' [33:13-33:43]. Custom shader paths (such as Arnold's open-source shader library) can be added in account settings and are uploaded for renders; Nuke gizmos work the same way [30:40].

**Use it:** for the platform's error messages, translate remote paths back to the user's own folders; people debug faster in their own path names.
