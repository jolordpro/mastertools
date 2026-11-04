---
id: comp-perez-aces-config-version-must-match
title: Use the same ACES config version as the show: ask which version, because files carry it in metadata and versions differ
domain: comp
tags: [victor perez, foundry, fmx, aces, ocio, config, version, deep-read]
applies_to: Nuke X, ACES OCIO configs 1.1-1.3
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts]
feeds: [CHECKS, lookdev]
conflicts: none
---
In Nuke set colour management to OpenColorIO, then pick the config (1.1 as his example, 1.2 in the demo) [28:45, 40:13].
His rule: to keep consistent, use the version the production uses, and ask which one (1.1, 1.2, 1.3). A custom config path exists for discontinued versions [29:17].
Matching card in this KB already warns about farm nodes drifting; this is the same risk at the artist's desk.

**Use it:** Add an ACES/OCIO version line to project setup and to the delivery notes so every machine opens the same config.
