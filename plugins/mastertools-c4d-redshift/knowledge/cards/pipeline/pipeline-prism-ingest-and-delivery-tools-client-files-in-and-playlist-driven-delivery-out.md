---
id: pipeline-prism-ingest-and-delivery-tools-client-files-in-and-playlist-driven-delivery-out
title: Prism IO tools: client files are auto-detected and batch-converted on the farm into shots, and the delivery tool packs whatever is in the approved review playlist
domain: pipeline
tags: [pipeline, prism, ingest, delivery, client, flow, kitsu, ftrack, colour conversion, deep-read]
applies_to: Prism 2 IO tools, Flow Production Tracking
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Prism's team studied the pain of receiving files from clients and delivering renders, since specs differ per project and do not match studio structure [07:23-07:55]. Ingest: drag plates, edit refs and colour files in; formats and shot structure are detected from a config file, overridable [08:26]. Files go to the farm for batch copy and colour conversion (a template), land in the project folder structure, and shots are created in Prism and in Flow, Kitsu or ftrack; a first shot publishes to Flow [08:58-09:28]. Delivery: a playlist in Flow is the source; the tool submits the files to the farm, converts colour to the client spec, packs the delivery package, and offers override options [09:28-10:01].

**Use it:** Make the approved playlist the single source for delivery, so what the client gets is exactly what was approved.
