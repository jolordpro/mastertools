---
id: redshift-maya-shadow-catcher-holdout-setup-two-catchers-reflection-weight-1-env-off
title: Redshift Shadow Catcher in Maya (2020): two catcher materials, background as environment, dome shadows off, environment off for the final render
domain: redshift
tags: [redshift, shadow catcher, holdout, alpha, backplate, maya, cryptomatte, aov, compositing, avfx, deep-read]
applies_to: Maya + Redshift (video April 2020, Redshift 2.x era)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=aplU2CXwXLY, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
AVFX student tutorial (Maya, not C4D) [01:05-10:39]. Rebuild rough stand-in geometry for the room so light bounces; give it a Shadow Catcher material. Make two catchers: one that only catches shadows (diffuse and reflection off) and a second for reflective surfaces (reflections on). Dome light with an HDRI similar to the plate; put the plate in the dome's backplate slot and tick background-is-environment on both catchers so the full frame shows [05:49-07:24]. Turn off shadows on the dome light. Before final render, switch the dome's environment visibility off so the alpha is clean; the two visible squares were only IPR artefacts [07:56-08:59]. Set catcher reflection weight to 1 (not 0.6): you can darken in comp later but cannot raise it [08:59-09:33]. Match render resolution to the plate; add a Shadow AOV and a Cryptomatte AOV; render EXRs [09:33-10:39]. Not verified against the ledger; version is early Redshift 2.

**Use it:** if a C4D shot needs a matte pass, mirror this: catcher for shadows, catcher for reflections, full reflection weight, cryptomatte AOV.
