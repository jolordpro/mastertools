---
id: c4d-2026-3-uv-seam-tag-mark-as-seam-and-relax-needs-an-open-edge
title: Seams now live in a dedicated seam selection tag (right-click, Mark as Seam); unwrap and relax cut along the seams without a live selection, and a watertight mesh with no seams gives an error
domain: c4d
tags: [uv seams, seam tag, mark as seam, seam selection tool, unwrap, relax, abf, watertight, error, 2026.3, deep-read]
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
Noseman, 2026.3 [17:58-25:19]. Workflow: create a first projection (cubic, box, shrink, frontal view) from the material tag's UV projection or the new palette [17:58-18:30]; pick edge loops and right-click Mark as Seam. This writes a special edge-selection tag in the object manager, so seams are not mixed with ordinary selections; Seams only matter for unwrap and relax [19:36-20:39]. A viewport filter can show seams. The Seam Selection tool combines loop select, path select and convert-to-seam: drag to add, Shift for loops, Ctrl to remove, symmetry works [21:11-22:11].
Failure he explains: Reset and Unwrap (ABF) on a closed, watertight mesh with no seams errors out, since relaxing needs open edges. Fix by marking a seam, or use a projection (cubic) and then relax each island [23:15-24:48]. Automatic UVs (Packed, Cubic, Angle) ignore the seam tag and suit 3D painting only; a copy with and without seams gave identical results [25:19-25:50].

**Use it:** Mark seams once in the tag, re-run relax freely, and read the watertight error as "no seam".
