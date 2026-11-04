---
id: broadcast-avalanche-2022-procedural-shapes-modifiers-booleans-svg
title: Avalanche 2022: draw procedural shapes with bevel and outline modifiers, mask with ID-linked Booleans, and import SVG logos as extruded geometry or sprites
domain: broadcast
tags: [unreal fest 2022, epic games, avalanche, andy blondin, bernt bk, modifiers, boolean, svg, procedural, motion design, deep-read]
applies_to: Unreal Engine 5.1 experimental
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XAtjoawRN_Y, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Shapes are drawn on a 2D canvas with rulers and guides, yet are real 3D with bevel, slant and mirror (welded) modifiers, outlines that extrude, and bend, taper and twist deformers [16:38-19:21]. Modifier stacks can be saved as presets [21:59].
Keyframing bevel and similar values works but recomputes geometry each frame, so it costs more than a normal animation [20:58]. Booleans work by giving shapes an ID and telling another shape to mask through it (dynamic geometry only so far) [22:00-22:31].
SVG import builds mesh from Illustrator paths, extrudes it and keeps colours; or flip it to a sprite (texture) to save resources [23:05-23:37]. Everything shown was experimental and not yet released [13:30].

**Use it:** The Motion Design mode that followed is the real-time route for logo, bar and shape graphics; mind the recompute cost when animating modifiers.
