---
id: c4d-pyro-advection-accuracy-settings-maccormack-runge-kutta-cubic
title: Pyro Output, Advanced, Advection tab raises particle-follow accuracy: his accurate pick was Runge-Kutta 4 with cubic interpolation and MacCormack at full correction strength
domain: c4d
tags: [pyro, advection settings, runge-kutta, maccormack, cubic interpolation, correction strength, accuracy, deep-read]
applies_to: Cinema 4D 2025 pyro (Sketchy Visuals, uploaded Dec 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vrE2wrqq0TM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Sketchy Visuals [15:10-16:44; 37:30]. Under the pyro output's Advanced settings there is an Advection tab with an advection mode (three, ordered low to high accuracy) and an interpolation mode (linear less accurate than cubic). Captions garble the names ("kafa", "coremac"): read as Runge-Kutta 4 and MacCormack. For the main scene the difference is subtle; for the shockwave he used Runge-Kutta 4, cubic, MacCormack, correction strength 3 (maximum raised) [37:30]. Right-click any setting, Show Help, to read the manual page.

**Use it:** Turn these up when advected particles drift off the smoke; expect slower sims, so test at a short frame range.
