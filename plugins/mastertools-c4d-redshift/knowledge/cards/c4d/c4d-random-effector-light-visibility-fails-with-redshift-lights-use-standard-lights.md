---
id: c4d-random-effector-light-visibility-fails-with-redshift-lights-use-standard-lights
title: A viewer's Christmas-lights question: a Random effector flickering lights worked with native Cinema 4D lights in Standard render, not with Redshift lights
domain: c4d
tags: [ledger-check, redshift lights, random effector, christmas lights, mograph color, standard render, deep-read]
applies_to: Cinema 4D 2022 with Redshift (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Trainer said at [21:44-22:46] that a Random effector driving individual light visibility did not work immediately with Redshift lights, while native lights rendered with Standard showed the variation when the effector had noise. He had tried a node material on the light and left it as to-be-determined; MoGraph colour plus user data was his next idea. A single speaker's 2022 observation, not a verified limit.

**Use it:** Test per-clone light flicker with a tiny scene before building it on Redshift lights; cloned emissive geometry may be the safer route.
