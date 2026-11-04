---
id: redshift-sss-use-cases-transmission-vs-subsurface-thin-wall-and-hybrid
title: Redshift standard material has two translucency tools: transmission scatter colour and depth (single scattering) and subsurface (multiple); thin wall for leaves; juice needs both at about 50 percent transmission
domain: redshift
tags: [subsurface, transmission, scatter color, depth, thin wall, random walk, translucency, orange juice, renderbaron, deep-read]
applies_to: C4D + Redshift standard material (renderbaron upload 2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=a5BDzPkwlUM, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Four cases [00:41-10:08]: (1) coloured glass uses transmission scatter colour and depth only, single scattering; near-zero depth turns it nearly opaque [01:20-02:48]. (2) Tomato, broccoli: subsurface weight, scale (max depth), colour and radius, in random-walk mode [02:48-05:57]. (3) Leaves and paper: tick Thin Wall in the geometry section; subsurface keeps only colour and weight, and refraction index is ignored [06:15-07:10].
(4) Juice: transmission-only with scatter colour orange and depth 1.2 cm looks flat because hue never varies; subsurface weight 1 alone changes nothing on a fully transmissive material; drop transmission weight to roughly 50 percent so multiple scattering has medium to live in [07:25-09:55].
He notes the Redshift docs call thin-wall behaviour translucency while common usage includes multiple scattering [07:00].

**Use it:** the coach maps a material (glass, skin, leaf, drink) to one of four setups. Complements `redshift-standard-material-transmission-depth-and-scatter-color-fake-sss`.
