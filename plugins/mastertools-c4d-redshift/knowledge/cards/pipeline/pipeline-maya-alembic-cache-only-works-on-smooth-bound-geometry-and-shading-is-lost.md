---
id: pipeline-maya-alembic-cache-only-works-on-smooth-bound-geometry-and-shading-is-lost
title: Maya Alembic cache (2015 video): only smooth-bound skinned geometry caches; parented or constrained objects drop out and shaders do not travel
domain: pipeline
tags: [3dmpro, maya, alembic, abc import, plug-in manager, smooth bind, geometry cache, reference, maya 2016, deep-read]
applies_to: Maya (video 2015-12; speaker believes reference import is new in Maya 2016); concept applies to any Alembic round trip
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jmjfqFuw0Sc, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Not C4D. Enable the AbcImport/AbcExport plugin in the Plug-in Manager and set it to auto-load so the Cache menu shows the Alembic item [03:42-04:13]. Export selection or whole scene; it writes the geometry's point animation, so geometry plays by itself [04:13-04:44]. Options: timeline or custom range, step size, even start before frame 0 to hold a pose [04:44-05:16].
Limits he demonstrates: a sphere parented to the arm or constrained is missing in the cache because only geometry bound by smooth bind to joints is cached [02:11-03:42, 06:49-07:19]. Shading does not export; re-apply shaders (new or existing) on the referenced copy [07:51-08:25]. Smooth preview needs re-setting on the cache [07:19-07:51].
Bring it back as a reference (he prefers it over import, saying it can still be manipulated) into a group, merging with a prefix on conflicts [05:16-06:49].
Applies the same in C4D: anything not in the point cache (parented props, constraint-driven items) will be missing; check one frame before sending.

**Use it:** in any Alembic hand-off, test by loading the cache in a clean scene and listing what is missing (parented props, materials) before sign-off.
