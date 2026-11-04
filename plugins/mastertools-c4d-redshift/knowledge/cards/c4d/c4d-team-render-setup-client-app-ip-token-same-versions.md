---
id: c4d-team-render-setup-client-app-ip-token-same-versions
title: Team Render setup: run the Team Render Client app on the node (not C4D), match C4D, Redshift and plugin versions, add the node by IP and security token
domain: c4d
tags: [team render, team render client, security token, ip address, bonjour, redshift, network render, ethernet, deep-read]
applies_to: Cinema 4D 2023, Redshift, Windows and Mac (2023 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=1Gtp3BjlTjY, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Royals & Rogues [03:06-15:09]. Both machines on Ethernet through the router (10 GbE preferred), same C4D, Redshift and plugin versions. In Preferences > Renderer > Team Render: share machine and announce service (Bonjour) on, set a security token, note the port. On the node do not open Cinema 4D; launch the Team Render Client from the C4D install folder [10:56-11:27]. On the main machine: Renderer > Team Render Machines > Add Machine, enter the node's IP (worked better than hostname) plus token. Use Ping and the connection test; slow speed means you are on Wi-Fi [13:32-14:03]. Keep Peer-to-peer asset distribution on; leave 'always fetch from server' off unless using a Team Render server [08:21-10:26]. Before sending, cache all sims and bake what you can, or each machine computes physics differently [14:03-15:05]. Start with Render > Team Render to Picture Viewer (Ctrl+Shift+R). Firewall, antivirus and running as administrator are the common blockers [18:13-18:45].

**Use it:** A Team Render pre-flight list: versions equal, token and IP right, wired, sims cached.
