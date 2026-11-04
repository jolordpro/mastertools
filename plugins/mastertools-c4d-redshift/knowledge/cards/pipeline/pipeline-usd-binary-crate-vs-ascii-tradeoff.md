---
id: pipeline-usd-binary-crate-vs-ascii-tradeoff
title: USD binary (usdc) reads faster and is smaller; ASCII (usda) is slower and bigger but readable
domain: pipeline
tags: [usd, usdc, usda, crate, file size, houdini, deep-read, nine between, solaris, file format]
applies_to: USD, Houdini Solaris 19.5
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts, https://www.youtube.com/watch?v=cE-Bbdspu_8]
feeds: [CHECKS, coach]
conflicts: none
---
Peter Arcara (SideFX) lists three extensions: .usd (binary by default, can be ASCII), .usda (ASCII only), .usdc (binary "crate" only) [10:25-12:00].
Binary: faster reads, smaller files, not human readable. Use for big geometry, whole assets and sims. ASCII: slower and larger but readable. Use for simple scenes and assets you may need to inspect [11:00-12:00].
His test: the same geometry-heavy scene written as ASCII vs binary was roughly 4x smaller as binary, and he says 4x is not guaranteed [1:11:16-1:11:47].
Merged from `pipeline-nineb-usda-for-reading-usdc-for-final`: USDA is ASCII: readable, bigger, slower to load. USD/USDC is binary: much smaller and faster, unreadable. Use USDA while checking and hand-editing, binary for the final output [18:08-19:12, 22:54-23:25]. Demo: he opened the USDA, changed a material's colour value from orange to green (0,1,0), saved and reloaded: the scene turned green, proving the scene reads the file and not the original network [25:31-26:01]. Houdini Apprentice (non-commercial) writes .usdnc, which cannot be opened or read [18:41-19:43].

**Use it:** Default heavy assets and anything handed downstream to binary; keep ASCII only for small files someone must open and read.
