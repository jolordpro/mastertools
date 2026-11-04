---
id: pipeline-union-guiding-principles-no-searching-no-guessing-versions
title: Union VFX pipeline rules: artists never search for assets, never guess versions, and every asset version links to the scene that made it
domain: pipeline
tags: [union vfx, rob hopper, dave schneider, pipeline principles, shotgrid, usd, houdini, version tracking, deep-read]
applies_to: Houdini, USD, ShotGrid
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nUXfEdZ-7Xs, src:yt-transcripts]
feeds: [pipeline plan, CHECKS]
conflicts: none
---
Union's pipeline team (Dave Schneider, CG and technical supervisor) wrote guiding principles after seeing email-chain hunts for the right camera and repeated renders [05:42-06:44]. Artists should not search for assets or work out versions. Artists and supervisors can inspect a shot's current state without rendering everything together [07:15]. Every asset version links to the scene file that created it, so a daily from a month ago can be traced and recreated [07:46-08:48].
Constraint: a one-developer team, so little custom code, reuse of third-party tools and Houdini-only skills for upkeep (keep it simple) [08:48, 18:09].

**Use it:** Pipeline spec checklist for a small studio.
