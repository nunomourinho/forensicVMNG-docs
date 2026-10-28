# Plug-ins

ForensicVM comes with a catalogue of **plug-ins**: small forensic actions the investigator runs on the
machine without leaving the browser. They are repeatable (the same plug-in does the same thing in every
case) and they are all recorded in the audit log.

```{video} 07-plugins
```

## The catalogue

The **Plug-ins** tab of the machine detail lists the available plug-ins. Each one says what it does and
which parameters it accepts. They can be filtered by operating system (Windows, Linux), and there are two
kinds:

- **Online:** they run with the machine **running** and use the QEMU agent inside the guest system.
- **Offline:** they run with the machine **stopped** and act directly on the disk, always after an
  automatic snapshot.

```{figure} /_static/img/07-plugins/02a.jpg
:alt: Plug-in catalogue with operating system filters and run offline and online buttons

The plug-in catalogue.
```

## Running a command (online)

The **SYSTEM Exec** plug-in asks the machine to run a command (for example `systeminfo`) and returns the
result. The reply comes from the running Windows system, through the agent.

```{figure} /_static/img/07-plugins/03b.jpg
:alt: Output of the systeminfo command returned by the SYSTEM Exec plug-in

Output of a command run on the machine.
```

## Extracting a file (online)

The **File Pull** plug-in extracts a file from the guest system to the server: in the example, the hosts
file `C:\Windows\System32\drivers\etc\hosts`. The result is available to download and analyse. The read
is done by the agent and nothing is written to the evidence disk.

```{figure} /_static/img/07-plugins/04b.jpg
:alt: Contents of the hosts file extracted by the plug-in

A file extracted from the machine.
```

```{note}
Online plug-ins need the QEMU agent. On a machine converted in snapshot mode, install it first with the
offline *Install QEMU Guest Agent* plug-in (see {doc}`../virtual-machines/qemu-agent`).
```

## In short

- **Online, through the agent:** run commands and extract files from the running machine.
- **Offline, on the disk:** with the machine stopped, you act on the disk, after a snapshot.
- In both cases, the original image and its *hash* are not touched and everything is recorded in the
  audit log.
