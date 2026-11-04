---
id: c4d-mcp-off-by-default-token
title: The C4D MCP server is off by default, local, token-gated, and free to use
domain: c4d
tags: [mcp, off by default, token, local, free, security, maxon, cinema 4d, cinema 4d 2026.4, c4d 2027, ai assistant, audit log, python]
applies_to: C4D 2026.4+
status: V
confidence: high
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://digitalproduction.com/2026/10/01/cinema-4d-2026-4-mcp/, https://architosh.com/2026/10/whats-in-maxons-new-cinema-4d-mcp-server/, https://www.youtube.com/watch?v=H53drzzUFfo, https://www.youtube.com/watch?v=XJ4OXjinuHg, https://help.maxon.net/c4d/2027/en-us/Content/html/MCPADAPTERPREFS.html.md, src:research-agency-pipelines, src:research-gaps-deep, src:research-frontier-ai, src:research-vfx-pipelines, src:research-youtube, https://www.cgchannel.com/2026/09/maxon-releases-cinema-4d-2026-4-with-a-new-mcp-server/, https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts, https://www.youtube.com/watch?v=ZKPCE7E56nk, https://www.youtube.com/watch?v=HxNqQKx0NWc]
feeds: [PLAN 0.2, connector reach, OPEN-STACK stage 1, PLAN 3, agent door]
conflicts: none
---
The user turns it on in Edit, Preferences, MCP. Access needs a token. Maxon says the server is free; the AI service on the other end may cost money.
Nothing connects until the user enables it.
Merged from `ai-models-maxon-c4d-mcp-server`: Release date 30 Sep 2026 in one source, 1 Oct in others. Windows and macOS only; not available in Team Render or the command line. Tool groups can be switched on or off (a Toolset setting under Preferences), undo steps are grouped, a local audit log is kept; Python execution and network access are separate opt-ins. Stated domains: Takes, MoGraph, Render Queue, camera tracking, geometry, materials, lighting, UV, rigging, animation. Demos: 100+ variations from a CSV via Takes and Render Queue.

**Use it:** the plugin must check the MCP on/off flag before assuming an assistant can touch the scene.
Transcript support: MCP is off by default under Edit > Preferences (https://www.youtube.com/watch?v=PCtsdWnYhx8 [02:29:51])
Transcript support: MCP off by default, local, protected by an auth token. (https://www.youtube.com/watch?v=ZKPCE7E56nk [01:23])
Transcript support: Official Maxon demo (uploaded 2026-10-01) of prompting an assistant to build a Python generator and save it to the Asset Browser database (https://www.youtube.com/watch?v=HxNqQKx0NWc [00:00-09:34])
