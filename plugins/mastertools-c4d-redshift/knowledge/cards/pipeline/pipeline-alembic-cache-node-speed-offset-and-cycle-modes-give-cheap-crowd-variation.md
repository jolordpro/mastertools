---
id: pipeline-alembic-cache-node-speed-offset-and-cycle-modes-give-cheap-crowd-variation
title: One Alembic cache plus node edits (speed 0.9, 0.5, offset 100 frames, loop, reverse, bounce) and instances gives a crowd with varied timing
domain: pipeline
tags: [3dmpro, maya, alembic, cache node, crowd, instances, duplicate special, offset, bounce, loop, variation, deep-read]
applies_to: Maya (video 2015-12); idea transfers to other cache readers
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jmjfqFuw0Sc, src:yt-transcripts]
feeds: []
conflicts: none
---
On the cache node you can change speed (0.5 plays at half, 2 at double) [08:38-09:27], add a start offset (100 frames holds until frame 100) [09:27-10:00], or use values like 0.9 so two copies drift apart and read as separate dancers [10:00-10:30]. Cycle options beyond the default hold: loop, reverse, bounce (forward then back) [10:30-11:32].
Crowd build: Duplicate Special with instances and a position offset (for example 2 units on X, five copies); all instances share one cache node, so one change (for example 0.95 speed) hits every copy [12:04-13:07]. A second reference of the cache gives a second line at a different speed; foreground bounce plus background loop makes a continuous loop [13:07-14:33]. Playback stays light because it reads only two cache files [13:38-14:33].
Mocap origin note: a rig test with free mocap, then edit the source keys and the skinned character updates [01:07-01:38].

**Use it:** for background crowds, use one cache with instanced copies and vary node speed or offset slightly rather than rendering separate takes.
