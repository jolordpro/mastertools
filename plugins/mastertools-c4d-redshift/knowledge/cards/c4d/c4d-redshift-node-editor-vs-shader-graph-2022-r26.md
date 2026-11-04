---
id: c4d-redshift-node-editor-vs-shader-graph-2022-r26
title: R26 and Redshift 3.5: the C4D node editor has the better viewport preview and drag-to-insert; the Redshift shader graph keeps multishaders
domain: c4d
tags: [maxon, node editor, shader graph, redshift, materials, R26, deep-read]
applies_to: Cinema 4D R26 / Redshift 3.5 (2022)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Maxon trainers on the two material UIs [54:57-1:09:13]: both build the same material. The C4D node editor shows the selected node's properties in the Attribute Manager, lets you drop a node onto a connection to insert it, has Solo, and since R26 has the improved viewport preview (maxon noise, reflections, textures); the improvements are not in the shader graph. The shader graph keeps properties in the same window and supports multishaders and C4D shaders, which the node editor lacks. Darren prefers the shader graph for that reason and looks at the IPR rather than the preview. The new Standard Material works in both [1:04:44-1:05:36].
Preference: Always Open Node Editor makes a double click open nodes; off gives the classic material editor [1:07:10-1:08:15]. A classic C4D material needs the Standard renderer to create it [1:09:18]. Dated; recheck for each release.

**Use it:** Tell a user to pick the UI by need (multishader or preview) and not by habit.
