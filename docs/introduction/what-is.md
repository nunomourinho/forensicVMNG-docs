# O que é o ForensicVM

O ForensicVM NextGen é uma plataforma de **virtualização forense**. Recebe uma imagem de disco adquirida
com as ferramentas habituais de aquisição (por exemplo um ficheiro E01 criado com FTK Imager, EnCase ou
Guymager) e transforma-a numa máquina virtual que arranca e se controla inteiramente a partir do
navegador.

## Para quem é

A plataforma destina-se a quem trabalha em forense digital: peritos e investigadores criminais,
laboratórios de forense, equipas de resposta a incidentes (CSIRT/SOC) e docentes e estudantes da área. O
investigador não precisa de instalar nada no seu posto de trabalho. Basta um navegador moderno e uma
conta no servidor.

## O que permite fazer

| Necessidade | Como o ForensicVM responde |
|---|---|
| Ver o sistema como o utilizador o via | A imagem é convertida numa máquina virtual e aberta numa consola no navegador. |
| Não alterar o indício | A imagem original é montada só de leitura. As alterações ficam em camadas separadas, e o {term}`snapshot de ouro` guarda o estado exato da aquisição. |
| Arrancar um Windows apreendido em hardware diferente | Injeção automática dos controladores VirtIO, num {term}`snapshot de prata` próprio. |
| Aceder a uma conta sem conhecer a palavra-passe | Plug-in em direto que dá acesso à sessão sem alterar a credencial gravada no disco. |
| Analisar memória volátil | Captura da memória da máquina em execução e análise com o Volatility3, ou introspeção ao vivo a partir do hipervisor. |
| Observar comunicações | Rede isolada por omissão, com captura de tráfego para PCAP quando o investigador decide. |
| Perceber o que faz um ficheiro suspeito | Envio para o laboratório de malware CAPE, sem o executar no posto do investigador. |
| Documentar o exame | Gravação de vídeo e capturas de ecrã da sessão, um disco próprio para os indícios recolhidos, registo de auditoria e relatório do caso. |
| Trabalhar em equipa | Casos com membros e papéis (leitor, investigador, gestor, proprietário), com permissões até ao nível do disco. |

## Origens de imagem suportadas

- **Formatos de imagem:** E01/EWF (incluindo imagens segmentadas), AFF, RAW/DD, VMDK e QCOW2.
- **Origens:** caminho no próprio servidor, partilha de rede Windows (SMB), envio a partir do computador
  do investigador (upload por blocos, com retoma), Proxmox VE, Proxmox Backup Server, Veeam Backup &
  Replication e aquisição remota por agente.

Veja {doc}`../conversion/index`.

## Como funciona, em traços largos

1. O investigador cria um **caso** e regista os **equipamentos** apreendidos.
2. No assistente de conversão, escolhe a imagem e o equipamento a que pertence.
3. O ForensicVM lê os metadados da imagem (examinador, data, *hashes* da aquisição) e monta-a só de
   leitura. Cria o snapshot de ouro, injeta os controladores e prepara a máquina virtual.
4. A máquina arranca em QEMU/KVM. O investigador trabalha na consola do navegador e usa as ferramentas
   de análise.
5. Cada ação fica registada. No fim, exportam-se as evidências, o registo de auditoria e o relatório do
   caso.

```{note}
O ForensicVM nasceu de uma dissertação de mestrado na Universidade Politécnica de Beja (Upbeja). Em
2026 foi reconstruído de raiz para a web, mantendo os scripts de conversão do projeto original. Veja
{doc}`../project/status-and-collaboration`.
```
