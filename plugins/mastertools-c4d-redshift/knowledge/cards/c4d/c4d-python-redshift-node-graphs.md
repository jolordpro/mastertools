---
id: c4d-python-redshift-node-graphs
title: C4D Python reads and writes Redshift node materials, AOVs, light groups and Takes
domain: c4d
tags: [python, maxon api, graphdescription, node material, aov, light group, takes, readout]
applies_to: C4D 2024+ (GraphDescription), docs for 2027.0.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_graph_descriptions.html, https://developers.maxon.net/docs/py/2027_0_0/examples/nodes/nodes_material_create_redshift.py.html, https://developers.maxon.net/forum/post/70800]
feeds: [elevate c4d_readout.py node-graph gap, PLAN 0.2, checks 5-7]
conflicts: none
---
`maxon.GraphDescription` describes a node graph as nested dictionaries, readable and writable. Forum threads show AOVs and light groups set from Python. Scene nodes were unsupported in early versions.

**Use it:** close the readout's Redshift node-graph gap; checks 5-7 run in the plugin.
