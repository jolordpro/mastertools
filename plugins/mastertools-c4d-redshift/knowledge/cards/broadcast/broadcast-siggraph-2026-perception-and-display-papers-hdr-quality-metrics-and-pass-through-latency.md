---
id: broadcast-siggraph-2026-perception-and-display-papers-hdr-quality-metrics-and-pass-through-latency
title: SIGGRAPH 2026 perception papers: HDR needs a common display-encoded space for quality metrics, plus HDR-display realism, foveated rendering and 2 ms pass-through
domain: broadcast
tags: [broadcast, siggraph, papers, hdr, perception, tone mapping, display, research-radar, deep-read]
applies_to: research papers (July 2026)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=u6xhzA40Af0, src:yt-transcripts]
feeds: []
conflicts: none
---
Short pitches, auto captions, unverified. HDR inputs cannot be fed to standard-dynamic-range image-quality metrics since they are in absolute luminance, so a pre-process maps HDR and SDR to a common display-encoded space, making tone-mapping quality assessment possible [2:22:20-2:22:56]. An HDR stereoscopic display produced imagery near indistinguishable from reality, testing which contrast and resolution levels perceptual realism needs [1:52:44-1:53:15]. Honorable-mention work on pass-through headsets reports typical pass-through cameras 70 mm from the eyes with about 40 ms latency, versus a built headset under 2 ms [1:52:14, 1:15:20]. Foveation: dichoptic (sharp one eye, blurred the other) cuts samples [1:51:10]; peripheral eye dominance varies with eccentricity [1:51:40]; level-of-detail by visual aberration in peripheral vision [2:18:10]. Game streaming that optimizes resolution and refresh rate jointly renders over 50% fewer pixels [39:06]. Burst-fusion HDR for mobile cameras avoids shadow noise [2:23:27].

**Use it:** When grading HDR deliverables, do not trust SDR-trained quality metrics without display-encoding both sides first.
