# ForensicVM NextGen

**Forensic virtualisation, from the lab to the courtroom.**

*Esta documentação também está disponível em
[português](https://forensicvmng-user-manual.readthedocs.io/pt/latest/).*

ForensicVM NextGen is a web platform that turns forensic disk images (E01/EWF, AFF, RAW, VMDK, QCOW2)
into bootable virtual machines, controlled from the browser. With it, the examiner can see the seized
system *running*: the user's desktop, the applications, the memory, the network traffic. And the
original image is never changed.

```{figure} /_static/img/32-resumo-sistema/03a.jpg
:alt: ForensicVM layered architecture — browser, server, QEMU/KVM machines and original image

The four layers of ForensicVM. The browser talks to a server that manages cases, permissions and
auditing. The virtual machines run on QEMU/KVM, on top of layers that protect the original image.
```

## The problem it solves

A seized disk is evidence. It must be preserved unchanged, and its *hash* must keep matching the one
taken at acquisition. But to understand what the user was doing, it is often very useful to get the
system running. Reconciling the two by hand is slow, risky and hard to document.

ForensicVM bridges that gap:

- **It preserves the evidence.** The image is mounted read-only. Everything that changes lives in layers
  on top, starting with the {term}`golden snapshot`.
- **It gets the system running.** It automatically injects the drivers Windows or Linux need to boot on
  virtual hardware.
- **It provides the analysis tools.** Browser console, plug-ins, memory capture and analysis with
  Volatility3, traffic capture, process introspection and sandboxed malware analysis.
- **It documents everything.** Every action is written to an immutable {term}`audit log`, tied to a case,
  a user and a time.

```{warning}
**Project status.** ForensicVM NextGen is under active development and **is not yet recommended for
production use**. All testing, including the demonstrations in this documentation, was done with public
forensic images from [CFReDS](https://cfreds.nist.gov/) (NIST), never on real cases. See
{doc}`project/status-and-collaboration`.
```

## Where to start

- **Want an overview?** Start with {doc}`introduction/overview`: the whole system in seven minutes.
- **Going to use the platform?** Follow {doc}`getting-started/first-steps` and then the order of the
  sections in the menu. It mirrors the path of an examination: from the case to the conversion, the
  virtual machine, the analysis and the report.
- **Going to install a server?** Go to {doc}`installation/index`.
- **Administering an existing server?** See {doc}`administration/index`.

Each page matches a demonstration video, recorded with real operations on public images. The video is at
the top of the page. The images and the text were adapted from those videos.

```{toctree}
:caption: Introduction
:maxdepth: 2

introduction/what-is
introduction/concepts
introduction/overview
```

```{toctree}
:caption: Getting started
:maxdepth: 2

getting-started/first-steps
getting-started/cases-and-team
```

```{toctree}
:caption: Using ForensicVM
:maxdepth: 2

conversion/index
virtual-machines/index
analysis/index
malware/index
management/index
```

```{toctree}
:caption: Installation and administration
:maxdepth: 2

installation/index
administration/index
```

```{toctree}
:caption: Project
:maxdepth: 1

project/status-and-collaboration
glossary
```
