---
id: c4d-ai-assistant-can-build-a-reusable-python-generator-tool-in-steps-with-the-maxon-mcp
title: Maxon's 2026-10 demo: ask the assistant for a knurl on selected polygons, then a reusable Python generator, then fix issues one prompt at a time
domain: c4d
tags: [maxon, jonas, claude, mcp, ai assistant, python generator, knurl, asset browser, reusable tool, cinema 4d 2026, deep-read]
applies_to: Cinema 4D with the MCP server (video uploaded 2026-10-01); build not stated
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=HxNqQKx0NWc, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Jonas from Maxon. Steps: describe the end goal and a file rule in the first prompt (any extra files go next to the current scene, which he always adds so files do not land elsewhere) [00:33-01:03]. Check the result in the viewport, then ask for a reusable modifier; the assistant asks whether to make a nodes modifier or a Python generator, he picks Python generator [01:03-01:38].
Generated user data: polygon selection input, subdivisions, depth, pattern (straight or diamond), invert, fix border [01:38-02:43]. He tests every control, including removing edge loops and updating the selection [03:16-03:46].
Fix rounds, one prompt each: (1) the knob vanishes when the generator is deactivated and it needs the taper as child of the knob [03:16-04:18]; (2) only the first child works, so ask for multiple children [04:49]; (3) a plane child with a named selection fails, so ask for all child objects [06:28-07:01].
Finish: ask for an icon in C4D colours and to save to the database; it lands under Uncategorized in the Asset Browser [07:31-08:04]. Cleanup he did: a leaked selection name in the input field, then add a new version with the plus button [08:04-08:34]. Custom databases on a network drive share it with a team [09:04].
The model name in the captions reads 'Opus 5.5 on Medium'; treat as unverified.

**Use it:** for in-house tools, ask for small steps, test each parameter, then save to a shared database; the existing MCP cards cover the switch-on and safety.
