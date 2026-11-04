---
id: pipeline-disney-zootopia-2-scale-and-the-open-formats-that-carried-it
title: "Disney Animation on Zootopia 2: 178 characters across 67 species, 50,000+ on screen, 9.6 million hairs on one giraffe, carried on USD, OpenEXR, OCIO, OpenVDB"
domain: pipeline
tags: [disney-animation, zootopia-2, scale, usd, openexr, aswf, whisper, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=T_iEI9ZF56k, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Numbers as stated by Bever: 178 unique characters, 67 species, 50,000+ on screen at once, 9.6 million hairs groomed on one giraffe, about 144,000 frames in the final film (stereo doubles that) [01:44-02:14, 10:16-10:49].
Snake without bones borrowed an animation vehicle-sim tool; scales got a new deformer that stays mostly rigid but flexes enough [02:14-02:48]. Glass and water overlap needed a new renderer capability so it knows which material to trust where they overlap [02:48-03:21].
Shared base: OpenEXR, OCIO, OpenVDB; USD used to compose assets, layout and animation, with new crowd-rig authoring; animation moved from Maya to Presto on this film [03:21, 08:36-09:12].
Tens of thousands of VDB files for one finale [09:42].

**Use it:** Reference scale for estimator sanity checks, and a reminder that overlapping refractive volumes need explicit material priority.
