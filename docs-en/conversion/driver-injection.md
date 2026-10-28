# Driver injection

This page explains why a seized Windows system does not boot as it is in a virtual machine, and how
ForensicVM injects the required drivers without touching the original image.

```{video} 04-injecao-de-drivers
```

## The problem

A seized disk carries Windows configured for the original hardware. In a virtual machine, the disk
controller is a different one, and Windows does not know it:

- Windows only boots if it knows the controller of the boot disk;
- without that driver, it stops with the `INACCESSIBLE_BOOT_DEVICE` error (blue screen) or falls into
  the recovery environment (WinRE);
- the classic solution is to prepare each machine by hand, installing the drivers. It takes hours and it
  touches the evidence.

ForensicVM does this automatically, during the conversion.

## Where the changes go

The changes never go into the original image:

1. First, the {term}`golden snapshot` is created, with the exact state of the evidence.
2. The drivers go into a layer on top, saved as the {term}`silver snapshot`.
3. The investigator's work goes into a third layer.

```{figure} /_static/img/04-injecao-de-drivers/03a.jpg
:alt: Diagram of the four layers of the virtual machine

The layers: original image, golden snapshot, silver snapshot and working layer.
```

## The conversion log

Each step can be followed in the conversion log:

1. **Golden snapshot:** created before any change.
2. **Inspection:** the tool opens the image and identifies the operating system. Windows 11 shows up as
   *Windows 10 Pro*, because it still identifies itself that way in the Windows registry.
3. **Conversion to KVM:** if the image already carries the VirtIO drivers, the tool confirms them instead
   of reinstalling them. It also detects whether the machine needs UEFI or BIOS firmware.
4. **Boot driver:** the `viostor` disk driver is registered as boot-critical (*CriticalDeviceDatabase*).
   Without this step, Windows would not find the disk on the first boot.

```{figure} /_static/img/04-injecao-de-drivers/04a.jpg
:alt: Conversion log with the creation of the golden snapshot and the system inspection

The golden snapshot and the start of the operating system inspection.
```

```{figure} /_static/img/04-injecao-de-drivers/04b.jpg
:alt: Conversion log with viostor registered as a critical driver

Registering `viostor` as a boot-critical driver.
```

## What changes, and what does not

| | |
|---|---|
| **Changes** | The `SYSTEM` registry hive, to mark `viostor` as critical, and the missing drivers. Only in the silver layer. |
| **Does not change** | The E01 image and its *hash*, which keep matching those of the acquisition. |
| **If something goes wrong** | You go back to the silver or the golden snapshot, in seconds. |

```{note}
In **snapshot mode**, injection is limited to what is essential for booting and the QEMU agent is not
installed. If you need the online plug-ins, see {doc}`../virtual-machines/qemu-agent`.
```

Next step: {doc}`../virtual-machines/boot-and-console`.
