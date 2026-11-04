---
id: redshift-ipc-secondary-gi-interior-faster-flicker-fix
title: Irradiance Point Cloud as the secondary GI engine halved an interior render; raise retrace threshold to 2-3 to stop animation flicker
domain: redshift
tags: [irradiance point cloud, brute force, secondary gi, retrace threshold, flicker, interior, arch viz]
applies_to: Redshift GPU
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Primary stays Brute Force (accurate, stable); IPC mainly for arch-viz stills as primary [32:07-32:41]. As secondary, IPC fires a point per screen radius of 16 pixels and interpolates, so it is faster and smoother for GI noise [33:11-34:14].
Interior test: 3:36 to 1:48 with a similar look [36:54]. Cost: interpolation can flicker in animation; raise Retrace Threshold to 2 or 3 [34:14, 43:15].
Brute force + brute force may still be needed when passes or AOVs must match in comp [38:04].

Ledger agrees: §6 "Brute Force primary + IPC secondary is a documented general starting point".

**Use it:** a draft-to-final planner treats IPC as a speed option for stills and checks flicker on a few frames before using it on a sequence.
