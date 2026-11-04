---
id: redshift-s22-era-ipr-shows-no-motion-blur-needs-bucket-render
title: Speaker's claim (S22 era): the IPR never applies motion blur; switch to bucket rendering or a region to judge it
domain: redshift
tags: [motion blur, ipr, progressive, bucket, render region, preview, ledger-check, deep-read]
applies_to: Redshift 3.x IPR / Render View, C4D S22 (2020); Redshift Live since 2026.4
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=tsx8Isq6m-s, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Derek Kirk [04:22-05:20]: with progressive rendering in the Redshift render view the sphere showed zero blur; switching to bucket still showed none in IPR. Motion blur appears only in a full render with bucket mode. The ledger says RT was discontinued in 2026.4 and Redshift Live replaced it, so this may not hold for Live; test Live on a moving object before trusting it.

**Use it:** Preview motion blur with a bucket region on a middle frame; treat IPR as blur-free until tested.
