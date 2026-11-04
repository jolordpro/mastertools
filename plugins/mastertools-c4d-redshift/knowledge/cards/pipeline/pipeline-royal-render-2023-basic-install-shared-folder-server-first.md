---
id: pipeline-royal-render-2023-basic-install-shared-folder-server-first
title: Royal Render basic install: one shared folder holds all apps, start the server first (it locks its name and IP), then clients
domain: pipeline
tags: [royal render, rr server, rr client, rrcontrol, shared folder, submission plugin, maya, network install, holger schoenberger, deep-read]
applies_to: Royal Render, video Oct 2023 (Windows, Maya 2022 Arnold)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=W5Ids9hoz-4, src:yt-transcripts]
feeds: []
conflicts: none
---
Holger Schönberger (captions 'holga'). Needs a file server all machines can see and one machine as server. Unzip, run the installer and point it at the shared project drive: it copies the bin folder (apps for Windows, Linux, Mac) and offers to open access rights for everyone; in a company tighten later [00:37-02:54]. Start the server first: it writes the main configuration with its name and IP and cannot move unless the config is reset [03:29-04:03]. On Windows do not click inside the server terminal (select mode pauses it). Then clients: a speed test of CPU and GPU decides how many frames each machine receives [04:34]; tray icon is hidden by default [05:05]. rrControl views jobs and clients. Workstation installer adds the submission plugins [06:06]. The scene file is not copied; it must sit on the shared drive [07:09].

**Use it:** the order to copy: share, server, clients, submit plugins, scene on shared storage.
