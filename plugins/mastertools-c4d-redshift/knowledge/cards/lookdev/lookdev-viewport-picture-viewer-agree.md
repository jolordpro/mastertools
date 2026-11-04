---
id: lookdev-viewport-picture-viewer-agree
title: Viewport, Picture Viewer and final render must read the same: compare one known patch in all three
domain: lookdev
tags: [lookdev, colour, viewport, picture viewer, render, mismatch, check]
applies_to: Redshift + C4D 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=sFRa_iZhpKw, src:research-youtube]
feeds: [CHECKS 5]
conflicts: none
---
Greyscalegorilla (2026-07-08, 1 min): colours differ between viewport, Picture Viewer and render, and one setting fixes it.
The setting is not named on the video page, so only the test idea is carried here.

**Use it:** render a small patch of known colour and compare its values in the three places; any gap is a warning before the farm run.
