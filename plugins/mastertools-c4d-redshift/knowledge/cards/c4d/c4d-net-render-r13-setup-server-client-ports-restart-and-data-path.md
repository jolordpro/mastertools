---
id: c4d-net-render-r13-setup-server-client-ports-restart-and-data-path
title: Legacy C4D Net Render (2011): install server and clients from the installer, set the same server IP and port on each, restart, then submit through the web page at port 8080
domain: c4d
tags: [net render, server, client, port 8080, port 1080, c4d training, legacy, deep-read]
applies_to: Cinema 4D R13-era Net Render (video 2011)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=09hP2XAi0Rk, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Run the installer: server on any machine (it needs little power), client on every render machine; one machine can run both [01:39-02:41]. Net Render needs the Studio bundle [20:21].
Server: File, Network Settings, set the Data Path (where finished images land, can differ per project), the server's TCP/IP address and its port; quit and restart for it to apply [03:12-04:15]. In the web browser the server answers at its IP plus the port, 8080 in the demo [08:54-09:26].
Client: it starts on port 1080; enter the server IP in its network settings and make sure the server port matches the server's; restart [04:15-05:48]. Put a client shortcut in each machine's Startup folder so it runs on boot [19:50].
Note that Team Render replaced Net Render in later Cinema 4D versions, so use this only to read old project notes.

**Use it:** Context for old farm documents; not a current workflow.
