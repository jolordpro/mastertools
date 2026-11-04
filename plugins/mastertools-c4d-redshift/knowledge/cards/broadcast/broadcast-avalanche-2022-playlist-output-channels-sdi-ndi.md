---
id: broadcast-avalanche-2022-playlist-output-channels-sdi-ndi
title: Avalanche's playlist tool sends pages to as many output channels as needed (SDI, Blackmagic, AJA, NDI, full-screen GPU); ST 2110 was untested
domain: broadcast
tags: [unreal fest 2022, epic games, avalanche, andy blondin, bernt bk, playlist, sdi, ndi, aja, blackmagic, st 2110, deep-read]
applies_to: Unreal Engine 5.1-5.2 (2022)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XAtjoawRN_Y, src:yt-transcripts, https://www.youtube.com/watch?v=crMTfD5XVkA]
feeds: [estimator]
conflicts: none
---
Live shows use many headless render engines. The playlist holds pages, each assigned to an output channel with local preview before air [30:24-31:27]. Outputs listed: SDI, Blackmagic, AJA, NDI, full-screen from the GPU, and 2110 via Rivermax, 'not tested' [31:27-32:30].
Epic wanted to focus on in-engine design and open the external control to third-party automation partners [34:05-34:37]. Intended also for Twitch and YouTube streamers [31:58].

**Use it:** When scoping live delivery, note the output path (SDI vs NDI vs fill/key) early, since it decides the hardware and test time.
Transcript support: NDI for animation, data and video as the soft alternative to SDI wiring in Unreal. (https://www.youtube.com/watch?v=crMTfD5XVkA [01:34-02:06])
