---
id: lighting-four-role-kit
title: Blender Studio light kit: only four light roles (key, key-soft, fill, rim), one colour per role, shared by every shot
domain: lighting
tags: [lighting, light rig, light kit, key, fill, rim, consistency, sequence, blender studio, key fill rim, lighting guide, shot consistency]
applies_to: any
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://studio.blender.org/tools/artist-guide/shot-production/lighting, src:research-vfx-pipelines, src:research-production-pipelines]
feeds: [PLAN sequence drift check, sequence drift check]
conflicts: none
---
Roles: key, key-soft, fill, rim. One RGB value per role per scene, kept in a library file linked into each shot.
Keep light direction consistent through a scene and track it with a direction chart; each shot must match its neighbours in intensity, colour and style.
When lighting is approved, switch quality from preview to final before the farm.
Merged from `pipeline-blender-studio-light-kit`: Keep the colours in a library file linked into shots, track direction on a chart, light key shots first (close-ups and inserts follow from the wide), start lighting only after a blocking pass and basic shading exist, and switch quality from preview to final before the farm.

**Use it:** use the four roles as the template for a project light kit and compare each shot's roles with the approved key shot.
