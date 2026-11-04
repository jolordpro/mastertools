---
id: c4d-mcp-undo-and-audit-log
title: C4D MCP batches AI changes into undo steps and writes a local audit log
domain: c4d
tags: [mcp, undo, audit log, history, trust]
applies_to: C4D 2026.4+
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://architosh.com/2026/10/whats-in-maxons-new-cinema-4d-mcp-server/, https://digitalproduction.com/2026/10/01/cinema-4d-2026-4-mcp/, https://www.youtube.com/watch?v=H53drzzUFfo, src:research-agency-pipelines, src:research-gaps-deep, src:research-youtube, https://www.youtube.com/watch?v=ZKPCE7E56nk, src:yt-transcripts, https://www.youtube.com/watch?v=DbyeC34VoEQ]
feeds: [PLAN 0.2, connector reach, OPEN-STACK stage 1]
conflicts: none
---
Results land in the project, can be inspected and undone. Each AI batch is grouped, and a log stays on the machine.
Maxon's own design shows the pattern the platform wants: every scene change one undoable step with a plain-words line.

**Use it:** copy the pattern: one undo step plus a history line per platform change.
Transcript support: One prompt built a scene as a single undo step; undo does not cover files on disk [03:30]. (https://www.youtube.com/watch?v=ZKPCE7E56nk [02:41])
Transcript support: Third-party news: MCP off by default, tool groups restrictable, Python execution can be disabled, actions in undo history and local audit log, local LLMs possible; C4D 2026.4 dated 13 Sept 2026 (https://www.youtube.com/watch?v=DbyeC34VoEQ [02:13-02:46])
