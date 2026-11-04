---
id: gpu-cloud-conductor-2019-render-is-a-quarter-of-budget-so-predict-cost-before-the-bid
title: Mac Moore (Conductor, 2019): rendering is about a quarter of production budget, so he wants to predict a farm cost before the bid from past metadata
domain: gpu-cloud
tags: [conductor, mac moore, render cost, bid, prediction, metadata, core hours, estimator, siggraph 2019, deep-read]
applies_to: Conductor, 2019 roadmap talk
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Moore claims the rendering problem eats roughly a quarter of a production budget and a bid must lock it down because margins are razor-thin [23:57]. Conductor holds metadata, not the customer's data, from over 250 million core-hours: software stack, run time, bumped or rerun on spot, file dependency size [38:39]. His goal is a ride-share style quote: how much to render 350 Arnold-and-Yeti shots on a Friday afternoon, before bidding, with analysis such as the success odds for a spot request at a given time and region [39:10-40:14].

