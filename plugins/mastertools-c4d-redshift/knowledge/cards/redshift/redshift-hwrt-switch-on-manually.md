---
id: redshift-hwrt-switch-on-manually
title: Hardware ray tracing has to be switched on by hand on an RTX 5090 for Redshift
domain: redshift
tags: [hardware ray tracing, hwrt, rtx 5090, settings, rt checkbox, performance]
applies_to: Redshift on NVIDIA RTX
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PJ3eNgTMNKo, https://www.youtube.com/watch?v=L4riSkE7FwA, src:research-youtube, https://www.youtube.com/watch?v=G43QVR1TqXg, src:yt-transcripts]
feeds: [CHECKS settings]
conflicts: none
---
iRender's 5090 test (2026-09-16) names it as the first trap; Maxon's stream has an RT checkbox chapter (39:58). Vendor video, not Maxon docs.
Apple Silicon behaviour is covered by the ledger's Mac rows (section 9), which win there.

**Use it:** warn on NVIDIA cards that support it when the switch is off; do not apply to Macs without the ledger.
Transcript support: Hardware ray tracing is a checkbox; no effect without RTX. RF [09:23] adds it helps brute force. (https://www.youtube.com/watch?v=G43QVR1TqXg [03:10])
