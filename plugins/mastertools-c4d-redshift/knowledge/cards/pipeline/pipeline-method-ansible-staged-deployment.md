---
id: pipeline-method-ansible-staged-deployment
title: Deploy pipeline services with idempotent Ansible roles through unit tests, staging, integration and load tests, and only environment variables differing
domain: pipeline
tags: [andre prado, method studios, ansible, jenkins, staging, deployment, idempotent, rez package, deep-read]
applies_to: Ansible
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=HuV0_AbDgYk, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Prado [26:53-28:28]: configuration is Ansible playbooks, idempotent so you can rerun and reach the same state. Each service passes unit tests on a VM (Jenkins CI), is redeployed to staging with integration and load tests, then to production [26:53].
The same artifact (a Rez package) goes to every environment; only environment variables differ [27:24]. Common roles handle metrics, log shipping, service discovery; each service adds one custom role (e.g. the farm service) [27:56].

**Use it:** Release checklist for any internal tool: unit, staging, load, then prod.
