---
id: lookdev-bump-in-two-scales-tiny-detail-checked-at-200-percent
title: Two bump layers: a very small high-frequency map (0.002 cm) plus a soft noise waviness (about 0.04 cm), judged at 200% zoom
domain: lookdev
tags: [[bump, waviness, micro-detail, arnold, ipr, subtle], deep-read]
applies_to: Arnold 6 in Cinema 4D (units are the scene's cm)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Qml8EakEAQ4, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
MographPlus: bump amount is hard to judge, so zoom the IPR region to 200% [07:01-07:33]. On smooth plastic even 0.1 cm was too much and about 0.002 cm worked ("little is always better") [07:33]. Real surfaces also have broad unevenness: a noise at scale about 13 with bump height 5 cm shows the idea, then drop to about 0.04 cm and chain it into the first bump node's normal input [08:04-09:41]. For wood, combine the roughness map and a second map with a layer-RGBA node, overwrite at 0.7 opacity, bump about 15 (as stated) [14:03-15:07]. On very rough concrete the second bump will hardly show [17:50].

**Use it:** Add a cheap bump-scale sanity check: review at 200% and reduce until the bump reads only on a zoom.
