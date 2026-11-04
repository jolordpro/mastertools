---
id: comp-light-group-rebuild-division
title: Rebuilding light groups by subtraction misbehaves, division is more stable, and mixing groups with material AOVs clashes
domain: comp
tags: [comp, light groups, aov, rebuild, subtraction, division, compositing mentor]
applies_to: Redshift light groups
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, src:research-youtube, https://www.youtube.com/watch?v=ir1x8Si9A8k]
feeds: [PLAN Phase 1]
conflicts: none
---
From the CompositingMentor video page (2025-05-27, the AOV Paradox); no transcript was readable, so the detail is thin.
Takeaway: do not mix light groups and material AOVs in one rebuild.

**Use it:** keep the sum-to-beauty check separate from any material-AOV rebuild.
