---
id: pipeline-deadline-cloud-silent-failures
title: Deadline Cloud misses nested Redshift proxies, and a GitHub issue reports an out-of-memory job marked SUCCEEDED
domain: pipeline
tags: [deadline cloud, nested proxy, out of memory, silent failure, redshift proxy]
applies_to: deadline-cloud-for-cinema-4d
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://docs.aws.amazon.com/deadline-cloud/latest/userguide/maxon-cinema-4d.html, https://github.com/aws-deadline/deadline-cloud-for-cinema-4d/issues/66, src:research-render-farms, src:research-agency-pipelines]
feeds: [preflight proxy check, honest failure states]
conflicts: none
---
Docs state nested Redshift proxies (a proxy inside a proxy) are not detected by asset scanning. Issue #66 reports a Redshift out-of-memory job ending as SUCCEEDED; only the search listing was seen, so the detail is unconfirmed.

**Use it:** the platform's preflight walks proxy chains itself and never marks a bad job done.
