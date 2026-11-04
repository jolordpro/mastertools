---
id: ai-models-mcp-resources-vs-tools-schema-validation-and-transports
title: MCP servers expose resources (read, no side effects) and tools (actions), validate arguments with a schema, and run over stdio locally or SSE/HTTP in the cloud
domain: ai-models
tags: [mcp, model context protocol, resources, tools, zod, stdio, sse, claude desktop config, server, deep-read]
applies_to: MCP TypeScript SDK (Mar 2025)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=HyzlYwjoXOQ, src:yt-transcripts]
feeds: [pipeline design, coach]
conflicts: none
---
Fireship (Code Report, 31 March 2025, sponsored video): MCP is a standard way to give an LLM context, likened to a USB-C port; a client (Claude Desktop) talks to a server over a transport [00:32][02:06]. Two main primitives: resources, roughly GET-like, a name, a URI and a callback that fetches data, and must have no side effects or computation; and tools, actions like a write, roughly POST-like [02:36][04:41]. Define argument shapes with a schema library such as Zod plus descriptions so the model fills arguments reliably instead of inventing them [04:09][05:13]. Run via stdio locally; for cloud use server-sent events or HTTP [05:44]. Client: add a command entry to the developer config, restart, and permissions are asked before writes [06:15][06:47]. Many servers are just APIs on top of existing APIs, which makes models swappable [05:13]. Hype claims about AI-written code in the video are opinion, skip.

**Use it:** design rule for a platform MCP: read-only status as resources, anything that submits or changes as tools with typed arguments.
