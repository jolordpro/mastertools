---
id: comp-light-group-remix
title: Light-group remix in comp: sum group passes and change gain or colour per light instead of re-rendering
domain: comp
tags: [comp, light groups, remix, relight, gain, aov, beauty]
applies_to: Redshift light groups
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/Light+Group+AOVs.html, src:research-vfx-pipelines]
feeds: [PLAN Phase 1 light match]
conflicts: none
---
A linear sum, so brightness and colour edits per light are exact.
Not possible in comp: moving or reshaping a light, or changing shadows.

**Use it:** prefer a comp remix for brightness or colour notes when light groups exist; re-render only for moved lights.
