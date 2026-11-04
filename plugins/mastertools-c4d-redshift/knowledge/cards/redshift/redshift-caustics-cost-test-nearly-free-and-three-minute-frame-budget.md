---
id: redshift-caustics-cost-test-nearly-free-and-three-minute-frame-budget
title: Redshift caustics test: all three lights 2:38, rim only 2:44, dome only 2:20, none about 2:40, so caustics were not the render-time cost; his budget is about 3 min a frame
domain: redshift
tags: [caustics, render time, frame budget, overnight render, denoiser, threshold, cost test, deep-read]
applies_to: Redshift, two RTX 4090, 1380x3055 coin scene (about 2025)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FYq8sdCtsoY, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
Vincent Schwenk [13:03-19:21]. Same scene: caustics from all lights 2:38; rim light only 2:44; dome only 2:20; no caustics about 2 s slower than the all-lights case, so little cost. Quality attempts: the denoised frame at threshold 0.05 was acceptable, but the undenoised one at about 2:40 was unusable; threshold 0.02 with 4,096 caustic rays took about 3 min and was still not good enough; 0.01 with about 8,000 added another minute and was his minimum; he concluded a denoised image is the practical route. Budget rule: about 3 min a frame, so 200 frames is about 10 hours, an overnight job [17:15-18:18]. A tip: shadows too black in a busy scene, so GI 2 and light multipliers 2-2.5 lifted the blacks [13:35].

**Use it:** Use the 'frames x minutes = overnight hours' check when proposing settings.
