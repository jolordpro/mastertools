---
id: gpu-cloud-aws-2014-scale-nodes-to-frames-so-a-two-thousand-frame-job-returns-in-one-frame-time
title: AWS 2014: scale to one node per frame so an overnight 2000-frame job returns in about one frame's render time, which means faster notes
domain: gpu-cloud
tags: [aws, 2014, scaling, frame per node, iteration speed, director notes, spot instances, gerald, deep-read, gpu-cloud]
applies_to: AWS EC2 c3.8xlarge (2014), Arnold, Maya 2015, Deadline
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=cm4sPe1nLjU, src:yt-transcripts, https://www.youtube.com/watch?v=aAjOM-JqnHI]
feeds: [estimator, coach]
conflicts: none
---
The pretend job was 300-plus shots at 2000 frames each, which three people on ten nodes put at about two years [02:11-02:43]. The pitch: a 2000-frame overnight job on 50 machines can instead run on 2000 nodes and finish in the time of one frame, "five or ten minutes", so the artist gets repetition and reaches the director's notes sooner [13:40-14:10].
Demo: 36 frames on 36 c3.8xlarge nodes, one frame each; each frame took about 3 min 40 s, which Autodesk said matched their high-end render blades [30:39-31:11, 36:31]. A 2000-frame shot would just mean more nodes [35:26].
Cost levers named: spot instances (a flag in the Python templates switches spot, reserved or on-demand) and a spot two-minute termination warning that was just announced [14:10-14:41, 17:52-18:54]. No prices were given.
Limit stated by the speaker: you can only scale to the licences you have bought; big houses have effectively unlimited render licences, small ones do not [15:41-16:12].

**Use it:** the estimator's node-count math should show both views: total node-hours (cost) and wall-clock (iteration time). See gpu-cloud-render-farm-time-math-1500-frames-100-nodes.
Transcript support: Zync (2016) example: 200 frames on 200 machines, job time is the slowest single frame; Conductor in https://www.youtube.com/watch?v=Fl_FdVgp2E0 [29:44] runs one node per frame (https://www.youtube.com/watch?v=aAjOM-JqnHI [05:18-06:19])
