---
id: c4d-mcp-python-network-switches
title: In C4D MCP, Python execution and network access are separate opt-in switches
domain: c4d
tags: [mcp, python, network, permissions, exec]
applies_to: C4D 2026.4+
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://architosh.com/2026/10/whats-in-maxons-new-cinema-4d-mcp-server/, src:research-gaps-deep, src:research-frontier-ai, src:research-agency-pipelines, https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts, https://www.youtube.com/watch?v=ZKPCE7E56nk]
feeds: [PLAN 0.2, connector reach, OPEN-STACK stage 1]
conflicts: none
---
Python control is available for harder jobs but needs its own switch; network access is another opt-in on top of the token.

**Use it:** do not rely on Python execution through MCP being enabled; ask or fall back to the plugin.
Transcript support: MCP preference warns it can run arbitrary Python; off by default (https://www.youtube.com/watch?v=PCtsdWnYhx8 [02:29:51])
Transcript support: Python access is a separate security switch, advised off to start. (https://www.youtube.com/watch?v=ZKPCE7E56nk [01:39])
