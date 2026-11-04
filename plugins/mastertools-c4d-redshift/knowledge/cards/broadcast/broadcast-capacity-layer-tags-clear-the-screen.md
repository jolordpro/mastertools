---
id: broadcast-capacity-layer-tags-clear-the-screen
title: Layer tags tell the rundown what to remove when a new graphic comes in: a full screen clears slabs and lower thirds
domain: broadcast
tags: [transition logic, layer tags, full screen alias, lower third, slab, rundown, deep-read]
applies_to: Unreal Engine 5.6 motion design transition logic
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts]
feeds: []
conflicts: none
---
Each graphic is tagged as a layer type such as lower third, slab or full-screen alias [1:26:24]. A full-screen alias is set to evict every other tag because it covers that much real estate; a slab evicts other slabs and full screens [1:31:40-1:32:42]. Same layer, same scene: it only updates changed text [1:29:02]; a different scene on that layer: it plays the out animation, then the in [1:34:46-1:35:50]. A debug button shows the states firing [1:33:44]. About 70 percent of the sample's levels use this logic; one-off hero effects (a ball wipe) do not, because they would be rendered out or played from another engine, not the overlay machine [1:36:50-1:37:21].

**Use it:** When building a graphics package, define the layer taxonomy (bug, lower third, slab, full screen) and what each evicts before animating, so the rundown can behave without extra work.
