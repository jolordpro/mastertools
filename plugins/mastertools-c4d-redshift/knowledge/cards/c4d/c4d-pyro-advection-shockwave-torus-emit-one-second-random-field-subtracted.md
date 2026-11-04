---
id: c4d-pyro-advection-shockwave-torus-emit-one-second-random-field-subtracted
title: Shockwave recipe: emit particles from a torus for one second, advect with a strong cylinder-field force, and subtract a random field in the field tab for fluffy irregular puffs
domain: c4d
tags: [shockwave, torus, mesh emitter, field force, random field, pyro advection, particles, fluffy, deep-read]
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
Sketchy Visuals [35:24-46:47]. Torus 70 by 25 (later 80 by 25). Mesh emitter in Volume mode, constant emission restricted to a range of 30 frames (1 second) so the count is true; start at 500,000 then 1,000,000 particles; lower the voxel size so particles sit inside the torus; accuracy settings raised (see the advection card). Force strength 5,000 up to 7,000 in the cylinder-field force.
Problems met: particles snap back when emission stops (the "ping back"); fix by pushing the force up and nudging torus size and the inner offset [39:33-40:33]. A Random field subtracted from the cylinder field in the Fields tab only restricts the push; placing it as a force adds push, and he finds the Fields tab better [40:33-41:07]. Best look: subtract the cylinder from the random field so the middle stays still and the edge is irregular [45:15-46:16]. More, smaller particles often beat more forces; change the random seed for variants. He prefers this to shooting particles out and following them [42:10-43:12].

**Use it:** A starting recipe for an impact shockwave in a sports open; expect many small tweaks to inner offset and torus size.
