---
id: pipeline-method-sites-stay-up-offline-and-sync-by-events
title: Each site mirrors services so it can work offline, and sites sync by queued events such as 'asset approved'
domain: pipeline
tags: [andre prado, method studios, multi site, rabbitmq federation, consul, read replica, events, high availability, deep-read]
applies_to: Studio infra
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=HuV0_AbDgYk, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Prado [23:32-26:53]: downtime is not an option, since a lost five-day frame means five more days; data cannot touch the internet, so services stay on premises and must tolerate power and disk loss. Every VM gets metrics (Zabbix), centralised logs (Logstash/Kibana) and service discovery (Consul) [24:47]. Services are mirrored per site so a studio works through network partitions [25:17].
Cross-site work uses RabbitMQ federation: when an asset is approved in Vancouver an event with metadata is emitted, each site updates a local database or notifies an artist; messages queue until the link returns [25:49]. Simple services use a master DB with read replicas; sites go read-only if cut off. CouchDB master-to-master was under trial [26:21].

**Use it:** Event naming for studio tools: asset approved, delivered, rejected.
