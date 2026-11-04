---
id: gpu-cloud-zync-2016-upload-only-job-syncs-assets-ahead-so-the-render-submit-sends-one-scene-file
title: Zync (2016): the C4D plugin has an upload-only mode you run daily or hourly, so at render time only the scene file goes up
domain: gpu-cloud
tags: [zync, upload only job, asset sync, cinema 4d, take, auxiliary files, bandwidth, ibc 2016, deep-read]
applies_to: Zync for Cinema 4D preview, 2016
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=aAjOM-JqnHI, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
Option 'do not render any take, just upload scene files' pushes textures, HDRIs and caches in the background; it costs nothing, and if nothing changed nothing moves [20:13-20:44]. At submit Zync diffs the scene, checks that all assets are present and uploads only what is missing [25:59]. A file is sent once even if several artists or shots use it [09:55]. For files the scan misses (caches, assets for another scene), 'select auxiliary files' adds them by hand [21:47-22:18]. Resolution, renderer, output path and format are read from the C4D scene [21:16]. Rule: manage file IO ahead of time rather than at render time [22:18].

**Use it:** model for the platform's pre-flight: separate 'sync assets' from 'render', show missing-file errors before the render starts, and offer an extra-files list for plugin caches.
