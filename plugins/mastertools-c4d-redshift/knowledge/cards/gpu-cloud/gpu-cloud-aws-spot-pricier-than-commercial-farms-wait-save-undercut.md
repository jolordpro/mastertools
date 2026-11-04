---
id: gpu-cloud-aws-spot-pricier-than-commercial-farms-wait-save-undercut
title: In one partner's Blender test, plain AWS spot cost more than two commercial render farms; only Wait & Save came out far below them
domain: gpu-cloud
tags: [[wait and save, spot, rebus farm, fox render farm, render farm cost comparison, deadline cloud, benchmark, johannes omen], deep-read]
applies_to: AWS Deadline Cloud
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Sz-Bmxj4POU, src:yt-transcripts, https://www.youtube.com/watch?v=cm4sPe1nLjU]
feeds: [estimator]
conflicts: none
---
Johannes Omen rendered one Blender scene (145 frames, full HD) with identical settings on Rebus Farm (German) and Fox Renderfarm (Asia-based), then on AWS [11:34-13:07]. The captions say it "was more expensive to do that on AWS" (ambiguous: the speaker may have meant the farm); read as: AWS spot was not the cheap option; what struck him was Wait & Save, which he put at about 94% cheaper than the pricier commercial option (the captions garble which farm, so read this as indicative) [13:07].
He also ran on-demand, spot and Wait & Save for the same job: spot is much cheaper than on-demand, Wait & Save cheaper again [33:24-34:27]. Spot interruptions were about 10%, after which another worker picks the task up [33:54].
One scene, one partner, vendor webinar: treat as a claim to retest.

**Use it:** the estimator should not assume that cloud spot beats a commercial farm; show Wait & Save as the lane that changes the answer.
Transcript support: 2014 talk already pitched spot switching as a one-flag change in the farm templates, with a two-minute termination warning newly announced; no prices given (https://www.youtube.com/watch?v=cm4sPe1nLjU [17:52])
