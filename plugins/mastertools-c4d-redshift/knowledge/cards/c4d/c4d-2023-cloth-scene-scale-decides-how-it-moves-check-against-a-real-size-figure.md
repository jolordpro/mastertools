---
id: c4d-2023-cloth-scene-scale-decides-how-it-moves-check-against-a-real-size-figure
title: The same cloth settings behave completely differently at a handkerchief or a bedsheet scale; model to real size and judge it against a six-foot figure before tuning forces
domain: c4d
tags: [cloth, scene scale, real world scale, turbulence, wind, school of motion, 2023, simulation, deep-read]
applies_to: Cinema 4D 2023 new simulation system, cloth (School of Motion, EJ, Oct 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dHQWVXWbsEM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ (School of Motion, Cinema 4D 2023, uploaded Oct 2022) [07:50-10:29]. He sets two plane cloths with identical tag settings and different sizes; the small one (handkerchief) is blown away by the smallest turbulence, the large one (king-size comforter) barely moves. A real-size figure object (a six-foot "Bob") placed beside them shows the size. If a big plane needs huge force values, the cause is probably its scale, not the force. Real thickness is tiny: a sheet of paper is about 0.01 cm [07:50]. Turbulence scales need to shrink along with a smaller cloth, or it flies off like a newspaper [09:57-10:29].
Keep the sim mesh light and cache before adding subdivisions [09:57].

**Use it:** Before arguing with cloth forces, put a human-scale reference in the scene and set the cloth to a real size.
