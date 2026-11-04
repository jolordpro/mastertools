---
id: motion-unreal-cache-cloner-to-sequencer-for-mrq
title: Cache a cloner as a Niagara track in Sequencer so scrubbing is deterministic and Movie Render Queue renders it
domain: motion
tags: [unreal engine, cloner, cache, sequencer, niagara, movie render queue, deterministic, deep-read]
applies_to: Unreal Engine 5.5
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5P-sO_2aiwU, src:yt-transcripts]
feeds: [pipeline, CHECKS]
conflicts: none
---
Cloners can be cached as a Niagara track: a Utilities panel at the end of each cloner has a button that adds a Sequencer track with the particle lifetime and a cache button [29:29] [30:00]. He says this makes scrubbing deterministic and lets the result render out of Movie Render Queue and Movie Render Graph (MRQ/MRG) [30:00].
Particle-physics results are also cacheable this way [10:48].
Also noted: right-click any actor in the Outliner to create a cloner from it, and bake a cloner to a static mesh to merge replicated shapes into one object [28:26].

**Use it:** Failure-mode note for any real-time motion render: uncached simulation scrubs differently each time; cache before the final render pass.
