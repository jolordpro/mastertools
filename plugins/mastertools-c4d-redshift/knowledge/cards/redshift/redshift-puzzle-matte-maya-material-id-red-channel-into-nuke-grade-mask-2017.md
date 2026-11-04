---
id: redshift-puzzle-matte-maya-material-id-red-channel-into-nuke-grade-mask-2017
title: Redshift Puzzle Matte in Maya (2017): use red channel with material ID 1, batch render, then use the matte as a Nuke grade mask set to rgba.red
domain: redshift
tags: [puzzle matte, material id, maya, nuke, grade mask, small robot studio, 2017, deep-read]
applies_to: Maya + Redshift 2017, Nuke
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=s-Cs6cg9JIc, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Host is Maya, not C4D. In the AOV tab add a Puzzle Matte, show its attributes and set Red Channel material ID to 1 [00:00-00:32]. In Hypershade each material's Redshift attributes get a matching ID [00:22-01:04]. Batch render, not IPR, so the beauty and matte files land in the project images folder [01:04].
In Nuke, grade the beauty, then plug the matte into the Grade mask input and set the mask channel to RGBA red; only the robot is affected. Hue shift and saturation work the same way [01:36-02:38]. Use: fine-tune one character against the background when the lights did not give the contrast wanted [02:38].
The transcript repeats its last minute twice (captions glitch); nothing new in the repeat.

**Use it:** supports `redshift-puzzle-matte-needs-object-id-tag-override-and-three-masks-per-matte` (C4D); the Nuke mask step is the same in any host.
