---
id: ai-models-gemini-video-modes-fps-tokens
title: Gemini's static video mode samples about 1 frame/s and misses fast motion; agentic mode saves up to 88% tokens on long clips
domain: ai-models
tags: [gemini, video understanding, agentic video, 1 fps, timestamps, tokens]
applies_to: Gemini 4 Argon
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://ai.google.dev/gemini-api/docs/video-understanding, src:research-frontier-ai]
feeds: [OPEN-STACK stage 6]
conflicts: none
---
The research suggests asking for timestamped observations and checking each against measured flow and keyframe curves, dropping notes that disagree.

**Use it:** never let a video model's motion note stand without a measured check.
