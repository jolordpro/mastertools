---
id: comp-cheap-tricks-depth-pass-as-gradient-wipe-map-for-through-space-transitions-and-stepped-blackout
title: A depth pass as the Gradient Wipe layer wipes a shot through its own space; posterizeTime makes the wipe step like grid blocks
domain: comp
tags: [gradient wipe, depth transition, rolling blackout, posterizeTime, city night, after effects, deep-read]
applies_to: After Effects
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp, motion]
conflicts: none
---
Transition: on the top clip add Gradient Wipe with its own depth pass as the gradient layer; the wipe then travels from near to far, with softness for a soft reveal; footage pairs with similar camera pushes work best [09:03-11:03].
City blackout [13:05-19:36]: track the camera, put a ground-plane solid from street-level points and run the Normalize Track script; build the dark version by Toner from a three-colour gradient ramp sampled from the fog colour, plus an inverted depth set to Multiply under a fog layer; mask headlights and streets from the darkening, with a fast box blur on the mask (repeat edge pixels off). Then Gradient Wipe with the depth, one second in to one second later at 0 to 100 percent. For a stepped, grid-by-grid blackout alt-click the completion slider and type posterizeTime(6); then value: higher numbers give more small sections, 3 gives big steps [18:31-19:05].
Transfers to broadcast graphics: same depth-driven reveal works on a rendered Z-depth.

**Use it:** Offer as a cheap transition or power-cut reveal when a depth AOV exists.
