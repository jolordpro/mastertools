---
id: pipeline-shotgrid-read-status-list-valid-values
title: "Flow Production Tracking (ShotGrid) API: read an entity's status list with schema_field_read; the Shot default list is wtg, rdy, ip, hld, omt, cbb, fin"
domain: pipeline
tags: [polish, deep-read, shotgrid, flow production tracking, python api, status list, sg_status_list, schema]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://community.shotgridsoftware.com/t/fetching-entity-level-status-list/4623, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
Each entity type has its own status list. Call sg.schema_field_read("Shot", "sg_status_list") and read properties.valid_values in the result (use another entity name for Asset or Sequence) [§1]. The Shot example shows valid values wtg, rdy, ip, hld, omt, cbb, fin, with default wtg, and display names Waiting to Start, Ready to Start, In Progress, On Hold, Omit, CBB, Final [§1]. Forum thread dated 2020, so confirm against current docs.

**Use it:** To show a user the allowed statuses for an entity, read the schema instead of hard-coding the list.
