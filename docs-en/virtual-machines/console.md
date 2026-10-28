# The console, your command post

The noVNC console is not just the machine's screen. It is ForensicVM's main working interface: its
bottom toolbar has everything you need, without leaving the session.

```{video} 17-consola
```

## The console toolbar

The bottom toolbar holds, from left to right: **acquisition**, **snapshots**, **keyboard**,
**hardware**, **disks**, **plug-ins**, **processes**, **CD**, **floppy**, **USB**, **network** and
**power**.

```{figure} /_static/img/17-consola/02a.jpg
:alt: Console with Windows 11 running and the bottom toolbar

The console, with the toolbar at the bottom.
```

## CD-ROM: inserting an ISO

You can mount an ISO image in the virtual CD drive (for example the VirtIO drivers or an analysis tool)
directly from the **Media** library, without stopping the machine.

## USB: attaching a stick

In the same way, you attach a USB stick image to the machine. This is useful for bringing in tools, or
for mounting the image of a seized USB stick in a controlled environment.

```{figure} /_static/img/17-consola/03b.jpg
:alt: Virtual USB image panel with a stick image selected

Attaching a USB stick image to the machine.
```

## Hardware and disks

The machine's hardware (memory, clock, network card) and the disks that make it up can also be viewed in
the console, without changing screens.

```{figure} /_static/img/17-consola/04b.jpg
:alt: Hardware panel in the console with memory, clock and network card

The hardware panel, open in the console.
```

## Screenshots and video

To document the examination, the **acquisition** button takes screenshots and records video of the
session. The recording keeps running with a red indicator. At the end, the video and the screenshots are
stored on the server, ready to be added to the case file. See {doc}`../analysis/recording`.

```{figure} /_static/img/17-consola/06b.jpg
:alt: Acquisition panel with screenshots, recording in progress and evidence

The acquisition panel, with a recording in progress.
```
