---
id: pipeline-gaffer-mcp-and-limits
title: Gaffer 1.7.5 (22 Oct 2026) ships an MCP server; the BSD node app supports Arnold, Cycles, 3Delight and RenderMan but not Redshift
domain: pipeline
tags: [gaffer, mcp, node graph, image engine, dispatcher, tractor, flamenco, comp, headless, bsd, self-check]
applies_to: Gaffer 1.7.5
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://github.com/GafferHQ/gaffer/releases/tag/1.7.5.0, https://www.gafferhq.org/, https://www.gafferhq.org/documentation/1.7.6.0/index.html, src:research-vfx-pipelines]
feeds: [comp-fix runner, agent door]
conflicts: none
---
`gaffer mcp` lets a model run Python, screenshot the UI and capture image-node output to check its own work. Task nodes plus dispatchers (Tractor, Flamenco) turn a graph into farm jobs. Built on OpenEXR, OIIO, OCIO, OSL.
Merged from `ai-models-gaffer-mcp-server-1-7-5`: Gaffer is a BSD node app for look-dev, lighting and comp, built on OpenEXR, OIIO and OCIO; it does not support Redshift but comp fixes only need EXR files. Autograph 2027 is also reported to have an MCP server (reseller page).

**Use it:** its image nodes could run comp fixes headless on EXRs, since those need no Redshift.
