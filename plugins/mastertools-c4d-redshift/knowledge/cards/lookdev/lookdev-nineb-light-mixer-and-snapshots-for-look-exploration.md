---
id: lookdev-nineb-light-mixer-and-snapshots-for-look-exploration
title: A light mixer controls all lights, even those inside a delivered asset, and snapshots save and restore whole looks with a render, so moods can be compared later
domain: lookdev
tags: [nine between, houdini, solaris, usd, light mixer, snapshot, look development, versions, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [coach, elevate]
conflicts: none
---
The light mixer lists every light in the stage; drag in the ones to change (colour, exposure) in one panel; red dots mark overridden values and can be reverted [2:20:09-2:21:40]. He made 'horror', 'basic' and 'vaporwave' looks, snapping each [2:22:45-2:24:17].
A snapshot saves the whole network plus a render; right-click 'revert network to snapshot' restores everything even after the camera and lights changed [2:24:17-2:25:18]. Snapshots can be tagged and rendered in the background [2:25:18].

**Use it:** Take a named still of each look option before moving on, so a client's 'go back to the first one' costs seconds.
