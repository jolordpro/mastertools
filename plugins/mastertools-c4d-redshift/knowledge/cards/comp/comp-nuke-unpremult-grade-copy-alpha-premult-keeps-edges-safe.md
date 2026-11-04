---
id: comp-nuke-unpremult-grade-copy-alpha-premult-keeps-edges-safe
title: Wrap CG corrections in Unpremult then Premult, and copy the alpha back in just before the Premult, so strong grades do not fringe the edges
domain: comp
tags: [alfie-vaughan, nuke, unpremult, premult, copy alpha, edges, cg comp, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=fxfuhl8Q7ys, src:yt-transcripts]
feeds: [composition]
conflicts: none
---
First thing he does with any CG render: Unpremult (edges expand slightly), do all corrections, then Premult to crop the edges back in [06:14-06:46]. Pushing gain hard without this gives strange artifacts on the edges [06:46]. A Copy node (K) just before the Premult takes the alpha from the original render so the alpha stays unchanged through the chain [07:17]. Tidy the node graph with dots (period key, or Ctrl-drag on the yellow dot).

**Use it:** Default CG stack in the comp scene template: unpremult, corrections, copy alpha from source, premult. Related card: comp-nuke-beauty-rebuild-from-diffuse-gloss-passes-and-premult-trap.
