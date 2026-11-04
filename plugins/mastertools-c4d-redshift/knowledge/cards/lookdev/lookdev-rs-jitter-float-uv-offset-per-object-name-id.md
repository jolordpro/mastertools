---
id: lookdev-rs-jitter-float-uv-offset-per-object-name-id
title: Redshift Jitter with Name ID drives a per-object random UV offset: plug float into every UV Remap offset, set max to 1, change the seed
domain: lookdev
tags: [redshift, jitter node, name id, uv remap, texture offset, variation, c4d, deep-read]
applies_to: Cinema 4D Redshift Jitter node
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UjThhVMuV18, src:yt-transcripts, https://www.youtube.com/watch?v=MuVzbVhMUvI]
feeds: [redshift, coach]
conflicts: none
---
Chad (Grayscalegorilla) randomises identical objects with the Jitter node, seeded by Name ID, Object ID or user data; the same names give the same value, so different names are needed [02:34]. Float Jitter output goes into the offset of a General UV Remap on every texture of the material (base colour, normal, and the rest) in exactly the same way, so maps do not slide apart [03:37][04:09]. Float min and max start at 0, so nothing happens until max is 1; then change the seed until the knot lands somewhere good, checking the close-up shot [04:39]. To make some objects match, give them the same name; rename one to break the match [08:20][08:51]. Colour and integer Jitter also exist; integer can pick between switches [03:05].

**Use it:** answer for "all my repeated objects look identical": Jitter on Name ID with UV offset, plus per-shot seed check.
Transcript support: Chad's earlier 2017 way before the Jitter node: ID colour, ramp, Change Range; no seed on the ID so he reshuffles via ramp knots. (https://www.youtube.com/watch?v=MuVzbVhMUvI [35:33-41:45])
