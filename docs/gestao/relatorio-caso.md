# Relatório forense do caso

O CAPE tem a sua própria interface web, mas o investigador não deve depender dela. No ForensicVM, os
resultados ficam reunidos no caso e exportam-se num relatório verificável.

```{video} 24-relatorio-do-caso
```

## As análises de malware do caso

No caso, o separador **Análises de malware** reúne todas as análises associadas, de todos os equipamentos
do caso. Para cada ficheiro ou processo enviado ao CAPE aparecem a pontuação de risco e o número de
assinaturas (críticas e avisos).

As análises ficam **guardadas no ForensicVM**. Podem ser consultadas mesmo com o CAPE desligado.

```{figure} /_static/img/24-relatorio-do-caso/02a.jpg
:alt: Separador Análises de malware do caso com as análises e os botões de exportação

O separador *Análises de malware* do caso.
```

```{figure} /_static/img/24-relatorio-do-caso/03a.jpg
:alt: Lista de análises com pontuação de risco e assinaturas

As análises do caso, com a pontuação de risco.
```

## O relatório em Word

**Relatório .docx** gera um documento que reúne:

- a identificação do caso (número, nome, estado, jurisdição, responsável);
- os equipamentos e as máquinas virtuais;
- as aquisições, com os respetivos *hashes*;
- as análises do CAPE: pontuação, assinaturas e comportamento.

O documento está pronto a juntar ao processo, fora do ForensicVM.

```{figure} /_static/img/24-relatorio-do-caso/04a.jpg
:alt: Relatório forense do caso aberto num leitor de documentos

O relatório do caso.
```

## Exportação verificável

| Exportação | Conteúdo |
|---|---|
| **Relatório Word (.docx)** | O relatório completo do caso. |
| **Pacote completo (.zip)** | O relatório e, por análise, o `report.json` original, as capturas de ecrã e a captura de rede (PCAP). |
| **Manifesto de integridade** | Um `manifest.json` com o SHA-256 de cada ficheiro do pacote, para confirmar a integridade. |

Tudo é gerado a partir da cópia local, mesmo com o CAPE desligado.

```{tip}
Para confirmar a integridade de um pacote recebido, recalcule o SHA-256 de cada ficheiro (por exemplo
com `sha256sum`) e compare-o com o `manifest.json`.
```
