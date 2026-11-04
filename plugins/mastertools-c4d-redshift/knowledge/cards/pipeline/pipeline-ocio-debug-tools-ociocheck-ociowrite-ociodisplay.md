---
id: pipeline-ocio-debug-tools-ociocheck-ociowrite-ociodisplay
title: OCIO command-line tools for debugging: ociocheck, ociowrite, ociodisplay shader print, ociomakeclf, ocioperf
domain: pipeline
tags: [ocio, debug, command line, ociowrite, ociocheck, clf, optimization, deep-read]
applies_to: OpenColorIO v2 (2020 preview, feature complete Aug 2020)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7e0SSka8Ar8, src:yt-transcripts]
feeds: []
conflicts: none
---
Hodoul lists [24:34-26:39]: ociocheck sends a numeric RGB value through a LUT and checks syntax; ociowrite builds a processor from a source and destination colour space and serialises the operators to CLF or CTF so you can read each step; ociodisplay prints the fragment shader and picks optimization level; ociomakeclf converts supported LUT formats to CLF, wrapping with ACES2065-1 conversions; ociobake-style convert now has a GPU option; ocioperf benchmarks a conversion on a given machine.
Optimizations can be turned off through the API or an environment variable for debugging [23:28]. Writing a CLF or CTF gives a readable ASCII file of the exact transform [53:25-53:56].

**Use it:** When a colour space conversion looks wrong, write it out to CLF and read the steps; disable optimizations to rule them out.
