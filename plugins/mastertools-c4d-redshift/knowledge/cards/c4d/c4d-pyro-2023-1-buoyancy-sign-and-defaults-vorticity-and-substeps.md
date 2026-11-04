---
id: c4d-pyro-2023-1-buoyancy-sign-and-defaults-vorticity-and-substeps
title: C4D 2023.1 Pyro buoyancy sign rule, temperature buoyancy default 0.015, vorticity for chaos, substeps cure wool-like smoke
domain: c4d
tags: [pyro, cinema-4d-2023, buoyancy, vorticity, substeps, simulation, deep-read]
applies_to: Cinema 4D 2023.1 Pyro
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=TLlITrj5A_4, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Effectatron, 2022 [07:48-14:30]. Settings are duplicated on the tag and the Pyro object.
- Density buoyancy drives smoke; temperature buoyancy drives fire. Negative density buoyancy lifts smoke (more negative = faster), positive sinks it. He used -200 so smoke fills the frame without waiting about 90 frames [08:50-11:22].
- Temperature buoyancy default is 0.015 (he calls it very small); 2 is very high and sprays like a jet, near 0 is a subtle burn [10:21].
- Vorticity strength is the chaos or energy; 10 gives busy small plumes, 2 gives calmer fluffy smoke [10:51-11:22]. Fluid force factor at 10 gave a wispy cigarette-smoke look [11:53].
- If smoke looks like wool instead of smooth connected volume, raise substeps (2 then 6 here); the cost is a slower sim [12:24-14:30].
- Surface emitter with surface thickness makes smoke form on the surface, not through the whole volume [12:24].
- Start density 10 and temperature 1000, each also adding per second; turbulence 10 for extra motion [12:56-14:30].

**Use it:** Starting values and the sign convention when tuning a Pyro sim for a logo or title burn.
