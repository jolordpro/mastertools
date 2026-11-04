---
id: c4d-pyro-advection-emit-over-time-lifetime-caps-particle-count
title: Budget advection particles by emission rate times lifetime: 50,000 per second at a 90-frame life tops out at 150,000; a particle group max count is the rate times the seconds alive
domain: c4d
tags: [particles, emitter, lifetime, particle count, max count, advection, budget, crash, deep-read]
applies_to: Cinema 4D 2025 particles (Sketchy Visuals, uploaded Dec 2025)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vrE2wrqq0TM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Sketchy Visuals [11:34-14:40]. Particles are only points. Emit constantly over the whole animation so points exist everywhere, but set a lifetime or the count climbs for ever (a million per second becomes about 12 million at the end and crashes the scene). With 50,000 per second at 30 fps and a 90-frame life the live count levelled at 150,000; the emitter value is per second, so 1,000,000 per second at a 3 s life means 3 million in the group. Restart the sim if the cap looks wrong [13:37-14:08].
His finals ran about 2.5 million particles; with life cut to 60 frames, up to about 5 million. More particles needs a smaller radius (0.3 instead of 1) to show finer trails [32:18-33:21].
Set the emitter speed to 0 so the pyro does the moving; the emitter box matches the source cube [11:01-12:05].

**Use it:** Do the arithmetic (rate x seconds alive) before any pyro-advection cache so memory and cache time are known.
