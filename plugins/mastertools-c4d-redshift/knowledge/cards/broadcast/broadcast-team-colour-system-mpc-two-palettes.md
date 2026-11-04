---
id: broadcast-team-colour-system-mpc-two-palettes
title: Team colours live in a data table, push into a material parameter collection, and use two palettes (primary and secondary/away)
domain: broadcast
tags: [unreal, team colours, data table, material parameter collection, palette, legibility, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Per-team branding (logos, car skins, colours) sits in a Data Table. On team change the Blueprint reads the row and writes colours into a Material Parameter Collection, which every master material and instance can read [10:12-11:47]. A shared material function with checkbox parameters says whether a surface is dynamic and which team colour slot it takes [11:47-12:19].
Be strategic: do not make everything dynamic. Primary palette shows a team at its best (core, background, accent slots); a secondary palette is for compositions with several teams where legibility needs a compromise, and acts as the away theme [12:19-13:22].

**Use it:** Copy the two-palette rule for matchup boards: a home look and a legibility-safe away look per team.
