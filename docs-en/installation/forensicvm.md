# Installing ForensicVM

With Ubuntu Server ready, installing ForensicVM is essentially **a single command**. That command takes
care of everything: dependencies, database, services and web server.

```{video} 27-forensicvm
```

## Getting the code

Install `git`, if it is not there yet, and clone the ForensicVM repository. Replace
`<REPOSITORY-URL>` with the address of the repository you were given:

```bash
sudo apt install -y git
git clone --depth 1 <REPOSITORY-URL> forensicVmNG
cd forensicVmNG
ls
```

`--depth 1` downloads only the latest version, which saves time and space. The installer is
`install.sh`.

```{figure} /_static/img/27-forensicvm/03b.jpg
:alt: Terminal with git clone, the folder listing and the start of install.sh

`git clone` and the start of `install.sh`.
```

## Running the installer

Inside the repository folder, as administrator:

```bash
sudo ./install.sh
```

The installer shows each step and carries on to the end with practically no questions:

1. **Node.js** and **pnpm**, in the exact version pinned by the project;
2. **System dependencies:** MariaDB, QEMU/KVM, forensic and memory analysis tools (some built from
   source) and the VirtIO drivers for Windows (`virtio-win.iso`);
3. **The application:** dependencies, building the server and the web interface;
4. **The database**, with a least-privilege user, the migrations and the initial administrator;
5. **The systemd service and nginx.**

On the reference installation it took about 25 minutes. It varies with the network and the processor.

Halfway through, there is a single question. Answer `y`:

```text
Install and enable the forensicvm systemd service? [y/N] y
```

```{figure} /_static/img/27-forensicvm/04a.jpg
:alt: Installer showing the installation of the system dependencies

The installer, step by step.
```

## The final summary

At the end, the installer shows:

- the server address (`http://<server-IP>`);
- the initial administrator account (`admin`) and the default password;
- the path of the configuration file (`apps/server/.env`) and the next steps.

```{figure} /_static/img/27-forensicvm/07a.jpg
:alt: Summary of the completed installation and status of the forensicvm service

Installation completed and service active.
```

```{danger}
**Keep the `DISK_ENCRYPTION_MASTER_KEY`** (in the `apps/server/.env` file) somewhere safe, off the
server. Without it, encrypted disks **cannot be recovered**. The `backup.sh` backups include it (see
{doc}`../administration/backups-and-troubleshooting`).
```

## Checking

```bash
systemctl status forensicvm --no-pager   # should be "active (running)" and "enabled"
curl -s http://localhost/api/v2/health   # should reply {"status":"ok",...}
```

## First sign-in

Open `http://<server-IP>` in the browser and sign in with the initial account. The system takes you
straight to setting up the **second factor, which is mandatory**. Then **change the default password**
(**Profile → Change password**). See {doc}`../getting-started/first-steps`.

```{figure} /_static/img/27-forensicvm/08b.jpg
:alt: Mandatory second-factor setup on the first sign-in

On the first sign-in, the second factor is mandatory.
```

## Hardening for production

- **HTTPS:** with `certbot` (server with a public name) or with a local certificate authority (isolated
  network, see {doc}`https-intranet`). After enabling HTTPS, set `COOKIE_SECURE=true` in `.env` and
  restart the service (`sudo systemctl restart forensicvm`).
- **Firewall:** open only ports 80 and 443 (and 22 for administration). Close the rest to the outside.
- Regular **backups** of the database and of the machine disks (see
  {doc}`../administration/backups-and-troubleshooting`).
