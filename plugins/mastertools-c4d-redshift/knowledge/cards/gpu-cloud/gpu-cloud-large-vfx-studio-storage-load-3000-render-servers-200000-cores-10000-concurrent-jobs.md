---
id: gpu-cloud-large-vfx-studio-storage-load-3000-render-servers-200000-cores-10000-concurrent-jobs
title: Studio storage scale used by A Cup Of Joe: a large VFX studio is 500-1000 artists, 3000 render servers, 200,000 cores, over a petabyte, with up to 10,000 concurrent jobs on the same files
domain: gpu-cloud
tags: [studio storage, render farm, nas, petabyte, isilon, netapp, vast data, a cup of joe, deep-read]
applies_to: VFX/animation studio storage (SIGGRAPH series intro)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=hkzJ3GETmNg, src:yt-transcripts, https://www.youtube.com/watch?v=XSqzTroN_ec]
feeds: [estimator, pipeline]
conflicts: none
---
Intro to a storage series by A Cup Of Joe VFX & Animation [01:04-02:36], undated. Reference large studio: 500 to 1000 artists, five-plus projects, about 3000 render servers, 200,000 cores, storage well over a petabyte [01:04]. Load: as many as 4000 hosts and 10,000 concurrent render jobs may read the same small set of texture and cache files at once, together with artists; you cannot solve it by plugging in more USB drives [02:06]. Each video compares three studio sizes (small, medium, large). Vendors named: Dell PowerScale (formerly Isilon), NetApp, Qumulo, VAST Data, Pixit Media, and some roll-your-own on commodity disk [02:36]. Render farms and storage go together; the series ties to SIGGRAPH birds-of-a-feather sessions on both.

**Use it:** Scale reference for farm-size questions: a freelancer's farm differs by orders of magnitude, but shared-texture contention is the same failure mode.
Transcript support: same 200,000-core large-studio tier appears in the Cup Of Joe size grid (https://www.youtube.com/watch?v=XSqzTroN_ec [17:38])
