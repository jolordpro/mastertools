---
id: pipeline-remote-desktop-lookdev-mac-render-pc
title: Look-dev on a Mac and send the render to another machine so IPR stays live; remote desktop into a render PC was the earlier fix
domain: pipeline
tags: [Nick, Greyscalegorilla, Parsec, remote desktop, IPR, render offload, Mac, deep-read]
applies_to: C4D + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts, https://www.youtube.com/watch?v=p0ARF7a6V28]
feeds: [estimator, coach]
conflicts: none
---
Nick (host, Greyscalegorilla) kept a Mac for email and calls and logged into a PC with a remote-desktop tool (Parsec) that ran Cinema 4D, so the loud, hot machine sat in another room [21:03-22:04].
The catch he names: when a render starts on the same GPU, the IPR dies because the GPU is busy rendering frames [28:23].
His fix was to do look-dev on the Mac and send the job to other machines through Team Render, so he kept working while it rendered: "kick it off, keep working" [28:54].
Transfers: the draft-render step can live on a different box from the one the artist is sitting at.

**Use it:** Scene advisor and estimator: treat 'render on the artist's own GPU' as a cost, the artist loses IPR and interactivity while it runs; offload when a look is nearly right.
Transcript support: AnyDesk vs Parsec comparison for working on a remote workstation; avoid for final comp or grading (https://www.youtube.com/watch?v=p0ARF7a6V28 [03:06-06:43])
