# Other sources

Besides an image that is already on the server, ForensicVM accepts evidence from several other sources.
They all share the same wizard and the same conversion workflow.

```{video} 16-outras-origens
```

## The available sources

| Source | When to use it |
|---|---|
| **Server Path** | The image is already in a folder on the server (examples {doc}`cfreds-bart` and {doc}`hacking-case`). |
| **Windows share (SMB)** | The image is read directly from a network share. |
| **Upload from PC** | The image is sent from the investigator's computer, in chunks and resuming if the connection drops. |
| **Proxmox VE/PBS** | The machine of interest is on a Proxmox cluster, or in its backups. |
| **Proxmox VE (streaming, experimental)** | Experimental variant that imports as a stream from Proxmox VE. |
| **Veeam Backup** | Imports a Veeam Backup & Replication restore point as evidence. |
| **Remote Acquisition** | Acquires the disk of a remote machine through an agent. |
| **Offline Agent** | Downloads a standalone acquisition agent (Linux, macOS or Windows) to run on the equipment itself: normal mode, with a write blocker, or automatic incident response. The resulting image is then imported. |

```{note}
The videos demonstrate the **Server Path** and **Proxmox** (VE and Backup Server) routes, against a real
lab. The **Veeam** integration and **remote acquisition by agent** exist, but were not demonstrated for
lack of a lab with those systems.
```

## Proxmox VE: live acquisition

Many organisations already run their infrastructure virtualised on Proxmox. In an incident, the machine
you need is often there, as a virtual machine on a cluster.

1. In the conversion wizard, choose the **Proxmox VE/PBS** source and the configured server.
2. Choose **Proxmox VE (live)**. ForensicVM connects to the cluster and shows the machines running on it.
3. Choose the machine that matters to the investigation.

ForensicVM triggers a backup at hypervisor level, without installing anything inside the machine and
without touching the evidence. The image is obtained, verified by *hash* and enters the same forensic
conversion workflow.

```{figure} /_static/img/16-outras-origens/03a.jpg
:alt: Conversion wizard with the Proxmox source and the list of configured servers

Proxmox source: choosing the server.
```

```{figure} /_static/img/16-outras-origens/04a.jpg
:alt: List of virtual machines running on the Proxmox VE cluster

Proxmox VE live: the cluster's machines.
```

## Proxmox Backup Server

When backups of the machines already exist, the history itself can be evidence.

1. Choose **Proxmox Backup Server**.
2. Choose the *datastore*, the backup group and the **restore point**.

You can recover an earlier state, for example from before a compromise, **without ever contacting the
source hypervisor**, whose integrity may be in question. From there on, the path is the same: *hash*,
conversion and boot.

```{figure} /_static/img/16-outras-origens/05a.jpg
:alt: List of backup groups on Proxmox Backup Server

Proxmox Backup Server: backup groups.
```

```{figure} /_static/img/16-outras-origens/05b.jpg
:alt: List of restore points of a machine on Proxmox Backup Server

Choosing the restore point.
```

## What all sources have in common

- The image is verified by *hash* and the audit log supports the chain of custody.
- The same workflow always follows: conversion, drivers and boot.
- The case is mandatory, and the evidence is tied to the right item of equipment.
