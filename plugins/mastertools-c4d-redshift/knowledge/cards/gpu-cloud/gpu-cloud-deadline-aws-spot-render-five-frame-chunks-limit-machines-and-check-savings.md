---
id: gpu-cloud-deadline-aws-spot-render-five-frame-chunks-limit-machines-and-check-savings
title: A TrackIt demo farm on AWS spot instances rendered a 196-frame Blender job in 5-frame tasks on 5 machines, with spot saving 61 percent against on-demand over three days
domain: gpu-cloud
tags: [deadline, aws, spot instances, chunk size, savings, trackit, deep-read]
applies_to: Deadline, AWS, Blender
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=F1ixqqFb2qQ, src:yt-transcripts, https://www.youtube.com/watch?v=kACWEs-XJcI]
feeds: [estimator]
conflicts: none
---
Vendor demo (TrackIt devops) [0:42-6:58]: submit from Blender's Render menu, cap the job at 5 machines, 5 frames per task (the last task has one frame); servers boot first so wait; estimated 14 minutes for the 196 frames; servers shut down automatically when the job finishes so billing stops [5:23]. Spot instances give up to a 90 percent discount; the catch is AWS can reclaim the server at any moment, harmless for rendering as work restarts with little loss [3:18]. The AWS console showed 39 spent in three days versus 102 on-demand, a 61 percent saving [6:30]; currency not stated in captions. Workstation stays free while the farm renders.

**Use it:** Cost estimator inputs: chunk size, machine cap, boot wait, spot discount "up to 90%" versus a measured 61%. Contradicts none, but see the existing card saying AWS spot can cost more than commercial farms.
Transcript support: spot event plugin maps Deadline groups to spot fleet requests; resource tracker heals fleets; idle shutdown timeout (https://www.youtube.com/watch?v=kACWEs-XJcI [14:34-16:07])
