# Process manager

In a forensic analysis, it is essential to know what is running inside the machine. ForensicVM's process
manager shows it live, has two data sources and links each process to the CAPE malware lab and to
VirusTotal.

```{video} 31-gestor-processos
```

## Two modes

The manager opens from the console toolbar and sits next to the machine's screen, which stays visible.
At the top you choose the data source:

| Source | How it works | Advantages |
|---|---|---|
| **Agent (fast)** | Talks to the QEMU agent installed inside the machine. | Immediate response. Shows the CPU percentage calculated inside the machine, the priority and the memory used. Lets you manage services. |
| **Memory (agentless)** | Reads the processes directly from the machine's memory, from the server. | Needs nothing installed on the machine. It is a view that is harder to fake for malware running in there. Allows a memory dump of a process. |

Each column sorts the list (by CPU, by memory…).

```{figure} /_static/img/31-gestor-processos/02a.jpg
:alt: Process manager on the Agent (fast) source with the CPU percentage per process

The process manager on the *Agent (fast)* source.
```

## Services

Below the processes are the **services**, with their status, start mode and the process running them.
With the agent, they can be **started** and **stopped** without leaving the screen. The status shown is
read from the machine itself, and every operation is recorded in the audit log.

```{figure} /_static/img/31-gestor-processos/03a.jpg
:alt: Services filter with the Windows Error Reporting service and the start button

Starting and stopping a service.
```

## Pause and resume

**Pausing is not the same as killing.** The process is frozen, with its memory and state intact, and can
be resumed later with the same PID, because it was never killed. It is useful for examining a suspicious
process without giving it time to do more damage.

The **Kill** button, in red and set apart, always asks for confirmation. Critical system processes and
the agent itself are protected.

```{figure} /_static/img/31-gestor-processos/04a.jpg
:alt: ping process paused in the process manager

A paused process.
```

## Draggable divider

The manager and the machine's screen share the window, and the divider between them can be dragged to
give more room to one or the other. The machine's screen readjusts in real time.

```{figure} /_static/img/31-gestor-processos/05a.jpg
:alt: Widened process manager with the machine's screen reduced

The draggable divider.
```

## Sending a process to CAPE

In each process's action menu, **CAPE Sandbox** sends the process's executable to the malware lab.
ForensicVM fetches the file from the machine, or rebuilds it from memory, and submits it. It only happens
when the investigator clicks. The task number and the link to the results appear in the bottom strip. See
{doc}`../malware/cape-usage`.

```{figure} /_static/img/31-gestor-processos/07b.jpg
:alt: Bottom strip with the CAPE task number and the link to the results

Process sent to CAPE.
```

## Looking up the hash on VirusTotal

The **VirusTotal** option computes the SHA-256 of the process's executable and shows it (visible and
copyable). It then opens a new browser tab with that *hash*'s page on
[VirusTotal](https://www.virustotal.com/).

- **The file is not sent to anyone**. Only the *hash* is looked up.
- No API key is needed.
- If the file has already been analysed by someone, the results of the antivirus engines appear straight
  away.

```{figure} /_static/img/31-gestor-processos/08b.jpg
:alt: VirusTotal page for the hash of a known piece of malware, with dozens of detections

An example, with the *hash* of known malware (simulation): dozens of engines flag the sample.
```

```{note}
The current integration looks up one process at a time and does not use the VirusTotal API. Automatic
checking of many samples through the API is not implemented yet and would require suitable paid access.
```

## In short

The process manager shortens the path between seeing a strange process and understanding what it is. The
agent shows what is consuming the machine and lets you pause without destroying evidence. Memory gives a
view that does not depend on what is inside. CAPE analyses the behaviour, and VirusTotal tells you
whether the file is already known. All on the same screen, and all logged.
