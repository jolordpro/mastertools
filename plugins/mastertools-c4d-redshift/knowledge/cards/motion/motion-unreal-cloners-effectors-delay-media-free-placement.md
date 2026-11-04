---
id: motion-unreal-cloners-effectors-delay-media-free-placement
title: Cloners and effectors in Unreal are Niagara-based, cheap, and 5.6 adds delay, media mapped to clones, and free placement
domain: motion
tags: [unreal, cloners, effectors, niagara, displacement, free placement, mograph, deep-read]
applies_to: Unreal Engine 5.5-5.6 Motion Design
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QWT8IAUfWSk, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker is David Grownick, Epic senior product specialist and ex Fox Sports real-time graphics, so vendor view. 5.5: effectors push clones aside in real time; clone counts can go high without much slowdown, collisions work because cloners are Niagara [09:19-10:54]. 5.6: delay property gives ripples that follow an effector and interact [18:36-19:38]; video or image maps across clones for colour and displacement (can invert) [19:38-22:14]; free placement cloner lets you load actors, place them and wipe them into place, with a 600-mesh bus demo that returns to rest after the effector leaves [22:46-24:42]. He cautions cost stays low only if clone counts are sane [21:11-21:42].

**Use it:** C4D users can expect MoGraph-style behaviour but should budget clone counts and watch 59.94 cost.
