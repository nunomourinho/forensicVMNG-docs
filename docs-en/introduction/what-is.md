# What ForensicVM is

ForensicVM NextGen is a **forensic virtualisation** platform. It takes a disk image acquired with the
usual acquisition tools (for example an E01 file created with FTK Imager, EnCase or Guymager) and turns
it into a virtual machine that boots and is controlled entirely from the browser.

## Who it is for

The platform is aimed at people who work in digital forensics: forensic examiners and criminal
investigators, forensic laboratories, incident response teams (CSIRT/SOC), and lecturers and students in
the field. The investigator does not need to install anything on their workstation. A modern browser and
an account on the server are enough.

## What it lets you do

| Need | How ForensicVM answers it |
|---|---|
| See the system as the user saw it | The image is converted into a virtual machine and opened in a console in the browser. |
| Leave the evidence unchanged | The original image is mounted read-only. Changes live in separate layers, and the {term}`golden snapshot` keeps the exact state of the acquisition. |
| Boot a seized Windows system on different hardware | Automatic injection of the VirtIO drivers, in a {term}`silver snapshot` of its own. |
| Get into an account without knowing the password | A live plug-in that gives access to the session without changing the credential stored on the disk. |
| Analyse volatile memory | Memory capture of the running machine and analysis with Volatility3, or live introspection from the hypervisor. |
| Observe communications | Network isolated by default, with traffic capture to PCAP when the investigator decides. |
| Understand what a suspicious file does | Submission to the CAPE malware lab, without running it on the investigator's workstation. |
| Document the examination | Video recording and screenshots of the session, a separate disk for collected evidence, an audit log and a case report. |
| Work as a team | Cases with members and roles (viewer, investigator, manager, owner), with permissions down to disk level. |

## Supported image sources

- **Image formats:** E01/EWF (including segmented images), AFF, RAW/DD, VMDK and QCOW2.
- **Sources:** a path on the server itself, a Windows network share (SMB), upload from the investigator's
  computer (chunked upload, resumable), Proxmox VE, Proxmox Backup Server, Veeam Backup & Replication and
  remote acquisition by agent.

See {doc}`../conversion/index`.

## How it works, in broad strokes

1. The investigator creates a **case** and registers the seized **equipment**.
2. In the conversion wizard, they choose the image and the equipment it belongs to.
3. ForensicVM reads the image metadata (examiner, date, acquisition *hashes*) and mounts it read-only. It
   creates the golden snapshot, injects the drivers and prepares the virtual machine.
4. The machine boots on QEMU/KVM. The investigator works in the browser console and uses the analysis
   tools.
5. Every action is logged. At the end, the evidence, the audit log and the case report are exported.

```{note}
ForensicVM started as a master's dissertation at the Polytechnic University of Beja (UPBeja), Portugal.
In 2026 it was rebuilt from scratch for the web, keeping the conversion scripts of the original project.
See {doc}`../project/status-and-collaboration`.
```
