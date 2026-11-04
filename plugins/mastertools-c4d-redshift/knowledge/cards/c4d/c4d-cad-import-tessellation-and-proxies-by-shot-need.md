---
id: c4d-cad-import-tessellation-and-proxies-by-shot-need
title: CAD import lets you choose tessellation, colours and UVs per part, and swap density by how close the camera gets; expect manual cleanup
domain: c4d
tags: [bas helmig, bart brinkman, italian giants, cad import, tessellation, proxies, step file, retopology, cinema 4d, deep-read]
applies_to: Cinema 4D R21-R22 era
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Cf9t-bPQkb0, src:yt-transcripts]
feeds: []
conflicts: none
---
Bas Helmig and Bart Brinkman (Italian Giants, Dutch 3D studio; Maxon 3D and Motion Design Show): clients send CAD from Siemens NX, Fusion 360 or SolidWorks; the old route was converting then exporting OBJ or STL [30:09-31:14].
The importer reads STEP and similar files, can use display colours or random colours to separate parts, imports UVs if present and sets tessellation detail [31:14-32:16].
Use low density for background parts and medium or high for those the camera approaches, even as proxies [32:47-33:48].
Clients expect instant beauty but it needs work; one 2.8-million-poly tyre had to be retopologised by hand [33:48-34:20].

**Use it:** Intake check: record tessellation setting and polycount per part; flag any CAD part over a polycount budget.
