---
id: comp-kelly-rec2020-limited-to-p3-means-clamp-at-p3
title: Kelly: "Rec 2020 limited to P3 D65" means master in P3, clamp to the 0-1 range in P3, then convert to the 2020 container
domain: comp
tags: [cullen kelly, rec 2020, p3 d65, netflix, deliverable, dctl, clamp, hdr, st2084, polish, cullen-kelly, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=upUAulx7sGI, src:yt-transcripts, src:polish-roster]
feeds: [CHECKS]
conflicts: none
---
Kelly [27:25-35:49]: no display shows all of Rec 2020, so a 2020-limited deliverable is graded in P3, kept inside P3's bounds, and stored in a 2020 container. In Resolve nodes his workaround: output to P3 D65 with ST 2084 and 1000-nit mapping, go P3 to Rec 2020 with tone and gamut mapping off, and add a clamp step to keep values in 0-1 while still in P3 (he uses a three-line DCTL; Resolve has no built-in clamp as far as he knows, and he says he was working it out live). He also notes a display claiming 97% of a gamut cannot show that gamut.

**Use it:** the check for streaming specs: confirm the limited-to-P3 box is respected by clamping before the container conversion. Unverified live workaround.
