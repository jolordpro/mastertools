---
id: broadcast-capacity-four-letter-team-codes-drive-path-swap
title: Four-letter team codes drive path behaviors that swap every logo, colour and photo for a team by typing the code
domain: broadcast
tags: [remote control, path behavior, team codes, naming convention, toolkit, capacity, epic, deep-read]
applies_to: Unreal Engine 5.6 / 5.7 remote control
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts, https://www.youtube.com/watch?v=Ty6etYkvaC8]
feeds: []
conflicts: none
---
A team or player needs strict naming, so the project used four-character codes [1:06:33]. One controller holds sport, league and asset-type inputs; a path behavior builds a content-browser path from them [1:12:54-1:13:56]. Typing a team code (e.g. 'hair') or a player code swaps colours, patterns, brush scripts and portraits at once [1:14:27-1:14:58]. In 5.6.1 each actor needed its own path behavior; 5.7 lets one behavior drive many actors, lets entries be reordered, and checks each path slot with ticks and a preview path [1:17:02-1:20:05]. Capacity said it also made rendering sample reels easy, and cleaner than the MOGRT-style template handoffs they did before (caption reads 'bogurt') [1:14:58-1:15:29].

**Use it:** Plan folder structure and file names so one short code resolves to every asset; this is the same trick as a driven take or a data-driven template in C4D/AE.
Transcript support: Brush edge colour comes from a pixel-coded texture exposed in remote control; typing the team code in the rundown changes the path that picks the texture. (https://www.youtube.com/watch?v=Ty6etYkvaC8 [06:47-08:24])
