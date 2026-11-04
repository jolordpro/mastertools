---
id: lookdev-c4d-plywood-edge-thicken-shell-selection-and-cube-projection
title: Parametric plywood: a Thicken generator with a shell selection gets a ply-edge material, cube-projected so no UVs are needed
domain: lookdev
tags: [cinema 4d, thicken, plywood edge, selection tag, cube projection, parametric, redshift, deep-read]
applies_to: Cinema 4D
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=UjThhVMuV18, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
A plane made 4 ft square under a Thicken at 1 in height; the Thicken's own selections (shell, PB) let a different material sit on the edge [09:51][10:23][10:56]. Veneer for the top and bottom, plywood-edge material only on the shell selection [11:26][11:56]. Mapping is wrong at first; switch the projection to cube and scale the texture down until a few plies show, so there is no UVing and the object can be resized without stretching [12:27][12:58][15:03]. A displace deformer with shading noise gives imperfect edges, with subdivision raised only as needed [15:35][16:06].

**Use it:** parametric stand-ins for wood or board edges that need to stay editable.
