# Installing CAPE

The CAPE malware analysis module is installed entirely from the ForensicVM administration console, with
no command line. To find out what CAPE is for, see {doc}`../malware/cape`.

```{video} 21-cape-instalacao
```

## The three phases

1. **CAPEv2 module:** the analysis lab, installed on the server.
2. **Windows ISO:** the system the analysis machine will run.
3. **Analysis machine:** an isolated, disposable Windows machine, with a clean snapshot it reverts to
   after each sample.

## The CAPEv2 Sandbox panel

Everything is gathered under **Administration → CAPEv2 Sandbox**: the module status, the services, the
web interface and the registered analysis machines.

```{figure} /_static/img/21-cape-instalacao/03a.jpg
:alt: CAPEv2 Sandbox administration panel with the phases and the status of the analysis machines

The CAPEv2 Sandbox panel.
```

## Downloading the Windows ISO

The Windows ISO (10 or 11) is downloaded directly from Microsoft, from the console itself. Progress is
shown live. It is a large file: in the demonstration it took about 55 minutes.

```{figure} /_static/img/21-cape-instalacao/04a.jpg
:alt: Downloading the Windows 11 ISO with the progress log

Downloading the Windows ISO.
```

## Building the analysis machine

With the ISO ready, ForensicVM builds the analysis machine by itself:

- it installs Windows unattended;
- it installs the CAPE agent;
- it saves a clean snapshot.

This is the longest phase (over an hour) and it runs in the background, with no intervention.

```{figure} /_static/img/21-cape-instalacao/05a.jpg
:alt: Building the analysis machine with the unattended installation log

Building the analysis machine.
```

## Ready

At the end, the analysis machine appears registered, with its clean snapshot. CAPE is ready to receive
samples. See {doc}`../malware/cape-usage`.

```{figure} /_static/img/21-cape-instalacao/06a.jpg
:alt: CAPEv2 Sandbox panel with the module installed, services running and machines registered

Installation completed.
```
