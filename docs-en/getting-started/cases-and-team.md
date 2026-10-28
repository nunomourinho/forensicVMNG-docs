# Cases and team

In ForensicVM, everything starts with a case. The case brings together the seized equipment, the virtual
machines created from it and the people who may access them. **No case, no conversion.**

```{video} 02-casos-e-equipa
```

## Creating the case

Under **Cases → New case**, you fill in:

- the **Case number** (for example, the case file or the forensic examination request number);
- the **Name** and the **Description**;
- the **Jurisdiction** and the **Classification** (for example *Restricted* or *Confidential*).

```{figure} /_static/img/02-casos-e-equipa/02a.jpg
:alt: New case form with number, name, description, jurisdiction and classification

Creating a case.
```

The case is open, with whoever created it as its **Owner**. Only the owner can close or archive the case.
From then on, the other members can only view it.

```{figure} /_static/img/02-casos-e-equipa/02b.jpg
:alt: Case overview with the status, the owner and the close and archive actions

Case overview.
```

## Seized equipment

The **Equipment** tab records the seized material: the type (desktop computer, laptop…), the name, the
make, the model and the serial number. This data often comes from the acquisition notes included in the
E01 image itself.

Each item of equipment then gets its own virtual machine. This is where the conversion wizard looks for
them. Until an image has been converted, the equipment is shown as **pending**.

```{figure} /_static/img/02-casos-e-equipa/03b.jpg
:alt: Registering a Dell Latitude laptop with make, model and serial number

Registering an item of equipment with make, model and serial number.
```

## Members and roles

The **Members** tab gives colleagues access, choosing each one's role:

| Role | Can |
|---|---|
| **Viewer** | View the case and the machines. |
| **Investigator** | All of the above, plus operate the virtual machines (start them, use the console, run plug-ins…). |
| **Manager** | All of the above, plus manage members and equipment. |
| **Owner** | All of the above, plus close and archive the case. |

```{figure} /_static/img/02-casos-e-equipa/04a.jpg
:alt: Adding a member to the case with the investigator role

Adding a colleague to the case, with the investigator role.
```

```{note}
Besides the role, you can set exceptions per item of equipment or per disk: read-only access to one
specific disk, for example. These exceptions take precedence over the role.
```

## The case audit log

The **Custody** tab shows the audit log of the actions on the case's machines. In a new case it is empty.
The first entry will be the conversion of the image. See {doc}`../management/audit-log`.

```{figure} /_static/img/02-casos-e-equipa/05a.jpg
:alt: Custody tab with an empty audit log

The audit log of a newly created case.
```

## In short

- Every virtual machine belongs to a case. No case, no conversion.
- Equipment records the seized material, with make, model and serial number.
- Access is decided case by case, with four roles: viewer, investigator, manager and owner.

Next step: {doc}`../conversion/cfreds-bart`.
