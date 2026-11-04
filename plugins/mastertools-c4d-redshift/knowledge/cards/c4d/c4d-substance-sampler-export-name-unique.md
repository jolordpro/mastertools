---
id: c4d-substance-sampler-export-name-unique
title: Substance Sampler export builds the Redshift material in C4D, but reusing a name keeps the old one
domain: c4d
tags: [substance, sampler, export, redshift material, exposed parameters]
applies_to: C4D 2026.1 / Redshift 2026.2
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZAom6DvSi3s, src:yt-transcripts, https://www.youtube.com/watch?v=Xh8A767yA1U]
feeds: [lookdev]
conflicts: none
---
Export to Maxon Cinema 4D from Sampler builds a Substance node material and wires normal/bump/displacement [1:03:49-1:04:50]. Parameters pinned in Sampler show up in Redshift [1:05:21-1:06:52]. Exports with a repeated name failed or reused the old one, so name each export uniquely [1:03:17, 1:05:51].

**Use it:** coach: troubleshooting step.
Transcript support: Second upload; trainer also says a phone photo of a floor imported into Sampler then exported builds a Redshift material. (https://www.youtube.com/watch?v=Xh8A767yA1U [1:01:52-1:07:23])
