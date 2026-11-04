---
id: comp-woodin-light-passes-one-light-per-collection-and-a-view-layer-per-light
title: Mitchell Woodin (compositor): put each light in its own collection, then render view layers: beauty, environment-only, key-only, fill-only and a data layer
domain: comp
tags: [mitchell-woodin, blender, cycles, light passes, view layers, collections, relight, nuke, deep-read]
applies_to: Blender (Cycles), method applies to any renderer
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tB5-Oe7pTUs, src:yt-transcripts]
feeds: [[post-composite, redshift]]
conflicts: none
---
Steps in his order: put the key and fill lights in separate collections so each can be switched off [00:32][01:03]. Make view layers: beauty (everything that is uniform: all lights and the data passes), key, fill, environment, and a data pass [01:34][02:08]. Beauty: no Z pass (he builds his own), keep object cryptomatte and denoising data [02:40]. Environment layer: key and fill off, direct and indirect colour passes on (he skips glossy passes he never uses), denoising data on [03:13]. Key layer: fill off, and turn off the HDRI by unticking Environment under the filter settings; fill layer the same the other way round [03:45][04:19]. Reason: lighting passes let a compositor rebalance each light in Nuke instead of re-rendering [00:02][12:20]. A compositor's favourite method, says the video; single-source claim.

**Use it:** a template for Redshift light groups (light AOVs) and for the comp relight step; compare lighting-render-light-groups-separately-denoise-each-then-add.
