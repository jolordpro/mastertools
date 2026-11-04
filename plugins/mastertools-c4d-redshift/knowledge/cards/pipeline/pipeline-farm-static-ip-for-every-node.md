---
id: pipeline-farm-static-ip-for-every-node
title: Give every render node a fixed address, because a changed DHCP address breaks the remote link and saved passwords
domain: pipeline
tags: [kent trammell, cg cookie, render farm, static ip, vnc, remote desktop, dhcp, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=FNhUnPWzVaw, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Nodes controlled over VNC from one main machine; if a node sleeps and the router hands it a new address, the viewer can no longer find it [17:32-18:34].
Fix: set a manual IPv4 address, mask and gateway on each machine; he chose numbers like .11 to .14 so they never collide with the router's low numbers, and warns not to reuse an address another device owns [31:09, 39:44].
A node that took long to connect was one he had not fixed yet; saved keychain passwords also break when the address changes [37:39-38:41].
VNC ports must be opened in the node's firewall (he used 5900 and checked the actual port the server printed, 5901) [28:36-29:37].

**Use it:** farm setup checklist item: fixed addresses, firewall port opened, one remote-control route that does not need a monitor on each node.
