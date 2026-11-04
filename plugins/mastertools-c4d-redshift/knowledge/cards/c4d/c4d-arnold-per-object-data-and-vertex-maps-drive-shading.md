---
id: c4d-arnold-per-object-data-and-vertex-maps-drive-shading
title: Feed MoGraph colour, user data and vertex maps (curvature from Houdini) into the shader instead of one material per object
domain: c4d
tags: [manuel-casasola-merkle, mograph, vertex map, curvature, worn edges, user data, houdini engine, arnold, deep-read, polish]
applies_to: Arnold C4DtoA (2015); idea portable to Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sxNf7Ei5Ezc, src:yt-transcripts, src:polish-roster]
feeds: [coach]
conflicts: none
---
Speaker: Manuel Casasola Merkle. The cloner writes its colour into each object's display colour, which Arnold reads by name; any plugin or Python tool can set that field and a user-data shader reads it [28:54-32:04].
User data is per object. Vertex maps carry a float per point, so a gradient can remap them to colour, or three maps can stand for R, G and B [32:04-33:17].
For worn edges he computed surface curvature in a Houdini asset (through the Houdini engine) and returned it as a vertex map, shaded by dragging the map name into a vertex map shader. A stretch tag also makes maps [33:52-35:58].

**Use it:** When an asset needs worn edges or varied colour across clones, bake the driver (curvature, random, field) to data the shader reads, rather than splitting objects.
