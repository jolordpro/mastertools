---
id: c4d-2027-liquid-effects-restrict-to-source-group
title: Point the Liquid Effects Emitter or Modifier at the right particle group, or the dropped object itself instantly turns to foam and spray
domain: c4d
tags: [Ellie, Maxon, liquid effects, emitter, modifier, particle group, deep-read]
applies_to: Cinema 4D 2027.0
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [coach, lookdev]
conflicts: none
---
Ellie (Maxon): in a drop-into-container test, leaving the emitter on every source made the falling drop react to the constraints almost at once, which she did not want. She restricted the emitter to the container's liquid-fill group so only that liquid makes secondary particles [25:27-25:59].
With the Modifier, a Basic Emitter is wrapped by dragging it under the new particle group so only those particles are converted; her liquid-fill emitter stayed unaffected [19:46].
Iterate the sim at low resolution on a Mac during a demo, and lower emitter Resolution if the machine slows [18:14, 27:00].

**Use it:** Coach: if secondary liquid fires too early or on the wrong object, check which source group the effect is attached to before touching thresholds.
