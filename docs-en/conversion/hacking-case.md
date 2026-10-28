# Hacking Case (NIST): a Windows XP system

This page goes through the whole process with the second CFReDS image, NIST's *Hacking Case*: Greg
Schardt's Dell Latitude laptop, running Windows XP. It shows that the same workflow serves modern and old
systems alike.

```{video} 13-hacking-case
```

## Getting the image

On the CFReDS portal you will find the *Hacking Case* and the image files, available in several formats.
Choose the E01 format and download the segments to the server's acquisitions folder.

```{figure} /_static/img/13-hacking-case/02b.jpg
:alt: Hacking Case page on CFReDS with the links to the segments

The image segments on the CFReDS portal.
```

```{figure} /_static/img/13-hacking-case/03a.jpg
:alt: Downloading the image segments in the browser

Downloading the segments (sped up in the video).
```

## Converting

In the wizard, choose the case, the equipment (Greg Schardt's laptop), the image and snapshot mode, and
start the conversion. The server folder browser shows the available files.

```{figure} /_static/img/13-hacking-case/04a.jpg
:alt: Conversion wizard with the case and the Hacking Case laptop selected

The wizard, with the Hacking Case equipment.
```

```{figure} /_static/img/13-hacking-case/04b.jpg
:alt: Server folder browser with the E01 image selected

Choosing the image in the server folder browser.
```

The tool recognises Windows XP, registers the disk driver as critical and detects that this machine,
being old, needs to boot with **BIOS** rather than UEFI. It is the same conversion as for Windows 11,
adapted to a 2004 system.

```{figure} /_static/img/13-hacking-case/05a.jpg
:alt: Windows XP conversion log

The Windows XP conversion log.
```

## Booting

The boot log shows the BIOS boot, and the automatic screenshots confirm that Windows XP is loading. The
classic Windows XP desktop appears in the console, ready to be examined.

```{figure} /_static/img/13-hacking-case/06a.jpg
:alt: Machine detail with the BIOS boot log

BIOS boot, with the live log.
```

```{figure} /_static/img/13-hacking-case/07a.jpg
:alt: Windows XP desktop in the browser console

The Windows XP desktop, in the browser console.
```

## In short

From Windows 11 to Windows XP, the workflow is the same: download, verification, conversion and boot.
The firmware (BIOS or UEFI) is detected automatically and can be adjusted later (see
{doc}`../virtual-machines/hardware`).
