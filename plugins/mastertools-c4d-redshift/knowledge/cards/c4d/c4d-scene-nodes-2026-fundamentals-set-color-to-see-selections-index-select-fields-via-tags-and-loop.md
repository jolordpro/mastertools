---
id: c4d-scene-nodes-2026-fundamentals-set-color-to-see-selections-index-select-fields-via-tags-and-loop
title: C4D scene nodes fundamentals - Set Color shows what is selected, selections by index, fields via selection tags, Loop Carve Value for repeated extrusion
domain: c4d
tags: [scene-nodes, set-color, select-facing, loop, fields, procedural-modeling, cinema-4d-2026, deep-read]
applies_to: Cinema 4D scene nodes, 2026 build (video 2026-02-18)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=jdBV7WrrIB8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Mikhail Sedov, uploaded 2026-02-18, part A of a series.
- Add a Set Color node after a selection: Cinema creates a Vertex Color tag, showing which polygons are selected; also readable in Redshift via vertex map [01:05-02:37].
- Select Facing defaults to all; axes plus "and opposite" extrude both sides [03:39-04:12]. Check whether a node reads polygons, points or edges; Chamfer defaults to points, Extrude to polygons [04:43].
- Select by polygon or point index (typed lists such as 7 and 1); order changes after an extrude or bevel, so selections break [05:16-06:47, 21:35].
- Fields: nodes have no direct fields, so make a point/edge selection tag with a Linear field and use it by name; a random selection node is better for animated meshes because noise on moving meshes changes selection quickly [07:55-11:03].
- Loop Carve Value (set to geometry) repeats operations inside by a Range; random selection plus extrude repeated builds abstract hard-surface forms [12:04-17:23]. Large iteration counts or subdividing three times can freeze Cinema [24:10].
- Works as a modifier or as a Nodes Mesh with children; a spline variant exists [26:17].
He points to Dominik Ruckli as the node expert.

**Use it:** A starting set of gotchas for node-based modelling; selection order is the main trap.
