---
id: ai-models-dcc-mcp-agent-metadata-json-per-part-drives-assembly
title: An MCP agent assembles a product from pre-made parts when each part carries JSON metadata tags (comfort, urban, stylish)
domain: ai-models
tags: [mcp, blender, claude, metadata, json, procedural assembly, creative agent, parts library, deep-read]
applies_to: Blender MCP (ahujasid), Claude Desktop
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=r7H60u0kHRA, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
Demo: an abstract prompt (a shoe for a marathon runner at a named university) made the agent pick the trainer base model, toggle collections, set the school colours on pre-made materials (fly-knit, carbon, textile, each with noise and bump already built), and print its rationale [01:32][02:35][03:08]. Why it works: each part has a JSON metadata file attached to the object data; the agent matches prompt words to tags, e.g. comfort and endurance for a marathon, urban and fashion for stylish [07:46][08:18]. Selected-part edits ("make this part metallic gold") and named edits ("laces to gold") then work [03:39][04:09]. Presenter stresses that existing 3D skill is what makes it useful [10:53].

**Use it:** for any parts library or template platform, tag assets with machine-readable metadata so an agent can compose them.
