---
id: broadcast-aximmetry-compound-pin-exposure-and-linked-compounds-for-reusable-effects
title: Aximmetry (2018) basics: group modules into a compound, expose pins as controls, and save a linked compound for reuse
domain: broadcast
tags: [aximmetry, composer, compound, exposed pin, dashboard, linked compound, switch video smooth, node based, post processing, deep-read]
applies_to: Aximmetry Composer (2018)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=aiG_r6-uU54, src:yt-transcripts]
feeds: []
conflicts: none
---
Aximmetry is node-based: video flows on yellow cables; modules have input and output pins [03:38-06:48]. Group a chain with ctrl-G to make a compound; drag a pin past the frame edge to expose it as a control, and top-level exposures appear in the dashboard panel [15:41-18:20, 22:30]. A dashboard scalar module gives a slider with chosen min and max; an integer module suits switch inputs [18:52-27:39].
Save compound and link keeps one file shared across projects; edits to the file update every linked copy, and unlink breaks the tie [20:26-21:28]. Change module type keeps wiring when swapping a hard switch for a smooth one [23:00]. Number fields change by 0.01 per drag step, 0.1 with shift, 1 with ctrl [07:20].
Beginner level; keep only if a pipeline needs Aximmetry.

**Use it:** A reusable-look pattern: expose a few controls on a grouped effect and link the file, mirroring a MOGRT's essential properties.
