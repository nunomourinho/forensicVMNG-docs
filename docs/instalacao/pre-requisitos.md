# Pré-requisitos e preparação

O que é preciso antes de instalar: o hardware recomendado, onde instalar e onde obter o Ubuntu Server
24.04.

```{video} 25-pre-requisitos
```

## O que vai ser instalado

O ForensicVM instala-se sobre um servidor **Ubuntu Server 24.04 LTS**. A partir daí, converte imagens de
disco (E01, RAW, VMDK, QCOW2) em máquinas virtuais QEMU/KVM, que o investigador controla pelo navegador.
É isso que determina o hardware necessário.

## Hardware recomendado

| Componente | Recomendação |
|---|---|
| **Processador** | x86-64 com virtualização por hardware (Intel VT-x ou AMD-V) **ativada na BIOS/UEFI**. |
| **Memória** | 16 GB no mínimo; 32 GB ou mais recomendados. Cada máquina em análise consome RAM. |
| **Disco** | Rápido (SSD ou NVMe), com espaço para várias vezes o tamanho das imagens a examinar. Em produção, discos de dados separados do disco do sistema. |
| **Rede** | Estável. Todo o acesso dos investigadores é feito pelo navegador. |

Mais núcleos e mais memória significam mais máquinas a correr ao mesmo tempo, com fluidez.

## Onde instalar

```{figure} /_static/img/25-pre-requisitos/04a.jpg
:alt: Opções de instalação — servidor físico dedicado ou dentro de um hipervisor

Servidor físico ou virtualizado.
```

- **Servidor físico dedicado (*bare-metal*):** a opção preferida. Evita a sobrecarga de uma camada extra
  e dá acesso direto à virtualização por hardware, o motor do ForensicVM.
- **Dentro de um hipervisor:** é possível, mas é obrigatório ativar a **virtualização aninhada** (sem
  ela, as máquinas não arrancam aceleradas) e há alguma perda de desempenho.

## Obter o Ubuntu Server 24.04

- Página oficial: <https://ubuntu.com/download/server>. A página propõe a versão mais recente: desça até
  *Previous releases* e escolha **Ubuntu Server 24.04.x LTS**.
- Todos os ficheiros e somas de verificação: <https://releases.ubuntu.com/24.04/>.
- Ficheiro: `ubuntu-24.04.x-live-server-amd64.iso` (edição Server, 64 bits, LTS).

Verifique a integridade do ISO comparando o SHA-256 com o publicado em `SHA256SUMS`:

```bash
sha256sum ubuntu-24.04.5-live-server-amd64.iso
```

Num servidor físico, grave o ISO numa pen USB de arranque (Rufus, balenaEtcher ou `dd`).

Próximo passo: {doc}`ubuntu-server`.
