# Project status and collaboration

This page describes the state of ForensicVM NextGen frankly: what is already mature, what is still being
stabilised and how you can contribute.

```{video} 23-estado-e-colaboracao
```

## Where the project comes from

- It started as a master's dissertation at the **Polytechnic University of Beja (UPBeja)**, Portugal.
- Its original purpose is converting forensic images into virtual machines.
- Since February 2026 it has been rebuilt from scratch for the web, with a new architecture, keeping the
  conversion scripts of the original project.

## The most advanced core

Converting a forensic image (VMDK, E01, AFF, RAW, QCOW2) into a bootable virtual machine and controlling
it from the browser, with boot, console, snapshots and an action log. It is the original purpose and the
most mature part of the system.

## Never tested on real cases

```{warning}
ForensicVM NextGen **has never been used on real cases**. All testing, including the demonstrations in
this documentation, was done with public forensic images from CFReDS (NIST). No result shown here should
be taken as validation in an operational context.
```

## What is still being stabilised

```{figure} /_static/img/23-estado-e-colaboracao/05a.jpg
:alt: Features being stabilised — live features, CAPE and acquisition integrations

The features being stabilised.
```

| Area | Status |
|---|---|
| **Live forensic features** (memory introspection, plug-ins, console, acquisition) | Delivered, in need of testing. |
| **CAPE, the malware lab** | Under active development. Not yet considered stable. It depends on the agent inside the machine, which is not installed by the fastest conversion (snapshot mode). |
| **Acquisition integrations** (Veeam, Proxmox, LXC containers) | Delivered, but still to be validated in real scenarios. |

## The project's position

- ForensicVM NextGen is **not yet recommended** for production use.
- The project is available now **for testing**, with full transparency about what works and what does
  not yet.

## How to contribute

1. **Point out what to improve:** what fails, what confuses, what is missing for real work.
2. **Suggest what to build:** new features and new plug-ins. The needs of investigators set the course.
3. **Use it for what you need:** try it on test cases, in your own context.

The ambition is a partnership between academia, which builds, documents and hardens the tool, and digital
forensics practitioners, who use it, test it and point out what really matters: pilots, joint validation
and a cycle of continuous improvement.

For comments on this documentation, use the
[documentation repository's *issues*](https://github.com/nunomourinho/forensicVMNG-docs/issues).
