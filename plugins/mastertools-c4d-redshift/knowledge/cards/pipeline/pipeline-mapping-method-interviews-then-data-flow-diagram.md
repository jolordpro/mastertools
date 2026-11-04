---
id: pipeline-mapping-method-interviews-then-data-flow-diagram
title: How to map a studio pipeline: interview, workflow map of software, directed interview on data management, then a data-flow diagram on a timeline
domain: pipeline
tags: [pipeline, mapping, data flow, interview, diagram, infrastructure, methodology, bill pollson, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=AiRjt7nWcZc, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
The team's four steps: 1) semi-directed interviews to learn what the pipeline is for; people reveal priorities, one studio talked money and politics, another Python architecture [11:15] [11:47]. 2) Map the software and steps (a simplified model from a 2017 master thesis by Flavio Perez) [13:21]. 3) Directed interviews on data management: infrastructure levels, processes, versioning, assets, scene composition, file formats [14:29]. 4) Data-flow diagrams following Bill Pollson's pipeline patterns, with time left to right and grey boxes for infrastructure levels, such as the artist's machine versus the server [15:00] [15:31].
Worked example at Cube: modeling in Blender holds only geometry; exports go through an internal tool; only the main and working files are versioned, LODs are not [16:35] [17:06].
Limits they name: the method cannot show Blender overrides or the role of the production tracker [37:10]. They plan a draw.io shape library [37:42].

**Use it:** Template for mapping a platform's own pipeline: draw time as x and infrastructure (artist, server, cloud render) as lanes, mark what is versioned and what is not.
