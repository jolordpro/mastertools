---
id: comp-render-view-vs-picture-viewer-save-identical
title: A JPEG saved from the render view and one rendered to the Picture Viewer matched pixel for pixel in a Difference test
domain: comp
tags: [Zak, i_go_by_zak, render view, picture viewer, difference, null test, deep-read]
applies_to: Cinema 4D + Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Zak tested whether C4D treats the two save routes differently by setting one over the other in Difference mode: only JPEG compression artifacts showed; 16-bit TIFFs would show nothing [44:13-45:16].
This removed a variable when his colour mismatch hunt needed explaining.

**Use it:** CHECKS: a colour-mismatch bug is not caused by which save route was used; look at colour management settings first.
