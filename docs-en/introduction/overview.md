# The system in seven minutes

This page summarises ForensicVM end to end, from the evidence to the analysis. Each feature then has its
own page, with more detail.

```{video} 32-resumo-sistema
```

## The problem and the solution

A seized disk must stay intact, but it is very useful to see it running. ForensicVM converts the image
into a virtual machine, controlled from the browser. The original evidence is never touched and every
action is logged.

The browser talks to a server that manages the cases, the permissions and the auditing. The machines run
on QEMU/KVM, on top of layers that protect the original image (see {doc}`concepts`).

## Secure access and organisation by case

Every account requires a second factor: an authenticator app or a security key. Without it, nobody gets
to the evidence.

Each item of evidence belongs to a case. Equipment and members are added to the case, with viewer,
investigator, manager or owner roles, and permissions that can go down to the disk. That way, each person
only sees what concerns them.

```{figure} /_static/img/32-resumo-sistema/06a.jpg
:alt: Registering an item of seized equipment in the case

Each item of evidence belongs to a case and to an item of seized equipment.
```

→ {doc}`../getting-started/first-steps`, {doc}`../getting-started/cases-and-team`

## From the image to the virtual machine

The forensic image (E01, RAW, VMDK…) is converted into a bootable machine, with automatic driver
injection. The process is automatic, the original is never written and the *hash* confirms that the
evidence has not changed.

```{figure} /_static/img/32-resumo-sistema/07b.jpg
:alt: Conversion completed, with the image identity and the conversion log

The conversion shows the identity of the image (examiner, date, *hashes*) and the log of each step.
```

→ {doc}`../conversion/index`

## Boot, console and account access

The machine boots with a real-time log and automatic screenshots, and the console opens in the browser
itself. The investigator drives the machine as if sitting in front of it, without installing any
program.

When the user's account is protected, there is a controlled procedure to get into the session without
changing the credential stored on the disk. It is logged too.

```{figure} /_static/img/32-resumo-sistema/08a.jpg
:alt: Machine detail with the live boot log

Boot with a live log.
```

→ {doc}`../virtual-machines/boot-and-console`, {doc}`../virtual-machines/account-access`

## Analysis tools

- **Plug-ins** run ready-made, repeatable analyses: system information, users, installed programs, file
  extraction.
- The **process manager** lists processes and services, suspends or resumes processes, looks up the
  *hash* on VirusTotal and sends samples to CAPE.
- **Snapshots** save the state of the machine. Experiment freely and go back in an instant.
- **Memory** is analysed with Volatility3: processes, network connections and injected code.
- **Introspection** shows processes and services from outside the machine, where malware can neither
  detect nor tamper with it.
- The **network** is isolated by default. When needed, the traffic is captured to a PCAP file.
- The **hardware** (memory, processors, BIOS/UEFI firmware, TPM) is adjusted to the seized equipment.

```{figure} /_static/img/32-resumo-sistema/13a.jpg
:alt: Snapshot panel with the protected golden snapshot

Snapshots: go back in seconds, with a protected starting point that is never lost.
```

→ {doc}`../analysis/index`, {doc}`../virtual-machines/index`

## Document and report

The session can be recorded on video and screenshots are available on demand. What is collected from the
machine goes to an **evidence disk**, separate from the original evidence. CAPE analyses suspicious
samples in an isolated lab. Disks can be encrypted at rest. Machines from Proxmox and backups from
Proxmox Backup Server can also be imported.

```{figure} /_static/img/32-resumo-sistema/20a.jpg
:alt: CAPE malware analysis report

Malware analysis with CAPE: signatures, behaviour and risk score.
```

At the end, the audit log (filterable and exportable) and the case report bring together the machines,
the analyses and the actions in a document ready to be added to the case file.

→ {doc}`../management/index`, {doc}`../malware/index`

## In short

- E01, RAW, VMDK, QCOW2, Proxmox and backup sources.
- Console, plug-ins, memory, network, malware and reports, all from the browser and in a single system.
- Every action logged, to support the chain of custody and underpin the evidence.
