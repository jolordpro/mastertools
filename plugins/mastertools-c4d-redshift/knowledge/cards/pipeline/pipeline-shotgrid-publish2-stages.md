---
id: pipeline-shotgrid-publish2-stages
title: ShotGrid's publisher runs three stages (collection and acceptance, item review, publishing) and can run validation only
domain: pipeline
tags: [shotgrid, flow, tk-multi-publish2, publisher, hooks, validate]
applies_to: tk-multi-publish2
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.shotgridsoftware.com/tk-multi-publish2/, src:research-vfx-pipelines]
feeds: [validator engine design]
conflicts: none
---
Plug-ins accept items, then run validate, publish and finalize passes. Three hooks: collector, publish plug-in, post-phase. The artist sees the validation list and can run it alone.

**Use it:** offer a "check only" run that changes nothing.
