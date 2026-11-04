---
id: c4d-usd-export-contents
title: C4D's USD export writes geometry, keyframed animation, cameras and materials, but not CMotion animation
domain: c4d
tags: [usd, export, cmotion, keyframes, cameras, materials, c4d usd, usd export, bridge, redshift 2027, command line]
applies_to: C4D 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2026/en-us/Content/html/FUSDEXPORTER.html, https://help.maxon.net/c4d/2027/en-us/Content/html/FUSDEXPORTER.html, src:research-agency-pipelines, src:research-gaps-deep, src:research-vfx-pipelines, https://help.maxon.net/c4d/2027/en-us/Content/html/78533.html, https://digitalproduction.com/2026/10/19/redshift-2027-memory-fur-live-rendering/]
feeds: [OPEN-STACK stage 1, PLAN USD stance]
conflicts: none
---
Only keyframed animation is written; CMotion is not. Studio adoption of USD for C4D motion work has no evidence in the research.
Merged from `pipeline-c4d-usd-limits`: Redshift materials export as Standard/Physical-style approximations; Maxon warns the look differs. Opening a USD makes a bridge with locked hierarchy (2027 docs say edits can be written back without overwriting). Redshift 2027.0 USD command-line render reads absolute frames and shutter attributes, hinting at rendering without C4D; untested. No studio use of USD for C4D motion work was found.

**Use it:** keep USD as an input to read, not a core path.
