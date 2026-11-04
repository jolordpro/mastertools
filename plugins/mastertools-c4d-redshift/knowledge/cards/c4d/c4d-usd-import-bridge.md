---
id: c4d-usd-import-bridge
title: Opening a USD in C4D creates a bridge with locked hierarchy; 2027 docs say edits can be written back without overwriting the file
domain: c4d
tags: [usd, import, bridge, hierarchy, c4d 2027]
applies_to: C4D 2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/html/78533.html, src:research-agency-pipelines, src:research-vfx-pipelines]
feeds: []
conflicts: none
---
The USD import is a bridge that keeps USD objects apart from native ones; the hierarchy is locked. Write-back behaviour is from the 2027 help only.

**Use it:** do not expect to restructure an imported USD stage inside C4D.
