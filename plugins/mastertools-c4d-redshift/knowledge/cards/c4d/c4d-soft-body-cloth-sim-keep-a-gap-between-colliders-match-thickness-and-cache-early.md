---
id: c4d-soft-body-cloth-sim-keep-a-gap-between-colliders-match-thickness-and-cache-early
title: Sim set-up in C4D 2023: gravity 0, a visible gap between colliders, matching cloth thickness, more collision passes, and cache the scene before look dev
domain: c4d
tags: [c4d, simulation, soft body, cloth, collision passes, cache, spline wrap, gravity, deep-read]
applies_to: Cinema 4D 2023 simulation
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wAVOwrxLHcA, src:yt-transcripts, https://www.youtube.com/watch?v=dHQWVXWbsEM]
feeds: [CHECKS]
conflicts: none
---
Anton (September channel, a self-taught artist then finishing a VFX degree), auto-captions. Project settings, simulation tab: scene gravity 0 and 300 frames [04:26]. Use uniform quads; fewer polygons means fewer creases, fine for a belt but a thin ribbon or paper wants more [12:23]. Avoid intersections at the start: scale the ribbon plane to about 1.25 so a gap shows between objects; overlaps cause trouble all through the sim [11:20]. Raise collision passes (he went to 10) and accept a slower sim [12:23]. Keep the cloth tag thickness equal to the Cloth Surface thickness (1.5) so ropes and belts interact correctly [14:58]. Cache the scene as soon as it works so look dev does not resimulate every play [13:24]. An attractor with an inverted spherical field in include mode keeps parts inside a zone; strength was raised to about 3,000 for a rubbery look, and a turbulence force adds chaos [05:59, 08:14].

**Use it:** supports a sim pre-flight check: gaps between colliders, matched thickness, cache before shading.
Transcript support: Do not start with cloth intersecting its collider (it sticks); thickness should be real-world sized; keep the sim mesh light and cache before subdivisions (C4D 2023) (https://www.youtube.com/watch?v=dHQWVXWbsEM [02:08, 07:50-10:29])
