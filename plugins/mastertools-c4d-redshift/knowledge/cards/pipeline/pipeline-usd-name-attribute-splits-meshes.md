---
id: pipeline-usd-name-attribute-splits-meshes
title: A name attribute on polygons becomes separate USD mesh prims when geometry is exported
domain: pipeline
tags: [usd, export, name attribute, mesh, packed, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
Three pieces named pig, Tommy and toy and merged were written as three meshes in the file [06:14-07:48]. The same happens on SOP create: spikes and grid arrive as two mesh prims you can select and move separately [1:07:39-1:08:09]. Re-importing gives packed USD (one point with the data) to save memory; unpack USD gives one packed prim per name, and unpack to polygons gives editable geometry back [07:48-08:52].
The import path prefix defaults to the importing node's name and can add a parent xform to group results [1:04:31-1:05:34].

**Use it:** Name parts before export so downstream departments get separate prims they can assign materials to.
