---
id: pipeline-usd-department-layers-merge-in-asset-and-shot-containers
title: Prism's USD layout: each department writes one layer, an asset or shot container references them, and the render merges them
domain: pipeline
tags: [pipeline, usd, department layer, container, sublayer, prism, references, deep-read]
applies_to: Prism 2.0 alpha, USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Prism's developer (name garbled in captions) describes the structure at FMX 2021 [02:37]. Each department exports one file, a department layer. One USD container per asset and one per shot references those layers: an asset container holds modeling and surfacing layers; a shot container holds layout, animation, effects and lighting layers [03:08] [03:39]. Rendering the container merges the layers.
Sublayers let two artists in the same department write without overwriting each other, for example body and cloth, both referenced into the department layer [05:12] [05:43]; lighting uses sublayers for sequence lighting and shot lighting [06:13].
Limits at the time: rigging was outside the USD flow (Maya referencing) [02:37] [12:56].

**Use it:** Vocabulary and template for any USD-style hand-off: one writer per layer, one container, merge at render. Useful when mapping C4D to USD pipelines.
