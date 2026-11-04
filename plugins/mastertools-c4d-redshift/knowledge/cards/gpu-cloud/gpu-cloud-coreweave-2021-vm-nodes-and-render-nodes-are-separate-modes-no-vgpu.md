---
id: gpu-cloud-coreweave-2021-vm-nodes-and-render-nodes-are-separate-modes-no-vgpu
title: CoreWeave (2021): a node is either a GPU-passthrough VM host or a plain render node, never both, and vGPU is skipped on purpose
domain: gpu-cloud
tags: [coreweave, kubevirt, pci passthrough, vgpu, huge pages, vfio, node mode, autoscaler, deep-read]
applies_to: KubeVirt, Nvidia pro GPUs, 2021
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=me25mlhgERI, src:yt-transcripts]
feeds: []
conflicts: none
---
In the Q&A the speaker explains how nodes switch role [21:01-22:33]: clusters run about 1,000 nodes; for VMs a node is rebooted with a flag so memory becomes 1 GB huge pages and every GPU attaches to VFIO for passthrough; otherwise it boots as a normal bare-metal Kubernetes node. They looked at slicing a node both ways and judged it not worth it. A cluster autoscaler flips nodes by demand. Scale then: about 150 VMs on roughly 50 physical nodes, 4 to 8 GPUs per node [21:31-22:02].
Why no vGPU [26:45-27:46]: users want the whole GPU, stability, and every card from RTX 4000 to V100, A100 and A6000 is just passed through; huge pages are hard to allocate and free at runtime, so dedicated nodes are simpler.
Quirks [18:23-19:25]: a VM with a lot of RAM needs its resource request raised above what KubeVirt sets; UEFI firmware in QEMU lets more than one GPU into one VM, some BIOS-mode guests are used when many GPUs are wanted. They forked Nvidia's device plugin to avoid a static PCI-ID map and to keep the same GPU resource labels for VMs and containers (useful for billing) [15:41-16:14].

**Use it:** a good reason to expect fixed pools (VM hosts vs render nodes) from GPU clouds rather than flexible slices; ask a provider which pool a desktop or farm job lands in before planning a burst.
