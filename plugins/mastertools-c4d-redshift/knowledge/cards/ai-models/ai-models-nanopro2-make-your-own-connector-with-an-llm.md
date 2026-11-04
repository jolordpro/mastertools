---
id: ai-models-nanopro2-make-your-own-connector-with-an-llm
title: Adding a model to NanoPro 2: give an LLM the API schema, the plugin file and two example connectors; for ComfyUI, save the workflow as API JSON and keep the JSON beside it
domain: ai-models
tags: [[nanopro 2, connector, api schema, comfyui, api json, llm written code, aggregator, kling, dani zaitcev], deep-read]
applies_to: NanoPro 2 plugin for Cinema 4D
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=R285PFittEA, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Dani Zaitcev's recipe [07:50-08:52]: on the aggregator's model page use the API schema (not pasted code samples), feed it with the plugin's Python file and a couple of similar connectors (for example SeeDance and Veo) to any LLM, ask for a connector, wait about a minute, put it in that provider's folder under the plugin's models folder (create the folder if needed) and restart the plugin.
For ComfyUI [14:31-15:03]: save the workflow as an API JSON, place it in the plugin's ComfyUI folder, give the JSON and the plugin file to an LLM for a connector, put the result in the same folder, and do not delete the JSON. Models differ between aggregators; one is cheaper and takes many payment methods but is less stable [07:20-07:50].
Codex CLI route: it runs locally and is confined to a chosen folder it asks about on first launch [10:26-10:56].

**Use it:** extension by schema plus example is a pattern the platform can copy for adding render services; keep the workflow file next to the generated glue code.
