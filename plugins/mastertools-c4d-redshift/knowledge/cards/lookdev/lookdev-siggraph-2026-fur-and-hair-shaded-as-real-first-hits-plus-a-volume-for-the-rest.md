---
id: lookdev-siggraph-2026-fur-and-hair-shaded-as-real-first-hits-plus-a-volume-for-the-rest
title: SIGGRAPH 2026 paper pitch: keep first hits on real hair strands and treat deeper scattering as a volume, near path-traced softness at 7-10x speed
domain: lookdev
tags: [lookdev, siggraph, papers, hair, fur, feathers, rendering, research-radar, deep-read]
applies_to: research paper, not a shipping tool
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=u6xhzA40Af0, src:yt-transcripts]
feeds: []
conflicts: none
---
From a 20-second pitch in the SIGGRAPH 2026 technical papers fast forward (auto captions; authors and title not captured). Claim: render the first fibre hits on real strands and model remaining multiple scattering as a volume, giving the soft look close to full path tracing about 7 to 10 times faster [1:14:10-1:14:41]. The same session has hair-generation papers: strand-by-strand generation from a language-like format, strands from meshes, hairstyle transfer between faces, and curved models for tightly coiled afro-textured hair [1:13:06-1:14:10].

**Use it:** Radar only: if hair or fur renders are the bottleneck, look up the 2026 hair/fur/feathers session papers before building tricks; not usable in C4D/Redshift today.
