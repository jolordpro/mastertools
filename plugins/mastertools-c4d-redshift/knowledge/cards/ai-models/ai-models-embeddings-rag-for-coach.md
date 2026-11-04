---
id: ai-models-embeddings-rag-for-coach
title: Open embedding picks for the coach: Qwen3-Embedding-8B (Apache), BGE-M3 as the lighter option, with a cross-encoder rerank
domain: ai-models
tags: [embeddings, rag, qwen3-embedding, bge-m3, reranker, coach, retrieval]
applies_to: 2026
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://blog.premai.io/best-embedding-models-for-rag-2026-ranked-by-mteb-score-cost-and-self-hosting, src:research-verticals]
feeds: [PLAN 1.2 coach]
conflicts: none
---
Pattern: retrieve 50-100 chunks, rerank, pass the top few. Chunk per setting tagged with source, version and date; the redshift ledger ranks first; evaluate on a fixed 50-question set. Vendor blogs are the evidence.

**Use it:** keep the ledger as the top-ranked source and always stamp the version.
