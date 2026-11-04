---
id: redshift-bokeh-normalization-none-unit-intensity-white-colour-sum
title: Redshift bokeh image normalization: none, unit intensity and white colour sum change how bright the bokeh is and whether tint is kept
domain: redshift
tags: [redshift, bokeh, normalization, brightness, polish, greyscalegorilla, deep-read]
applies_to: C4D + Redshift (2022)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aWkfAAJgiJ0, src:yt-transcripts, src:polish-roster]
feeds: [redshift]
conflicts: none
---
Normalisation balances the white pixels of the bokeh texture [03:37]. Per the Redshift docs as he reads them: colour sum makes the colours add to white, removing tint in the in-focus pixels; unit intensity keeps the tint but not darker [04:09]. Switching none to unit intensity made all the bokeh much brighter, and white colour sum looked nearly identical in his scene [04:41]. He usually uses unit intensity or none depending on the look, and none gives a dimmer feel [04:57; 08:50].

**Use it:** Set unit intensity as default; flip to none for a dimmer look. Check docs before relying on the exact wording of each mode.
