---
id: gpu-cloud-cinesite-2020-spot-vs-on-demand-vs-reserved-and-hopping-regions
title: Cinesite's Extinct (2020): spot saved about 90% but lost nodes overnight; fix was a larger AWS region over a virtual gateway
domain: gpu-cloud
tags: [spot instances, on-demand, reserved, aws, cinesite, extinct, region, virtual gateway, licensing cost, 2020, deep-read]
applies_to: AWS EC2 spot and on-demand, 2020
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=7DpHiT0CCSA, src:yt-transcripts]
feeds: []
conflicts: none
---
Extinct: feature animation, 1,400 shots, 2K stereo, furry creatures, heavy files [19:43]. Petty's three AWS modes [20:14-21:22]: spot (price moves with demand, about 90% off on some, but on-demand jobs take priority), on-demand (fixed price per blade-hour, yours), reserved (book a block, negotiated). They connected to the nearby Canada Central region on a 10 Gb link, picked beefy blades so fewer nodes meant lower licence cost [21:22-21:52].
Failure [22:23]: a job of about 700 spot blades overnight lost them in chunks of 50 to 75 as on-demand customers took them (Montreal demand for these blades was high). Fix: connect to the much larger US East (Virginia) region through a virtual gateway [22:56]. Peak: 61,500 render hours in one 24-hour period, a record; about 36% of the show (650,000 hours) rendered on AWS [23:26].

**Use it:** a cautionary pair for the cost estimator: spot is cheapest but plan for interruption and a bigger region fallback on deadlines.
