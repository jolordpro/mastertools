---
id: broadcast-test-stadium-scale-graphics-by-outputting-tracking-from-a-digital-twin
title: Test stadium-size AR graphics by driving a real tracked-camera chain from a digital twin, not by scaling the graphic or moving it far away
domain: broadcast
tags: [stadium, digital twin, scale testing, camera tracking, blackmagic, ar graphics, girraphic, unreal, deep-read]
applies_to: Unreal Engine 5 (2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=2DoF-oYNQgU, src:yt-transcripts]
feeds: []
conflicts: none
---
Girraphic [10:22-14:04]. Unreal features depend on camera distance and on size in viewport (LODs, culling and similar), so scaling the graphic down or pushing it away either creates false problems or hides real ones. Instead a plugin outputs camera tracking data instead of taking it in: a digital twin of the stadium goes out through a Blackmagic card as video, with camera XYZ tracking, and the broadcast chain treats it as a tracked camera at real scale. This tested look, controls and placement systems. Caveat: it looks like a movie render, so it does not prove to a client that a tracked, composited chain is working. Because it speaks a standard protocol it also tests non-Unreal graphics engines over the same digital-twin background.

**Use it:** If a graphic must work at huge scale, test in a real-scale scene rather than shrinking it; keep a clear note that this is a test chain and not a camera proof.
