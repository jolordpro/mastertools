---
id: pipeline-moonray-timeline-2012-to-2023
title: MoonRay timeline: studied in 2012, project started 2013, proof of concept end 2014, first film 2019, open-source greenlight Jan 2022, public release Mar 2023
domain: pipeline
tags: [[moonray, dreamworks, timeline, open source, aswf, how to train your dragon hidden world, bill ballew, renderer development], deep-read]
applies_to: MoonRay, ASWF
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fQUnq6drevw, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Bill Ballew (DreamWorks CTO) [06:46-11:47]: in 2012 the studio saw its most ambitious film (How to Train Your Dragon: The Hidden World) needing global illumination, soft shadows and physically accurate bounce light at a new scale, while CPUs had stopped doubling clock speed and offered more cores and wider SIMD vector units instead. In 2013 it launched an in-house renderer, had a proof of concept by the end of 2014, and committed the first show within a couple of years; the film shipped in 2019.
Open source: greenlit January 2022, announced at SIGGRAPH August 2022, first public release March 2023 after months of untangling and hardening. About 13 community updates in three years, and ASWF membership in 2026 [11:11-11:47, 17:28].
Lesson of the pace: a clean-slate renderer was a six-year road to production use.

**Use it:** use as a realism check when scoping any custom render tooling: a proof of concept in about 18 months, production use years later.
