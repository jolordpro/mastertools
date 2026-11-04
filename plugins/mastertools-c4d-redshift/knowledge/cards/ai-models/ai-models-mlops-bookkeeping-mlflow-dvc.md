---
id: ai-models-mlops-bookkeeping-mlflow-dvc
title: MLflow and DVC are the usual open tools for tracking runs and versioning datasets (frozen test set as a versioned object)
domain: ai-models
tags: [mlflow, dvc, mlops, frozen test set, dataset versioning, duckdb]
applies_to: 2026
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://aimultiple.com/mlops-tools, src:research-verticals]
feeds: [frozen test set]
conflicts: none
---
Weak roundup sources. The research suggests pytest plus a score table in DuckDB as the evaluation harness, since no render-specific harness was found. Licences (Apache) are unverified.

**Use it:** tie every model run to the data it saw and to consent tags.
