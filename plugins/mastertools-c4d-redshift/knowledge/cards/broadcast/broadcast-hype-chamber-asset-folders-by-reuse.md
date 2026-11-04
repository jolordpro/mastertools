---
id: broadcast-hype-chamber-asset-folders-by-reuse
title: Hype Chamber splits assets into shared artist elements, per-graphic scenes and per-team elements
domain: broadcast
tags: [unreal, folder structure, naming, team elements, broadcast package, deep-read]
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
Three top folders [06:01-06:33]: _ArtistElements holds reusable engineering assets (core Blueprint logic, environment meshes, materials, media, presets); _Scenes holds anything tied to exactly one broadcast element, e.g. a BUMP_TeamVictory folder with its map, sequence, sound and Blueprints; _TeamElements holds per-team textures, logos and materials.
Reason: reuse vs one-off vs per-client data are kept apart so a new team never touches core logic.

**Use it:** Mirror this split (shared / per-graphic / per-team) when naming and foldering a sports package in C4D or AE.
