---
id: c4d-python-store-color-aov-unreliable
title: Linking a Store Color To AOV node to an existing AOV from Python was reported unreliable
domain: c4d
tags: [python, store color to aov, aov, node, port id, limitation]
applies_to: C4D 2025 threads
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.maxon.net/forum/post/70800, https://developers.maxon.net/forum/post/76522, src:research-gaps-deep, https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [PLAN 0.2]
conflicts: none
---
A port-id workaround exists and the AOV must already exist. Status on 2027 is unknown.

**Use it:** create the AOV first, then link, and verify by reading back.
Transcript support: Store Color to AOV is the manual route to exclude materials from an AO AOV. (https://www.youtube.com/watch?v=CXx75LxGxOw [53:58])
