# Boot and console

This page shows how to boot the converted machine, follow the boot log and the automatic screenshots,
and work in the system console from the browser.

```{video} 05-arranque-e-consola
```

## The machine detail

In the VM list, the machine appears with the computer name (for example `DESKTOP-1K54EA2`) and the
detected operating system. The machine detail has several tabs: Overview, Hardware, Snapshots, Media,
Network, Forensics, Plug-ins and Sandbox. The **Overview** shows the image identity, the available
actions and the boot log.

```{figure} /_static/img/05-arranque-e-consola/02a.jpg
:alt: Virtual machine detail with identity, actions and boot log

The machine detail, with the case it belongs to.
```

## Booting and following the log

When you press **Start VM**, the boot log shows live what QEMU and the firmware are doing: the isolated
network, the monitor and the loading of the system's boot manager (for example Windows Boot Manager).

```{figure} /_static/img/05-arranque-e-consola/03a.jpg
:alt: Live boot log, with the Open Console, Screenshot, Snapshot, Shutdown and Force Stop actions

Live boot log.
```

During boot, the system takes **two automatic screenshots**, at 10 and 30 seconds. They confirm at a
glance that the machine booted properly, without having to open the console.

```{tip}
If a machine does not boot, the boot log is the first place to look. The log of the previous run is also
kept, for comparison.
```

## The browser console

**Open Console** shows the machine's screen inside the browser, without installing anything. The console
uses a VNC server provided by QEMU itself. The investigator controls the machine as if sitting in front
of it, but the evidence always stays on the server.

```{figure} /_static/img/05-arranque-e-consola/05a.jpg
:alt: Browser console with the Windows 11 lock screen

The browser console, with Windows reaching the lock screen.
```

The console toolbar has the keyboard, acquisition (screenshots and recording), snapshots, hardware,
plug-ins, processes, devices (CD, floppy, USB), network and the power menu. See {doc}`console`.

## Keyboard and shortcuts

Special combinations, such as **Ctrl+Alt+Del**, are sent through the **keyboard shortcuts menu** in the
console toolbar, because the browser would not let them through directly.

```{figure} /_static/img/05-arranque-e-consola/06a.jpg
:alt: Windows sign-in screen after sending Ctrl+Alt+Del

The sign-in screen, after sending Ctrl+Alt+Del through the shortcuts menu.
```

Next step: {doc}`account-access`.
