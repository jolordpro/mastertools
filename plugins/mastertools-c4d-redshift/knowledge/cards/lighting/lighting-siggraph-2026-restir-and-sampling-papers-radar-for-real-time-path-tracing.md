---
id: lighting-siggraph-2026-restir-and-sampling-papers-radar-for-real-time-path-tracing
title: SIGGRAPH 2026 pitches on real-time path tracing: ReSTIR variance fixes, one sample per four pixels with a learned sampler, unbiased real-time caustics, 50% fewer light draws
domain: lighting
tags: [lighting, siggraph, papers, restir, real-time, path tracing, research-radar, caustics, deep-read]
applies_to: research papers (July 2026), not shipping tools
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=u6xhzA40Af0, src:yt-transcripts]
feeds: []
conflicts: none
---
Claims as pitched in 10-20 second clips (auto captions, unverified): ReSTIR with control variates reducing neighbour contributions for cleaner stable colour [1:10:53]; real-time unbiased caustics by combining bidirectional path tracing with ReSTIR [1:11:27]; a one-line-style fix for ReSTIR blowing up under some settings, about 100 lines of code [1:12:04]; a method clearing disoccluded regions so noise level stays consistent when temporal reuse fails [1:12:04-1:12:35]; a sampler that takes one sample per four pixels and learns to concentrate on shadows, speculars and complex geometry [1:12:35-1:13:06]. Also: differentiable removal/merging of lights cutting light overdraw by up to 50% [39:41]; neural light transport baked into an 8D function, authors admit it is still far from a real path tracer [1:02:35-1:03:41]; neural baking of volumes to 200 fps with dynamic light [1:46:34]. Awards: a 2015 paper on ML filtering of Monte Carlo noise won a test-of-time award [1:25:01].

**Use it:** Real-time path tracing for sports graphics is improving mainly via sample reuse and learned samplers; recheck when an engine ships them.
