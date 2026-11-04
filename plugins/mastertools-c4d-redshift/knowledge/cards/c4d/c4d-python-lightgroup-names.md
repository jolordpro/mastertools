---
id: c4d-python-lightgroup-names
title: Light groups are set through the REDSHIFT_AOV_LIGHTGROUP_NAMES parameter, newline separated
domain: c4d
tags: [python, light groups, redshift, aov, parameter]
applies_to: C4D 2023-2025 threads
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.maxon.net/forum/post/70802, https://developers.maxon.net/forum/post/76522, src:research-gaps-deep]
feeds: [PLAN 0.2]
conflicts: none
---
The names are one string, one group per line. Seen in forum threads, not in documentation.

**Use it:** write and read light groups with this parameter, then verify on a render.
