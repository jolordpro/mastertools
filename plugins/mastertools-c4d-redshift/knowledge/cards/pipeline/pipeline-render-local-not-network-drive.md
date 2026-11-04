---
id: pipeline-render-local-not-network-drive
title: Render to a local drive and move frames afterwards; never render straight to a network drive
domain: pipeline
tags: [render output, network drive, local render, dropbox, output path, irender, render local, farm, io, delivery]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PJ3eNgTMNKo, src:research-youtube, https://www.youtube.com/watch?v=FNhUnPWzVaw, https://www.youtube.com/watch?v=9mcDxU9P2Hs]
feeds: [CHECKS 4 output setup, CHECKS 4]
conflicts: none
---
iRender's 5090 test warns about this beside hardware ray tracing needing a manual switch. Its cloud workstation is a remote machine, not a queue.
Merged from `redshift-render-local-then-move`: Stated in iRender's 5090 test description as a trap. It is vendor advice for cloud workstations, in the same spirit as the planned Dropbox watcher rule.

**Use it:** warn when the output path sits on a mounted or synced volume.
Transcript support: output on the remote machine's C drive, then copy to the persistent drive (https://www.youtube.com/watch?v=9mcDxU9P2Hs [01:39])
