# Audit log

Every action in ForensicVM is logged: who did it, when and on which machine. The log is immutable, has
filters and can be exported in several formats.

```{video} 14-auditoria
```

```{important}
This log **is not the chain of custody itself**. It is a record of actions that **supports and
documents** it. It is immutable: the database has mechanisms (*triggers*) that prevent entries from being
changed or deleted, even by a database administrator.
```

## The case log

The case's **Custody** tab shows the list of actions on its machines: the image conversion, the boots,
the plug-ins, the captures, the hardware changes, enabling the network. Each line has the user and the
exact time.

You can filter by **machine** (UUID), **user**, **action** and **date range**.

```{figure} /_static/img/14-auditoria/02a.jpg
:alt: Case audit log filtered by the VM action

The case's action log, with filters.
```

## Exporting

The log can be exported as **CSV** or **JSON**, for analysis or to attach to the case file.

```{figure} /_static/img/14-auditoria/03a.jpg
:alt: CSV and JSON export buttons in the audit log

Exporting the log.
```

## Report and comments per machine

For each machine you can generate a **Word report** (DOCX) with the history of actions. The investigator
can also add their own **comments** (for example "Initial examination completed, no changes"), which are
recorded in the same way.

```{figure} /_static/img/14-auditoria/04a.jpg
:alt: A machine's log with the investigator comment field and the DOCX export

Investigator comment and export of the machine report.
```
