# Memory analysis with Volatility3

The memory of a running machine holds what the disk does not show: running processes, open network
connections and malicious code that only exists in memory (*fileless*). ForensicVM captures the machine's
memory and analyses it with [Volatility3](https://github.com/volatilityfoundation/volatility3), a
reference tool in memory forensics, without shutting the machine down.

```{video} 10-memoria
```

## Memory introspection

The **Memory Introspection** page lets you choose the analysis (the Volatility3 *plugin*) and run it. The
**Fresh dump** option forces a new memory capture. Without it, the last capture is reused.

```{figure} /_static/img/10-memoria/02a.jpg
:alt: Memory introspection page with no results yet

The memory introspection page.
```

## Process list

The first analysis captures the memory and lists all the processes: the system ones (`lsass.exe`,
`services.exe`, `svchost.exe`…) and the user's, with PID, PPID, *threads*, session and creation time.

The following analyses reuse the same capture, without touching the machine again.

```{figure} /_static/img/10-memoria/03b.jpg
:alt: Process list extracted from memory with PID, name and creation time

Process list extracted from memory.
```

## Network connections

The **network connections** analysis shows the connections and listening ports that existed in memory.
It is useful for reconstructing who the machine was talking to.

```{figure} /_static/img/10-memoria/04b.jpg
:alt: List of network connections extracted from memory

Network connections found in memory.
```

## Suspicious memory

The **suspicious memory** search (the equivalent of *malfind*) flags executable and writable memory
regions (`PAGE_EXECUTE_READWRITE`) with injected code, a classic sign of malware and the starting point
for an intrusion analysis.

```{figure} /_static/img/10-memoria/05a.jpg
:alt: Suspicious memory search results with PAGE_EXECUTE_READWRITE protection

Suspicious memory regions.
```

```{note}
The memory dump can also be downloaded (in the console's acquisition panel), for external analysis with
other tools.
```
