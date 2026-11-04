---
id: motion-unreal-54-motion-design-cloner-honeycomb-noise-effector-settings
title: Unreal 5.4 Motion Design: Cloner (honeycomb, 100x100), an Unbound noise-field effector with Z 30 and pan about 7, and a second spherical effector at 200-400
domain: motion
tags: [unreal engine, motion design, cloner, effector, honeycomb, noise field, school of motion, deep-read]
applies_to: Unreal Engine 5.4 preview (2024)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=DOgfmp_ot9E, src:yt-transcripts]
feeds: []
conflicts: none
---
School of Motion, Aaron [00:25-06:16, 08:21-10:25]. Enable the Motion Design plugin and restart; the Motion Design button gives defaults and a mode with Actors. Cloner: delete the default cube, drop your hex mesh inside, set layout from grid to honeycomb, width and height counts 100 x 100, then tighten spacings from a top view. 'Spawn Link Effector' adds a linked effector. Effector 1: type Unbound (affects all), mode Noise Field, location Z strength 30 (later lowered to 20), pan on to move the fractal (tried 20 and 10, chose about 7). Effector 2: sphere, strength raised to 200 then 300 to 400, outer radius up and inner radius 0 for one high point, falloff easing from linear to InOut Cubic (Quint also tried); Visualize thickness 2-4 to see it. Sequencer: 24 fps, 120 frames, camera plus effector 2 keyed with Transform; camera made via the Cinematic camera actor and snapped to the view.

**Use it:** Reference for a C4D-style Cloner/Effector workflow in a real-time tool; values show how a field-driven wave can be keyed on one effector.
