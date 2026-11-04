---
id: motion-ae-conditional-logic-for-traded-picks
title: Encode trade and protection rules as conditionals on one number per team, so the live operator only types the pick
domain: motion
tags: [conditionals, traded picks, live graphics, essential graphics, data driven, nba draft, lottery]
applies_to: After Effects
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=M4FLVszXkbk, src:yt-transcripts]
feeds: [broadcast, coach]
conflicts: none
---
The unknown result arrives live, so rules were pre-built [F 00:01-00:34]: Dallas pick 11-14 conveys to New York, 1-10 stays; Chicago top-four stays, 5-14 goes to Orlando [05:19-06:22]. Each team's layer reads its own slider (set via Essential Graphics) and wipes name A out and B in on Y position, not opacity [08:26-11:08].
If slider <= threshold use the same value (no motion), else follow the keyframes from 50 to -50 [10:01-11:40]. Percentages and odds do not change and are not driven [22:31].

**Use it:** the template spec should list every conditional and a test table before air; prefer a position wipe to a cross-fade for cohesion.
