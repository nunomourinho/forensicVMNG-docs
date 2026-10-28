# Managing the server

The technical side of the ForensicVM server: which services make it up, how to stop and start them
without shutting down the virtual machines, where the logs are and how to update with a single command.

```{video} 33-gestao-operacao
```

## The services

```{figure} /_static/img/33-gestao-operacao/02a.jpg
:alt: The four ForensicVM components — nginx, forensicvm.service, MariaDB and forensicvm-vms.slice

The server components.
```

| Service | Role |
|---|---|
| `nginx` | Web server: serves the interface and forwards `/api` and `/socket.io` to the application server. |
| `forensicvm` | The application server (Node.js), on `127.0.0.1:3000`. |
| `mariadb` | Database: users, cases, audit log, metadata. |
| `forensicvm-vms.slice` | Where the virtual machines run (QEMU/KVM), each in its own systemd *scope*. That is why they survive a restart of the application server. |
| `cape*` | Optional: malware analysis. |

```bash
systemctl status forensicvm nginx mariadb --no-pager
systemd-cgls -u forensicvm-vms.slice      # running virtual machines
ls /forensicVM/mnt                        # vm/ iso/ acquire/: the data disks
```

```{figure} /_static/img/33-gestao-operacao/05a.jpg
:alt: systemctl status output with the three services active

The three services active.
```

The data lives in `/forensicVM/mnt` (acquisitions, virtual machines, ISOs). **In production, each of
these folders should be on a disk of its own.** The service definition has a `RequiresMountsFor` line
with those folders: if a data disk is not mounted, the service refuses to start, instead of filling up the
system disk.

## Stopping and starting

```bash
./stop.sh                       # stops the server; running virtual machines keep running
./start.sh                      # starts it and finds the machines again
systemctl restart forensicvm    # restart (for example, after editing .env)
```

With the service stopped, nginx replies `502 Bad Gateway` to API requests.

```{note}
Before shutting down the physical server, first shut down the virtual machines through the interface, or
from inside each one.
```

## Logs

```bash
tail -f /var/log/forensicvm/server.log            # the application server
journalctl -u forensicvm -n 50 --no-pager         # systemd starts, failures and restarts
tail -50 /forensicVM/mnt/vm/<uuid>/run/qemu.log   # why a virtual machine did not boot
```

`server.log` is rotated daily by `logrotate`, which keeps 90 days compressed.

## Updating

```bash
./backup.sh       # before updating, a backup
./update.sh       # code, Node.js, dependencies, migrations, build and restart
./diagnose.sh     # confirm that everything is fine
```

`update.sh`:

- updates the code and, if needed, Node.js to the required version;
- rebuilds the native modules and installs the dependencies;
- applies the database migrations, giving the application user schema-change permissions only during
  that step;
- updates the system packages and tools;
- builds the server and the interface, publishes it in nginx and restarts the service.

```{figure} /_static/img/33-gestao-operacao/04b.jpg
:alt: update.sh output with the update steps

The update in progress.
```

```{tip}
On a very old installation, where `update.sh` is not executable yet, first bring in the code with
`git pull` and only then run `./update.sh`.
```

## Checking

`diagnose.sh` only reads the system and changes nothing. It checks the services, the API, the database,
the disks and free space, virtualisation, the server log and the running machines. Each problem is
flagged with ✗ and the suggested fix (→).

```bash
./diagnose.sh
```

```{figure} /_static/img/33-gestao-operacao/08a.jpg
:alt: diagnose.sh output with no problems found

The diagnosis, with no problems found.
```
