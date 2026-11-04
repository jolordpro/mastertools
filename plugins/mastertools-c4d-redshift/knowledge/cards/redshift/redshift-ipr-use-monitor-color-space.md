---
id: redshift-ipr-use-monitor-color-space
title: A saturated colour can render paler than the IPR shows until 'Use monitor color space' is switched on in the IPR gear menu
domain: redshift
tags: [ipr, monitor color space, desaturated, pale render, render view, redshift]
applies_to: Redshift in C4D (version not stated, 2026)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=sFRa_iZhpKw, src:yt-transcripts]
feeds: [CHECKS 5, redshift, coach]
conflicts: none
---
Greyscalegorilla [00:00]: a bright orange-red looked clearly more washed out in the final render than in the IPR.
Fix shown [00:24]: the IPR settings gear, then 'Use monitor color space'. A separate 'monitor color space' toggle in the render view also exists and stays on once set; the IPR one had to be rechecked in every scene file, so he suspects a bug or a bad default.
Single creator, caption heard at 246 words a minute, so the exact menu label is from the ear.

**Use it:** add both toggles to the first-aid list for check 5 (viewport vs Picture Viewer vs EXR colour compare), and have the coach ask which one is off.
