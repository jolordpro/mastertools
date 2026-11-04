---
id: c4d-mcp-community-kumo-bridge
title: The community server kumoproductions/mcp-cinema4d offers 72 tools in 17 groups, including render and exec_python
domain: c4d
tags: [mcp, community, kumo, bridge, exec python, take_override, graph description, mcp-cinema4d, community bridge, tools, cinema 4d, exec_python]
applies_to: unknown version
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://github.com/kumoproductions/mcp-cinema4d, src:research-gaps-deep]
feeds: [PLAN 0.2, connector reach, OPEN-STACK stage 1, connector test, PLAN 3]
conflicts: none
---
Not Maxon's. Tools include render, preview_render, exec_python, take_override, apply_graph_description, dump_shader and set_params, with no Redshift-specific or AOV tools. It connects through a Python plugin inside a running C4D over TCP.
Merged from `pipeline-kumo-community-mcp`: It connects through a Python plugin inside a running C4D over TCP.
Merged from `ai-models-kumo-mcp-cinema4d-bridge`: Tools include render, preview_render, exec_python, take_override, apply_graph_description, dump_shader, set_params. Connects over TCP through a Python plugin inside a running C4D (so not headless).

**Use it:** a reference for what an MCP bridge can expose, not a dependency.
