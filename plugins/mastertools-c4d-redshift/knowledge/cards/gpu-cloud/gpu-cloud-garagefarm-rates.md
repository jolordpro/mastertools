---
id: gpu-cloud-garagefarm-rates
title: GarageFarm GPU rates are $0.004 / $0.006 / $0.012 per OB-hour by priority, billed per second
domain: gpu-cloud
tags: [garagefarm, farm, price, redshift, ob-hour, priority, calculator]
applies_to: prices as of 2026-10
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://garagefarm.net/pricing, https://garagefarm.net/cost-calculator, https://garagefarm.net/redshift-render-farm, src:research-render-farms]
feeds: [PLAN 5b, competitor table]
conflicts: none
---
Low / medium / high priority; CPU $0.024 / $0.036 / $0.072 per GHz-hour. Failed and queue time not charged; price includes licences. The OB-hour unit is not defined on the page.
GPUs: RTX 6000 Pro Blackwell 96 GB, L40S 48 GB, RTX A5000, RTX 4000 Ada; node caps 15 / 30 / 60 GPU nodes by tier.
The calculator is animation-only and gives best-case time. For stills, render a 1/4 or 1/5 res test and multiply (about x25 at 1/5).

**Use it:** borrow the low-res-test-then-scale trick for hero-frame estimates.
