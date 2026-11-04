---
id: gpu-cloud-opencue-2019-sony-imageworks-core-counts-from-2500-in-2009-to-100000
title: Sony Imageworks' farm software (the base of OpenCue): about 2,500 cores in 2009, 6,500 on AWS in 2017, 16,000 on Google plus 6,000 on AWS for Hotel Transylvania 3, 100,000 peak on The Emoji Movie
domain: gpu-cloud
tags: [sony imageworks, opencue, q3, aws, google cloud, core counts, emoji movie, hotel transylvania 3, siggraph 2019, deep-read]
applies_to: Sony Imageworks q3 queue, 2009 to 2019
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Ben Dean (Sony Imageworks; name as captioned) recounts: the third queue version first ran on Cloudy with a Chance of Meatballs (delivered July 2009, peak about 2,500 cores) and G-Force switched in the last three weeks, peaking about 2,200 [02:13-02:45]. First cloud use was Smurfs: The Lost Village in 2017, entirely AWS, peak about 6,500 cores; Google capacity was added a year later, and Hotel Transylvania 3 peaked around 16,000 Google cores plus 6,000 on AWS [03:17-03:50]. The local farm was about 55,000 cores, but the peak total was about 100,000 in May 2017 on The Emoji Movie, including about 40,000 Amazon cores [03:50-04:23]. Hosts: mostly Dell PowerEdge nodes with 16 physical cores, 32 threads, all reading production data from NFS mounts [13:39-14:12].

**Use it:** scale reference for a very large hybrid farm; the point for a small platform is that the queue software did not change between on-prem and cloud, only the network link.
