---
id: ai-models-pipeline-agent-gets-execution-graphs-as-tools-not-the-whole-api-and-records-actions
title: Giving a pipeline agent only named execution graphs as tools limits what it can touch; the agent is best as a prototyping tool whose steps are recorded and replayed
domain: ai-models
tags: [ai-models, prism, mcp, agent, guardrails, claude, pipeline, execution graph, deep-read]
applies_to: Prism MCP, Claude API (2026 demo)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Richard's team made a documentation chatbot that first made things up; they fixed it by forcing a source link for every answer, so it now says when nothing is found [51:44-52:16]. With MCP the agent can list assets and tasks, create shots, find the latest USD of an asset, batch-compare renders, and run publishes in Maya [52:46-53:49]. To avoid teaching it the whole Python API, the agent is given only the execution graph runner; each graph (media to MP4 with burn-ins, publish to Kitsu) is a tool, so it cannot move or delete data outside it [54:20-55:21, 1:01:10-1:01:42]. A studio guest said he would not unleash an agent on a feature but would on a commercial [1:01:10]. A second panelist: the agent works as an action builder like Photoshop actions: run it once, record the MCP calls, then replay those with new inputs, rather than letting it improvise each time [1:05:19-1:06:52]. Model behind it is not fixed; they used the Claude API, and local agents work [1:02:13]. Test in a sandbox first [1:06:52].

**Use it:** Expose small, named graphs to any agent and record a good run as the permanent script.
