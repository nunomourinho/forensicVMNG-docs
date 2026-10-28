# Encrypting and decrypting disks

Virtual machine disks can be encrypted at rest with **LUKS**. This page shows how to decrypt (or
encrypt) an existing disk, without losing data.

```{video} 30-desencriptar-disco
```

## Encryption policy

- By default, **new disks are not encrypted**, because encryption weighs on the processor, especially on
  older servers.
- An administrator can switch on the option to encrypt new disks by default. It requires the server to
  have an encryption master key configured.
- **Any existing disk** can be encrypted or decrypted at any time, with the machine stopped.

```{warning}
The keys of encrypted disks depend on the server's master key (`DISK_ENCRYPTION_MASTER_KEY`). Without it,
encrypted disks **cannot be recovered**. Keep it with the backups (see
{doc}`../administration/backups-and-troubleshooting`).
```

## Decrypting a disk

1. With the machine **stopped**, open the **Hardware** tab and the **Disks and Encryption** card. Each
   disk shows whether it is encrypted.
2. Press **Decrypt** on the disk you want.
3. Read the warning: the whole disk is rewritten without encryption, and the result is verified against
   the original before replacing it. It can take a while and needs free space on the server.

```{figure} /_static/img/30-desencriptar-disco/02a.jpg
:alt: Confirmation dialogue to decrypt disk sda

Confirming the decryption.
```

4. If the machine has memory snapshots, the system asks for an extra confirmation: the operation does not
   touch them, but restoring them afterwards is no longer guaranteed.

```{figure} /_static/img/30-desencriptar-disco/02b.jpg
:alt: Warning that the machine has snapshots, with the option to continue

Warning about the existing snapshots.
```

## Conversion and verification

The disk is rewritten to a new file, next to the original, which is not touched. A bar shows the
progress. In the demonstration, an 80 GB disk with about 29 GB in use took under a minute.

The new disk is then **verified**: the structure and, byte by byte, the content, compared with the
original. Only if they are identical does it replace it. At the slightest difference, the original would
stay as it was.

```{figure} /_static/img/30-desencriptar-disco/03b.jpg
:alt: Disk conversion progress bar

Converting the disk.
```

```{figure} /_static/img/30-desencriptar-disco/04b.jpg
:alt: Verification of the new disk completed, with the disk decrypted notification

Verification completed: disk decrypted.
```

```{note}
If the server restarts halfway through the operation, the original stays intact and the operation is
recovered at the next start-up.
```

## In short

- Encrypting or decrypting is a per-disk decision, taken with the machine stopped and without data loss.
- The original stays protected until the result is verified, and is only removed at the end.
- The operations are recorded in the audit log.
