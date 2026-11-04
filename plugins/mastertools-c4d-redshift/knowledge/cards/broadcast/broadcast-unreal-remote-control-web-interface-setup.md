---
id: broadcast-unreal-remote-control-web-interface-setup
title: Expose controller properties to Unreal's Remote Control API and drive them from a browser page
domain: broadcast
tags: [unreal, remote control, web interface, show control, port 7000, node.js, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Plan from day one for external control (web page, tablet or show-control software) [53:26-53:58]. Enable the Remote Control API and Remote Control Web Interface plugins; first run installs prerequisites such as node.js; project settings hold the port and an autostart-web-server toggle. On the same machine the page is at 127.0.0.1:7000 [53:58-55:04].
One Remote Control preset exposes properties (eye icon) and actor functions; add a Pause button by exposing the function, then drag it onto the page; a tab toggles Control and Design mode so edits are not made by accident [56:07-57:40]. Exposed in the sample: team, text, player names, play/reset, SDI on/off and ray-trace quality [55:04-56:07].

**Use it:** Design operator panels with the same split: preset of exposed items, drag-and-drop page, a locked control mode.
