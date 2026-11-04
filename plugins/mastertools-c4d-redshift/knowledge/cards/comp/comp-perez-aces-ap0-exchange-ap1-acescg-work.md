---
id: comp-perez-aces-ap0-exchange-ap1-acescg-work
title: ACES2065-1 (AP0) is the exchange space; ACEScg (AP1) is the working space, and 'scene linear' in the ACES config means ACEScg
domain: comp
tags: [victor perez, foundry, fmx, aces, acescg, ap0, ap1, acescc, deep-read]
applies_to: Nuke with ACES OCIO config
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts, https://www.youtube.com/watch?v=AAeZKZ5feGA, https://www.youtube.com/watch?v=SD8QRldaj94]
feeds: [coach, redshift]
conflicts: none
---
AP0 (ACES2065-1) has primaries wide enough to hold every visible colour, so it is the space for exchanging files [08:58-09:31]. ACEScg (AP1) is the smaller space made for VFX, close to Rec.2020 but with a few imaginary corners kept for the maths; it is the space Nuke works in [09:31-10:32].
ACEScc and ACEScct are log spaces for colourists, not for comp [11:36].
Once the ACES config is set, 'default linear' or 'scene linear' is ACEScg. Relabelling a CG render as ACEScg changed nothing on screen [29:47, 46:26].
Without colour management Nuke only linearises light; it has no primaries at all [10:32].

**Use it:** When a ticket says 'send linear', ask which primaries; the answer for ACES shows as ACEScg to work, ACES2065-1 to hand over.
Transcript support: Kelly's plain definition: a framework turning what the camera saw into what a display reproduces, with an intermediate stage for colour and VFX work. (https://www.youtube.com/watch?v=SD8QRldaj94 [00:32-01:02])
