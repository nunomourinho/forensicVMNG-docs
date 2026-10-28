# Installing the QEMU agent on snapshot-mode evidence

Evidence converted in **snapshot mode** has no QEMU agent (*QEMU Guest Agent*), and the online plug-ins
that depend on it stop working. The **Install QEMU Guest Agent** plug-in solves this offline, before the
first boot, without downloading anything from the internet.

```{video} 29-instalar-agente
```

## The symptom

On a machine converted in snapshot mode, an online plug-in (for example **SYSTEM Exec**, which runs a
command with SYSTEM privileges through the agent) keeps waiting and ends in an error: there is no agent on
the other side.

```{figure} /_static/img/29-instalar-agente/02a.jpg
:alt: SYSTEM Exec plug-in waiting for a reply on a machine with no agent

An online plug-in with no reply, for lack of an agent.
```

## Why it happens

| Mode | Conversion tool | QEMU agent |
|---|---|---|
| **Snapshot** (fast) | `virt-v2v-in-place`, which only injects the disk drivers | Not installed |
| **Copy** (complete) | Full `virt-v2v` | Installed automatically on first boot |

Without the agent (and the `virtio-serial` driver), the online plug-ins are blind.

## The Install QEMU Guest Agent plug-in

The plug-in runs **with the machine stopped, before the first boot**. It does not need the agent to
install the agent.

- The source is the `virtio-win.iso` image the ForensicVM installer already left on the server. Nothing
  is downloaded at that point.
- The original evidence is never touched: the action goes into a new layer, on top.

```{figure} /_static/img/29-instalar-agente/04a.jpg
:alt: Plug-in catalogue filtered to the Install QEMU Guest Agent plug-in

The plug-in in the catalogue.
```

## Running it

1. With the machine stopped, open **Plug-ins** and look for *Install QEMU Guest Agent*.
2. Give the driver folder matching the Windows version (for example `w10`).
3. Press **Run offline**. The plug-in mounts `virtio-win.iso`, extracts the `virtio-serial` driver and
   the agent installer, and leaves them ready to run automatically at the machine's next real boot.

```{figure} /_static/img/29-instalar-agente/05b.jpg
:alt: Offline run of the plug-in with the log of the steps

Offline run of the plug-in.
```

## The result

On the first boot, Windows installs the driver and the agent by itself. The same online plug-in then
replies, and the whole online catalogue is available again: extracting files, running commands,
inspecting drivers.

```{figure} /_static/img/29-instalar-agente/06b.jpg
:alt: SYSTEM Exec plug-in replying after restarting the machine

After a restart, the online plug-in replies.
```

## In short

- Snapshot-mode conversion stays fast, and the investigator is no longer left without online plug-ins.
- Nothing is downloaded from the internet. The source is local, already verified by the installer.
- The action is recorded in the audit log, like any other plug-in.
