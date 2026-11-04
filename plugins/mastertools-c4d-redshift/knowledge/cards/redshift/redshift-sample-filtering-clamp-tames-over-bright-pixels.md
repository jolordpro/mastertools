---
id: redshift-sample-filtering-clamp-tames-over-bright-pixels
title: Chad Ashley: pixels reading around 2.5 in the render cause fireflies and ratty edges; a clamp at 2 cleans them but costs dynamic range
domain: redshift
tags: [chad-ashley, greyscalegorilla, clamp, fireflies, bright pixels, sample filtering, ledger-check, deep-read]
applies_to: Redshift 2.x for C4D (2017)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=LcxjkHFS-2k, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
In an interior with over-bright environment scattering, hovering the render view showed RGBA values near 2.5; these over-bright pixels are where fireflies and ratty edges start [59:39-1:00:10]. He clamped the sample output (an old-UI "sample filtering" setting, probably today's max sample intensity) to 2 and the grain on the probed areas dropped [1:00:10-1:00:41].
Trade-off: not good where the shot needs that dynamic range; fine for a flaring bokeh highlight in the background [1:00:41-1:01:12]. The cause here was a too-bright scattering setting, so lowering the source first is better [59:07-59:39].
Ledger check: ledger section 7 separates Max Subsample Intensity (per sample) from Max Secondary Ray Intensity; do not assume the old label maps to either.

**Use it:** suggest finding the over-bright pixel with the pixel readout first, fixing the source, and clamping last.
