---
id: comp-scene-referred-vs-display-referred-and-why-linear-adds-correctly
title: Linear light adds correctly (two half-lit images sum to the both-lights image); display-referred and log footage need converting first
domain: comp
tags: [gamma, linear light, scene referred, display referred, log, raw, aces2065-1, gamut, transfer function, deep-read]
applies_to: ACES concepts (Blender-oriented creator)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=aJF2sAjRsy0, src:yt-transcripts, https://www.youtube.com/watch?v=w0ubDSzEEYg, https://www.youtube.com/watch?v=Hlj5ep-85ys, https://www.youtube.com/watch?v=AAeZKZ5feGA]
feeds: [comp, CHECKS]
conflicts: none
---
Gamma is an exponent on input luminance; value 1 is linear. Linear: 0.25 plus 0.25 gives 0.5, so light renders can be added; a non-linear curve breaks that arithmetic (his gamma 0.5 example: 0.25 in gives 0.5 out) [03:13-04:44]. Proof he shows: render two lights separately, add in comp, result equals both lights on; this is why multi-pass compositing works [04:44-05:15]. Eyes judge brightness non-linearly, more sensitive in the darks [05:15-06:16].
Footage: display-referred (phones, basic cameras) throws away scene light and bakes a curve; scene-referred raw keeps linear light; log is scene-referred with a log curve and smaller files than raw, so ACES can reverse it. Log looks flat because the monitor curve does not match [06:16-08:20]. ACES 2065-1 gamut covers the whole visible range and is linear, so footage from smaller gamuts can be placed inside it [02:09-03:11, 08:20-08:52].

**Use it:** supports the passes-must-sum check; a flat-looking plate is a log or raw plate, not a broken file, and should be given its input transform.
