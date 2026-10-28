# Backups and troubleshooting

A backup is only worth something if you know how to restore it. This page shows how to make a backup with
`backup.sh`, keep it on a separate disk and schedule it; how an altered archive is refused; how to restore
everything with `restore.sh`; and how to diagnose and fix the most common failures.

```{video} 34-copias-troubleshooting
```

```{note}
In the demonstration, the disaster and the failures were caused on purpose, on a lab server. **Never**
reproduce those steps on a production server.
```

## What goes into the backup

| Contents | Notes |
|---|---|
| Database | Users, cases, permissions and the audit log, with the immutability *triggers*. |
| `.env` file | Includes the `JWT_SECRET` and the master key of the encrypted disks. |
| System configuration | systemd service, nginx and TLS certificates, sudoers, logrotate. |
| Virtual machine metadata | |
| Machine disks and ISOs | Only with `--include-vms` and `--include-iso`, as they are large. |
| `MANIFEST` and SHA-256 checksums | Origin and date of the backup, and the checksum of each file. |

```{danger}
The archive carries the **master key of the encrypted disks**. Without it, those disks cannot be opened,
and with it anyone can open them. The backup is a secret: keep it **off the server**, with restricted
access.
```

## Making the backup

```bash
./backup.sh --help
./backup.sh                                   # → /var/backups/forensicvm/forensicvm-YYYYMMDD-HHMMSS.tar.gz
./backup.sh --dest /mnt/nas/forensicvm --include-vms --include-iso
```

The database backup is taken without stopping the server. At the end, `backup.sh` reports what it saved
(users, cases, *triggers*), computes the SHA-256 checksums and reminds you that the archive contains
secrets. A `.sha256` file with its checksum sits next to the archive.

```{figure} /_static/img/34-copias-troubleshooting/04a.jpg
:alt: The backup archive and its SHA-256 checksum in /var/backups/forensicvm

The archive and its SHA-256 checksum.
```

## Keeping it off the server

The backup cannot stay only on the server itself. Copy the archive and its checksum to an external disk,
a NAS or another machine, and confirm at the destination that it arrived intact:

```bash
cp /var/backups/forensicvm/forensicvm-*.tar.gz* /mnt/external-disk/
cd /mnt/external-disk && sha256sum -c forensicvm-*.tar.gz.sha256
```

```{figure} /_static/img/34-copias-troubleshooting/04b.jpg
:alt: Copy to a separate disk with the sha256sum check OK

Copy to a separate disk and checksum verification.
```

## Scheduling it every night

```bash
echo '30 2 * * * root '"$PWD"'/backup.sh --dest /mnt/backup/forensicvm >>/var/log/forensicvm/backup.log 2>&1' \
  | tee /etc/cron.d/forensicvm-backup
```

## Verifying a backup

```bash
./restore.sh --verify /var/backups/forensicvm/forensicvm-YYYYMMDD-HHMMSS.tar.gz
```

The `--verify` option changes nothing. It checks every SHA-256 checksum and shows the manifest (date,
server, version, counts). An altered archive, for example with a single line added to `MANIFEST`, is
**refused** and nothing is restored.

```{figure} /_static/img/34-copias-troubleshooting/05b.jpg
:alt: restore.sh --verify validating the checksums and showing the manifest

Verifying an intact archive.
```

## Restoring

```bash
./restore.sh /var/backups/forensicvm/forensicvm-YYYYMMDD-HHMMSS.tar.gz
```

`restore.sh`:

1. checks the SHA-256 checksums again and refuses an altered archive;
2. warns that it is about to replace the database and asks for **this server's name**, so as not to
   restore in the wrong place;
3. saves the current state to `/var/backups/forensicvm/pre-restauro/`;
4. stops the service, restores the database and confirms the counts and the audit log *triggers*;
5. restores `.env` and the system configuration, reloads nginx and restores the metadata of any missing
   machines (it never overwrites a machine that already exists);
6. starts the service again and only finishes when the API responds.

```{figure} /_static/img/34-copias-troubleshooting/07a.jpg
:alt: restore.sh output with the confirmation by server name and the restore steps

The restore, with the confirmation by server name.
```

After the restore, users sign in again with the same password and the **same second factor** as
before: they were in the backup too.

## Troubleshooting

The method is always the same:

1. Run `./diagnose.sh`. It only reads, and each problem comes with the suggested fix.
2. Look at the service in question: `systemctl status <service>` and `journalctl -u <service>`.
3. Fix it and run `./diagnose.sh` again.

| Symptom | Likely cause | Fix |
|---|---|---|
| The browser shows *502 Bad Gateway*. The sign-in screen says the ForensicVM server is not responding. | `forensicvm` service stopped. | `./start.sh` and then look at `server.log`. |
| The sign-in screen says the server cannot use its database. | MariaDB stopped, or database deleted. | `systemctl start mariadb`. If it was deleted, `./restore.sh <backup>`. |
| The sign-in screen says *Invalid username or password*. | Wrong credentials (server and database are fine). | See the next row. |
| The administrator forgot the password and/or lost the authenticator. | | `apps/server/scripts/reset-admin-password.sh admin --clear-2fa` |
| A virtual machine does not boot. | Look at the machine's `run/qemu.log`. | Depending on the message (missing disk, KVM, memory). |
| Data disk nearly full. | Old machines or acquisitions. | Delete them through the interface. `journalctl --vacuum-size=500M`. |

```{figure} /_static/img/34-copias-troubleshooting/08a.jpg
:alt: Sign-in page with the error message when the server does not respond

The sign-in screen message when the application server is stopped.
```

### Recovering administrator access

```bash
apps/server/scripts/reset-admin-password.sh admin --clear-2fa
```

Without the `--password` option, the script generates a random password and shows it **only once**. With
`--clear-2fa`, it also removes the second factor. On the next sign-in, the system makes you set it up
again.

### When a virtual machine does not boot

- The machine's boot log is in `/forensicVM/mnt/vm/<uuid>/run/qemu.log`.
- The previous run is kept in `qemu.log.prev`.
- `diagnose.sh` lists the running machines and points to this path.

## In short

- **Back up:** `./backup.sh`, kept off the server and scheduled in cron.
- **Verify:** `./restore.sh --verify <archive>`, which refuses altered archives.
- **Restore:** `./restore.sh <archive>`, which asks for the server name and saves the current state first.
- **Diagnose:** `./diagnose.sh`, then `systemctl status` and `journalctl`.
- **Lost access:** `apps/server/scripts/reset-admin-password.sh admin --clear-2fa`.
