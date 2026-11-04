---
id: redshift-usd-cli-render-2027
title: Redshift's USD command-line renderer (redshiftUsdCmdLine, since 2025.2.0) renders .usd files without a DCC, but is built for Solaris scenes
domain: redshift
tags: [usd, command line, headless, shutter, redshiftusdcmdline, solaris, redshift 2025.2, redshift 2027, farm]
applies_to: Redshift 2025.2.0 and later; 2027.0 notes add frame and shutter handling
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/USD+Command+Line.html, https://digitalproduction.com/2026/10/19/redshift-2027-memory-fur-live-rendering/, src:research-gaps-deep]
feeds: [PLAN 0A spike, Phase 3]
conflicts: none
---
The tool is not new in 2027: Maxon's release notes add it in 2025.2.0. It ships inside Redshift, Mac included, and needs no Houdini or other DCC installed.
Maxon's page says it was built for SideFX Solaris scenes; scenes from other DCCs are supported only once those DCCs support the full Redshift USD pipeline. So a C4D USD export is not promised to render (checked 2026-10-31; ledger §9 row).
Per the 2027 coverage, it treats Start/End as absolute frames, uses the stage's default render settings and reads shutter attributes. Rendering C4D work without C4D this way is untested.
Material appearance differs in C4D's USD export (see the C4D card on Redshift material approximations).

**Use it:** test one scene through both paths before any USD farm plan.
