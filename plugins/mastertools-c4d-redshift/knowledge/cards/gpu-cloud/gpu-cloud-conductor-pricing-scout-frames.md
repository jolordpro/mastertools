---
id: gpu-cloud-conductor-pricing-scout-frames
title: Conductor bills per core-hour prorated to the minute, storage $0.18/GB-month, and renders scout frames first
domain: gpu-cloud
tags: [conductor, farm, price, scout frames, validation, storage, cinema 4d, scene validation, core-hour, studio farm]
applies_to: prices as of 2026-10
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.conductortech.com/pricing, https://conductortech.com/maxon, src:research-render-farms]
feeds: [PLAN 5b, competitor table]
conflicts: none
---
Licences are included for named vendors; the pricing page does not name Maxon. The C4D submitter validates the scene first (for example warns when a Redshift job has no GPU machine) and renders a few scout frames by default.
Studio-grade rather than designer-friendly.
Merged from `pipeline-conductor-profile`: The C4D submitter warns, for example, when a Redshift job has no GPU machine. Licences for named vendors are included in the rate (the page does not name Maxon). It is aimed at studios, not at designers.

**Use it:** scout frames are the nearest existing pattern to a draft before the full run.
