# Installing Ubuntu Server 24.04

The Ubuntu Server 24.04 installer from start to finish: language and keyboard, network, LVM disks, user,
SSH server, installation, first boot and, at the end, how to automate it all with autoinstall.

```{video} 26-ubuntu-server
```

## Downloading

At <https://ubuntu.com/download/server>, scroll down to *Previous releases* and press
**Download 24.04.5 LTS**. The ISO is about 3 GB (see {doc}`prerequisites`).

```{figure} /_static/img/26-ubuntu-server/02a.jpg
:alt: Ubuntu Server download page with the previous releases

The download page, in the previous releases section.
```

## Step by step in the installer

Boot the server from the ISO and choose **Try or Install Ubuntu Server**. Then, screen by screen:

1. **Language:** `English (UK)`, just below plain English.
2. **Keyboard:** layout and variant `English (UK)` (preselected after the language). Confirm. This is what
   makes sure the keys, especially in passwords, come out as expected.
3. **Installation type:** `Ubuntu Server` (default).
4. **Network:** DHCP by default. Note down the IP address. **In production, set a fixed IP address**, so
   that ForensicVM always answers at the same address.
5. **Proxy:** blank, unless the network requires one.
6. **Mirror:** the detected one. Wait for the message *This mirror location passed tests*.
7. **Storage:** `Use an entire disk` with `Set up this disk as an LVM group`. LVM makes it easier to add
   space later, as images pile up. Confirm the summary and, at the *Confirm destructive action* warning,
   choose **Continue**. The disk is about to be formatted.
8. **Profile:** your name, the server name (for example `forensicvm`), the administrator user and a strong
   password.
9. **Ubuntu Pro:** `Skip for now`.
10. **SSH:** tick `Install OpenSSH server`, for secure remote administration.
11. **Featured snaps:** do not choose any. ForensicVM installs what it needs.
12. Wait for the installation to finish and choose **Reboot Now**. Remove the boot media when asked and
    press Enter.

```{figure} /_static/img/26-ubuntu-server/04a.jpg
:alt: Choosing the English (UK) language in the Ubuntu Server installer

Choosing the language.
```

```{figure} /_static/img/26-ubuntu-server/07a.jpg
:alt: Storage configuration with the entire disk and LVM

Storage: entire disk with LVM.
```

```{figure} /_static/img/26-ubuntu-server/08a.jpg
:alt: Profile screen with name, server name, user and password

Profile and administrator user.
```

```{figure} /_static/img/26-ubuntu-server/09a.jpg
:alt: SSH configuration screen with the Install OpenSSH server option ticked

OpenSSH server.
```

```{figure} /_static/img/26-ubuntu-server/10a.jpg
:alt: System installation log in progress

The installation in progress.
```

## First boot and time zone

On the first boot, log in at the console with the user you created. The welcome screen shows the server's
**IP address**. That is the address you will open ForensicVM with in the browser.

```{figure} /_static/img/26-ubuntu-server/13b.jpg
:alt: Ubuntu Server welcome screen after the first login

The first login, with the server's IP address.
```

The installer does not ask for the time zone, and the server is left on UTC. Set it (example for the
United Kingdom):

```bash
timedatectl                                  # show the current zone
sudo timedatectl set-timezone Europe/London  # set it
timedatectl                                  # confirm
```

```{tip}
The correct server time matters in a forensic context: it is the time written to the audit log. Also
confirm that NTP synchronisation is active (`System clock synchronized: yes`).
```

## Automating with autoinstall

To install several servers without questions, Ubuntu supports **autoinstall**: a `user-data` file, in
YAML, describes the choices made above, and the installer follows it by itself, delivered through
cloud-init or on a USB stick labelled `CIDATA`.

Ready-to-adapt example: {download}`user-data </_static/autoinstall/user-data>` and
{download}`meta-data </_static/autoinstall/meta-data>`. Before using it, change the server name, the user
and, above all, the password *hash*:

```bash
openssl passwd -6 'your-strong-password'
```

Next step: {doc}`forensicvm`.
