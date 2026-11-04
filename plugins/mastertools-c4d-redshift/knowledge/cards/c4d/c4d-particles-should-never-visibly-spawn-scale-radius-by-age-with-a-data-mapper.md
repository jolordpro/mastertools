---
id: c4d-particles-should-never-visibly-spawn-scale-radius-by-age-with-a-data-mapper
title: Hide particle birth by scaling radius with age through a Data Mapper (zero, up to full size, back to zero), switch the emitter radius to 0, and delay the force with a time field
domain: c4d
tags: [particles, data mapper, radius by age, spawning, soft keys, emitter radius, time field, field force, deep-read]
applies_to: Cinema 4D 2025 particles (Sketchy Visuals, uploaded Dec 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vrE2wrqq0TM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Sketchy Visuals [17:14-20:24]. His golden rule: you should not see particles popping in [17:45]. Use a Data Mapper as a size-by-age modifier (rename it that way): age 0 to the life (90 frames) mapped to radius 0, up to 1, back down to 0, spline points set to soft. Then set the emitter's own radius to 0, otherwise the original radius still shows at birth [19:53].
Tuning [33:21-34:53]: with many particles, pull the size ramp forward so they reach full size sooner; at their speed the growth is barely visible, and a steep curve is fine. If the fade-in still shows beside already-moving pyro, put a Time field at minus 5 on the field force so particles grow before they are pushed, or keyframe the force's enabled switch; wrong values give odd results.
Same in the shockwave scene: remember to turn the emitter radius off again, or the spawn shows [42:10].

**Use it:** Any particle-driven graphic; do this before judging the sim, since fade-in popping reads as a bug on air.
