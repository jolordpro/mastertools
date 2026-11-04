---
id: pipeline-bowerbot-asset-validation-and-modes
title: BowerBot checks every asset package for wrong units, outside dependencies and bad structure, and runs standalone or as an MCP server
domain: pipeline
tags: [bowerbot, usd validation, units, self-contained, mcp server, litellm, aswf]
applies_to: BowerBot 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=opfHGm0lWyM, src:yt-transcripts]
feeds: [agent door, asset checks]
conflicts: none
---
Output is a self-contained ASWF-compliant asset folder; the scene file keeps references only [06:37-06:48]. Agent mode uses LiteLLM with OpenAI, Anthropic or local models; MCP mode lets Claude Desktop, Cursor or VS Code drive the same tools [05:45-06:17].

**Use it:** Reuse the units, dependency and structure checks as the template for platform asset checks.
