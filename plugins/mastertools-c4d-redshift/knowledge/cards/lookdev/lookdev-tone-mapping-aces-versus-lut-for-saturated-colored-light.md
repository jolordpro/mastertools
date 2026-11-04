---
id: lookdev-tone-mapping-aces-versus-lut-for-saturated-colored-light
title: ACES tone mapping keeps strongly saturated coloured light solid; a LUT with highlight compression gives more punch control
domain: lookdev
tags: [aces, tone mapping, lut, saturation, coloured light, highlight compression, vignette, deep-read]
applies_to: Octane camera imager
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=siNE2SEgD7E, src:yt-transcripts, https://www.youtube.com/watch?v=SD8QRldaj94]
feeds: [redshift, comp]
conflicts: [transcript-SD8QRldaj94]
---
With Octane's ACES tone mapping the red light stays solid and can be pushed past true saturation and still look good, at the cost of disabling the highlight-compression controls [06:54, 10:10-10:41]. He then swaps to a LUT pack plus higher highlight compression and lower exposure/vignette and liked the gamma control over punchiness; ACES was pushing the colours too orange [14:20-14:51].
Two area lights with the same hue shift drifted to slightly different oranges; he evened them by dropping power [17:32-18:03]. Emission colour gets odd in Octane, so saturate the emission colour further instead [12:14].
Process lesson: expect to play a long time before a look works; he is 'not 100 percent comfortable' even at a decent state [15:21].

**Use it:** when a coloured-light look reads muddy, try the view transform or LUT before changing the lights; ACES-like transforms desaturate bright reds toward orange.
Transcript contradicts: Cullen Kelly says ACES is about accuracy and efficiency, not aesthetics, and will not make grades look better; the existing card credits ACES tone mapping with a visual benefit on saturated light. Mild: the existing claim is about Octane's tone mapper, Kelly speaks about the colour management framework. (https://www.youtube.com/watch?v=SD8QRldaj94 [02:04-02:57])
