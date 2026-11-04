---
id: pipeline-ocio-v2-app-upgrade-needs-feature-work
title: Upgrading an app to OCIO v2 is easy, but user-facing benefits need the app to adopt the new features
domain: pipeline
tags: [ocio, dcc, upgrade, gpu api, menus, deep-read]
applies_to: OpenColorIO v2 (2020 preview, feature complete Aug 2020)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7e0SSka8Ar8, src:yt-transcripts]
feeds: []
conflicts: none
---
Old configs keep working and updating an app is meant to be simple; only the GPU API changed a lot because multiple textures must be uploaded [47:07]. Two steps: get running for better precision, then implement new features (menus, rules, display spaces); many user-experience gains depend on that second step [47:39-48:42]. Python bindings were rewritten with Pybind11, NumPy-aware [06:16-07:19].

**Use it:** If a tool 'supports OCIO v2' but still shows a 300-item menu, it only did step one.
