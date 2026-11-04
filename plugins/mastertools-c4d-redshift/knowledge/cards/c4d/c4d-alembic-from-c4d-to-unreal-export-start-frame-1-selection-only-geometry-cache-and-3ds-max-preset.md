---
id: c4d-alembic-from-c4d-to-unreal-export-start-frame-1-selection-only-geometry-cache-and-3ds-max-preset
title: Alembic C4D to Unreal 4.25 (2020) - export from frame 1, selection only, import as Geometry Cache from frame 0 with the 3ds Max preset
domain: c4d
tags: [alembic, unreal, datasmith, geometry-cache, cinema-4d, unreal-4-25, flags, deep-read]
applies_to: Cinema 4D (version not stated) and Unreal Engine 4.25, video 2020-10-29
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=cut-ZBaB1b0, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
The Pixel Lab flag pack tutorial (presenter Jonathan Winbush), uploaded 2020-10-29.
- Alembic export [05:05-06:18]: select only the alembic objects, File, Export, Alembic; keep timeline short (600 to 300 frames) because file size grows with length; start at frame 1 (frame 0 gave glitches in Unreal for him); Selection Only on; Global coordinates for splines.
- File size warning: his import dialog showed a huge number that the captions give as "200 gigs for three frames", which is likely a mishear [08:52].
- Unreal import [08:31-09:53]: Alembic type Geometry Cache (experimental, worked for him), frame start 0 and end 300 though C4D started at 1, preset 3ds Max so it arrives upright; checks that all boxes are ticked or the export was wrong.
- Materials: Datasmith C4D plugin (enable in Plugins, restart) imports the scene and only native C4D materials, not Redshift, V-Ray or Octane; geometry cache textures must be reassigned in Unreal [11:58-13:32]. Light made Movable for dynamic lighting [12:30].
- Playback needs a Level Sequence with the geometry cache track; set end frame 300 and loop [16:25-17:39].
- Reflectance in C4D was a GGX layer at 1 percent, as the best match to Unreal [02:41-03:11].

**Use it:** Check list for C4D to Unreal cache hand-off (see also c4d-cineware-unreal-5-7 for the newer path).
