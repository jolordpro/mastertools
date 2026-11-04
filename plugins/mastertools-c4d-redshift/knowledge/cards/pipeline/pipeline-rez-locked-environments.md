---
id: pipeline-rez-locked-environments
title: Rez builds a locked, re-evaluable software environment per request and has a time-lock that ignores newer packages
domain: pipeline
tags: [rez, environment lock, package manager, version pinning, reproducible]
applies_to: Rez (Apache-2.0)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/AcademySoftwareFoundation/rez, https://github.com/AcademySoftwareFoundation/rez, src:research-vfx-pipelines, https://www.youtube.com/watch?v=HuV0_AbDgYk]
feeds: [render environment lock]
conflicts: none
---
Each package states its needs; the resolved environment can be saved and re-evaluated later.

**Use it:** store a manifest (C4D, Redshift, plug-ins, OCIO config, textures) per approval; a farm node must match it or say why not.
