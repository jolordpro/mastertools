---
id: lookdev-approval-fingerprint
title: Approval fingerprint idea: hash scene card, OCIO config, Redshift version and approved frame to show which approvals a change voids
domain: lookdev
tags: [lookdev, approval, fingerprint, drift, scene diff, version, ocio]
applies_to: any
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [src:research-vfx-pipelines, https://github.com/AcademySoftwareFoundation/rez]
feeds: [PLAN render environment lock]
conflicts: none
---
Diff the scene card as JSON by stable object id, not by name; the .c4d file is binary.
usddiff is a plain text diff and no C4D scene diff tool was found. All of this is proposal, not practice.

**Use it:** report changes since approval in plain words (for example key light up 0.4 stops) and mark the approval stale.
