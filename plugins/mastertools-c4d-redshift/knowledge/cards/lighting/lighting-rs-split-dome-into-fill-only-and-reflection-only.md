---
id: lighting-rs-split-dome-into-fill-only-and-reflection-only
title: Split a dome into two: one fill with reflection off, one with everything zero but reflection, so each can be balanced separately
domain: lighting
tags: [redshift, dome light, hdri, fill light, reflection light, split lights, c4d, deep-read]
applies_to: Redshift dome light
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BlEM9iOzqMI, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Order: add an HDRI dome; it floods the scene, so reduce [16:02]. Tint it bluish to cancel an unwanted brown cast in the HDRI [16:40]. Make the first dome a fill light with reflection removed so the effect on lighting is read alone [16:40]. Duplicate it for the second dome and set every contribution to zero except reflection, then raise intensity until knobs and edges show reflections [19:26][20:03]. He placed it by hand, cheated rotation and intensity, and called it a push and pull. Turn the viewport preview off while duplicating lights so the machine does not choke [19:26].

**Use it:** use the two-dome split when reflections should be tuned without changing the diffuse fill.
