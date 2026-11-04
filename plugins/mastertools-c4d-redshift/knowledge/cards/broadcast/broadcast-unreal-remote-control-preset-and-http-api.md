---
id: broadcast-unreal-remote-control-preset-and-http-api
title: Unreal Remote Control gives artists a web panel from toggled properties, and developers a REST API; the generated panel drives only one engine
domain: broadcast
tags: [unreal, remote control, broadcast ar, web interface, rest api, main and backup, girraphic, deep-read]
applies_to: Unreal Engine 5, Remote Control API (2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=2DoF-oYNQgU, src:yt-transcripts]
feeds: []
conflicts: none
---
Aidan, virtual production tech lead at Girraphic (Unreal Fest 2025) [03:48-07:25]. Create a Remote Control Preset, toggle the remote icon beside any property (text, float, bool, location, rotation) and it appears in an auto-generated web interface with no Blueprint. Blueprint public variables and functions can be exposed too. Developers use the HTTP API (get, put, post, delete) from Node, Python or C++. Girraphic used it for a Netflix event, then their own control app on the same API. Limit: the API can control several engines, but the generated web UI cannot, and broadcast needs a main and a backup engine driven together; they changed the plugin (shared on GitHub, not robust) for that.

**Use it:** For a live graphics control surface, plan for a main plus backup engine from the start, and test that both receive every command.
