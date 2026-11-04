---
id: ai-models-dcc-mcp-agent-renames-objects-and-builds-small-tools
title: The same MCP agent renamed meaningless objects from shape and position, organised lights into mood collections, and wrote a switcher panel (with a bug)
domain: ai-models
tags: [mcp, blender, claude, python, scene cleanup, rename objects, lighting collections, plugin generation, deep-read]
applies_to: Blender MCP, Claude Sonnet
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=r7H60u0kHRA, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
Translating Chinese object names to English changed little; the useful step was asking it to rename cubes by shoe anatomy (laces, tongue, collar foam), which it inferred from position and dimensions [05:42][06:12][06:43]. He calls it instant for a job that takes hours at scale [07:14]. Lighting: it grouped the existing rig into a collection, duplicated it three times and varied it by mood [08:50][09:20]. A prompt for a Python panel to switch HDRI plus its matching light collection produced a plugin, but the collection switch did not work and needed troubleshooting [09:51][10:22][10:53]. Limits stated: modelling from scratch gives primitives; animation and geometry nodes are weak; code runs hit usage limits fast [14:32][15:03].

**Use it:** good first uses of an MCP agent in C4D: rename, group and light-variation housekeeping, with a human fixing the last bugs.
