---
id: comp-alfie-vaughan-colour-chart-neutralize-match-then-reverse
title: Chart-match recipe: neutralize plate and HDRI to the same grey, render a chart in CG until its mid-grey reads about 0.2, comp over the original plate with the neutralizing grade inverted
domain: comp
tags: [alfie vaughan, colour chart, white balance, neutralize, hdri, grey card, aces cg, nuke, reverse grade, shadow catcher, deep-read]
applies_to: Nuke, Blender, ACEScg working space (2025)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UB6nz4lVOyQ, src:yt-transcripts]
feeds: [[comp, lookdev, CHECKS]]
conflicts: none
---
Alfie Vaughan (VFX artist, single creator, low). Order [00:01-03:36]: film the chart at the end of the plate, rotated a few ways so one angle has the best light; convert log to a linear working space (ACEScg) before comp, all sources in one space; neutralize the plate and the HDRI (shot at the same location with a chart) using a chart-analysis tool (MM Color Target in Nuke) that fixes white balance and exposure; build the CG scene with the neutral plate on a shadow catcher and the HDRI rotated to match; put a chart texture plane in the CG scene, render one frame, sample the middle grey and raise the HDRI strength until it matches the neutralized plate (denoise only for this test, it flattens the patch); render beauty, depth, shadow catcher; comp over the original, un-neutralized plate by inverting the colour matrix on the CG so the grade is not baked into the footage; then judge by eye (he dropped exposure on the shoe and matched black point) and add defocus from depth and a little bloom. Without a chart tool [05:07-06:42]: grade the plate and HDRI until the grey patch reads about 0.2 in R, G and B (exposure first, then channels), put the grade under the CG and tick reverse; or comp over the neutralized plate if the software cannot invert.

**Use it:** Numeric match step before art direction for any plate-based job; the 0.2 grey target is his working figure in linear, not a standard.
