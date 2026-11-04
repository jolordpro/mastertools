---
id: redshift-sss-rgb-range-0-1-radius-scale-multiplies-channels-and-anisotropy-like-gamma
title: Chad Ashley on random-walk SSS: set colour range to 0-1, scale in cm multiplies each radius channel, red travelling farthest looks creamy, weight 1 replaces base colour
domain: redshift
tags: [chad ashley, greyscalegorilla, random walk, subsurface, radius, anisotropy, rgb range, preferences, ledger-check, deep-read]
applies_to: C4D + Redshift standard material (Greyscalegorilla upload 2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=P75L5fo0Xf0, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Guest Chad Ashley (host Nick of Greyscalegorilla asks): random walk is more accurate and is becoming the standard [02:09]. Weight up, then scale sets how deep light goes (0.148 cm, later 0.646 cm shown) [02:41-04:15]. Colour feeds the general subsurface colour and can be the base texture [03:12].
Radius is the part that makes it look good: set C4D Preferences > Units colour range to 0-1, because the scale (cm) multiplies the R, G and B radius values, so each colour penetrates differently; red far, blue least looks creamy like milk, butter or marble [03:12-04:45].
Anisotropy, he says, acts like a gamma: negative keeps the effect near the surface, positive pushes colour all the way through; Chad rarely touches it and works with scale and radius [04:45-05:46, 07:21]. Weight 1 overrides the base colour; lower it to blend back [06:19-06:50]. For grain he starts with the generic quality buttons, then lowers threshold [07:52-08:23].

**Use it:** `ledger-check` for the anisotropy wording: renderbaron describes it as a direction control (see `redshift-sss-use-cases-transmission-vs-subsurface-thin-wall-and-hybrid`). Treat as untested; supports `redshift-sss-radius-colour-and-scale`.
