---
id: redshift-render-view-lut-display-mode-gamma-22-display-only
title: Redshift Render View can preview a LUT in display only (not in the output); set gamma 2.2 for Greyscalegorilla's LUTs and back to 1.0 when returning to sRGB
domain: redshift
tags: [lut, render view, display mode, gamma 2.2, gorilla grade, color management, preview look, deep-read]
applies_to: Redshift Render View in C4D (2018 video; later builds use OCIO)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=q1UuKhdmAyU, src:yt-transcripts]
feeds: [comp, redshift]
conflicts: none
---
Chad (Greyscalegorilla) [01:02-04:43]: use Render View, not IPR. Settings cogwheel > Display > Color Management: change sRGB to LUT, load a .cube, and the folder's LUTs populate a list you can arrow through; a strength slider mixes the look. Gorilla Grade LUTs assume gamma 2.2, so set gamma 2.2 in LUT mode. The LUT is applied to the display only; sending to Picture Viewer renders without it [03:08-03:39], so grade in comp later. Mistake he made: switching back to sRGB mode while gamma was still 2.2; set gamma back to 1.0 because sRGB already applies it. Good for judging lighting under the intended grade.

**Use it:** Preview a look while lighting but never rely on it being in the file. On current Redshift (OCIO) use the view transform instead.
