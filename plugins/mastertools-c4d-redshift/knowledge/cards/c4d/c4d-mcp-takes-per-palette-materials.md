---
id: c4d-mcp-takes-per-palette-materials
title: An MCP run of 12 colour directions needed one material per palette because a take could not change the colour inside a material
domain: c4d
tags: [mcp, takes, palette, variants, materials, claude, redshift]
applies_to: C4D 2026.4
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ZKPCE7E56nk, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Claude set up 12 takes in seconds; the first attempt failed, then it made a material per palette and let each take swap them [L 02:50-03:12]. Original scene stayed untouched. Renders ran in the background.

**Use it:** when a variant matrix is planned, expect swap-the-material takes, not colour overrides inside one material.
