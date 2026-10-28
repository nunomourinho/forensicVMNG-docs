# Introspection: live processes and memory

A running machine has a lot to tell while it is alive. ForensicVM observes it **from outside**, from the
hypervisor (*virtual machine introspection*): it shows the processes and services live and lets you
extract the memory of any process, without leaving the console.

```{video} 18-introspecao
```

## In the console

In the console toolbar, the **Processes** button opens the process manager next to the machine's screen.
It is not the Windows Task Manager: it is ForensicVM observing the machine from outside, with nothing
installed inside it.

```{figure} /_static/img/18-introspecao/03b.jpg
:alt: Process manager open next to the console with the list of processes

The running processes, read from the hypervisor.
```

## Processes and services

The list shows the processes running inside the machine, with the identifier (PID) and the name of each
one, refreshable live, from the system kernel to the applications. For each process you can **pause**,
**resume** or **kill** it.

Right after them come the running system **services**, with the name of each one and the process hosting
it.

```{figure} /_static/img/18-introspecao/04b.jpg
:alt: List of processes with the pause, dump and kill actions

Actions on each process.
```

## Extracting the memory of a process

1. Choose a process and press **Dump**.
2. ForensicVM walks through that process's memory regions, live, and shows the progress.
3. At the end, the extracted memory is in a file, ready to download and analyse with the usual tools.

The extraction is done from outside the machine, by the hypervisor. The evidence is read, not changed,
and the operation is recorded in the case.

```{figure} /_static/img/18-introspecao/06a.jpg
:alt: Result of extracting a process's memory, with the regions extracted

The extraction result, ready to download.
```

```{tip}
Because it is done from outside, introspection works even if the guest system is locked or has crashed,
and it is harder to deceive for malware trying to hide inside the machine. See also
{doc}`process-manager`.
```
