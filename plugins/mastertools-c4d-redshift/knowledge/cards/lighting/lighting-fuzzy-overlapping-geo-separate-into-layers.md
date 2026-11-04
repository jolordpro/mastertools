---
id: lighting-fuzzy-overlapping-geo-separate-into-layers
title: Very thin, fuzzy overlapping geometry makes artifacts in flat 2D-style depth; separate those elements into layers
domain: lighting
tags: [francesco giroldini, dreamworks, trolls world tour, katana, artifacts, crowds, layers, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=GcPlNw9kFVk, src:yt-transcripts]
feeds: []
conflicts: none
---
Francesco Giroldini (lead lighting/comp artist at DreamWorks, ex-Pixar and Blue Sky; Academy of Animated Art interview): on Trolls World Tour (his first show in a vanilla Katana, with little time to write tools) crowds were large and everything was fast [17:16-17:46].
Much of the film's fuzz was 2D-like, so overlapping thin geometry produced artifacts and had to be separated into layers [17:46-18:18].

**Use it:** Comp note: if thin overlapping elements produce edge artifacts, split into layers before blaming the renderer.
