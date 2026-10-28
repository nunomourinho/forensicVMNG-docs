# First steps

This page follows an investigator's first sign-in to the platform: language, authentication with a
mandatory second factor, recovery codes and the main navigation.

```{video} 01-primeiros-passos
```

## Sign-in screen

ForensicVM runs on a server and is used from the browser. There is nothing to install on the
investigator's workstation. On the sign-in screen you can choose the interface language (English,
Portuguese and others) and the light or dark theme, with the controls in the top right-hand corner.

The investigator signs in with the username and password the administrator assigned to them.

```{figure} /_static/img/01-primeiros-passos/02b.jpg
:alt: ForensicVM sign-in screen with the username and password fields

Sign-in screen.
```

## Two-factor authentication (mandatory)

On the first sign-in, the system requires a second factor to be set up. Without it, nobody gets to the
evidence. There are two options:

- **Security key or biometrics (FIDO2/WebAuthn):** a YubiKey, Windows Hello or Touch ID. It requires the
  server to be reached over HTTPS and by name (see {doc}`../installation/https-intranet`).
- **Authenticator app (TOTP):** Google Authenticator, Microsoft Authenticator, Authy, 1Password and
  similar.

To set up the authenticator app:

1. Choose **Authenticator app**.
2. Scan the QR code with the app on your phone.
3. Type the first six-digit code to confirm.
4. Keep the **eight recovery codes** the system shows in a safe place. Each one works only once, if you
   lose access to the authenticator.

```{figure} /_static/img/01-primeiros-passos/03a.jpg
:alt: Two-factor authentication setup with a QR code

Setting up the second factor with an authenticator app.
```

```{tip}
Register two factors per account (for example two security keys, or a key and an app) so that you do not
lose access if one of them goes missing. If you still lose access, the administrator can reset the
account (see {doc}`../administration/backups-and-troubleshooting`).
```

## Main navigation

Once authenticated, the investigator reaches the main screen: the server status (CPU, memory, disk,
network) and the virtual machines they have access to. **Each user only sees the machines of the cases
they are a member of.**

```{figure} /_static/img/01-primeiros-passos/04a.jpg
:alt: Main screen with the server resources and the list of virtual machines, still empty

Main screen: server resources and virtual machines (none yet).
```

The bottom navigation bar gives access to the main areas:

| Area | What it is for |
|---|---|
| **VMs** | The forensic virtual machines the user has access to. |
| **Cases** | Organising investigations. Every virtual machine belongs to a case. |
| **Convert** | The wizard that turns a forensic image into a virtual machine, from eight different sources. |
| **Media** | Library of VirtIO driver discs, ISO images, floppy disks and USB stick images, to mount on the machines. |
| **More** | Profile, administration and the remaining options. |

```{figure} /_static/img/01-primeiros-passos/04b.jpg
:alt: Conversion wizard with the eight image sources

The conversion wizard, with the possible image sources.
```

## Subsequent sign-ins

On subsequent sign-ins, after the password, the platform asks for the code from the authenticator app or
a touch of the security key.

```{figure} /_static/img/01-primeiros-passos/05b.jpg
:alt: Authenticator code prompt after the password

On subsequent sign-ins, the authenticator code is requested.
```

## In short

- Access from the browser, with nothing installed on the investigator's workstation.
- Mandatory second factor (FIDO2 or an authenticator app), with recovery codes.
- Each investigator only sees the machines of their own cases.

Next step: {doc}`cases-and-team`.
