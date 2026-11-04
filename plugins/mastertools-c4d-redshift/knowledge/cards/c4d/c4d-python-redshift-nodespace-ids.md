---
id: c4d-python-redshift-nodespace-ids
title: Redshift node graphs are reached in Python through the nodespace id com.redshift3d.redshift4c4d.class.nodespace
domain: c4d
tags: [python, maxon api, redshift, node material, nodespace, setportvalue, connect]
applies_to: C4D 2024+ (docs 2027.0.0)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.maxon.net/docs/py/2027_0_0/examples/nodes/nodes_material_create_redshift.py.html, src:research-gaps-deep]
feeds: [PLAN 0.2]
conflicts: none
---
Node ids look like com.redshift3d.redshift4c4d.nodes.core.standardmaterial. Ports are set with SetPortValue and wired with Connect inside a transaction. Port ids must be looked up in the Node Editor with id display on. Port get/set methods exist from 2024.0; older names differ.
The official example is one small graph.

**Use it:** build a port-id table once per version rather than hard-coding from memory.
