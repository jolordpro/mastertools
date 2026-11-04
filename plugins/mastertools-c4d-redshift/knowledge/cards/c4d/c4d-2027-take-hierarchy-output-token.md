---
id: c4d-2027-take-hierarchy-output-token
title: C4D 2027 can name a render after the whole nested take path, so child takes no longer share a file name
domain: c4d
tags: [takes, take hierarchy, output name, token, nested takes, naming]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts, https://www.youtube.com/watch?v=Cf9t-bPQkb0]
feeds: [estimator, delivery naming]
conflicts: none
---
[01:09:24] A new take-hierarchy token in the output path. With a take XYZ nested under ABC, the saved file carried the whole chain, like one_ABC_XYZ.
Useful for variation jobs that use nested takes.

**Use it:** check that the output pattern includes the take hierarchy token when a project uses nested takes, so variations cannot overwrite each other.
