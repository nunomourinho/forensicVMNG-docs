# Glossário

```{glossary}
Agente QEMU
  O *QEMU Guest Agent*: um serviço que corre dentro do sistema convidado e permite ao ForensicVM correr
  comandos, ler ficheiros e gerir serviços na máquina em funcionamento. Usado pelos plug-ins online.

CAPE
  Laboratório automático de análise de malware (*sandbox*) integrado no ForensicVM. Executa uma amostra
  numa máquina isolada e descartável e produz um relatório de comportamento.

CFReDS
  *Computer Forensic Reference Data Sets*: repositório de imagens forenses de referência mantido pelo NIST
  (EUA). Fonte das imagens usadas nas demonstrações.

E01 / EWF
  Formato de imagem forense (*Expert Witness Format*), usado por ferramentas como o EnCase e o FTK Imager.
  Guarda os metadados da aquisição e os *hashes* dentro da própria imagem e pode dividir-se em segmentos.

Hash
  Valor calculado (MD5, SHA-1, SHA-256) que identifica univocamente o conteúdo de um ficheiro ou de uma
  imagem. Se o conteúdo mudar, o *hash* muda. Serve para provar a integridade.

Introspeção
  *Virtual machine introspection*: observação do interior de uma máquina virtual (processos, memória) a
  partir do hipervisor, sem software instalado no sistema convidado.

LUKS
  *Linux Unified Key Setup*: formato de cifra de disco usado pelo ForensicVM para cifrar em repouso os
  discos das máquinas virtuais.

Modo cópia
  Modo de conversão em que o disco é copiado para um ficheiro próprio. A máquina fica independente da
  imagem de origem e o agente QEMU é instalado.

Modo snapshot
  Modo de conversão em que a máquina usa a imagem original como base só de leitura. É rápido e ocupa
  pouco espaço, mas depende da imagem de origem.

PCAP
  Formato de ficheiro de captura de tráfego de rede, lido por ferramentas como o Wireshark.

Plug-in
  Ação forense pré-definida que o investigador corre sobre a máquina: online (máquina ligada, pelo agente)
  ou offline (máquina parada, sobre o disco).

QEMU/KVM
  O hipervisor em que correm as máquinas virtuais do ForensicVM. O KVM é a aceleração por hardware do
  núcleo Linux.

Registo de auditoria
  Registo imutável de todas as ações feitas no ForensicVM (quem, quando, sobre que máquina). Apoia e
  documenta a cadeia de custódia, mas não a substitui.

Snapshot
  Estado guardado de uma máquina virtual num dado instante (disco e, com a máquina ligada, memória).

Snapshot de ouro
  O snapshot criado automaticamente na conversão, antes de qualquer alteração: o estado exato do indício.
  Está protegido e não pode ser apagado.

Snapshot de prata
  O snapshot criado depois da injeção de controladores e antes do primeiro arranque. Está protegido.

VirtIO
  Família de controladores de dispositivos virtuais (disco, rede, série) para máquinas QEMU/KVM. O Windows
  precisa deles para arrancar numa máquina virtual.

Volatility3
  Ferramenta de referência, de código aberto, para análise forense de memória.
```
