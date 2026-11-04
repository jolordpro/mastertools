---
id: c4d-mcp-no-headless-teamrender-cli
title: C4D MCP does not run headless, under Team Render, or on the command line
domain: c4d
tags: [mcp, headless, team render, command line, farm, commandline, maxon mcp, c4d 2026.4, mcp server, toolset, audit log]
applies_to: C4D 2026.4-2027.0
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.cgchannel.com/2026/09/maxon-releases-cinema-4d-2026-4-with-a-new-mcp-server/, https://help.maxon.net/c4d/2027/en-us/Content/html/MCPADAPTERPREFS.html.md, src:research-vfx-pipelines, src:research-frontier-ai, https://digitalproduction.com/2026/10/01/cinema-4d-2026-4-mcp/, https://architosh.com/2026/10/whats-in-maxons-new-cinema-4d-mcp-server/, https://www.cgchannel.com/?p=179009, src:research-agency-pipelines, src:research-gaps-deep]
feeds: [Phase 2 farm, Phase 4 agent door, connector test, PLAN 5b]
conflicts: none
---
Maxon's server needs a running C4D GUI session. One search-summary source adds that the After Effects Lite edition does not include it (single source).
So an agent audit on a farm node needs the platform's own connector instead of Maxon's.
Merged from `pipeline-maxon-mcp-scope`: Windows and macOS only. Stated domains: Takes, MoGraph, Render Queue, camera tracking, geometry, materials, lighting, UV, rigging, animation. Demos: 100+ variations from a CSV via Takes and Render Queue. Python and network access are separate opt-ins. No Redshift or AOV tools are described, and the full tool list is unpublished. Maxon's own video does say an assistant can set up render passes, so test which tools exist.

**Use it:** plan a platform-owned headless route (c4dpy, redshiftCmdLine) for anything that must run on a node.
