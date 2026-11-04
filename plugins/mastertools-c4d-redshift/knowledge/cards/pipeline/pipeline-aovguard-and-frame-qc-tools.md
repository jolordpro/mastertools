---
id: pipeline-aovguard-and-frame-qc-tools
title: Frame QC that exists: missing-frame scripts (Ramma, Nuke, Render Copilot), EXR-Tools (alpha), and AOVGuard, a thesis tool for missing or empty AOVs, NaN/inf and size mismatch
domain: pipeline
tags: [aovguard, exr tools, missing frames, ramma, render copilot, qc]
applies_to: 2026
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://nccastaff.bournemouth.ac.uk/jmacey/MastersProject/MSc26/07/, https://www.nukepedia.com/tools/python/render/rendercopilot/, https://github.com/xoaocardoso/EXR-Tools/releases, src:research-agency-pipelines]
feeds: [frame checks]
conflicts: none
---
Missing, dropped or corrupt frame detection is cheap and solved. AOVGuard (Bournemouth MSc, tested on Maya/Arnold) is a CLI with JSON/HTML output, not a shipped product, and checks per file, not across frames. EXR-Tools is an alpha GitHub release.

**Use it:** borrow AOVGuard's check list; add the temporal checks it lacks.
