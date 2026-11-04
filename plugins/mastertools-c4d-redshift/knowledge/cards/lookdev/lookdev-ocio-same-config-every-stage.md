---
id: lookdev-ocio-same-config-every-stage
title: Use the same OCIO config at every stage including compositing, with EXR as the exchange format
domain: lookdev
tags: [lookdev, ocio, config, exr, comp, colour pipeline, aces, colour management, compositing]
applies_to: any
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/Color%2BManagement%2B-%2BOCIO%2BACES.html, https://www.youtube.com/watch?v=-g6JTD8cge4, src:research-agency-pipelines, src:research-youtube, https://www.youtube.com/watch?v=7e0SSka8Ar8]
feeds: [CHECKS 5]
conflicts: none
---
Maxon's colour management page: one config end to end, EXR between apps.
ASWF talk (Aug 2026) makes the same point: moving a colour transform is not the same as moving a pipeline.
Merged from `redshift-ocio-same-config-everywhere`: The Redshift colour-management page recommends the same OCIO config for render, comp and delivery steps, passing images between them as EXR. Moving a colour transform is not the same as moving a pipeline: a config swapped at one stage gives a mismatch the other stages cannot see.

**Use it:** record the OCIO config id in the approval fingerprint and compare it on the farm and in comp.
