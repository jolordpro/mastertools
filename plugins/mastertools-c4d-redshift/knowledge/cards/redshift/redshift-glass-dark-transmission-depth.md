---
id: redshift-glass-dark-transmission-depth
title: Coloured glass that renders too dark: check Transmission Depth before raising trace depth or samples
domain: redshift
tags: [glass, transmission depth, dark glass, refraction, material, greyscalegorilla, lookdev]
applies_to: Redshift 2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=LhWCVXRn9xk, src:research-youtube]
feeds: [CHECKS 7, CHECKS 7 starved glass]
conflicts: none
---
Greyscalegorilla (2026-08-07, 1:48) says coloured glass reading dark is fixed with Transmission Depth. Source is the video description and title only.
This is a material control, separate from the refraction and combined trace depths in the ledger (section 5).
Merged from `lookdev-glass-dark-transmission-depth`: Greyscalegorilla (2026-08-07, under 2 minutes) names Transmission Depth as the fix. Video-page evidence only; the spoken numbers were not available.

**Use it:** in the starved-glass check, point at transmission depth first when trace depth is already enough.
