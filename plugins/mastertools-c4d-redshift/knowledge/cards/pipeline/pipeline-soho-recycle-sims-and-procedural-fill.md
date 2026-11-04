---
id: pipeline-soho-recycle-sims-and-procedural-fill
title: Over 100 pyres: simulate a few long fire sims and clone them onto matching shapes, and fill dense scenes procedurally
domain: pipeline
tags: [george razon, soho vfx, game of thrones, fire, simulation reuse, procedural, matte painting, cloning, houdini, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4Z6s5-9o7W0, src:yt-transcripts]
feeds: []
conflicts: none
---
For over 100 burning pyres in a Game of Thrones sequence, a unique fire per pyre would have needed far too much data and time [17:30].
Soho simulated a handful with much longer frame sequences and cloned them onto the pyre each one matched best [18:01].
Dense extensions (Winterfell, tent camps) were built from a matte painting base, procedural trees, procedural snow and scattered crowds, not unique geometry per item [15:25, 21:39].
Fire was matched to a few practical fires that were shot [18:32].
Transfers: for repeated elements in a package (crowd, particles, confetti), simulate a few long variants and re-time/offset copies.

**Use it:** When many copies of a hard-to-render element are needed, plan N unique long variants plus instanced copies and test that repeats do not read.
