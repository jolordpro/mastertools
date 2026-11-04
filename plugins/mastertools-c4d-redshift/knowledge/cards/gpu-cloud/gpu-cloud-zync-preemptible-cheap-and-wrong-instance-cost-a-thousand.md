---
id: gpu-cloud-zync-preemptible-cheap-and-wrong-instance-cost-a-thousand
title: Slayden's cloud-farm habits: use preemptible nodes, test at low samples first, ask for higher instance quotas
domain: gpu-cloud
tags: [zync, google cloud, preemptible, arnold, cinema 4d, render farm, cameron slayden, cloud rendering, deep-read]
applies_to: Zync (Google), Cinema 4D + Arnold, 2020
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=1HVf5LEIa-8, src:yt-transcripts, https://www.youtube.com/watch?v=aAjOM-JqnHI, https://www.youtube.com/watch?v=heDHOWmVMbU, https://www.youtube.com/watch?v=uqVdGI5XnNI]
feeds: [estimator]
conflicts: none
---
Cameron Slayden (Microburst Studios) used Google's Zync, a render service built into Cinema 4D that rents Google machines and bundles render licences [09:24-12:36]. Preemptible instances cost much less than standard and he never lost a job to preemption in a year and a half; a dropped job restarts [14:10-15:12]. Rates he read off the screen in 2020: Arnold about $1.76 per hour preemptible, Redshift about $13 per hour with eight Tesla GPUs; a small 8 vCPU box about $1.26 (captions are garbled, treat as rough) [12:06-14:10]. His mistake: a thousand dollars spent on the wrong instance type, about 5% of that project's cost [15:12, 17:15]. Always a low-sample test render before the big run [16:45]. New accounts start with a small quota (about 50 instances), raised by asking: 100, then 200 [22:29]. Reason for chunk size: it is the frames per virtual machine [10:27]. Results: 20-minute Arnold frames, 5,000-6,000 frame jobs, a half hour on cloud where a local farm needs weeks [15:43].

**Use it:** Pattern for the estimator: test render first, cheap interruptible nodes by default, quota requests early. Zync itself has been shut down (the title says so); the habits transfer.

Also: the $1.26 machine price is the non-preemptible rate [14:10]. 100 machines for one hour cost about the same as one machine for 100 hours, so a wide farm buys speed, not savings [16:13]. Machines can be added while a job runs [18:49].
Transcript support: adds 2016 numbers: preemptible about 70% cheaper, 24-hour cap, set frames per task to one (https://www.youtube.com/watch?v=aAjOM-JqnHI [36:18-38:55])
Transcript support: Google's own 2018 terms for preemptible GPUs: 24 hour cap, CPU 80 percent off, GPU 50 percent off (https://www.youtube.com/watch?v=heDHOWmVMbU [26:28])
Transcript support: Google (2015): preemptible VMs last up to 24 h, 30 s warning, 70% off; use checkpointing for long renders. (https://www.youtube.com/watch?v=uqVdGI5XnNI [09:23-10:25])
