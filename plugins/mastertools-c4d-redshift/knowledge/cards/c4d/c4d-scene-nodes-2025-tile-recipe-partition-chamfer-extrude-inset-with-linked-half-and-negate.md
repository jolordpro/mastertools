---
id: c4d-scene-nodes-2025-tile-recipe-partition-chamfer-extrude-inset-with-linked-half-and-negate
title: C4D 2025 scene nodes tile build - Partition, Chamfer, Edge to Line, Extrude Line, Select Facing, Inset, Extrude linked to Divide and Negate
domain: c4d
tags: [scene-nodes, partition, chamfer, inset, extrude, fracture, glass, redshift, cinema-4d-2025, deep-read]
applies_to: Cinema 4D 2025 with Redshift (video 2025-03-25)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=2z2pB3vIbk0, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Taras Makar, uploaded 2025-03-25. Add nodes by pressing C in the node editor and typing the name; drag one on a wire to insert it; Q connects or disconnects the selected node from the output [00:34-02:41].
- Plane 1x1 to Partition (skew 75 percent, gap 0.5 cm) to Chamfer (size 1 cm, 10 subdivisions) to Edge to Line to Extrude Line (direction set to 0,0,1) to Resample (300 points to restore corners) [02:11-07:30].
- Select Facing picks Y faces; "and opposite" takes both sides. Nodes cannot show a selection, so use Store Selection and a material set to that selection tag to preview in red [07:30-10:13].
- Inset (about 35 with 50 percent variation), then Extrude; to keep the inner extrude centered at any depth, read the first extrude offset by Ctrl-clicking its port, feed it through Divide by 2 and Negate into the second extrude's offset [11:17-15:03]. Split with Swap removes the selected faces [15:35-16:07].
- Convert to normal geometry (C), split each piece (U F selection, P), centre axes, put in a Fracture, then a Shader effector (position Y 75, noise 500 percent, speed 0.5, 300 frames, loop period 10, time dependent on) [16:37-20:45]. Shear and Bevel deformers on the group [20:49-23:23].
- Look: dome plus HDRI, camera focal length 300 for near-isometric, glass roughness 0, transmission 1, dispersion; black and white planes behind with primary ray visibility off; rotate the black plane 180 degrees for a loop [23:23-32:42]. He saw odd black glass and suspected a Redshift quirk, not solved [26:05-28:57].

**Use it:** A node-based variant of a broadcast glass-tile look; the linked-value trick generalises.
