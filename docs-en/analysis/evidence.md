# The evidence disk

During the examination, the investigator comes across items of interest: a file, a sample, a log. They
need to collect them without contaminating the rest. For that, each machine has an **evidence disk**,
created automatically.

```{video} 19-evidencias
```

## Inside the machine

Inside the guest system, the evidence disk appears as a drive of its own, called **possible evidence**.
This is the drive the investigator copies what they find to: the examination note, a collected artefact,
a sample set aside for analysis. The original disk is not touched.

```{figure} /_static/img/19-evidencias/03a.jpg
:alt: Windows Explorer with the evidence folder on the possible evidence drive

The evidence folder on the *possible evidence* drive.
```

## A separate disk

In the platform's disk management, the evidence disk is marked as such. Its rules:

- it is created automatically with each machine;
- it is writable;
- it **cannot be removed**, so that nothing stored on it is lost;
- it is stored **encrypted** at rest.

```{figure} /_static/img/19-evidencias/03b.jpg
:alt: Attached disks panel with the evidence disk identified

The evidence disk in disk management.
```

## Downloading the evidence

In the console's **acquisition** panel, **Download Evidence Image** delivers the contents of the disk.
ForensicVM decrypts it, mounts it and delivers the files in a **ZIP** ready to open.

```{figure} /_static/img/19-evidencias/04a.jpg
:alt: Acquisition panel with the Download Evidence Image option

Downloading the evidence from the acquisition panel.
```

The ZIP contains exactly the items gathered on the drive, decrypted and ready to examine with the usual
tools. For example:

- `Evidence/investigator-note.txt`: the note from the examination itself;
- `Evidence/collected-hosts.txt`: an artefact collected from the machine;
- `Evidence/suspicious-sample.txt`: a sample set aside for analysis.

```{tip}
After downloading the ZIP, compute and record its *hash* before handing it over or analysing it, as you
would with any other item of evidence.
```
