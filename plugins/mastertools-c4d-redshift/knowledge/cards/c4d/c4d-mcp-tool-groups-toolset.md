---
id: c4d-mcp-tool-groups-toolset
title: C4D MCP exposes tools in groups the user can switch, set under a Toolset preference
domain: c4d
tags: [mcp, toolset, tool groups, permissions, preferences]
applies_to: C4D 2026.4+
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://architosh.com/2026/10/whats-in-maxons-new-cinema-4d-mcp-server/, https://www.youtube.com/watch?v=XJ4OXjinuHg, https://help.maxon.net/c4d/2027/en-us/Content/html/MCPADAPTERPREFS.html.md, src:research-gaps-deep, src:research-agency-pipelines, src:research-youtube, src:research-vfx-pipelines, https://www.youtube.com/watch?v=ZKPCE7E56nk, src:yt-transcripts]
feeds: [PLAN 0.2, connector reach, OPEN-STACK stage 1]
conflicts: none
---
Screenshots show groups named "rendering entities and document" (on) with "shot setup" and "transforms selection" off by default. A Toolset setting limits what an assistant may touch.
The full group list is not published (see the unpublished tool-list card).

**Use it:** the connector reads the toolset state so it knows what an assistant is allowed to do.
Transcript support: Toolset lists groups such as rendering, modeling, animation, MoGraph. (https://www.youtube.com/watch?v=ZKPCE7E56nk [01:39])
