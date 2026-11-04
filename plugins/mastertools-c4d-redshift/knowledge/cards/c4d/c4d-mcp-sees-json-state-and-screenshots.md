---
id: c4d-mcp-sees-json-state-and-screenshots
title: The C4D MCP shows the assistant scene state as JSON text, plus viewport screenshots and renders on request
domain: c4d
tags: [mcp, json, screenshot, viewport, render, tool count, multiple c4d instances]
applies_to: C4D 2027.0 MCP
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[02:35:32] He says the module has about 68 ways (rules) to interact with Cinema; counted by memory, not checked. The assistant reads lists of materials, objects and parameters as a text document [02:36:03].
It can request a viewport screenshot or render and view it as an image [02:36:03].
Trick [02:30:52]: duplicate the C4D executable and give each copy its own preferences folder so one install talks to Claude Desktop and another to ChatGPT; unsure whether this works on Mac.

**Use it:** the platform should expect text-based scene reads, not pixel access, unless a render is requested.
