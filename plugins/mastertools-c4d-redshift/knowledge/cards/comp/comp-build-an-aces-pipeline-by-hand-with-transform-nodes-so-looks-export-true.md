---
id: comp-build-an-aces-pipeline-by-hand-with-transform-nodes-so-looks-export-true
title: Resolve's ACES mode gives a more contrasty start than Resolve colour management, so Mostyn builds ACES by hand with an in node, a grade node and an out node
domain: comp
tags: [aces, resolve, aces transform node, acescct, look lut, darren mostyn, deep-read]
applies_to: DaVinci Resolve (ACES 1.3)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AAeZKZ5feGA, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Mostyn [17:36-22:47]: the same raw clip starts more contrasty in ACES (ACEScct, version 1.3) than under DaVinci colour management with wide-gamut timeline, which is lifted and less contrasty; he prefers the latter unless a show like Netflix demands ACES [16:33]. ACEScc has a slightly lower shadow point; ACEScct has a slightly lifted toe that is easier to grade, and most use cct [5:40]. His trick: stay unmanaged, then node 1 = ACES Transform from camera to ACEScct, node 2 = the grade, last node = ACES Transform from ACEScct to Rec.709. Creative tools such as a film-look plugin must be told the input is ACES AP1 and ACEScct, then the look can be exported as a LUT that works in a true ACES pipeline (for VFX on Flame, on set) [21:46]. Grading controls behave in AP1, not in raw AP0 [9:18].

**Use it:** Same pattern for After Effects or Nuke: convert in, grade in the nice space, convert out, and tell every look tool its input space.
