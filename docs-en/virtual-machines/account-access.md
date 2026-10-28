# Account access without changing the credential

On a seized machine, the investigator rarely has the user's password. This page shows how to get into the
session for an **authorised examination**, without changing the original credential or touching the
image.

```{video} 06-acesso-sem-alterar-password
```

```{important}
This procedure is intended exclusively for **lawfully authorised** forensic examinations, as part of an
investigation. The operation is recorded in the case audit log, with the user and the time.
```

## The account is protected

Without the right password, Windows refuses access, just as it would on the original computer.

```{figure} /_static/img/06-acesso-sem-alterar-password/02a.jpg
:alt: Windows sign-in screen with the password-protected account

The user's account is protected.
```

## The access plug-in

ForensicVM includes a **live** plug-in with a single purpose: to give the investigator access to the
user's session when the credential is not known.

- It acts on the **running** virtual machine, in memory, not on the disk.
- The original image and its *hash* are not touched.
- The account's real password stays exactly as it was in the evidence.

## Running the plug-in

1. In the console, open the **live plug-ins** catalogue in the bottom toolbar.
2. Choose the access plug-in (Windows session unlock) and run it against the machine.
3. The plug-in runs on the virtual machine and returns the result. Nothing is written to the evidence
   disk.

```{figure} /_static/img/06-acesso-sem-alterar-password/04a.jpg
:alt: Live plug-ins catalogue in the console

The live plug-ins catalogue, open in the console.
```

```{figure} /_static/img/06-acesso-sem-alterar-password/04b.jpg
:alt: Unlock plug-in running, with its log

The plug-in running.
```

## Getting into the session

From there, the investigator signs into the session and can examine the account as the user saw it: the
desktop, the local applications and the signed-in cloud services.

```{figure} /_static/img/06-acesso-sem-alterar-password/06b.jpg
:alt: The user's desktop after signing into the session

The user's desktop, ready to be examined.
```

## What is guaranteed

- The original image (E01) and its *hash* keep matching those of the acquisition.
- The account's real password stays as it was on the seized machine.
- The operation is in the case audit log, with the user and the time.
- When the machine is shut down, the access no longer applies. Nothing persists in the evidence.
