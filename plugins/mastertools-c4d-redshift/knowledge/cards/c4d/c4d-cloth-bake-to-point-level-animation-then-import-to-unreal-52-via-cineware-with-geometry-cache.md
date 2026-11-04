---
id: c4d-cloth-bake-to-point-level-animation-then-import-to-unreal-52-via-cineware-with-geometry-cache
title: Cloth from C4D to Unreal 5.2 without Alembic: cache, Bake Objects to point-level animation, save, import with Cineware (2023.7) and Datasmith, geometry caches on
domain: c4d
tags: [winbush, cloth, bake objects, point level animation, cineware, unreal engine 5.2, datasmith, geometry cache, sequencer, unreal hand-off, cinema 4d 2023, deep-read]
applies_to: Cinema 4D 2023 (latest at upload, 2023-08), Unreal Engine 5.2, Cineware for Unreal 2023.7
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=TEM9BU-Fp0E, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker: Winbush. Scene: 2000x2000 landscape as collider, 200x200-segment plane (dense mesh) with a cloth tag [00:00-01:33]. Project set to 60 fps and 300 frames in both Render Settings and Project settings before caching [01:33-02:05]. Make the plane editable, cache the cloth, play to check [02:05-02:35].
Bake: in the Animate layout, drop the cloth in the timeline, at first frame choose Functions, Bake Objects, turn everything off except the point-level animation attribute, keep 300 frames; this creates a copy with keys; delete or keep the original [02:35-03:39]. In Project settings, under the Cinema 4D file save-geometry options, choose Cache Polygon Animation (caption reads garbled; menu name is unsure) [03:39]. Save the file.
Unreal: install the Cineware for Unreal installer from the Maxon site before opening Unreal; the plugin appears as Cineware by Maxon (2023.7 that day) and should be on [03:39-05:10]. He says not to use the older Datasmith C4D importer [05:10]. Datasmith, File Import, pick the .c4d, leave defaults, but keep Import Geometry Caches on (others grey out without it) [05:10-06:10]. Pick only the object that actually has a cache (the cloth, not the static landscape) [06:10-06:40]. Result: two sequencers, one for the cloth and a main one; plays in Unreal with no Alembic file [07:11-07:42]. He mentions Redshift textures can come across in this route as of that day [05:40], which conflicts with the later Cineware card noting Redshift materials do not map (see updates).

**Use it:** for a cloth/sim hand-off to Unreal, bake to point-level animation first, set fps to match the engine, import with Cineware plus geometry caches on; re-check the steps each Cineware release.
