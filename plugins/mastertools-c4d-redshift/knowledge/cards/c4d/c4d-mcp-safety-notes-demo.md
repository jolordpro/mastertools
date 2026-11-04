---
id: c4d-mcp-safety-notes-demo
title: Hands-on MCP notes: undo does not cover files, whatever Claude sees goes to the provider, and two MCP servers confuse the assistant
domain: c4d
tags: [mcp, undo, privacy, community plugin, python, toolset]
applies_to: C4D 2026.4
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ZKPCE7E56nk, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Prefs, MCP, tick Allow, pick Claude Desktop, update client, fully quit and reopen Claude [L 01:23-01:49]. Turn off the community plugin first [01:08]. A read-only prompt returned objects, lights, camera, render settings and flagged an unsaved file and missing materials [02:14].
Limits: undo skips files written to disk, so save a copy before big jobs; some tasks need Python; local does not mean private [03:30-03:53].

**Use it:** the setup guide tells the user to save a copy before agent runs and to run only one MCP bridge.
