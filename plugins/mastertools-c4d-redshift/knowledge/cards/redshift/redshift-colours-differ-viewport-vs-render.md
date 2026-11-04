---
id: redshift-colours-differ-viewport-vs-render
title: Colour can differ between viewport, Picture Viewer and final render, and one setting is said to fix it
domain: redshift
tags: [colour mismatch, picture viewer, viewport, render, ocio, greyscalegorilla]
applies_to: Redshift 2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sFRa_iZhpKw, src:research-youtube, https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts]
feeds: [CHECKS 5]
conflicts: none
---
A 1-minute Greyscalegorilla video (2026-07-08) names the symptom and says a single setting cures it; the description does not name the setting and no transcript was readable.
The research turns it into a symptom-first test: render a patch of known colour and compare the same pixel in viewport, Picture Viewer and the EXR.

**Use it:** run the known-colour patch compare before a farm run and warn if the three disagree.
Transcript support: Maxon trainer: viewport never matches Render View like for like, and Render View differs slightly from final. (https://www.youtube.com/watch?v=KnfiJy2ND2o [55:31])
