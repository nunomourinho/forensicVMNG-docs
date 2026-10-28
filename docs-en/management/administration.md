# Administration

ForensicVM administration is on a single page, under **More → Administration**, and is reserved for
administrators.

```{video} 15-administracao
```

## What you will find in administration

- **Two-factor authentication** and **Security Keys & Biometrics** for your own account;
- **API Keys** for external clients;
- **Users** and their roles;
- **SSH Keys** (for integrations that use SSH, such as Proxmox);
- **System Setup**, including the system check with a software inventory (SBOM) and storage;
- **Integrations** with Veeam, Proxmox and the CAPEv2 Sandbox.

```{figure} /_static/img/15-administracao/02a.jpg
:alt: Administration page with its sections and the list of users

The administration page.
```

## Users and roles

Users are created and managed here: name, initial password, status (active or inactive) and whether they
are **superusers** (administrators). Access to the machines is then controlled case by case, through each
member's role (see {doc}`../getting-started/cases-and-team`).

## API keys

API keys let external clients (for example Autopsy, or automation scripts) talk to ForensicVM on behalf
of a user.

- Each key has a label and is assigned to a user.
- The full value is only shown at the moment it is created.
- Keys are **revocable, but never deleted**, to keep the trail, just like the action log.

```{figure} /_static/img/15-administracao/03a.jpg
:alt: List of API keys with label, user, masked key, date and status

The API keys.
```
