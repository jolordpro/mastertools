---
id: c4d-moextrude-layers-each-driven-by-its-own-plane-effector-and-one-shared-linear-field
title: C4D MoExtrude layered by Ctrl-drag, each layer cancelled by its own Plane effector, all sharing one Linear field to animate
domain: c4d
tags: [mograph, moextrude, plane-effector, linear-field, effectors, redshift, cinema-4d-2023, deep-read]
applies_to: Cinema 4D 2023 with Redshift (Greyscalegorilla, Feb 2023)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=7-q1JKG8638, src:yt-transcripts]
feeds: [motion-critique, coach]
conflicts: none
---
Greyscalegorilla (Nick), uploaded 2023-02-07.
- MoExtrude extrudes every polygon of the object, so more polygons mean more extrusions; it can sit directly on a primitive without making it editable, so the cube can be swapped later [00:32-01:34, 04:11].
- Layer them: Ctrl-drag a MoExtrude below itself to duplicate; test used one step of 5 cm with 0.7 scale, then smaller second and third layers (second scaled to 0.5 so the third does not touch) [02:36-03:40].
- To animate: one Plane effector per MoExtrude, added with the MoExtrude selected so it connects automatically; set it to Z with the same amount negative (5 cm extrude, Plane Z -5 cm returns the plain cube). Go further (about -6, or -2.1 for subtle) to cut into the object [06:17-09:24]. Copies need to be dragged into each MoExtrude's effector list [07:49-08:52].
- Add one Linear field to all three Plane effectors (same field); length about 13; move it through the object to go from extruded to flat. Any field (random, delays) works the same way [09:55-11:59].
- Name MoExtrudes 0, 1, 2 so the pairing is obvious [06:17].

**Use it:** A non-destructive animated panel or tile reveal where one field is the only control.
