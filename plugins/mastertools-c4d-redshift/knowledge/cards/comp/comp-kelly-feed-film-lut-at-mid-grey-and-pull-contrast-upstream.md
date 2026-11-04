---
id: comp-kelly-feed-film-lut-at-mid-grey-and-pull-contrast-upstream
title: "Cullen Kelly parks exposure at the container's middle grey before a film-print LUT, and pulls contrast upstream if the LUT is too crunchy"
domain: comp
tags: [cullen-kelly, lut, exposure, middle grey, toe, shoulder, 2383, davinci wide gamut, polish, deep-read]
applies_to: DaVinci Wide Gamut Intermediate
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, coach]
conflicts: none
---
A film-print LUT has a roughly linear middle with a toe and shoulder; shadows that land in the toe are pushed further down, highlights in the shoulder further up, while middle grey does not move [1:00:51-1:02:28]. So under- or over-exposed input gets exaggerated. Ideal feed: middle grey of the working space; for DaVinci Wide Gamut Intermediate he recalled about 344 on a 10-bit scale and said to check his cheat sheet, so the number is unverified [1:02:28]. Film prints are contrasty; if the crunch is too much, pull contrast out upstream and keep the LUT as is. He says that is not cheating [1:03:00-1:04:02].

**Use it:** Expose or normalise renders so mid grey sits at the working space's middle grey before applying a print-style look.
