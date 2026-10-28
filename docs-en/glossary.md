# Glossary

```{glossary}
Audit log
  Immutable record of every action taken in ForensicVM (who, when, on which machine). It supports and
  documents the chain of custody, but does not replace it.

CAPE
  Automated malware analysis lab (*sandbox*) integrated into ForensicVM. It runs a sample in an isolated,
  disposable machine and produces a behaviour report.

CFReDS
  *Computer Forensic Reference Data Sets*: a repository of reference forensic images maintained by NIST
  (USA). Source of the images used in the demonstrations.

Copy mode
  Conversion mode in which the disk is copied to a file of its own. The machine becomes independent of
  the source image and the QEMU agent is installed.

E01 / EWF
  Forensic image format (*Expert Witness Format*), used by tools such as EnCase and FTK Imager. It stores
  the acquisition metadata and the *hashes* inside the image itself and can be split into segments.

Golden snapshot
  The snapshot created automatically at conversion, before any change: the exact state of the evidence.
  It is protected and cannot be deleted.

Hash
  Value calculated (MD5, SHA-1, SHA-256) that uniquely identifies the content of a file or an image. If
  the content changes, the *hash* changes. It is used to prove integrity.

Introspection
  *Virtual machine introspection*: observing the inside of a virtual machine (processes, memory) from the
  hypervisor, without any software installed in the guest system.

LUKS
  *Linux Unified Key Setup*: disk encryption format used by ForensicVM to encrypt virtual machine disks at
  rest.

PCAP
  File format for network traffic captures, read by tools such as Wireshark.

Plug-in
  Predefined forensic action the investigator runs on the machine: online (machine running, through the
  agent) or offline (machine stopped, on the disk).

QEMU agent
  The *QEMU Guest Agent*: a service that runs inside the guest system and lets ForensicVM run commands,
  read files and manage services in the running machine. Used by the online plug-ins.

QEMU/KVM
  The hypervisor ForensicVM's virtual machines run on. KVM is the hardware acceleration of the Linux
  kernel.

Silver snapshot
  The snapshot created after driver injection and before the first boot. It is protected.

Snapshot
  Saved state of a virtual machine at a given moment (disk and, with the machine running, memory).

Snapshot mode
  Conversion mode in which the machine uses the original image as a read-only base. It is fast and takes
  up little space, but depends on the source image.

VirtIO
  Family of virtual device drivers (disk, network, serial) for QEMU/KVM machines. Windows needs them to
  boot in a virtual machine.

Volatility3
  Open-source reference tool for memory forensics.
```
