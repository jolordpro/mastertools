---
id: broadcast-aximmetry-composer-2018-number-the-monitors-and-sdi-ports-and-sync-to-the-sdi-output
title: Aximmetry Composer (2018) startup: number the preview monitor 1 and the SDI output 2, input ports 1-3, sync render rate to the SDI output
domain: broadcast
tags: [aximmetry, composer, startup configuration, sdi, aja corvid, 1080i50, sync, device mapper, preview monitor, backup settings, deep-read]
applies_to: Aximmetry Composer (video uploaded 2018-09-15)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=IWoq_ezCoTY, src:yt-transcripts]
feeds: []
conflicts: none
---
Setup order in a three-camera, one-output virtual studio with no tracking [00:00-07:17]. Use two monitors: one for the control panels and one as preview. Click a device's index to flash its ID tag on the screen. Give the preview monitor number 1, because control boards default to it; give the SDI output number 2.
On an AJA Corvid card with four ports, one port is output and the others are inputs. Default video mode is 1080i50. Tick the sync box on the main SDI output so the render rate follows it (50 per second here). Then number the inputs 1, 2, 3 in the device mapper so control boards pick them up without extra wiring.
Use Manage settings to back up the startup group to a file and restore it after a reset. A preview monitor shows half the frame rate (25p) in interlaced mode, which looks choppy but is normal; SDI figures must match.
Version is the 2018 Composer; later releases may differ.

**Use it:** Copy the numbering order (preview 1, output 2, inputs 3+) and the backup habit when documenting a virtual-studio start-up checklist.
