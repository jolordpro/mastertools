---
id: comp-kelly-peak-brightness-alone-does-not-fix-middle-grey
title: Kelly: a brighter display with the same gamma simply exposes the image up; middle grey placement has to be chosen in the pipeline
domain: comp
tags: [cullen kelly, hdr, peak luminance, middle grey, gamma 2.4, exposure, display, 200 nits, 100 nits, polish, cullen-kelly, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=upUAulx7sGI, src:yt-transcripts, src:polish-roster]
feeds: [redshift, CHECKS]
conflicts: none
---
Kelly [15:55-18:00]: a 200-nit and a 100-nit display with the same gamma 2.4 curve differ by exactly one stop of exposure. So the assumption that middle grey stays put when peak luminance changes (for example mastering 1000 vs 700 nits) is something the pipeline must impose, by targeting peak luminance, gamma and where middle grey sits in that display's range. He says he learned this the hard way on a project.
On camera dynamic range [2:55-5:24] he relays an ARRI colour scientist's point: more stops means a gentler roll-off, so he still wants highlights "creamy, not pingy".

**Use it:** when moving a look between SDR and HDR targets, set the middle grey level explicitly in each output transform and test it.
