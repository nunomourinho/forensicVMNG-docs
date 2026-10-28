# Snapshots

A snapshot saves the exact state of the machine at a moment in time: the disk and the memory. It lets you
experiment without fear and go back.

```{video} 09-snapshots
```

## The golden snapshot

The console's snapshot panel shows the {term}`golden snapshot`, created automatically at conversion. It
is protected with a padlock: it is the exact state of the evidence and cannot be deleted. It is the
reference you can always go back to.

There is also the {term}`silver snapshot`: the state right after driver injection, before the first
boot.

```{figure} /_static/img/09-snapshots/02a.jpg
:alt: Snapshot panel with the silver and golden snapshots and the field to create a new one

The snapshot panel, with the protected golden snapshot.
```

## Creating and restoring

1. Before a risky operation (running a sample, changing a setting), give the snapshot a name and press
   **Save**. With the machine running, the snapshot includes the memory.
2. To go back, choose the snapshot and **Restore**. The machine returns exactly to where it was,
   including the open programs.
3. **Restore to origin** returns the machine to the protected starting state.

```{figure} /_static/img/09-snapshots/02b.jpg
:alt: Named snapshot being saved in the panel

Creating a named snapshot.
```

```{figure} /_static/img/09-snapshots/03a.jpg
:alt: Machine restored to the snapshot created, with a confirmation notification

Restoring a snapshot.
```

```{note}
Snapshot memory is encrypted when the server has an encryption master key configured. Creating,
restoring and deleting snapshots is recorded in the audit log.
```
