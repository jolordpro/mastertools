---
id: comp-aces-show-look-lmt-vs-look-lut-in-cct
title: In ACES, a show look is an LMT; Resolve can only export a Look-LUT that must be applied in ACES CCT, along with its CDLs
domain: comp
tags: [aces, lmt, show look, look lut, cdl, aces cct, davinci resolve, colour pipeline, deep-read]
applies_to: DaVinci Resolve ACES
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=uaynELBZdSE, src:yt-transcripts]
feeds: [CHECKS, delivery]
conflicts: none
---
Show look = tonal adjustments to the whole image that carry the show's identity; scene tweaks (exteriors, night, warmer) ride as CDLs on top [00:38]. A true LMT takes ACES2065-1, ACEScg or linear in and out, but Resolve's LUT export limit means the look LUT is applied in ACEScct, so call it a Look-LUT, not an LMT [01:43][02:18]. If the look is built with Resolve controls it lives in ACEScct; if shared as CDL plus show LUT, both must be applied in ACEScct [02:18]. Document this so every department loads the recipe the same way [02:54]. Colour-managed ACES lets grade recipes move between on-set, dailies, post and VFX with the same result [01:09].

**Use it:** when sending a look to anyone, state the working space (ACEScct) next to the LUT or CDL.
