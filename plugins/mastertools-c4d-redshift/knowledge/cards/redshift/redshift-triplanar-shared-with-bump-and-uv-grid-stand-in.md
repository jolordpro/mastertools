---
id: redshift-triplanar-shared-with-bump-and-uv-grid-stand-in
title: Triplanar: same image on every axis by default, reuse one triplanar for colour and bump or they drift apart, debug with a UV grid image
domain: redshift
tags: [triplanar, bump, uv grid, texture mapping, auto request texture, normal map, greyscalegorilla, chad, deep-read]
applies_to: Redshift 2.x in C4D (2017 stream)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=MuVzbVhMUvI, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
The triplanar node puts the same image on all three axes unless told otherwise, saving clicks; raise the blend so the projections meet softly [32:54-35:00].
The bump needs the same triplanar settings or it will not line up, and as far as he knew a copy could not keep connections, so he rewired by hand; a normal map node would not take the triplanar, so he used the height map through a bump node [43:18-44:53].
He keeps a UV grid image to stand in for the real texture while judging mapping, and uses the option that opens a file browser when a texture node is dropped in [34:00-34:30, 32:23].

**Use it:** lookdev tip for scenes with no UVs; the UV Context Projection cards are the newer way to do the same.
