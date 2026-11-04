---
id: pipeline-royal-render-2023-permanent-install-services-mapped-drives
title: Royal Render permanent install: run server and client as services, map UNC paths, move the job list to disk
domain: pipeline
tags: [royal render, service, mapped drive, unc path, memory cache, error reporting, firewall, client watch, windows, linux, deep-read]
applies_to: Royal Render, video Oct 2023
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=HKLXU4do4Jc, src:yt-transcripts]
feeds: []
conflicts: none
---
Important settings [00:04-03:13]: the server keeps jobs in memory and backs up every 30 minutes, so a power loss can lose jobs; the memory cache database option (SSD) saves on receipt. Job list limit settable up to about 50,000; finished jobs deleted by count or days; history database purged after 800 days. Company/project is read from the scene or image path folder. A service cannot use mapped drives of the logged-in user, so tell it which UNC path is drive M; mixed Windows/Linux needs path mapping pairs.
Service reasons [03:50-05:53]: starts on boot with no login, access to larger file shares than the user, auto restarts stuck server tasks. Client service needs a user with file-server rights; add to Administrators to install apps. Installer turns off Windows error reports (a crash dialog would block the machine), adds firewall rules, and installs a 'client watch' tray icon [06:24-07:25]. The service pulls the client from the share, so updating the share updates every machine. Server service waits 30 seconds at boot for network and Active Directory [07:56].

**Use it:** the failure list for a Windows farm: mapped drives, crash dialogs, boot order, login dependence.
