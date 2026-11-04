---
id: lookdev-one-greyscale-map-drives-roughness-and-bump-then-remap-with-ramp
title: Realism recipe: one grey map into roughness (inverted if it is a gloss map) and bump, remapped with a ramp so it stays subtle
domain: lookdev
tags: [[roughness, bump, arnold, standard-surface, ramp, plastic, concrete, metal, mographplus], deep-read]
applies_to: Arnold 6 Standard Surface in Cinema 4D (principle transfers to Redshift)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Qml8EakEAQ4, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
MographPlus: keep specular weight 1, colour white, IOR about 1.5 for everyday dielectrics, and put realism into specular roughness variation [01:35-02:07]. Load a B/W map as Utility/Raw (ACES) [02:37]; if it was made as gloss, invert it with a complement node before a ramp-float [02:37-03:40]. The same map then feeds bump (inverted so white raises) [06:30]. Tame contrast with the ramp: darkest values lifted to about 0.85, brightest pulled to about 0.5 for plastic [03:40-04:45]; concrete reuses its colour map for roughness and bump (bump height about 0.1 cm) [16:44-17:50]; gold: brightest values from 1 to about 0.4 [19:31]. Swap the map to change the whole feel; "specular roughness is the key" [21:37]. Base colour texture is sRGB; roughness/bump data maps are raw [12:28-13:32].

**Use it:** Matches the CHECKS idea that data maps must not be colour-managed; also a quick roughness remap recipe for Redshift ramps.
