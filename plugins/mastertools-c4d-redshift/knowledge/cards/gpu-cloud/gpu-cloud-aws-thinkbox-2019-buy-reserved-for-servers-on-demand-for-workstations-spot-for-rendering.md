---
id: gpu-cloud-aws-thinkbox-2019-buy-reserved-for-servers-on-demand-for-workstations-spot-for-rendering
title: AWS Thinkbox 2019 rule: reserved instances for licence server and database, on-demand for artist workstations, spot for rendering
domain: gpu-cloud
tags: [ec2, reserved, on demand, spot, licence server, virtual workstation, studio in the cloud, siggraph 2019, deep-read]
applies_to: AWS EC2 purchase options, 2019
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
On-demand: pay by the second, launch anything, good for spiky loads you cannot lose [09:00]. Reserved: one- to three-year commitment, for steady always-on items like licence servers and databases [09:18-09:49]. Spot: spare capacity for fault-tolerant work such as rendering [09:49]. In the studio-in-the-cloud layout the speaker puts workstations on on-demand because artists would not accept machines being taken away [50:12], with spot for render workers [50:12-50:42].

**Use it:** the platform's architecture: keep manager, database and licence server always on; never put an artist session on a preemptible node. See gpu-cloud-aws-2014-keep-manager-and-licence-server-up-and-tear-down-the-render-clients.
