# O sistema em sete minutos

Esta página resume o ForensicVM de ponta a ponta, do indício à análise. Cada funcionalidade tem depois a
sua página, com mais detalhe.

```{video} 32-resumo-sistema
```

## O problema e a solução

Um disco apreendido tem de ficar intacto, mas é muito útil vê-lo a correr. O ForensicVM converte a
imagem numa máquina virtual, controlada pelo navegador. O indício original nunca é tocado e cada ação
fica registada.

O navegador fala com um servidor que gere os casos, as permissões e a auditoria. As máquinas correm em
QEMU/KVM, sobre camadas que protegem a imagem original (veja {doc}`concepts`).

## Acesso seguro e organização por casos

Todas as contas exigem segundo fator: aplicação de autenticação ou chave de segurança. Sem ele, não se
chega aos indícios.

Cada indício pertence a um caso. Ao caso juntam-se equipamentos e membros, com papéis de leitor,
investigador, gestor ou proprietário, e permissões que podem ir até ao disco. Assim, cada pessoa só vê o
que lhe compete.

```{figure} /_static/img/32-resumo-sistema/06a.jpg
:alt: Registo de um equipamento apreendido no caso

Cada indício pertence a um caso e a um equipamento apreendido.
```

→ {doc}`../getting-started/first-steps`, {doc}`../getting-started/cases-and-team`

## Da imagem à máquina virtual

A imagem forense (E01, RAW, VMDK…) é convertida numa máquina arrancável, com injeção automática de
controladores. O processo é automático, o original nunca é escrito e o *hash* confirma que o indício não
mudou.

```{figure} /_static/img/32-resumo-sistema/07b.jpg
:alt: Conversão concluída, com a identidade da imagem e o registo da conversão

A conversão mostra a identidade da imagem (examinador, data, *hashes*) e o registo de cada passo.
```

→ {doc}`../conversion/index`

## Arranque, consola e acesso à conta

A máquina arranca com um registo em tempo real e capturas automáticas, e a consola abre-se no próprio
navegador. O investigador comanda a máquina como se estivesse à frente dela, sem instalar nenhum
programa.

Quando a conta do utilizador está protegida, há um procedimento controlado para obter acesso à sessão
sem alterar a credencial gravada no disco. Também fica registado.

```{figure} /_static/img/32-resumo-sistema/08a.jpg
:alt: Detalhe da máquina com o registo de arranque em direto

Arranque com registo em direto.
```

→ {doc}`../virtual-machines/boot-and-console`, {doc}`../virtual-machines/account-access`

## Ferramentas de análise

- **Plug-ins** executam análises prontas e repetíveis: informação do sistema, utilizadores, programas
  instalados, extração de ficheiros.
- O **gestor de processos** lista processos e serviços, suspende ou retoma processos, pesquisa o *hash*
  no VirusTotal e envia amostras para o CAPE.
- Os **snapshots** guardam o estado da máquina. Experimenta-se à vontade e volta-se atrás num instante.
- A **memória** é analisada com o Volatility3: processos, ligações de rede e código injetado.
- A **introspeção** mostra processos e serviços a partir de fora da máquina, onde o malware não a
  consegue detetar nem adulterar.
- A **rede** está isolada por omissão. Quando é preciso, o tráfego é capturado para um ficheiro PCAP.
- O **hardware** (memória, processadores, firmware BIOS/UEFI, TPM) ajusta-se ao equipamento apreendido.

```{figure} /_static/img/32-resumo-sistema/13a.jpg
:alt: Painel de snapshots com o snapshot de ouro protegido

Snapshots: voltar atrás em segundos, com um ponto de partida protegido que nunca se perde.
```

→ {doc}`../analysis/index`, {doc}`../virtual-machines/index`

## Documentar e reportar

A sessão pode ser gravada em vídeo e há capturas de ecrã a pedido. O que se recolhe da máquina vai para
um **disco de evidências**, à parte do indício original. O CAPE analisa amostras suspeitas num
laboratório isolado. Os discos podem ser cifrados em repouso. E também se importam máquinas do Proxmox e
cópias do Proxmox Backup Server.

```{figure} /_static/img/32-resumo-sistema/20a.jpg
:alt: Relatório de análise de malware do CAPE

Análise de malware com o CAPE: assinaturas, comportamento e pontuação de risco.
```

No fim, o registo de auditoria (filtrável e exportável) e o relatório do caso reúnem as máquinas, as
análises e as ações num documento pronto a juntar ao processo.

→ {doc}`../management/index`, {doc}`../malware/index`

## Em resumo

- Origens E01, RAW, VMDK, QCOW2, Proxmox e cópias de segurança.
- Consola, plug-ins, memória, rede, malware e relatórios, tudo a partir do navegador e num único sistema.
- Cada ação registada, para apoiar a cadeia de custódia e sustentar a prova.
