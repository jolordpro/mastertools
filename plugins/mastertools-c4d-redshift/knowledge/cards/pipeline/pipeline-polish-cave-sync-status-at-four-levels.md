---
id: pipeline-polish-cave-sync-status-at-four-levels
title: "CAVE syncs status at four levels, asset or shot, discipline, version and publish, and sends clients only near-final work"
domain: pipeline
tags: [cave academy, shotgrid, status sync, discipline, asset status, client delivery, polish, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://caveacademy.com/wiki/production/production-statuses/, src:polish-roster]
feeds: [pipeline]
conflicts: none
---
In ShotGrid status can be set on the asset or shot, each discipline (model, texture, rigging, animation, lighting), each version, and the published file [§6]. Triggering FINAL on the asset or shot should set PUBLISHED-FINAL on the discipline and publish status [§6]. Publish statuses should sync with discipline statuses so the shot page shows every discipline's state [§7]. Clients get close-to-final assets or shots, not blocking files, unless a client asks to see earlier [§6].

**Use it:** When a user tracks status, keep all four levels in step and show clients only work at final-candidate stage.
