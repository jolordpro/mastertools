---
id: gpu-cloud-coreweave-2021-golden-image-clone-gets-a-gpu-desktop-up-in-30-seconds
title: CoreWeave (2021): clone a base OS image per user so a GPU desktop launches in about 30 seconds
domain: gpu-cloud
tags: [coreweave, kubevirt, cdi, volume cloning, golden image, vdi, boot time, ceph csi, deep-read]
applies_to: KubeVirt CDI, Ceph, 2021
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=me25mlhgERI, src:yt-transcripts]
feeds: []
conflicts: none
---
The target was a desktop launching within 30 seconds, so copying a root disk was out [15:11]. They keep one namespace holding base images (CentOS, Ubuntu and so on) and clone from it into each user's namespace using the storage driver's clone call; stock CDI could not clone across namespaces, so they wrote that feature and filed a pull request, running their own fork meanwhile [15:41, 17:17]. Block-mode Ceph volumes make the clone near zero-copy [26:14].
Measured start: pod running in 10 to 20 seconds after the VM object, about 30 more seconds for the OS to boot, so a desktop in roughly 30 seconds when launcher images are cached [24:07]. Comparison made in the Q&A: minutes on AWS.
A small helm-based form (Kubeapps UI) let users pick region, OS image, GPU and CPU, later replaced by a single custom 'virtual server' resource that also attaches the shared file system and creates the user via cloud-init [12:34-14:08].

**Use it:** when comparing remote workstations, ask for the cold start and the warm start separately; a golden-image clone is why one vendor can promise 30 seconds.
