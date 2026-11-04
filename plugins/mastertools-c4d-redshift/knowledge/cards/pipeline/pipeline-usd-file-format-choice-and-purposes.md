---
id: pipeline-usd-file-format-choice-and-purposes
title: Use usda for small readable assemblies, usdc for heavy data, usdz to ship one self-contained asset, and proxy purposes for fast viewports
domain: pipeline
tags: [usd, usda, usdc, usdz, purpose, proxy, render purpose, draco, hydra, render delegate, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=TLJPDt4YpYM, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
From the Q&A [28:59-30:24]: usda is text, for small data like assemblies you want to search; usdc is binary and optimised for large data; usdz is a package holding usda, usdc and textures for transport (Apple AR). Draco geometry compression exists but the consumer must support it [36:46-37:16].
Keating suggests a reduced proxy purpose for GL and lighting, and a full-resolution render purpose pulled only at render time [37:48-38:19].
Hydra lets any viewport use any installed renderer (Storm, RenderMan, others); renderer-specific shader data goes in render-context namespaces [06:49-08:25, 40:33-41:06]. No standard rigging schema exists; studios write their own [33:33].

**Use it:** Export plan for C4D USD: proxy for viewport, full for render; usdc for caches.
