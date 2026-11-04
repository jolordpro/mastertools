---
id: c4d-bake-polyfx-explosion-to-alembic-from-connect-without-weld
title: To cache a PolyFX or field explosion as Alembic, bake from a Connect object with Weld off; welding changes the point count, which Alembic cannot stream
domain: c4d
tags: [alembic, bake, polyfx, connect object, weld, point count, cache, fields, explosion, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Trainer (Nosman; captions render Alembic as "Olympic"). PolyFX plus a linear field and a randomised plane effector gives a quick explosion of polygons on an icosahedron [17:32-19:06]. To play it in real time: right-click the object, Bake as Alembic. For several objects put them under one Connect object and bake that, because Alembic holds hierarchy [19:39-20:10].
Remove Weld on the Connect object first: welding merges points and the point count then varies per frame [20:10-21:12]. In the Alembic preview, red markers flag varying point count; green means points are retained. An untitled project makes the bake ask for a folder; a saved project writes an alembic folder beside it [20:42].

**Use it:** Before sending a field-driven effect to a farm, bake it to Alembic from a Connect with Weld off and check the point counts show green.
