---
id: c4d-redshift-matrix-scatter-landscape-minus-90-pitch-random-effector-and-sequential-vs-random
title: C4D Matrix scatter on landscapes (Redshift object tag): pitch -90, random effector rotation, one scatter per landscape, 50-100k counts for grass
domain: c4d
tags: [c4d, matrix scatter, redshift object tag, grass, landscape, mograph, random effector, stepan hka, deep-read]
applies_to: Cinema 4D + Redshift (video Dec 2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=0GD6OeiB6dk, src:yt-transcripts]
feeds: [redshift, c4d]
conflicts: none
---
Stepan HKA, grass tutorial [06:15-14:08]. Set up: Matrix object in Object mode with the landscape as its surface, then in the Redshift object tag choose custom objects and drag in grass instances separately (a grouped null worked once but he prefers separate) [08:53-10:27]. Grass lay flat until Matrix transform pitch is set to -90 [11:32-12:04]. Counts: 10,000 first, 50,000 to 100,000 to fill; a scale multiplier lets a smaller count cover gaps [12:34-13:38, 36:12-36:42]. Distribution sequential gives patches of one type; random mixes [13:38-14:08]. Random effector: turn off position, enable rotation 360 degrees on the horizontal axis [14:08-14:39].
Organisation: one Matrix per landscape named by number, child grass nulls, so scatter folders hide as one [18:52-20:26]. Related existing card: `redshift-matrix-scatter-object-tag-particles`.

**Use it:** use the -90 pitch and per-landscape matrix tidy-up as defaults in scatter scenes.
