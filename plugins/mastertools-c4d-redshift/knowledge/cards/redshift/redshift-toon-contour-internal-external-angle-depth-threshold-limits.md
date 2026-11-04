---
id: redshift-toon-contour-internal-external-angle-depth-threshold-limits
title: Redshift Toon contours (v1, 2024): external vs internal lines, angle and depth thresholds, smooth vs geometric normals, and control only per material
domain: redshift
tags: [redshift toon, contour, outline, angle threshold, depth threshold, npr, c4d, school-of-motion, ledger-check, deep-read]
applies_to: Cinema 4D + first Redshift Toon release (video April 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=i3YczHKxtbo, src:yt-transcripts]
feeds: [redshift, shakedown]
conflicts: none
---
EJ, tested on a pug and a rig [11:53-18:40]. The Contour node has an external line (silhouette side) and an internal line (creases and folds), each with colour, thickness, thickness modifier and opacity. A bigger thickness number means a thicker line.
Angle threshold decides which polygon creases count as an edge: raising it removes crease lines, lowering it brings more in. Depth threshold lowering gives a sketchy stroke along polygon edges, useful with displacement [12:54-14:28]. Normal type: smooth for organic models, geometric for hard-surface or CAD-like models (low threshold plus geometric normals gives a wireframe look) [14:28-15:31].
Limits he hit at v1: lines where two objects intersect are thick and cannot be switched off with one checkbox; the only fix is giving different objects different Toon materials and turning external or internal off per material, then matching thicknesses by eye [15:31-18:09]. His claim that the internal line also drives some outer lines is confusing in his own telling; test it rather than trust it [17:38-18:09]. He expected Maxon to add intersection and line-placement controls later (his statement, not checked).
Why this is low: single tutorial, early version; later releases may differ.

