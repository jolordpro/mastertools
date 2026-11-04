---
id: ai-models-claude-code-plan-first-then-execute-then-commit-each-state-that-matches-the-vision
title: Claude Code workflow: ask for a plan (Shift+Tab), review it, execute, and commit each state that matches the vision, since agents can delete or rename files
domain: ai-models
tags: [claude code, plan mode, execute, commit, git, non-deterministic, front end first, maria panneer rajan, deep-read]
applies_to: Claude Code (Apr 2026 video)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=8kL1Ae9AWWs, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Same video [05:09-11:28]. Direct execution of a vague request ("modern, minimal") can go many ways because agents are non-deterministic. Switch to plan mode with Shift+Tab, review the plan (it may ask questions), take your time on a complex build, then approve and execute [05:41-07:43].
Scope the first pass: front end only, no back end. Then small fixes by prompt; here the video player showed only audio, so she asked for video and a scrub timeline and renamed "task" to "discipline" [07:43-09:53].
Commit as soon as something matches the vision, because agents can remove or rename files; she has Claude create the GitHub repo and push [09:53-11:28]. Iterate between plan and execute whenever a big change appears.

**Use it:** a safe loop for scripts and pipeline tools: plan, execute, check, commit.
