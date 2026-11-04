---
id: c4d-2026-3-new-uv-editor-uses-viewport-axes-soft-selection-and-live-size
title: The 2026.3 UV editor is rebuilt on viewport technology: no UV gizmo, normal move/scale/rotate axes with quantize, soft selection, a live bounding-box size readout, and a UDIM-aware tile grid
domain: c4d
tags: [uv editor, 2026.3, udim, soft selection, coordinate manager, axis, viewport technology, maxon, deep-read]
applies_to: Cinema 4D 2026.3 UV editor (Maxon Training Team, Noseman, Jul 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fsFbFDtLDT0, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Noseman (Athanasios Posansis, Maxon Training Team), Cinema 4D 2026.3, uploaded Jul 2026 [00:00-06:28]. The editor was rewritten around the viewport engine, so modeling tools work in UV space. The old UV gizmo is gone; use the regular axes: arrows move (quantizing available), Shift scales on one or both axes, rotation bands rotate, axis mode can be moved to rotate about another point [04:21-05:24]. Soft selection works in UV space with its own radius [05:24-05:57]. The Coordinate Manager is live and shows the selection's bounding-box size; in this build it displayed values ten times too big, so read the numbers divided by ten (a bug he notes) [05:57-06:28].
Tile colours show UDIM numbering; UDIM allows 10 tiles across and about 99 up, and islands in the red zone are invalid tiles [03:47-04:21].

**Use it:** For UDIM work in 2026.3, check tile colours before packing; treat the coordinate readout as 10x in this early build.
