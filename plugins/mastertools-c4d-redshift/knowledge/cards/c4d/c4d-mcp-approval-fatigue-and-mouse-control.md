---
id: c4d-mcp-approval-fatigue-and-mouse-control
title: C4D MCP preference warns it can run arbitrary Python, and repeated 'allow' prompts can hide a mouse-control grant
domain: c4d
tags: [mcp, python, approval, security, mouse control, auto approve, safety]
applies_to: C4D 2027.0 MCP
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [coach, safety notes]
conflicts: none
---
[02:29:51] Edit > Preferences > MCP is off by default and shows a warning that it can run any Python, which can delete files outside C4D.
[02:34:31] He set the client to auto-approve safe actions, and warns it is risky. [02:46:21] After many 'allow' clicks he approved a different kind that gave mouse control, then stopped; his master prompt now says never take the mouse.
[02:46:52] The assistant saved the scene unprompted when the prompt lacked his standing rules.

**Use it:** tell users to read each approval and put 'never take the mouse, never save' in a standing prompt.
