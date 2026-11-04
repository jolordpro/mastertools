---
id: comp-move-to-comp-decision
title: Which fixes can move to comp (light levels, straight-move blur, hard-edged DoF, per-object grade) and which must stay in the render
domain: comp
tags: [comp, decision, motion blur, dof, light groups, cryptomatte, render cost]
applies_to: Redshift to Nuke/AE
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [src:research-vfx-pipelines]
feeds: [PLAN comp-first planner]
conflicts: none
---
Move to comp: light brightness or colour (needs light groups), per-object grade (needs Cryptomatte), straight-move blur (needs vectors), opaque hard-edged DoF (needs clean depth).
Keep in render: moved or reshaped lights, rotation, transparency, glass, hair, reflections of out-of-focus things.
All hypotheses; no published Redshift quality comparison exists. Extra AOVs cost memory and write time (not documented).

**Use it:** score each shot as comp-fix safe from its content, then measure the real gap with ꟻLIP before relying on it.
