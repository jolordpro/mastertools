---
id: lighting-light-link-focus-lights-so-they-do-not-blast-the-floor
title: Use light linking so accent lights meant for one object do not light the floor and distract
domain: lighting
tags: [light linking, octane object tag, ids, focus, distraction, school of motion, deep-read]
applies_to: Octane (2022); Redshift has equivalents
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KbuUzj0Yj4A, src:yt-transcripts]
feeds: []
conflicts: none
---
School of Motion [04:17-05:28]. Strong lights meant to focus attention on a small object also blasted the floor. In Octane: give the floor an object tag that ignores lights with ID 2, then set the area lights to ID 2. Result: the floor no longer lights up from them. He credits this with saving the project. Related caution in this repo: light linking and GI bounce can still carry light into the excluded object.

**Use it:** Use when an accent light is helping the hero but ruining the surroundings; check the existing card on light linking and GI bounce first.
