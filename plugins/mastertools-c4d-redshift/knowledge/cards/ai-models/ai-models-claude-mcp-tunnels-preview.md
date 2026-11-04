---
id: ai-models-claude-mcp-tunnels-preview
title: Claude MCP tunnels (research preview) let Claude reach a private MCP server with no inbound ports, using cloudflared
domain: ai-models
tags: [claude, mcp tunnels, cloudflared, private mcp, studio, preview]
applies_to: research preview, Oct 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview, src:research-frontier-ai]
feeds: [PLAN 3, agent door]
conflicts: none
---
A studio's private MCP server becomes reachable by Claude without opening inbound ports; runs on cloudflared. Not zero-data-retention eligible.

**Use it:** candidate way to put the platform's brain behind a studio firewall.
