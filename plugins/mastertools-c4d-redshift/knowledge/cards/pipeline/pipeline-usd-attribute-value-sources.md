---
id: pipeline-usd-attribute-value-sources
title: USD attributes show where a value comes from: computed, fallback, default, time-sampled or empty
domain: pipeline
tags: [usd, attributes, time samples, fallback, value clips, relationship, deep-read]
applies_to: Houdini Solaris details pane
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
The details pane colour-codes sources: purple = computed (bounds, world position), grey = no value written, yellow = fallback the viewer needs, light blue = default (a non-animating authored value), and pink or green appear once values are time-sampled or come from value clips. A separate colour marks relationships such as material bindings and proxy links [36:49-38:23]. Red dots in the tree show viewport-only overrides such as hiding or unselectable [36:18].
Colour names are from the live demo and may differ by version.

**Use it:** Reference when explaining why a property reads zero: no authored value vs a fallback.
