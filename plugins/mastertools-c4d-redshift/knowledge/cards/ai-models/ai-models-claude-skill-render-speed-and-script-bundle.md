---
id: ai-models-claude-skill-render-speed-and-script-bundle
title: A Claude skill for Redshift speed asks questions first, builds a new render setting, was tuned for hours on a test scene, and can ship a script
domain: ai-models
tags: [claude skill, redshift speed, render settings, test scene, exploded view, controller null, user data]
applies_to: Claude skills with C4D MCP (Oct 2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ysIL6NORGIo, src:yt-transcripts]
feeds: [plan, coach]
conflicts: pipeline-greyscalegorilla-claude-skills-signal
---
[1:00:17] The skill asks how much grain is acceptable and how photoreal, checks animation range for motion blur, and writes a new render setting rather than touching the original [1:01:50].
[1:01:19] It built its own test scene with volumes and subsurface and iterated render, check time, change setting for hours.
[1:03:52] Skills can include a C4D script that adds a controller null with user data (speed, randomness).

**Use it:** mirror the ask-first pattern and never overwrite the user's settings.
