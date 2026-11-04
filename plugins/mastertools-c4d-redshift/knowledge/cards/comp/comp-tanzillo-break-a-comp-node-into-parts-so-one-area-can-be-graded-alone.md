---
id: comp-tanzillo-break-a-comp-node-into-parts-so-one-area-can-be-graded-alone
title: When a merged result is right in one area and wrong in another, split the node into its components so the part can be graded alone
domain: comp
tags: [mike-tanzillo, nuke, comp-method, light-wrap, gain, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cP3AELeZf6o, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
His working rule [17:42-19:16]: if you like what a combine does here but not there (common), break the node into components. Example: output the light wrap only, mask it softly to the hair, grade the wrap down with a gain, then plus it back to the base. Now one gain controls only the amount of wrap on the hair. "Generate wrap only" in the node just plus-es the wrap back inside; doing the plus outside the node gives the control.

**Use it:** build comps so each effect (wrap, glow, bloom) is a separate additive branch with its own gain. Easier notes later.
