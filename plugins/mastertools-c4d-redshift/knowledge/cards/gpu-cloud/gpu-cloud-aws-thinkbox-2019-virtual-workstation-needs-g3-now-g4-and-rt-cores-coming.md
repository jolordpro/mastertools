---
id: gpu-cloud-aws-thinkbox-2019-virtual-workstation-needs-g3-now-g4-and-rt-cores-coming
title: AWS Thinkbox 2019 virtual workstation spec: G3 GPU instances (Tesla M60), up to four monitors, Teradici zero clients and Direct Connect to keep latency low; G4 with RT cores in demo
domain: gpu-cloud
tags: [virtual workstation, g3, g4, teradici, direct connect, latency, wacom, ec2, siggraph 2019, deep-read]
applies_to: AWS EC2 G3/G4, 2019
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Requirements customers gave: a range of machine specs from Photoshop to fluid sim, Linux and Windows, dual 2K monitors, colour accuracy, audio/video sync, Wacom Cintiq pen support [44:24-46:31]. G3 instances use NVIDIA Tesla M60 GPUs, with multi-GPU sizes and up to four monitors [46:31-47:02]. G4 (with RT cores for real-time ray tracing and game engines) was in the booth demo but not generally available [47:02-48:40]. Setup: Teradici zero or thin clients, a Direct Connect link to the nearest region for latency, and Amazon machine images [48:40-49:41]. MacDonald says the Wacom pressure test showed no lag [51:45]. Workstations can be resized up or down per task [44:56].

**Use it:** pen-pressure latency and region distance are the tests for a remote C4D seat; 2019 hardware is out of date, so use only the checklist.
