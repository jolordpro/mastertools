---
id: c4d-pyro-2023-1-tag-and-object-material-goes-on-the-pyro-object-and-visibility-toggles-are-off
title: C4D 2023.1 Pyro makes a tag and a Pyro object; the Pyro Volume material goes on the object and its visibility toggles start off
domain: c4d
tags: [pyro, cinema-4d-2023, redshift, simulation, setup, deep-read]
applies_to: Cinema 4D 2023.1 (Pyro first release, Nov 2022) with Redshift
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=TLlITrj5A_4, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Effectatron (Derek Kirk), uploaded 2022-11-10, a day after Pyro shipped in C4D 2023.1 [00:00-05:42].
- Adding Pyro from the Simulation Tags menu creates two things at once: a Pyro tag on the emitter (look of the sim: smoke, temperature, fuel, velocity, noise) and a Pyro object (scene-wide behaviour: turbulence, combustion, dissipation, substeps) [02:05-03:38].
- A scene floor only interacts if it carries a Cloth Collider tag [02:05].
- Render shows only a white ball until a Redshift Pyro Volume material is on the Pyro object, not on the emitter [04:09]. It is the normal Volume material with the simulation channels (temperature etc.) already wired.
- Still blank after that: the object tab has per-property toggles (a few on for export only, the rest off). Switch all to on so the sim shows in the viewport and render [04:39-05:42]. He does not know why they default to export only.
- Gravity must be on in project settings (Ctrl+D) or buoyancy does nothing [08:19].

**Use it:** A "Pyro renders empty or white" check: material on the Pyro object, visibility toggles on, gravity on, collider tag on any floor.
