---
id: pipeline-garagefarm-estimate-method
title: GarageFarm's calculator is animation-only and best-case; for stills, render a 1/5-resolution test on the farm and multiply by about 25
domain: pipeline
tags: [garagefarm, cost estimate, test render, calculator, scene load, queue time]
applies_to: Oct 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://garagefarm.net/cost-calculator, https://garagefarm.net/how-to-use-online-render-farms, src:research-render-farms, src:research-verticals, https://www.youtube.com/watch?v=6y4PSQOsJck]
feeds: [estimator design]
conflicts: none
---
The calculator uses local frame times and leaves out queue time and scene load. At 1/5 linear resolution a frame has 1/25 of the pixels, hence about x25. Another GarageFarm post says farm calculators also ignore load time, GI cache time and re-renders (unverified).

**Use it:** the estimator must add scene load, cache build and a re-render allowance, and give a range, not a single number.
Transcript support: director of operations advises the step value (every Nth frame) to get cost per frame (https://www.youtube.com/watch?v=6y4PSQOsJck [08:19-08:50])
