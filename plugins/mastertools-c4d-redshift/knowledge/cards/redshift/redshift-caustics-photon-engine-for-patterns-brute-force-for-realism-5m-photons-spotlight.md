---
id: redshift-caustics-photon-engine-for-patterns-brute-force-for-realism-5m-photons-spotlight
title: Redshift caustics: use the Photon engine (not Brute Force) for visible patterns, 5 million photons to clear the noise, and a spotlight rather than an area light
domain: redshift
tags: [caustics, photon, brute force, photons, spotlight, diamond, deep-read]
applies_to: Redshift in C4D (2025-26 era)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BJrUgdVBDts, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Advanced tab: enable Caustics. Brute Force caustics only help glass look more realistic; per Maxon's manual it is not meant for caustic patterns, so choose Photon [01:37-02:41].
The dome light is not needed for the pattern; use a light and bucket-render, since photon caustics do not show without bucket rendering [02:41].
Noise cleared by raising photons to 5 million [02:41-03:11]. An area light was fiddly because of spread; a spotlight worked better [03:11-03:43].
In the final scene photons stayed at 5M, threshold 0.005 [09:04-09:34]. He points to Maxon's caustics manual page for slider examples [00:35].

**Use it:** Caustics scene check: engine Photon for patterns, photon count in millions, bucket mode for preview.
