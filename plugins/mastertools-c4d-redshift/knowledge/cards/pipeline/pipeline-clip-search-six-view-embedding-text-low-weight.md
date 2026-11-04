---
id: pipeline-clip-search-six-view-embedding-text-low-weight
title: Asset search by CLIP: embed each asset from six rendered views and weight text metadata lower than images
domain: pipeline
tags: [[clip, semantic-search, asset-library, mcp, yolo-world, ubisoft], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Rahgoshay's asset search over about 30,000 assets: natural-language query or a mood-board image cropped with YOLO-World by free-text classes, each crop searched through an MCP tool [2:09:24-2:10:28]. Every asset was embedded from six rendered viewpoints so back-side details count; costs more to index, retrieval cost unchanged [2:10:58][2:18:50].
Text embeddings were used at lower weight, because equal weight favoured productions with good metadata and poor images [2:11:28][2:18:50]. YOLO-World confidence dropped on stylised art, so a manual crop fallback was added [2:18:19]. Wrapping search as MCP tools let the agent compose calls without bespoke API code [2:19:20]. Problem it fixes: tribal knowledge (code names, which NAS) [2:03:39].

**Use it:** A reusable pattern for searching C4D asset and texture libraries by look, with a person confirming matches.
