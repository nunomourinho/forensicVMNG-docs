# Key concepts

This page explains the ideas ForensicVM is built on. It is worth reading before the others, especially
if forensic virtualisation is new to you.

## Forensic virtualisation

In traditional forensics, the disk image is examined "cold": it is mounted read-only and the files, the
Windows registry and the artefacts are analysed with dedicated tools. It is the reference method and it
remains so.

Forensic virtualisation **complements** that examination. It gets the seized system running, to observe
what can only be seen while it is alive: the desktop as the user saw it, the open applications, the
sessions in cloud services, the behaviour of a suspicious program, the processes in memory, the network
connections. The challenge is to do it **without changing the evidence** and while documenting
everything that is done.

## Layers: the original image is never written

ForensicVM never writes to the acquired image. The virtual machine is built in layers, each on top of the
previous one:

```{figure} /_static/img/04-injecao-de-drivers/03a.jpg
:alt: Layer diagram — working layer, silver snapshot, golden snapshot and original image

Where the changes go: the original image at the bottom and the working layers on top.
```

| Layer | Contents | Protection |
|---|---|---|
| **Original image** (E01, RAW…) | The evidence, exactly as acquired. | Mounted read-only; never written. |
| **{term}`Golden snapshot`** | The exact state of the image, before any change. | Protected; cannot be deleted. |
| **{term}`Silver snapshot`** | The state after driver injection, before the first boot. | Protected. |
| **Working layer** | Everything that happens while the machine runs. | Can be encrypted; you can go back at any time. |

If something goes wrong, you are back at the silver or golden snapshot in seconds. The *hash* of the
original image always keeps matching the one taken at acquisition.

## Snapshot mode and copy mode

At conversion time you choose one of two modes:

- **Snapshot mode.** The machine uses the original image directly, as a read-only base. It boots quickly
  and takes up almost no disk space, but it depends on the source image remaining available. Driver
  injection is limited to what is essential for booting, and the QEMU agent is not installed. See
  {doc}`../virtual-machines/qemu-agent`.
- **Copy mode.** The disk is copied to a file of its own. It takes longer and uses more space, but the
  machine becomes independent of the source and the conversion also installs the QEMU agent.

## "Online" and "offline" analysis

Many ForensicVM tools come in two variants:

- **Online (live):** they act on the running machine. Some use the **QEMU agent** installed inside the
  guest system: run a command, extract a file, manage services. Others read the memory **from outside**,
  from the hypervisor, without depending on anything installed in the machine.
- **Offline:** they act on the disk with the machine stopped, always after a snapshot.

Reading from outside, through the hypervisor (*virtual machine introspection*), has an important forensic
advantage: it leaves no trace inside the examined system and is harder to deceive for malware running in
there.

## Cases, equipment and roles

Everything in ForensicVM belongs to a **case**. A case brings together:

- the seized **equipment** (computers, laptops…), with make, model and serial number;
- the **virtual machines** created from the images of that equipment;
- the team **members** who can access them, each with a role.

| Role | Can |
|---|---|
| Viewer | View. |
| Investigator | View and operate the virtual machines. |
| Manager | All of the above, plus manage members and equipment. |
| Owner | All of the above, plus close and archive the case. |

A closed or archived case becomes read-only for everyone except the owner. Permissions can also be
fine-tuned per item of equipment or per disk.

## Audit log and chain of custody

Every action (converting, booting, running a plug-in, capturing memory, creating a snapshot…) is logged
with the user, the time and the machine. The log is **immutable**: the database prevents entries from
being changed or deleted.

```{important}
The {term}`audit log` **is not the chain of custody itself**. It is a record of actions that **supports
and documents** it. The chain of custody remains the responsibility of the examiner and the
organisation, according to their procedures.
```

## Access security

- **Mandatory second factor** for every account: an authenticator app (TOTP) or a FIDO2 security key
  (YubiKey, Windows Hello, Touch ID).
- Optional **encryption at rest** of the virtual machine disks (LUKS).
- **Network isolated by default:** virtual machines have no network until the investigator decides to
  connect it.
