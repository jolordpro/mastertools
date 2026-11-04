---
id: pipeline-usd-swap-ascii-binary-without-breaking-links
title: A .usd file can be flipped between ASCII and binary with usdcat while keeping the same path
domain: pipeline
tags: [usd, usdcat, ascii, binary, handoff, file path, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
A .usd file is either format, and the extension alone does not tell which. The USD command-line tool usdcat can convert between them [13:59-14:30].
Reason given: another department already points at that file path, so a .usd can be changed to ASCII, checked by eye, then changed back to binary without breaking anyone's link [14:30-15:01].
To write ASCII straight from a .usd path, append a format argument string (colon, SDF format args, format=usda) to the output path [15:01-16:35]; the result matched the real .usda file in size and content.

**Use it:** When a USD handoff misbehaves, flip the shared .usd to ASCII to inspect it, then flip it back; never rename the extension and break downstream references.
