---
id: c4d-2023-1-decay-modifier-layer-slows-the-return-after-a-field-passes
title: The C4D 2023.1 field Decay layer makes clones outside the field return to rest more slowly, leaving a trail
domain: c4d
tags: [mitch scott, behind the button, decay, field modifier layer, mograph, cinema 4d 2023.1, plane effector, wetness map, deep-read]
applies_to: Cinema 4D 2023.1 (video uploaded 2023-03)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tQbqZzk7Kc0, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Mitch Scott (Behind the Button), setup: cloner with a plane effector, driven by a spherical field that moves through [00:32-01:04]. Decay is a modifier layer on the field that acts after the field has left: clones return to their start state slower, so a tail follows the field [01:35-02:39]. Lower effect strength gives a shorter tail, higher gives a longer one. He uses Maximum mode only, noting the help file points to it as well [02:39].
Before reaching for it, he reminds that the field's own Remapping section (inner offset, contour curve) already shapes speed and falloff [01:04].
Side use he floats but does not build: drive a roughness map from the decayed field to get condensation or wet trails on a bottle [02:39-03:41].
Not the same thing as the Delay effector; he flags the name clash.
Transfers to broadcast: a cheap way to give a hit/pulse on a bar graph or tile wall a settling tail without keys.

**Use it:** when a field-driven clone wave looks too snappy, add Decay (Max mode) and tune strength before adding keys; try the same field as a roughness source for wet looks.
