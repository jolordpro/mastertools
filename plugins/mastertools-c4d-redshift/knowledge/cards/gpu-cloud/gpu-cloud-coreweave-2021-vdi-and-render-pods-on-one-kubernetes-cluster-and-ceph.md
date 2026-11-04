---
id: gpu-cloud-coreweave-2021-vdi-and-render-pods-on-one-kubernetes-cluster-and-ceph
title: CoreWeave (Feb 2021): GPU virtual desktops and Deadline render pods share one Kubernetes cluster and one Ceph file system
domain: gpu-cloud
tags: [coreweave, kubevirt, kubernetes, vdi, deadline, ceph, virtio-fs, virtual desktop, vfx studio, 2021, deep-read]
applies_to: KubeVirt, Kubernetes, Deadline, Teradici or Parsec, 2021
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=me25mlhgERI, src:yt-transcripts]
feeds: []
conflicts: none
---
A CoreWeave engineer (KubeVirt community talk, Feb 2021) describes moving a VFX studio fully off its on-prem plus AWS setup in about six months (proof of concept two months, customer migrated in December) [10:00-10:31]. Artists sit in GPU virtual desktops (at least one pro Nvidia GPU each, Teradici or Parsec for the stream) [05:52]. Root disks are Ceph block volumes; the project files are a shared Ceph file system mounted into the VM through virtio-fs, quoted at tens of thousands of IOPS [06:25-06:55]. Jobs go to Deadline running in containers on bare-metal nodes, which read the same file system, so nothing is copied between artist and farm [07:27].
Why not AWS: the speaker says a full pipeline there is cost-prohibitive and S3 plus egress fees hurt; the common half-way design (desktops in the cloud, NFS back to on-prem storage) is called not performance optimal [03:45-05:52]. Typical VFX project size given: 2 to 200 TB, studios hold 300 to 500 TB on site [03:15]. About 70 people were on the desktops, each with one to four GPUs [12:04].
A single Kubernetes API drives desktops and render software; billing came from Prometheus metrics [08:28-11:34]. Vendor's own account, a 2021 snapshot.

**Use it:** when sizing a studio cloud move, check the same three things the speaker did: desktop and farm see one file system, no copy step, one control plane. Transfers to a small C4D + Redshift shop only as a design reference, not a build recipe.
