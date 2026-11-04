---
id: gpu-cloud-ec2-spot-with-an-on-demand-base-behind-one-load-balancer-keeps-service-up
title: Mix a few on-demand instances with spot behind one load balancer so the service survives spot loss; a one-time spot request can only be cancelled, not stopped
domain: gpu-cloud
tags: [aws, ec2, spot, on-demand, load-balancer, availability, rahul-wagh, deep-read]
applies_to: AWS EC2, video uploaded 2024-07
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=b6oPVrDvV8E, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Demo: 4 spot + 2 on-demand instances in one target group; refreshing the load balancer URL alternated between spot and on-demand hosts [29:01-35:19].
Cancelling the spot request shut all four spot machines down and traffic kept flowing from the on-demand pair [37:22-37:55].
A spot instance from a one-time request cannot be stopped from the console; only a persistent request allows stop. You cancel the request instead [36:21-37:22].
The on-demand base capacity and replace-interrupted options in the spot request do the same job without hand-building [13:56].
He describes spot as a bidding game with a couple of minutes' warning; that is his framing and may be out of date.

**Use it:** for a render farm, keep the head node, licence server and database on on-demand and put only workers on spot.
