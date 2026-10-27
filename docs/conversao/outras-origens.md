# Outras origens

Além de uma imagem que já está no servidor, o ForensicVM aceita indícios de várias outras origens. Todas
partilham o mesmo assistente e o mesmo fluxo de conversão.

```{video} 16-outras-origens
```

## As origens disponíveis

| Origem | Quando usar |
|---|---|
| **Caminho no servidor** | A imagem já está numa pasta do servidor (exemplos {doc}`cfreds-bart` e {doc}`hacking-case`). |
| **Partilha Windows (SMB)** | A imagem é lida diretamente de uma partilha de rede. |
| **Carregar do PC** | A imagem é enviada do computador do investigador, por blocos e com retoma se a ligação cair. |
| **Proxmox VE / PBS** | A máquina de interesse está num cluster Proxmox, ou nas suas cópias de segurança. |
| **Proxmox VE (streaming, experimental)** | Variante experimental de importação em fluxo a partir do Proxmox VE. |
| **Veeam Backup** | Importa um ponto de restauro do Veeam Backup & Replication como indício. |
| **Aquisição remota** | Adquire o disco de uma máquina remota através de um agente. |
| **Agente offline** | Descarrega um agente de aquisição autónomo (Linux, macOS ou Windows) para correr no próprio equipamento: modo normal, com bloqueador de escrita ou resposta a incidentes automática. A imagem resultante é depois importada. |

```{note}
Nos vídeos são demonstradas as vias **caminho no servidor** e **Proxmox** (VE e Backup Server), contra
um laboratório real. As integrações com o **Veeam** e a **aquisição remota por agente** existem, mas não
foram demonstradas por falta de laboratório com esses sistemas.
```

## Proxmox VE: aquisição ao vivo

Muitas organizações já têm a infraestrutura virtualizada em Proxmox. Num incidente, a máquina de que se
precisa está muitas vezes lá, como máquina virtual num cluster.

1. No assistente de conversão, escolha a origem **Proxmox VE/PBS** e o servidor configurado.
2. Escolha **Proxmox VE (ao vivo)**. O ForensicVM liga-se ao cluster e mostra as máquinas que lá correm.
3. Escolha a máquina que interessa à investigação.

O ForensicVM desencadeia uma cópia de segurança ao nível do hipervisor, sem instalar nada dentro da
máquina e sem tocar no indício. A imagem é obtida, verificada por *hash* e entra no mesmo fluxo de
conversão forense.

```{figure} /_static/img/16-outras-origens/03a.jpg
:alt: Assistente de conversão com a origem Proxmox e a lista de servidores configurados

Origem Proxmox: escolha do servidor.
```

```{figure} /_static/img/16-outras-origens/04a.jpg
:alt: Lista de máquinas virtuais em execução no cluster Proxmox VE

Proxmox VE ao vivo: as máquinas do cluster.
```

## Proxmox Backup Server

Quando já existem cópias de segurança das máquinas, o próprio histórico pode ser indício.

1. Escolha **Proxmox Backup Server**.
2. Escolha o *datastore*, o grupo de backup e o **ponto de restauro**.

Pode recuperar-se um estado anterior, por exemplo de antes de um comprometimento, **sem nunca contactar
o hipervisor de origem**, cuja integridade pode estar em causa. Daí em diante, o caminho é o mesmo:
*hash*, conversão e arranque.

```{figure} /_static/img/16-outras-origens/05a.jpg
:alt: Lista de grupos de backup no Proxmox Backup Server

Proxmox Backup Server: grupos de backup.
```

```{figure} /_static/img/16-outras-origens/05b.jpg
:alt: Lista de pontos de restauro de uma máquina no Proxmox Backup Server

Escolha do ponto de restauro.
```

## O que é comum a todas as origens

- A imagem é verificada por *hash* e o registo de auditoria apoia a cadeia de custódia.
- Segue-se sempre o mesmo fluxo: conversão, controladores e arranque.
- O caso é obrigatório, e o indício fica associado ao equipamento certo.
