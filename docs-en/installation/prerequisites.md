# Prerequisites and preparation

What you need before installing: the recommended hardware, where to install and where to get Ubuntu
Server 24.04.

```{video} 25-pre-requisitos
```

## What will be installed

ForensicVM is installed on an **Ubuntu Server 24.04 LTS** server. From there, it converts disk images
(E01, RAW, VMDK, QCOW2) into QEMU/KVM virtual machines, which the investigator controls from the browser.
That is what determines the hardware needed.

## Recommended hardware

| Component | Recommendation |
|---|---|
| **Processor** | x86-64 with hardware virtualisation (Intel VT-x or AMD-V) **enabled in the BIOS/UEFI**. |
| **Memory** | 16 GB minimum; 32 GB or more recommended. Each machine under analysis uses RAM. |
| **Disk** | Fast (SSD or NVMe), with room for several times the size of the images to be examined. In production, data disks separate from the system disk. |
| **Network** | Stable. All investigator access is through the browser. |

More cores and more memory mean more machines running at the same time, smoothly.

## Where to install

```{figure} /_static/img/25-pre-requisitos/04a.jpg
:alt: Installation options — dedicated physical server or inside a hypervisor

Physical or virtualised server.
```

- **Dedicated physical server (*bare metal*):** the preferred option. It avoids the overhead of an extra
  layer and gives direct access to hardware virtualisation, ForensicVM's engine.
- **Inside a hypervisor:** possible, but **nested virtualisation** must be enabled (without it, the
  machines do not boot accelerated) and there is some loss of performance.

## Getting Ubuntu Server 24.04

- Official page: <https://ubuntu.com/download/server>. The page offers the latest version: scroll down to
  *Previous releases* and choose **Ubuntu Server 24.04.x LTS**.
- All the files and checksums: <https://releases.ubuntu.com/24.04/>.
- File: `ubuntu-24.04.x-live-server-amd64.iso` (Server edition, 64-bit, LTS).

Check the integrity of the ISO by comparing its SHA-256 with the one published in `SHA256SUMS`:

```bash
sha256sum ubuntu-24.04.5-live-server-amd64.iso
```

On a physical server, write the ISO to a bootable USB stick (Rufus, balenaEtcher or `dd`).

Next step: {doc}`ubuntu-server`.
