---
id: c4d-alembic-crowd-of-offset-dancers-with-multi-instance-cloner
title: A cheap crowd: ten copies of one Alembic dance with different time offsets, cloned in Multi-Instance mode and varied by a Random effector acting on Modify Clone
domain: c4d
tags: [alembic, crowd, multi-instance, cloner, time offset, modify clone, random effector, stadium, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Trainer (Nosman, Apr 2022). Load one Alembic clip, make 10 copies, and give each a different animation offset (20 frames apart; a 1-frame offset reads as copies) [23:17-24:18]. Clone them 10 by 10 for 100 dancers. Iterate mode cycles through the copies [24:49].
Use Multi-Instance because it renders light, but it cannot blend or sort, so the 10 separate permutations stand in for that. They are cheap because every copy references the same file on disk [25:21]. A Random effector set to affect Modify Clone (not position) randomises which permutation plays; in Multiply blend mode a second random field adds a touch more [25:51-27:28].
Stadium idea: one cloner for seated people, another for people standing up, each with ready animation [26:26]. Redshift rendering in the background slows the viewport; turn it off to judge real time [24:49].

**Use it:** Background crowds for a broadcast open without a crowd sim: offset permutations, instance, then randomise with fields.
