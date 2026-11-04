---
id: c4d-particle-colour-mapper-age-distance-or-velocity-is-data-for-the-render
title: Colour Mapper on age, distance traversed, or velocity magnitude gives a look-dev view now and a data channel later; re-colour in the renderer with a gradient or ramp
domain: c4d
tags: [particles, color mapper, velocity magnitude, distance traversed, age, gradient, look dev, redshift user data, deep-read]
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
Sketchy Visuals [20:24-24:00]. The colour in the Colour Mapper is data, not final colour: extra knots just add data points that a renderer gradient or ramp reads later (Octane, Redshift). Three drivers: age (progress through life), distance traversed (the particles that move most change colour; his favourite and the one used in most renders), and velocity magnitude (best with several colour points). His default look-dev ramp is white to blue; switch between drivers freely.
Clamping data is stable after caching and in render, so adjust the data range, not the shown colour [22:26]. In the render, feed it to the material: Octane instance colour; he says in Redshift this would be the user colour data with particle colour [49:21-49:51].
Angular velocity: particles carry no rotation by default; random angular velocity at 360 degrees spins cubes and rocks, and random direction with tiny velocity also spawns them differently; it changed a lot between sim types, so he treads lightly [24:31-26:37].

**Use it:** Wire velocity or distance into a gradient in Redshift for sparks or trail looks that follow the sim, not hand-painted colour.
