---
id: gpu-cloud-coreweave-2019-synced-folder-keeps-big-caches-on-the-farm-and-launch-render-freezes-the-scene
title: CoreWeave Concierge synced a local folder to the farm so 300 GB of caches never re-upload; pressing launch freezes the scene as sent
domain: gpu-cloud
tags: [coreweave, blender, upload, sync, cache, versioning, marco, deep-read]
applies_to: CoreWeave Concierge, Blender Conference talk uploaded 2019-10
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sh8UhQ1zofg, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Marco: re-uploading textures and simulation caches for every test was the big complaint; their fix is a shared folder on the artist's machine mirrored into the web file manager, so changes sync after save [15:57-17:32]. He cites 300 GB of simulation cache that stays put [17:01].
When launch render is pressed, the file is wrapped and sent; later edits do not affect that job, the artist must save, wait for sync, and launch again [22:39-24:49].
Planned: accept any zip with dependencies, with the main file picked in the file manager [24:49-25:50].

