---
id: ai-models-mcp-spec-2026-07-28
title: MCP spec 2026-07-28 adds MCP Apps (server-shipped UI), Tasks (long calls with a handle) and auth hardening
domain: ai-models
tags: [mcp, model context protocol, mcp apps, tasks, linux foundation, spec]
applies_to: MCP 2026-07-28
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://dev.to/rcsxplatform/mcp-just-grew-up-what-the-2026-07-28-spec-actually-means-3f71, src:research-frontier-ai]
feeds: [agent door]
conflicts: none
---
Stateless core; Tasks let a long call be polled, updated or cancelled; governed by the Linux Foundation. The only source is a blog.

**Use it:** a render job fits the Tasks pattern; report UI could ship as an MCP App.
