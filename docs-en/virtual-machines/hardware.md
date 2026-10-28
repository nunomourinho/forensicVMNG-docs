# Hardware and firmware

The machine's virtual hardware is configurable: memory and CPU cores, firmware profile and the Windows
11 requirements (TPM 2.0 and Secure Boot), emulated in software.

```{video} 12-hardware
```

All these options are in the **Hardware** tab of the machine detail. Changes take effect at the
machine's **next boot**.

## Memory

Choose the amount (there are shortcuts for 2, 4 and 8 GB) and press **Apply**.

```{figure} /_static/img/12-hardware/02b.jpg
:alt: Virtual machine memory setting with 2, 4 and 8 GB shortcuts

Setting the memory.
```

## CPU cores

Choose the number of virtual cores. Windows 11 requires at least two.

## Firmware profile

The firmware profile is detected at conversion: **UEFI** for modern systems, **BIOS** for old systems
such as Windows XP. It can also be forced manually, if the detection gets it wrong.

```{figure} /_static/img/12-hardware/04a.jpg
:alt: BIOS, UEFI or automatic firmware profile, and the Windows 11 requirements

The firmware profile and the Windows 11 requirements.
```

## Windows 11 requirements: TPM 2.0 and Secure Boot

ForensicVM can emulate a **TPM 2.0** and **Secure Boot** in software, when they are needed: for example,
to boot a Windows 11 installation that requires them or to open BitLocker disks. They are off by default
and are switched on when the investigation needs them.

```{figure} /_static/img/12-hardware/05a.jpg
:alt: TPM 2.0 and Secure Boot options switched off, read cache and clock override

TPM 2.0, Secure Boot and other hardware options.
```

## Other options

The same tab also has:

- **Local Read Cache:** speeds up snapshot-mode machines whose image is on slow storage.
- **Clock Override (RTC):** boots the machine with a set date and time. Useful for reproducing the time
  context of the evidence.
- **Network Card (hotplug):** adds a network card while the machine is running.
- **Disks and Encryption:** see {doc}`disk-encryption`.

With the hardware and firmware adjusted, the machine faithfully reproduces the seized computer.
