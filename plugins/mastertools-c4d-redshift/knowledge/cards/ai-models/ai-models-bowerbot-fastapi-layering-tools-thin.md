---
id: ai-models-bowerbot-fastapi-layering-tools-thin
title: BowerBot layers like FastAPI: tools are thin adapters, services do the work, and external libraries (including pxr) live only in utils
domain: ai-models
tags: [bowerbot, architecture, thin tools, services, utils, library isolation, usd]
applies_to: BowerBot 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=opfHGm0lWyM, src:yt-transcripts]
feeds: [agent door]
conflicts: none
---
Tools act like endpoints; services hold logic; only utils import libraries, so a library change is fixed in one place [03:43-04:38]. Fixed tools replace on-the-fly code because generated code costs tokens and time and markdown rules drift [04:38-05:14].

**Use it:** Same layering for the platform tool layer: tested tools, one library boundary.
