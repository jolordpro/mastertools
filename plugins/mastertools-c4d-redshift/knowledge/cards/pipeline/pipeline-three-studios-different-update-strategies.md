---
id: pipeline-three-studios-different-update-strategies
title: Three similar TV-series studios chose three different update strategies: push for static assets, pull everywhere, or switch at animation
domain: pipeline
tags: [pipeline, push, pull, cube creative, woolly, level of detail, library overrides, studio comparison, deep-read]
applies_to: Blender studios (Cube Creative, Autour de Minuit, Normal Animation)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AiRjt7nWcZc, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Cube Creative (Cheeky): push for background components across the whole chain, with LODs exported and linked per shot, chosen by step and camera distance [28:11] [28:42]; pull for animated assets from layout to render [31:21]. They did not trust library overrides then, so assets are appended into shot files and need re-appending per update [31:53] [32:26].
Normal Animation (Woolly Woolly): push for all assets in layout only, then frozen to the latest published version from animation onward (pull); each publish is also saved as a numbered version, e.g. cube_v1 [28:11] [29:13] [30:51].
The third studio (Autour de Minuit, captioned "Ola") pulls at every step, "safety first", linking working versions directly in shots with no publish area. That demands disciplined artists but saves duplicated data [32:26] [32:56] [33:30].
Researchers' summary: same type of show, totally different data flow and philosophy [36:36].

**Use it:** Reference when someone asks whether there is a best pipeline: the same format used three patterns. Match the strategy to team discipline and trust in tools.
