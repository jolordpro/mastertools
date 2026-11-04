---
id: pipeline-blank-frames-rgb-not-rgba
title: Blank or messy composite frames came from PNGs rendered RGB only; switching to RGBA gave usable layers
domain: pipeline
tags: [rgba, alpha, composite, blank frames, png, deadline cloud, layers]
applies_to: AWS Deadline Cloud demo (Apr 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=zz10CeybNeQ, src:yt-transcripts]
feeds: [preflight]
conflicts: none
---
[02:40 to 03:46] Two suspects: the composite script, or PNGs without alpha. Fixing the script showed all layers but transparency was inconsistent; rendering RGBA gave good layer definition.

**Use it:** check that layered renders write alpha before a composite step.
