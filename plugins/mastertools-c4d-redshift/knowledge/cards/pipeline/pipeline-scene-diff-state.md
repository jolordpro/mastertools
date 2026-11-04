---
id: pipeline-scene-diff-state
title: Scene diff is primitive: usddiff is a plain-text diff, BlenDiff and Unity Scene Diff match by content or id, and nothing exists for C4D
domain: pipeline
tags: [scene diff, usddiff, blendiff, unity scene diff, approval fingerprint, stable id]
applies_to: 2026
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://openusd.org/release/toolset.html, https://pypi.org/project/blendiff, src:research-vfx-pipelines]
feeds: [scene diff, approval fingerprint]
conflicts: none
---
C4D files are binary, so the idea is to diff the scene-card JSON by stable object id. Proposal: store the card at approval, report changes in plain words ("key light up 0.4 stops"), and mark the approval stale; fingerprint = card + OCIO config + Redshift version + approved frame.

**Use it:** nobody ships this for C4D.
