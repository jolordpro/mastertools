---
id: pipeline-method-network-services-not-direct-database-libraries
title: Put asset, farm and disk functions behind network services so show-locked libraries never hold database credentials or block schema changes
domain: pipeline
tags: [andre prado, method studios, services, rez, library versions, runtime dependencies, api, credentials, deep-read]
applies_to: Python
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=HuV0_AbDgYk, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Prado [21:37-24:14]: with 500+ libraries and tools, runtime dependency breaks are common; an innocent argument reorder in a minor release broke tools. If libraries talk to the database directly, every artist machine holds credentials and old shows locked to old library versions block schema updates. Shows lock versions near delivery.
Method moved core features into services (asset, farm, disk) over the network, decoupling backend from tools: services run under a WSGI server behind nginx, with message-queue workers for async work like thumbnails [22:40-23:12].
Environments are resolved just-in-time with Rez: say which shot and app, get that app plus matching pipeline libraries, no system installs [19:32-21:07].

**Use it:** Pipeline principle: thin clients, versioned API, locked environments per project.
