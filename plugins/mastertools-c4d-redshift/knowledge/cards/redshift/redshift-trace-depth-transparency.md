---
id: redshift-trace-depth-transparency
title: Transparency has its own depth and is not capped by Combined depth; it is cheaper than refraction
domain: redshift
tags: [trace depth, transparency, refraction, combined depth, glass, per material]
applies_to: Redshift 3.0+, 2026-2027
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/html/VPRSRENDERER-REDSHIFT_RENDERER_TAB_GLOBALS.html.md, src:research-agency-pipelines]
feeds: [CHECKS 7]
conflicts: none
---
Transparency depth was added in Redshift 3.0; set it equal to refraction depth to match older scenes. It is not limited by Combined depth and costs less than refraction. Materials can override depths.
Evidence is a search summary of the Maxon Globals page. The ledger states Combined caps reflection and refraction (section 5, carried).

**Use it:** before raising refraction depth for a see-through panel, ask whether transparency will do.
