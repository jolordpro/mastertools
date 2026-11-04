---
id: ai-models-agent-built-scene-needs-dimension-check
title: An agent built a room from a sketch with cube primitives, got a 540 cm wall against a 530 cm brief, and attached images waste tokens
domain: ai-models
tags: [agent, scene build, gemini, sketch, dimensions, primitives, tokens, verification]
applies_to: NanoPro 2, Gemini agent
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=R285PFittEA, src:yt-transcripts]
feeds: [shakedown, coach]
conflicts: none
---
Gemini wrote a script for a bedroom from a hand sketch [G 00:33-01:03]. Check by measuring: inside wall was 540 not 530, TV shelf 500 exact; the agent made the walls thicker unprompted. Everything was cubes unless told otherwise.
Remove unused reference images from the tab before agent edits, or tokens and time are wasted [05:49]. High reasoning was not needed for a simple instancing rename task [06:19].

**Use it:** any agent-built scene gets a dimension check against the brief; the platform's agent prompts strip unneeded images.
