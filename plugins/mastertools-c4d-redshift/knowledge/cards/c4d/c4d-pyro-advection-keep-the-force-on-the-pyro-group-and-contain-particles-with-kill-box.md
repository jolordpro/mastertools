---
id: c4d-pyro-advection-keep-the-force-on-the-pyro-group-and-contain-particles-with-kill-box
title: Put the pyro-only field force in its own particle group so particles ignore it, and bound the scene with a Kill modifier on an inverted field condition rather than a collider
domain: c4d
tags: [particles, particle group, field force, kill, field condition, collider, optimise, pyro, deep-read]
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
Sketchy Visuals [14:08-14:40; 28:10-32:18]. Particles and pyro share the force by default; make a second particle group, put only the pyro field force in it (call it the pyro group), and the particle group ignores that force. Tidy with nulls named for what they hold (pyro, pyro forces, particles).
Containment: a Collider tag on a box (collision side both) stops particles but also changes the pyro's behaviour, because the box's size changes how the sim is bounded; taller boxes sit closer to the original look [28:40-29:42]. Alternative: a Field Condition holding a Kill modifier, fed a box in Volume mode, then Invert so everything outside the box dies. It trims the count, speeds the sim and avoids bouncing back [30:13-31:47]. Moving the box floor-level changes how much room the particles have to fall.

**Use it:** Prefer Kill with invert for a clean frame boundary on a cached pyro-particle sim; test before and after for the look change.
