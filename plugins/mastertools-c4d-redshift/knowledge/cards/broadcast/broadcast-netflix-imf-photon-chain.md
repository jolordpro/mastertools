---
id: broadcast-netflix-imf-photon-chain
title: Netflix IMF deliveries run Photon, then IMF validations, then Inspection as a Service, then Automated QC; a Photon failure blocks upload
domain: broadcast
tags: [netflix, imf, photon, venera pulsar, delivery validation]
applies_to: 2017-2026
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/Netflix/photon/wiki/Home/48a26be25f9dd8ece2939927484636f9774e67e6, https://www.veneratech.com/wp-content/uploads/docs/Venera-Pulsar-Photon-News-Sept-2017.pdf, src:research-vfx-pipelines]
feeds: []
conflicts: none
---
Photon is an open IMF validator (AssetMap, PackingList, Composition Playlist, essence). Pulsar ran it in 2017.

**Use it:** an example of staged delivery gates where the first failure blocks.
