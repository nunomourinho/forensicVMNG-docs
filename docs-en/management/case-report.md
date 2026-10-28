# Forensic case report

CAPE has its own web interface, but the investigator should not depend on it. In ForensicVM, the results
are gathered in the case and exported in a verifiable report.

```{video} 24-relatorio-do-caso
```

## The case's malware analyses

In the case, the **Malware analyses** tab brings together all the associated analyses, from all the
case's equipment. For each file or process sent to CAPE, the risk score and the number of signatures
(critical and warnings) are shown.

The analyses are **stored in ForensicVM**. They can be viewed even with CAPE switched off.

```{figure} /_static/img/24-relatorio-do-caso/02a.jpg
:alt: The case's Malware analyses tab with the analyses and the export buttons

The case's *Malware analyses* tab.
```

```{figure} /_static/img/24-relatorio-do-caso/03a.jpg
:alt: List of analyses with risk score and signatures

The case's analyses, with the risk score.
```

## The Word report

**Report .docx** generates a document that brings together:

- the case identification (number, name, status, jurisdiction, person responsible);
- the equipment and the virtual machines;
- the acquisitions, with their *hashes*;
- the CAPE analyses: score, signatures and behaviour.

The document is ready to be added to the case file, outside ForensicVM.

```{figure} /_static/img/24-relatorio-do-caso/04a.jpg
:alt: Forensic case report open in a document viewer

The case report.
```

## Verifiable export

| Export | Contents |
|---|---|
| **Word report (.docx)** | The complete case report. |
| **Full package (.zip)** | The report and, per analysis, the original `report.json`, the screenshots and the network capture (PCAP). |
| **Integrity manifest** | A `manifest.json` with the SHA-256 of each file in the package, to confirm its integrity. |

Everything is generated from the local copy, even with CAPE switched off.

```{tip}
To confirm the integrity of a package you have received, recompute the SHA-256 of each file (for example
with `sha256sum`) and compare it with `manifest.json`.
```
