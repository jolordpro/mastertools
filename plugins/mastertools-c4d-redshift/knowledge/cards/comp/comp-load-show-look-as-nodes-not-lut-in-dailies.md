---
id: comp-load-show-look-as-nodes-not-lut-in-dailies
title: Load the show look as a DRX node tree rather than a LUT, because nodes stay editable and LUTs have limited accuracy
domain: comp
tags: [davinci resolve, drx, show look, lut accuracy, timeline grade, clip grade, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=uaynELBZdSE, src:yt-transcripts, https://www.youtube.com/watch?v=JWa0YpS98-w]
feeds: [comp]
conflicts: none
---
One look for the whole project goes on the timeline level so every clip passes through it; the DIT's per-clip CDL goes on the first node of each clip [03:26]. With multiple looks, create groups per look and put the look in the group's post-clip level [03:59]. Even though the LUT exists, loading the real nodes keeps every operation reviewable and changeable, and avoids LUT accuracy limits; swapping LUT for the grade should change nothing in the image [04:32][05:03]. Import the DRX through the gallery, switch Node window to Timeline mode, Alt-S for a new node, then Apply Grade [17:15].

**Use it:** prefer the node-based look in any shared grade project; keep a LUT only for devices that cannot read nodes.
