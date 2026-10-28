# Network: isolation and traffic capture

For safety, the machine boots **isolated from the network**. The investigator decides whether and when to
give it access, and everything that goes over the network can be captured.

```{video} 11-rede
```

## Isolated by default

In the **Network** tab of the machine detail, the indicator shows that the network interface is switched
off (*TAP disabled*). The machine sees neither the internet nor the local network.

```{figure} /_static/img/11-rede/02a.jpg
:alt: Network tab with the interface switched off and the list of previous captures

The isolated network, with the previous captures.
```

```{important}
Connecting a seized system to the network can have consequences: synchronisation with cloud services,
contact with command-and-control servers, changes to remote data. Connect it only when necessary and
justified, and document it.
```

## Live traffic capture

1. Press **Start Capture**. The network is connected and the system starts logging every packet.
2. The machine's requests appear live: DNS queries and remote connections, with the host, the service,
   the port and the volume.
3. Press **Stop Capture**. The capture is saved and the machine is isolated again.

```{figure} /_static/img/11-rede/03a.jpg
:alt: Live traffic inspection with DNS queries and remote connections

Live traffic capture.
```

## The PCAP file

The traffic goes into a **PCAP** file, which you download to analyse with tools such as
[Wireshark](https://www.wireshark.org/) and to add to the case file. **Download all** puts all the
captures into a ZIP.

```{figure} /_static/img/11-rede/04a.jpg
:alt: List of captured PCAP files with the download option

The PCAP files, ready to download.
```
