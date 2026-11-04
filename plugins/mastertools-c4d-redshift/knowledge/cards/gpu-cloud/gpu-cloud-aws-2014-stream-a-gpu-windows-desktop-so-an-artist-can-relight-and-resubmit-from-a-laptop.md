---
id: gpu-cloud-aws-2014-stream-a-gpu-windows-desktop-so-an-artist-can-relight-and-resubmit-from-a-laptop
title: AWS 2014: a streamed GPU Windows desktop let an artist fix a note in dailies, preview in about 10 seconds and resubmit to the farm from a laptop
domain: gpu-cloud
tags: [aws, 2014, appstream, g2 instance, remote workstation, dailies fix, shotgun, maya, deadline, gpu-cloud, deep-read]
applies_to: AWS AppStream, g2 instances, Maya 2015 (2014)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=cm4sPe1nLjU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Problem stated: remote desktop and VNC cannot run DirectX/OpenGL 3D tools well, so cloud farms stayed headless while artists still needed a GPU box for relighting [20:57-21:59]. The fix shown: a g2 GPU instance streamed with AppStream, which sends H.264 over UDP with an adaptive protocol and reported about 30 fps on the desktop [22:29-23:30, 37:01].
Demo with an Autodesk artist: a Shotgun note says the character needs more sun on his face; from a laptop in the dailies room he opened Maya on the streamed desktop, rendered a preview in about 10 seconds, saved a new file version, submitted through Deadline's Maya toolbox, watched the monitor, and the result appeared back in Shotgun for the director [31:11-37:34].
Failure story: the presenter once shut down a 200-node farm by mistyping on slow in-flight wifi without termination protection on [20:26].

**Use it:** turn on termination protection on cloud nodes; the "fix it during dailies" loop is the benchmark for any remote-workstation-plus-farm setup.
