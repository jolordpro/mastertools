---
id: pipeline-image-engine-update-mailbox-and-qc-renders
title: Image Engine's pipeline tells each artist when a newer upstream version exists, and uses QC renders to catch a wrong or missing asset
domain: pipeline
tags: [image engine, gaffer, versioning, bundle, qc render, thomas schelesny, alex fuller, deep-read]
applies_to: Gaffer, Maya, Houdini, Nuke
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cID-j-f3Mj8, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Alex Fuller (lighting TD) and VFX supervisor Thomas say the wrong-version failure (animation not picked up by the lighter) was solved with software, not post-its [1:03:27, 1:01:22]. When an artist is ready to show a shot they bundle the work as "unapproved", link a render, and it is dailied; production approves the bundle and it passes on like a mailbox update. Opening a scene shows "newer version waiting", so a compositor is warned before a final comp that lighting has a new version. QC renders show the correct starter asset came in, catching a publish that is missing a character or has the wrong animation [1:01:52]. Their old example: 5 of 40 bugs rendered with stale animation on a 1996 film [4:15]. They claim near-zero overtime comes from this support. Host-level claim, no numbers beyond that.

**Use it:** Model for the platform's handoff checks: show "newer upstream version exists" before a final render or comp, and keep a QC render that proves every expected asset is present.
