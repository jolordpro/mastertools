---
id: lighting-expanse-hdr-per-location-from-70-dng-named-by-date-and-time-to-match-the-plate
title: Expanse shot a new HDR for each location and light set-up (320 on one film, 70 DNG exposures each), named by year-date-time to match the plate metadata
domain: lighting
tags: [lighting, expanse, hdr, hdri, naming, nuke, light groups, plate, deep-read]
applies_to: Houdini PDG, Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
On the Mouse feature the team always tries to capture an HDR for each location and each new light set-up, ending with 320 [36:39-37:10]. Each HDR is about 70 DNG files at different exposures [36:39]. Houdini PDG is the hub to batch-convert them; they sit in an HDR asset folder, named year, date and time so the right one is found by reading the timecode and date burned into the shot plate [37:10-37:41]. Final step in Nuke: match the HDR and the plate colour checker and split lights into separate images for flexible light groups and comp [37:41].

**Use it:** Name environment maps by capture time so the shot metadata finds them; split lights into group AOV sources.
