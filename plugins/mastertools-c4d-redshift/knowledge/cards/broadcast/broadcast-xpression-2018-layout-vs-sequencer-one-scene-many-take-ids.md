---
id: broadcast-xpression-2018-layout-vs-sequencer-one-scene-many-take-ids
title: Ross XPression (2018): build in Layout, run in Sequencer; one scene file feeds many take IDs with their own text
domain: broadcast
tags: [ross xpression, layout mode, sequencer, take id, lower third, scene file, static data, widget, datalink, frame buffer, deep-read]
applies_to: Ross XPression (video 2018-04-09; version not stated)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VZO7A0F7pZ0, src:yt-transcripts]
feeds: []
conflicts: none
---
Layout mode builds scenes (scene manager, object library, object manager, inspector); Sequencer mode (F3 and F4) plays them out [00:02-06:47]. A scene in the sequencer gets a take ID; duplicates are copies that still point at the same scene file, so one edit to the look updates every lower third [08:53-10:56].
Each take ID gets its own data source: static text, datalink (spreadsheets and databases, covered only briefly here) or a widget for live clocks and countdowns [09:25, 10:56-11:58]. Fix in/out transitions per take (dissolve 15 frames in, 20 out) rather than cut [07:50-08:46]. Colour-code takes for fast reading [13:30-14:01].
Channels: lower thirds and bugs on channel 1, full screens on channel 2 is the common split, using layers so a bug and a lower third do not clear each other [14:34-17:15]. The speaker calls it a two-channel system.

**Use it:** Map the same pattern to any show-control template: one scene, many takes, separate layer for bugs.
