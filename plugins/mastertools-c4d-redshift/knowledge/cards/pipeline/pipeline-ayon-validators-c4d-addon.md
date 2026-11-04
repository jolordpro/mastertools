---
id: pipeline-ayon-validators-c4d-addon
title: AYON validators are classes with a family, order and optional on/off switch; AYON's C4D addon only publishes cameras, Alembic caches and workfiles
domain: pipeline
tags: [ayon, openpype, validator, cinema 4d addon, universal publisher, tray publisher]
applies_to: AYON, Oct 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://help.ayon.app/articles/7284251-working-with-ayon-in-cinema4d, https://docs.ayon.dev/ayon-maya/latest/autoapi/client/ayon_maya/plugins/publish/validate_animation_rig_content.html, https://github.com/ynput/ayon-core, src:research-vfx-pipelines]
feeds: [validator engine design]
conflicts: none
---
Open core is Apache-2.0 with per-DCC addons and a server; a Tray Publisher works without the DCC open. The C4D addon lists camera, pointcache and workfile publishing plus loaders for cameras, pointcaches and XRefs. No C4D validators or render publishing were listed.

**Use it:** a C4D validator suite with pixel checks fills a real gap; match AYON's validator shape so studios can read it.
